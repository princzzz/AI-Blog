# Generated by Django 3.1.7 on 2021-06-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='address',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]