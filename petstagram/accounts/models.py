from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from helpers.choices import GenderChoices
from helpers.validators import name_has_only_letters


class PetstagramUser(AbstractUser):
    # take all fields from AbstractUser, but override the following fields:
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=[
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            name_has_only_letters,
        ]
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=[
            MinLengthValidator(MIN_LEN_LAST_NAME),
            name_has_only_letters,
        ]
    )

    email = models.EmailField(unique=True, )

    profile_picture = models.URLField()

    gender = models.CharField(
        choices=GenderChoices.choices,
        max_length=12,
    )
