# Generated by Django 4.2.4 on 2023-08-06 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, height_field='product_image_height', null=True, upload_to='products/<function uuid4 at 0x000001BCD6C949D0>/', width_field='product_image_width'),
        ),
    ]
