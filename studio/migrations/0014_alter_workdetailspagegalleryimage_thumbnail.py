# Generated by Django 4.1.2 on 2022-10-31 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('studio', '0013_workdetailspage_rename_body_workpage_intro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdetailspagegalleryimage',
            name='thumbnail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnailimages', to='wagtailimages.image'),
        ),
    ]
