# Generated by Django 4.1.7 on 2023-03-29 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Kurs Adını yazınız', max_length=200, unique=True, verbose_name='Kurs Adı')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(default='courses/default-image.jpg', upload_to='courses/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
