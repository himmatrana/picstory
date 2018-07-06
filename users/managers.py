from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            #date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email, password=password)
        u.is_staff = True
        u.is_superuser = True
        u.save(using=self._db)
        return u

    def get_user(self, email):
        try:
            return self.filter(email=email)
        except self.ObjectDoesNotExist:
            return None

