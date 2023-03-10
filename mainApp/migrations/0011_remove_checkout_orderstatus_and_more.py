# Generated by Django 4.0.5 on 2023-01-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_remove_checkoutproducts_product_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='orderstatus',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='paymentmode',
        ),
        migrations.AddField(
            model_name='checkout',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='status',
            field=models.IntegerField(choices=[(1, 'Not Packed'), (2, 'Packed'), (3, 'Out for Delievery'), (4, 'Delivered')], default=1),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='paymentstatus',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Done')], default=1),
        ),
    ]
