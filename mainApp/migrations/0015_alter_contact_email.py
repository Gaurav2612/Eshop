# Generated by Django 4.0.5 on 2023-01-29 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0014_contact_alter_newslatter_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
