# Generated by Django 4.1.2 on 2022-11-16 05:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("studio", "0002_remove_formfield_page_remove_formfield_page_ptr_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogdetailspage",
            name="blog_abstract",
            field=ckeditor.fields.RichTextField(blank=True, max_length=500),
        ),
    ]