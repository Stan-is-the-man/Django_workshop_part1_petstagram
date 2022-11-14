from django.shortcuts import render

from petstagram.pets.models import Pet


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


# adding extra variables username and pet_name, so the url can be displayed for testing
# pet_slug instead pet_name ?????????
def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')


def details_pet(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')


def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def show_pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context)
