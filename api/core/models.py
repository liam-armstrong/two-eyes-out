from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.http import HttpResponse 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re, time

class sectionManager(models.Manager):
    
    def is_valid_section(self, a, b, c):
        # General function plugs in section information to a link and tests that it is not a blank page
        link = 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + a + '&course=' + b + '&section=' + c
        raw_html = urlopen(link, timeout = 5)
        html = BeautifulSoup(raw_html, "lxml")
        return re.search("Outline/Syllabus", html.get_text()) != None

    def create(self, dept, code, sect):
        if not sectionManager().is_valid_section(dept, code, sect):
            raise ValueError("Not a valid course")
        section = self.model(dept = dept, code = code, sect = sect)
        section.save()
        return section

class section(models.Model):
    # Model to represent a UBC course section
    dept = models.CharField(max_length = 5) # ex. CPSC
    code = models.CharField(max_length = 5) # ex. 110
    sect = models.CharField(max_length = 5) # ex. 101
    open_seats = models.BooleanField(default = False) # True if open General Seats
    objects = sectionManager() # Sets use of our custom manager as defined above

    class Meta:
        # Forces section entries to be unique at a DB level
        unique_together = ('dept', 'code', 'sect')

    def __str__(self):
        return self.dept + " " + self.code + " " + self.sect

    def get_link(self):
        # Returns link to course section
        return 'https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=' + str(self.dept) + '&course=' + str(self.code) + '&section=' + str(self.sect)

    def update_seats(self):
        # Scrapes webpage for course entry and returns a boolean value representing if general seats are open
        raw_html = urlopen(self.get_link(), timeout = 5) # urllib to get unrefined html
        html = BeautifulSoup(raw_html, "lxml") # BeautifulSoup to refine html TODO Check if this is required for RE search to work 
        gen_table_line = re.search(r"General Seats Remaining:\d+",html.get_text()).group(0) # Pulls table line displaying open gen seats
        open_seats = int(re.search(r'\d+', gen_table_line).group(0)) > 0 #pulls int from line and checks if it's not 0
        self.save(update_fields=["open_seats"], force_update=True) #updates boolean value for section
        return open_seats

class customUserManager(BaseUserManager):
    # Custom user manager to handle our custom user
    def create_user(self, email, password, **args):
        #Creates and saves user with given email and password
        if not email:
            raise ValueError("Email field is required")
        email = self.normalize_email(email)
        user = self.model(email = email, **args)
        user.set_password(password)
        user.save()
        return user     
    def create_superuser(self, email, password, **args):
        #creates user same way as above but with elevated privlages for Django Auth
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
    sections = models.ManyToManyField(section)
    is_staff = models.BooleanField(
        #Django auth default field
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        #Django auth default field
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email' #specified so users can sign in with email
    objects = customUserManager() #sets use of our custom manager as defined above

    class Meta: # Required for Django Auth
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
