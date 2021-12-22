from django import forms
from django.core import validators
from first_app.models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model= Musician
        fields = "__all__"  #    For all fields


def even_number_check(value):
    if value % 2 == 1:
        raise forms.ValidationError("Please Insert an Even Number")

class Validator(forms.Form):
    name_field= forms.CharField(validators=[validators.MaxLengthValidator(20), validators.MinLengthValidator(10)])
    number_field=forms.IntegerField(validators=[validators.MaxValueValidator(15),validators.MinValueValidator(5)])
    number_even= forms.IntegerField(validators=[even_number_check])

class Email_match_Check(forms.Form):
    email = forms.EmailField()
    email_varification = forms.EmailField()
    def clean(self):
        all_cleaned_data= super().clean() # Now this super() will take all the values of fields and store to the 'all_cleaned_data' variable
        #all_cleaned_data grabs the value of to email fields.
        email1= all_cleaned_data['email']
        email2= all_cleaned_data['email_varification']

        if email1 !=email2:
            raise forms.ValidationError("Fields are not matched!")



class Mucician(forms.Form):
    first_name= forms.CharField(label='First Name',  widget =forms.TextInput(attrs={'placeholder': "Enter your first name ", 'style':'width:300px;'}) )
    last_name= forms.CharField(error_messages={'required': 'Please enter your name'})
    email= forms.EmailField()
    name = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])
    date_of_birth=forms.DateField(widget= forms.TextInput(attrs={
        'type':'date',
    }))

class Form_fields(forms.Form):
    boolean_field = forms.BooleanField(required=False)          # its a check box input
    char_field=forms.CharField(max_length=20,min_length=5)

    # sturcture of tuple--> ('value for database', 'value to show user')
    choice = (
        (None, 'rating'),
        (1, 'worst'),
        (2, 'bad'),
        (3, 'not good'),
        (4, 'good'),
        (5, 'excellent'),
    )
    choice_field= forms.ChoiceField(choices=choice)
    redio_button =forms.ChoiceField(choices=choice, widget= forms.RadioSelect) # by 'RadioSelect' built in widget we can make it redio button
    Multiple_Choice=forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)   # values will come as a list ['1', '2']