# Generated by Django 4.1.2 on 2022-10-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0003_alter_aboutpagegalleryimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='AboutPageGalleryImage',
        ),
    ]