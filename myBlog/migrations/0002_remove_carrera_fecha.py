# Generated by Django 4.2.9 on 2024-01-28 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrera',
            name='fecha',
        ),
    ]