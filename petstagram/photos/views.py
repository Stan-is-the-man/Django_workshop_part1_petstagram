from copy import copy

from django.shortcuts import render, resolve_url, redirect


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def details_photo(request, pk):
    return render(request, 'photos/photo-details-page.html')


def edit_photo(request, pk):
    return render(request, 'photos/photo-edit-page.html')