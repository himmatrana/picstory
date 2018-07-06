from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext as _
from django.conf import settings
from .managers import UserManager

class CustomAbstractUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        abstract = True


class User(CustomAbstractUser):

    email = models.EmailField(verbose_name='Email ID', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #image = FileBrowseField(verbose_name = _('Profile Image'), max_length=255, null=True)
    name = models.CharField(verbose_name=_('Name'), blank=True, null=True, max_length=255)
    date_joined = models.DateTimeField(_('date_joined'), auto_now_add=True)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['modified_date']
