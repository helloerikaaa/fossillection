# Generated by Django 3.1 on 2020-08-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinoapp', '0003_auto_20200806_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meteor',
            name='photo',
            field=models.ImageField(upload_to='assets/meteors'),
        ),
    ]
