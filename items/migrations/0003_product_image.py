# Generated by Django 4.1.6 on 2023-03-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_category_rename_company_companie_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, default="avatar.svg", null=True, upload_to=""
            ),
        ),
    ]
