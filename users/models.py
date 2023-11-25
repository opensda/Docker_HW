from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {"null": True, "blank": True}


class UserRoles(models.TextChoices):
    MEMBER = "member", _("member")


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=35, verbose_name="номер телефона", **NULLABLE)
    city = models.CharField(max_length=70, verbose_name="город", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)
    chat_id = models.CharField(
        unique=True, max_length=250, verbose_name="id чата", **NULLABLE
    )
    role = models.CharField(
        max_length=15,
        choices=UserRoles.choices,
        verbose_name="роль",
        default=UserRoles.MEMBER,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
