# Generated by Django 4.2.4 on 2023-08-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, height_field='product_image_height', null=True, upload_to='products/d1b5abaaf4af43578b96626f4a2089f7/', width_field='product_image_width'),
        ),
    ]