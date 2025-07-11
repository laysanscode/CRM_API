# Generated by Django 5.1.7 on 2025-06-16 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_department_users_data'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Category_img',
            field=models.ImageField(upload_to='media/Category/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='Dealer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.users_data'),
        ),
        migrations.AlterField(
            model_name='products',
            name='Products_img',
            field=models.ImageField(upload_to='media/Products/'),
        ),
    ]
