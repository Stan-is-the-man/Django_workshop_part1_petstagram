# Generated by Django 4.1.1 on 2022-10-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0005_alter_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date_of_birth',
            field=models.DateField(blank=True, editable=False, null=True),
        ),
    ]
