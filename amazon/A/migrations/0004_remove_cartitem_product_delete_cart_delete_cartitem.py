# Generated by Django 4.2.5 on 2023-09-22 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('A', '0003_remove_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
