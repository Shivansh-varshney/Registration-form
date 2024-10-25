import os
from django.db import models
from django.contrib.auth.models import User

# create your models here

class Family_detail(models.Model):
    father_occupations_choices = [
        ('Goverment Employee','Goverment Employee'),
        ('Private Sector','Private Sector'),
        ('Professional','Professional'),
        ('Self-Employed','Self-Employed'),
        ('Unemployed','Unemployed')
    ]

    mother_occupations_choices = [
        ('Goverment Employee','Goverment Employee'),
        ('Private Sector','Private Sector'),
        ('Professional','Professional'),
        ('Self-Employed','Self-Employed'),
        ('Home Maker','Home Maker')
    ]

    annual_income_choices = [
        ('below 4 lakh', 'below 4 lakh'),
        ('between 4 to 8 lakh','between 4 to 8'),
        ('more than 8 lakhs','more than 8 lakhs')
    ]

    username = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=20,choices=father_occupations_choices)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=20,choices=mother_occupations_choices)
    annual_income = models.CharField(max_length=20, choices=annual_income_choices)

    def __str__(self):
        return self.username
    
class Personal_detail(models.Model):
    identity_choices = [
        ('pan card','Pan Card'),
        ('ration card','Ration Card'),
        ('passport','Passport'),
        ('adhar card','Adhar Card'),
        ('other','Other Id')
    ]

    gender_choices = [
        ('male','Male'),
        ('female','Female'),
        ('others','Others')
    ]

    reservation_choices = [
        ('unreserved','Unreserved'),
        ('ews','EWS'),
        ('sc','SC'),
        ('st','ST'),
        ('obc','OBC')
    ]

    special_reservation_choices = [
        ('none','None'),
        ('k-migrant','Kashmir Migrant'),
        ('staff quota','Staff Quota'),
        ('sports','Sports Quota'),
        ('pwd','PWD')
    ]

    username = models.CharField(max_length=50, null= True)
    identity = models.CharField(max_length=12,choices= identity_choices)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=6, choices=gender_choices)
    mobile = models.CharField(max_length=14)
    correspondance_address = models.CharField(max_length=500) #correspondance address
    permanent_address = models.CharField(max_length=500) #permanent address
    reservation = models.CharField(max_length=10,choices=reservation_choices)
    special_reservation = models.CharField(max_length=12,choices=special_reservation_choices)

    def __str__(self):
        return self.username
    
class school_detail(models.Model):
    username = models.CharField(max_length=50, null= True)
    board = models.CharField(max_length=500)
    rollnumber = models.CharField(max_length=25)
    result_status = models.CharField(max_length=10, choices=[('pass','Passed'),('appearing','Appearing')])
    school_type = models.CharField(max_length=16,choices=[('private','Private'),('government','Government'),('semi-government','Semi-government')])
    school_name = models.CharField(max_length=250)
    medium = models.CharField(max_length=8, choices=[('hindi','Hindi'),('english','English'),('other','Other')])
    
    def __str__(self):
        return self.username

class subject_mark(models.Model):

    subjects = [
        ('maths','Mathematics'),
        ('english','English'),
        ('hindi','Hindi'),
        ('sanskrit','Sanskrit'),
        ('comp','Computer Science'),
        ('physics','Physics'),
        ('chemistry','Chemistry'),
        ('bio','Biology'),
        ('accounts','Accounts'),
        ('economics','Economics'),
        ('business','Business Studies'),
        ('physical','Physical Sciences'),
        ('history','History'),
        ('geography','Geography'),
        ('psychology','Psychology'),
        ('political','Political Science')
    ]

    username = models.CharField(max_length=50, null= True)
    subject1 = models.CharField(max_length=10, choices=subjects)
    maximum_marks_Sub1 = models.CharField(max_length=4) # maximum marks for subject 1
    obtained_marks_Sub1 = models.CharField(max_length=4) # marks obtained in subject 1
    
    subject2 = models.CharField(max_length=10, choices=subjects)
    maximum_marks_Sub2 = models.CharField(max_length=4) #maximum marks for subject 2
    obtained_marks_Sub2 = models.CharField(max_length=4) # marks obtained in subject 2

    subject3 = models.CharField(max_length=10, choices=subjects)
    maximum_marks_Sub3 = models.CharField(max_length=4) #maximum marks for subject 3
    obtained_marks_Sub3 = models.CharField(max_length=4) # marks obtained in subject 3

    subject4 = models.CharField(max_length=10, choices=subjects)
    maximum_marks_Sub4 = models.CharField(max_length=4) #maximum marks for subject 4
    obtained_marks_Sub4 = models.CharField(max_length=4) # marks obtained in subject 4

    subject5 = models.CharField(max_length=10, choices=subjects)
    maximum_marks_Sub5 = models.CharField(max_length=4) #maximum marks for subject 5
    obtained_marks_Sub5 = models.CharField(max_length=4) # marks obtained in subject 5

    def __str__(self):
        return self.username

class bank_detail(models.Model):
    username = models.CharField(max_length=50, null= True)
    accound_holder_name = models.CharField(max_length=70)
    account_number = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username

class progressreport(models.Model):
    username = models.CharField(max_length=50, null=True)
    family_detail = models.BooleanField(default = False)
    personal_detail = models.BooleanField(default = False)
    education = models.BooleanField(default = False)
    bank_detail = models.BooleanField(default = False)

    def __str__(self):
        return self.username