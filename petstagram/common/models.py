# # common models
# from django.db import models
#
# from petstagram.photos.models import Photo
#
# '''
# ''
# The field Comment Text is required:
# •	Comment Text - it should consist of a maximum of 300 characters
# An additional field should be created:
# •	Date and Time of Publication - when a comment is created (only), the date of publication is automatically generated
# One more thing we should keep in mind is that the comment should relate to the photo (as in social apps users comment
# on a specific photo/post, i.e., the comment object is always connected to the photo object).
#
# Finally, create the Like model which should connect one photo to one user. However, we do not have a user object,
# so we will just create the model and add the photo relation:
#
# '''
#
#
# class PhotoComment(models.Model):
#     MAX_COMMENT_TEXT = 300
#
#     comment_text = models.CharField(max_length=MAX_COMMENT_TEXT)
#     publication_date_and_time = models.DateTimeField(auto_now_add=True)
#     to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
#
#
# class PhotoLike(models.Model):
#     # CASCADE - when deleting a photo, the likes also should be deleted
#     to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


# common models


from django.db import models
from petstagram.photos.models import Photo


class Comment(models.Model):
    MAX_TEXT_LEN = 300
    text = models.CharField(max_length=MAX_TEXT_LEN)
    date_and_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CharField,
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
    )
