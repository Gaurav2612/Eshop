# Generated by Django 4.0.5 on 2023-01-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0013_remove_checkout_orderstatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Done')], default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='newslatter',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
