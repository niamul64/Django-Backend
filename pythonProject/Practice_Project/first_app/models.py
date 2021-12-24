from django.db import models
from django.utils import timezone

class Musician(models.Model):
    #id = models.AutoField(Primary_key=True)  # But we dont need this id field. its genarated by django automaticaly.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self): #function to_string
        return self.first_name+" "+ self.last_name

class Album(models.Model):
    # id = models.AutoField(Primary_key=True)  # But we dont need this id field. its genarated by django automaticaly.
    artist = models.ForeignKey(Musician, on_delete= models.CASCADE) # By using on on_delete: if Musician object deleted then coresponding album obj will also deleted
    name= models.CharField(max_length=100)
    release_date = models.DateField()
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
    def getRating(self):
        value, char = self.choice[self.num_stars]
        return char
