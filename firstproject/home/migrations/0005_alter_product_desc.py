# Generated by Django 4.2.4 on 2023-08-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=5000),
        ),
    ]
