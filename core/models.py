from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re, time

class section:
    def __init__(self, dept, course_code, sect):
        self.dept = dept
        self.course_code = course_code
        self.sect = sect
        self.link = 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + str(self.dept) + '&course=' + str(self.course_code) + '&section=' + str(self.sect)
    def __str__(self):
        return self.dept + " " + self.course_code + " " + self.sect
    def open_gen_seats(self):
        raw_html = urlopen(self.link, timeout = 5)
        html = BeautifulSoup(raw_html, "lxml")
        gen_table_line = re.search(r"General Seats Remaining:\d+",html.get_text()).group(0)
        return int(re.search(r'\d+', gen_table_line).group(0)) > 0

class newBaseUserManager(BaseUserManager):
    # Custom user manager to handle our custom user
    def _create_user(self, email, password, **extra):
        #creates and saves user with given email and password
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra)
        user.set_password(password)
        user.save()
        return user
    def _create_superuser(self, email, password, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_active', True)
        if extra.get('is_staff') is not True:
            raise ValueError("is_staff must be True")
        if extra.get('is_superuser') is not True:
            raise ValueError("is_superuser must be True")
        return self._create_user(email, password, **extra)

class User(AbstractBaseUser, PermissionsMixin):
    #Custom user for Django Auth with email as username and fields removed
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = newBaseUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
