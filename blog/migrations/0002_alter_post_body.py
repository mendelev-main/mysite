# Generated by Django 4.2.2 on 2023-07-20 11:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="body",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
