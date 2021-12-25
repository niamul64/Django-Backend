## Django model class relations(oneTOone, oneTOmany, manyTOmany ) https://www.webforefront.com/django/setuprelationshipsdjangomodels.html

### for Mysql database setup see: 'WITH MySql Database' folder README.md, and video --> 'connecting mysql database.mp4'

### All the imports:

```
from django.db import models
from django.utils import timezone

## for user model use any of this, but not both:
from django.conf import settings 			#we can use this to get user model from settings, we allso can import user model directly by:
from django.contrib.auth.models import User # importing the User model for using authrization
                                            # we will use username, email, password from this Model
```


### 1. Built in models, Django Models, sqlLite3. Built in database.(This is not recommended for production level work)
1. We need django-models to work with db.sqlite3. SQL-Lite3 is a build in databsase with django.
2. In every app we have models.py file.
3. 'from django.db import models' this library should already been included in models. And this library contains all the classes and functions we need.
4. models have some other usefull parameters 

```
class Musician(models.Model): # models have some other usefull parameters (see step11 )
    # id = models.AutoField(Primary_key=True)     #But we dont need this id field. its genarated by django automaticaly.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
	content = models.TextField(null=True, blank= True)
	facebook_id = models.URLField(blank=True)
    
    # when using MySql
    # class Meta: # by this , we can say to make the table with exactly this give name(force)
    #     db_table = "Musician" # table will be created by this name exactly.

    def __str__(self): #function to_string
        return self.first_name+" "+ self.last_name

class Album(models.Model):

    artist = models.ForeignKey(Musician, on_delete= models.CASCADE) # (oneTomany)By using on on_delete: if Musician object deleted then coresponding album obj will also deleted
    name= models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars =models.IntegerField()

    def __str__(self): #function to_string
        return self.name
```

4. Now we need to migrate the models. (allways run these 3 commands, when ever we change in models.py)
 python manage.py migrate
 python manage.py makemigrations [app_name: in which app we need to add models changes, if we do not give the app name, then it will do makemigrations to whole project ]
 python manage.py migrate

5. Now, we have succesfully created database in sql-lite3.

7. models have some other usefull parameters
8. by default all parameter value is false, but we can set those to true.
9. NULL, by default-> null= false, means value can not be null. But we can set it to True-> can set to be null.
10. BLANK, by default-> null= false, means value can not be blank. If you only set blank=True, then we can keep that fill blank


```
## default values:
columnName = models.CharField(max_length=120, default="" , null=False , blank= False)
## but we can:
columnName = models.CharField(max_length=120 null=True , blank= True) 

Example For img field:
img1= models.ImageField(upload_to='images/post',default='demo.png',blank=True) #img1 will be uploaded to 'media/images/post' folder
# to set media folder in django project: see 'media folder add to keep iser input file or image.md' folder
```

11. choices, Structure--> ('value for database', "value will show to user")
```
# we need to use tulpes data structure to keep the choices:
# example 1:(for charecter value)
    choice =(
            ('', 'Location'),
            ('Dhamrai', 'Dhamrai'),
            ('Dhanmondi', 'Dhanmondi'),
            ('Gulshan', 'Gulshan'),
            ('Jatrabari', 'Jatrabari'),
            ('Keraniganj', 'Keraniganj'),
            )
    location = models.CharField(max_length=120, null=False , blank= False, choices= choice)

# example 2 for integer value
    choice = (
        (None, 'rating'),
        (1, 'worst'),
        (2, 'bad'),
        (3, 'not good'),
        (4, 'good'),
        (5, 'excellent'),
    )
    num_stars =models.IntegerField(choices=choice)
    
    def __str__(self): #function to_string
        value,char= self.choice [self.num_stars]
        return self.name+ " "+ char
    
    def getRating(self): # Get the actuall String value from choices list
        value, char = self.choice[self.num_stars]
        return char
```

12. User Auth model: 

```
from django.conf import settings
# Create your models 'Status' with one to many relation ship with user model.
class Status(models.Model):
      user =models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
	  
#Or : we can use:
from django.contrib.auth.models import User # importing the User model for using authrization
                                            # we will use username, email, password from this Model

class UserInfo(models.Model): #one to one relation                               # To extend the information for User model we are creating another model which will be one_to_one relation-ship with user model
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True) # connect user model in one_To_one relationship

```


13. image field:
