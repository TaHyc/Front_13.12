# Generated by Django 4.2.4 on 2023-10-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webflut', '0003_breakfast_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_product',
            name='calories_in',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='carbohydrates',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='fats',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='add_product',
            name='proteins',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personal_inform',
            name='weight',
            field=models.IntegerField(),
        ),
    ]