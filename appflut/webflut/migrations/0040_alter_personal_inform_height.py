# Generated by Django 4.2.4 on 2023-10-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0039_alter_personal_inform_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_inform',
            name='height',
            field=models.FloatField(default=0),
        ),
    ]