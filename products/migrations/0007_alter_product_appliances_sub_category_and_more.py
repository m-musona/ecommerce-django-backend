# Generated by Django 4.2.4 on 2023-08-20 07:57

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_appliances_sub_category_and_more'),
        ('products', '0006_alter_product_appliances_sub_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='appliances_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.appliancessubcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='electronics_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.electronicssubcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='fashion_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.fashionsubcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, height_field='product_image_height', null=True, upload_to=products.models.product_image_path, width_field='product_image_width'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sports_and_leisure_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.sportsandleisuresubcategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='watches_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.watchessubcategory'),
        ),
    ]
