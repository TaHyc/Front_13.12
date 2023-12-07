# Generated by Django 4.2.6 on 2023-12-07 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0058_remove_waterconsumption_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_inform',
            name='active',
            field=models.CharField(choices=[('L', 'Малоактивный'), ('M', 'Активный')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='goals',
            field=models.CharField(choices=[('L', 'Снижение веса'), ('M', 'Набор веса'), ('F', 'Поддержание веса')], default='L', max_length=1),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='sex',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('', '')], default='', max_length=1),
        ),
    ]
