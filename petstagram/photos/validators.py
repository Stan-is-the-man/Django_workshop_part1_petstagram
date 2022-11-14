
from django.core.exceptions import ValidationError


def validate_image_size_less_than_5mb(image):
# #filter for image size field -
# copy/paste from stackoverflow - hardcode for 5mb

    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError(f"Max file size is {megabyte_limit}MB %")
#
# def validate_size_is_max_5mb(image):
#     current_size = image.file.size
#     mg_limit = 5
#     if current_size > mg_limit*1024*1024:
#         raise ValidationError(f"Max size of an image is {mg_limit}mb %")
















