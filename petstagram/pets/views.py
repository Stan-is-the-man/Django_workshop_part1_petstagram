from django.shortcuts import render


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


# adding extra variables username and pet_name, so the url can be displayed for testing

def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')


def details_pet(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')


def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')
