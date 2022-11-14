# # photo model
#
# from django.core.validators import MinLengthValidator
from django.core.validators import MinLengthValidator
from django.db import models
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_image_size_less_than_5mb


#
# from petstagram.pets.models import Pet
# from petstagram.photos.validators import validate_image_size_less_than_5mb
#
# '''
# The field Photo is required:
# •	Photo - the user can upload a picture from storage, the maximum size of the photo can be 5MB
# The fields description and tagged pets are optional:
# •	Description - a user can write any description of the photo; it should consist of a maximum
#     of 300 characters and a minimum of 10 characters
# •	Location - it should consist of a maximum of 30 characters
# •	Tagged Pets - the user can tag none, one, or many of all pets. There is no limit on the number
#     of tagged pets
# There should be created one more field that will be automatically generated:
# •	Date of publication - when a picture is added or edited, the date of publication is automatically
#     generated
# Note that the photo field has additional validation for a maximum size of 5MB. We should create a
# custom validator to validate the requirement. Let us create a new validators.py file in the photos app:
# '''
#
#
# class Photo(models.Model):
#     MAX_DESCRIPTION_LENGTH = 300
#     MIN_DESCRIPTION_LENGTH = 10
#
#     MAX_LOCATION_LENGTH = 30
#
#     photo = models.ImageField(
#         null=False,
#         blank=True,
#         # Validator for max size 5mb - in validators.py
#         validators=(validate_image_size_less_than_5mb,),
#     )
#
#     description = models.CharField(
#         max_length=MAX_DESCRIPTION_LENGTH,
#         null=True,
#         blank=True,
#         # MIN LENGTH
#         validators=(
#             MinLengthValidator(MIN_DESCRIPTION_LENGTH),
#         )
#     )
#
#     location = models.CharField(
#         max_length=MAX_LOCATION_LENGTH,
#         null=False,
#         blank=True,
#     )
#
#     date_of_publication = models.DateField(
#         auto_now=True,
#         null=False,
#         blank=True,
#     )
#
#     # FK -none(blank=True) one, or many of all pets
#     tagged_pets = models.ManyToManyField(
#         Pet,
#         blank=True,
#     )
#
#     #
#     # def __str__(self):
#     #     return self.description
#
#     def __str__(self):
#         return self.description


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='images',
        validators=(validate_image_size_less_than_5mb,)
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(auto_now=True, )

    def __str__(self):
        return f"{self.photo}"
