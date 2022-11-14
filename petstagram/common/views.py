from django.shortcuts import render, redirect, resolve_url

from petstagram.common.models import Like
from petstagram.photos.models import Photo
from pyperclip import copy


def show_home_page(request):
    all_photos = Photo.objects.all().distinct()

    context = {
        "all_photos": all_photos
    }
    return render(request, 'common/home-page.html', context)


# functionality to like a photo
# def like_functionality(request, photo_id):
#     # Call to DB and create a new object with the given kwargs, saving it to the database
#     # and returning the created object.
#     Photo.objects.create(photo_id=photo_id)
#     # from Word descr.
#     return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()

    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    # това чудо се пише така
    host_name = request.META.get('HTTP_HOST')
    pet_photo_url = resolve_url('details photo', photo_id)

    # tук копира в клипборда пътя до снимката. за да те върне/редиректне към нея
    copy(host_name + pet_photo_url)

    # 'HTTP_REFERER' гърмеше, защото нямахме страница 'от' която сме кликнали на линка
    # ще е по-интересно да достъпиш линка от друг адрес, защото после ще те върне на самата снимк, това е идеята тук
    return redirect(request.META['HTTP_REFERER']  + f'#{photo_id}')





#