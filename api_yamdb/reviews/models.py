from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_username

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'
USER_RU = 'юзер'
MODERATOR_RU = 'модератор'
ADMIN_RU = 'админ'
ROLES = (
    (USER, USER_RU),
    (MODERATOR, MODERATOR_RU),
    (ADMIN, ADMIN_RU),
)


class User(AbstractUser):
    username = models.CharField(validators=(validate_username,),
                                max_length=150,
                                unique=True,
                                blank=False,
                                null=False,)
    email = models.EmailField(verbose_name='E-Mail',
                              unique=True,
                              max_length=254,)
    bio = models.TextField(verbose_name="О себе",
                           blank=True,
                           null=True,
                           max_length=300,)
    first_name = models.CharField('имя',
                                  max_length=150,
                                  blank=True)
    last_name = models.CharField('фамилия',
                                 max_length=150,
                                 blank=True)
    role = models.CharField(verbose_name='Уровень доступа',
                            choices=ROLES,
                            default=USER,
                            max_length=50)

    @property
    def is_user(self):
        return self.role == USER

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    def __str__(self):
        return self.username


class Categories(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.TextField(max_length=256)
    slug = models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.name