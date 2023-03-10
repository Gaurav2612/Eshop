# Generated by Django 4.0.5 on 2023-01-17 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pic', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Newslatter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('basePrice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('finalPrice', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('stock', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('pic1', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('pic2', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('pic3', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('pic4', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('addressline1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('addressline3', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('pic', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory'),
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(blank=True, default=0, null=True)),
                ('shipping', models.IntegerField(blank=True, default=0, null=True)),
                ('final', models.IntegerField(blank=True, default=0, null=True)),
                ('mode', models.CharField(blank=True, default='COD', max_length=20, null=True)),
                ('paymentmode', models.CharField(blank=True, default='COD', max_length=20, null=True)),
                ('orderstatus', models.CharField(blank=True, default='COD', max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('rppid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('rpoid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('rpsid', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
    ]
