# Generated by Django 4.2.4 on 2023-10-25 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0030_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]