# Generated by Django 4.1.2 on 2022-10-31 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_aboutpage_image_delete_aboutpagegalleryimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='wagtailimages.Image'),
        ),
    ]
