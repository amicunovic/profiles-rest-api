from django.db import models
from django.contrib.auth.models import AbstractBaseUser #add custom user requirements for profiles
from django.contrib.auth.models import PermissionsMixin #add permissions to user models, what user can and can't do
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)  #it will encrypt the password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password): #administrator user, has a full controll
        """Creates and saves a new superuser with given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' #This is set as required by default as it is a username
    REQUIRED_FIELDS = ['name'] #Set required fields as a list of strings

    def get_full_name(self): #returns the full name of the user
        """Used to get users full name."""

        return self.name

    def get_short_name(self): #also returns the full name of the user, since in this case we have one filed for name and surname
        """Used to get users short name"""

        return self.name

    def __str__(self): #return a object as a string
        """Django uses this when it needs to convert the object to a string"""

        return self.email
