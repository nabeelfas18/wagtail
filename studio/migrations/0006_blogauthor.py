# Generated by Django 4.1.2 on 2022-11-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studio", "0005_remove_emailorderables_author_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogAuthor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100, null=True)),
            ],
        ),
    ]