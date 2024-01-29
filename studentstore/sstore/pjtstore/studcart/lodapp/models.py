from django.db import models

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    DEPARTMENT_CHOICES = [
        ('CS', 'Computerscience'),
        ('IT', 'Information Technology'),
        ('BS', 'BiologyScience'),
        ('CM', 'Commerce'),
        # Add more choices as needed
    ]
    COURSE_CHOICES = [
        ('BBA', 'Bachelor of business administration'),
        ('Bcom', 'Bachelor of commerce'),
        ('CHEM', 'Chemistry'),
        ('BIO', 'Biology'),
        ('ENG', 'English'),

    ]
    PURPOSE_CHOICES = [
        ('Enquiry', 'Enquiry'),
        ('Placeorder', 'Placeorder'),
        ('Return', 'Return'),

    ]
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    address = models.TextField()
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)

    def __str__(self):
        return self.name
