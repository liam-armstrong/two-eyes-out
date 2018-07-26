from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re, time

class section(models.Model):
    dept = models.CharField(max_length = 5)
    code = models.CharField(max_length = 5)
    sect = models.CharField(max_length = 5)
    def __str__(self):
        return self.dept + " " + self.code + " " + self.sect

    def get_link(self):
        return 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + str(self.dept) + '&course=' + str(self.code) + '&section=' + str(self.sect)
    
    # write this function and have it validate section before saving to DB
    # def is_valid_section(self):

    def open_gen_seats(self):
        raw_html = urlopen(self.get_link(), timeout = 5)
        html = BeautifulSoup(raw_html, "lxml")
        gen_table_line = re.search(r"General Seats Remaining:\d+",html.get_text()).group(0)
        return int(re.search(r'\d+', gen_table_line).group(0)) > 0

class customUserManager(BaseUserManager):
    # Custom user manager to handle our custom user
    def create_user(self, email, password, **args):
        #creates and saves user with given email and password
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **args)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **args):
        args.setdefault('is_staff', True)
        args.setdefault('is_superuser', True)
        args.setdefault('is_active', True)
        if args.get('is_staff') is not True:
            raise ValueError("is_staff must be True")
        if args.get('is_superuser') is not True:
            raise ValueError("is_superuser must be True")
        return self.create_user(email, password, **args)

class customUser(AbstractBaseUser, PermissionsMixin):
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
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    objects = customUserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

class userProfile(models.Model):
    profile = models.OneToOneField(
        userProfile,
        on_delete=models.CASCADE,
    )
    sections = models.ManyToManyField(section)