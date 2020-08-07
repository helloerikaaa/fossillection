# Generated by Django 3.1 on 2020-08-05 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fossil',
            name='photo',
            field=models.ImageField(upload_to='assets/fossils'),
        ),
        migrations.AlterField(
            model_name='meteor',
            name='photo',
            field=models.ImageField(upload_to='assets/meteors'),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='photo',
            field=models.ImageField(upload_to='assets/minerals'),
        ),
        migrations.AlterField(
            model_name='rock',
            name='photo',
            field=models.ImageField(upload_to='assets/rocks'),
        ),
    ]