# Generated by Django 4.1.1 on 2022-11-10 13:24

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_alter_photo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='images', validators=[petstagram.photos.validators.validate_image_size_less_than_5mb]),
        ),
    ]