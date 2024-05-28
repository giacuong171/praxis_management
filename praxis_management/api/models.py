from django.db import models
from django.contrib.auth.models import AbstractUser
#from ckeditor.fields import RichTextField
# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="upload/%y/%m")

PATIENT_TYPES= [
    ("N",'KH mới'),
    ("R","KH thân quen")
]

GENDER_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác'),
    ]

class Personality(models.Model):
    class Meta:
        abstract=True
        unique_together = ("first_name","last_name","phone_number")

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(blank=True)
    address = models.CharField(max_length=255,null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Doctor(Personality):
    specialization = models.CharField(max_length=255)
    medical_school = models.CharField(max_length=255, null=True)
    certifications = models.TextField(blank=True)
    photo = models.ImageField(upload_to='upload/doctors/%y/%m', blank=True, null=True)
    biography = models.TextField(blank=True)

class Nurse(Personality):
    specialization = models.CharField(max_length=255)


class Patient(Personality):
    class Meta:
        ordering = ["-created_date"]
    created_date = models.DateField(auto_now_add=True)
    active=models.BooleanField(default=True)
    description = models.TextField(blank=True)
    process = models.TextField(blank=True)
    paid = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    total_due = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    next_appointment = models.DateField()
    patient_type = models.CharField(max_length=1, choices=PATIENT_TYPES)
    discount = models.DecimalField(max_digits=2, decimal_places=1)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    nurses = models.ManyToManyField(Nurse, related_name='patients')
    x_ray = models.ImageField(upload_to='upload/doctors/%y/%m', blank=True, null=True)

    @property
    def actual_pay(self):
        return self.total_due * (100 - self.discount) / 100

    @property
    def fully_paid(self):
        if self.patient_type == "N":
            return self.paid >= self.total_due
        elif (self.patient_type == "R"):
            return self.paid >= (self.total_due * (100 - self.discount) / 100)
