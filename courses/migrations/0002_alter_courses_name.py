# Generated by Django 4.1.7 on 2023-03-30 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
