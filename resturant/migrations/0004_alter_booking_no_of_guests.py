# Generated by Django 4.1 on 2023-07-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0003_menuitem_delete_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.SmallIntegerField(),
        ),
    ]
