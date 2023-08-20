# Generated by Django 4.2.4 on 2023-08-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_appliances_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='appliances_sub_category',
            field=models.ManyToManyField(to='category.appliancessubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='electronics_sub_category',
            field=models.ManyToManyField(to='category.electronicssubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='fashion_sub_category',
            field=models.ManyToManyField(to='category.fashionsubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sports_and_leisure_sub_category',
            field=models.ManyToManyField(to='category.sportsandleisuresubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='watches_sub_category',
            field=models.ManyToManyField(to='category.watchessubcategory'),
        ),
    ]