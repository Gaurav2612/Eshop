# Generated by Django 4.0.5 on 2023-01-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_checkout_paymentstatus_alter_checkout_orderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='orderstatus',
            field=models.CharField(blank=True, default='Not ', max_length=20, null=True),
        ),
    ]
