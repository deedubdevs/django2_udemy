# Generated by Django 2.0.2 on 2018-10-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181002_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='Date published',
            new_name='pub_date',
        ),
    ]
