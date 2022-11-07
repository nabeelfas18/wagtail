# Generated by Django 4.1.2 on 2022-10-31 08:31

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('studio', '0006_remove_aboutpage_image_aboutpagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpage',
            name='description',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='workpage',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='workpage',
            name='subtitle',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.CreateModel(
            name='workPageGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='studio.workpage')),
                ('thumbnail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnailimages', to='wagtailimages.image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
