from django.contrib import admin

from petstagram.photos.models import Photo


# from petstagram.photos.models import Photo
#
#
# @admin.register(Photo)
# class PhotosAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'date_of_publication', 'get_tagged_pets',)
#
#     # We cannot list a Many-to-Many field, but we can list the result of a function that gets all objects
#     # from a Many-to-Many field and concatenate their names in a string:
#     @staticmethod
#     def get_tagged_pets(current_photo_obj):
#         already_tagged_pets = current_photo_obj.tagged_pets.all()
#         if already_tagged_pets:
#             return ', '.join(pet.name for pet in already_tagged_pets)
#         return 'No tagged pets at this picture'

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(photo_obj):
        all_tagged_pets = photo_obj.tagged_pets.all()
        result = (pet.name for pet in all_tagged_pets)
        return ', '.join(result)
