# Generated by Django 4.2.4 on 2023-08-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_appliancessubcategory_electronicssubcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='appliances_sub_category',
            field=models.ManyToManyField(to='products.appliancessubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='electronics_sub_category',
            field=models.ManyToManyField(to='products.electronicssubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='fashion_sub_category',
            field=models.ManyToManyField(to='products.fashionsubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='sports_and_leisure_sub_category',
            field=models.ManyToManyField(to='products.sportsandleisuresubcategory'),
        ),
        migrations.AlterField(
            model_name='category',
            name='watches_sub_category',
            field=models.ManyToManyField(to='products.watchessubcategory'),
        ),
    ]
