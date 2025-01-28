from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    ROLE_OPTION=(
        ("STUDENT","STUDENT"),
        ("INSTRUCTOR","INSTRUCTOR")
    )

    role=models.CharField(max_length=100,default="STUDENT",choices=ROLE_OPTION)

class InstructorProfile(models.Model):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    experties=models.CharField(max_length=200,null=True)

    description=models.CharField(max_length=200,null=True)

    picture=models.ImageField(upload_to="Profilepics",null=True,blank=True,default="Profilepics/default.png")

from django.db.models.signals import post_save

def create_instructor_profile(sender,created,instance,**kwargs):

    if created and instance.role == "instructor":

        InstructorProfile.objects.create(owner=instance)

post_save.connect(create_instructor_profile,User)