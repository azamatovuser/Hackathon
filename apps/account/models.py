from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError(_('User should have a username'))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if password is None:
            raise TypeError(_('Password should not be None'))

        user = self.create_user(
            username=username,
            password=password,
            **extra_fields,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Country(models.Model):
    title = models.CharField(max_length=221)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country')
    title = models.CharField(max_length=221)


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    ROLE = (
        (0, 'stuff'),
        (1, 'user'),
        (2, 'seller'),
    )
    username = models.CharField(max_length=50, unique=True, verbose_name=_('Username'), db_index=True)
    email = models.EmailField(max_length=50, unique=True, verbose_name=_('Email'), db_index=True, null=True, blank=True)
    full_name = models.CharField(max_length=50, verbose_name=_('Full name'), null=True)
    image = models.ImageField(upload_to='accounts/', verbose_name=_('Account image'), null=True, blank=True)
    role = models.IntegerField(choices=ROLE, default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, related_name='city')
    is_superuser = models.BooleanField(default=False, verbose_name=_('Super user'))
    is_staff = models.BooleanField(default=False, verbose_name=_('Staff user'))
    is_active = models.BooleanField(default=True, verbose_name=_('Active user'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=_('Date modified'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date created'))

    objects = AccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.full_name:
            return f'{self.full_name} ({self.username})'
        return f'{self.username}'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'

    @property
    def image_url(self):
        if self.image:
            if settings.DEBUG:
                return f'{settings.LOCAL_BASE_URL}{self.image.url}'
            return f'{settings.PROD_BASE_URL}{self.image.url}'
        else:
            return None

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data