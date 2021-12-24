from django.db import models
from django.contrib.auth.models import User # importing the User model for using authrization
                                            # we will use username, email, password from this Model
# Create your models here.

class UserInfo(models.Model): #                                                  # To extend the information for User model we are creating another model which will be one_to_one relation-ship with user model
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True) # connect user model in one_To_one relationship
                                                                                 # And saying that, User model id willbe its ID
    facebook_id = models.URLField(blank=True)                                   # user can keep this field empty
    profile_pic= models.ImageField(upload_to='profile_pics', blank=True) # profile image will be uploaded to 'media/profile_pics' folder

    def __str__ (self):
        return self.user.username # accessing the user name from User model
