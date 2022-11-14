from django.contrib import admin

from petstagram.common.models import Comment, Like


# from petstagram.common.models import PhotoComment, PhotoLike
#
#
# @admin.register(PhotoComment)
# class PhotoCommentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(PhotoLike)
# class PhotoLikeAdmin(admin.ModelAdmin):
#     pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_and_time_of_publication')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


