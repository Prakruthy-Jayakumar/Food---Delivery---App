# Generated by Django 3.2.12 on 2022-04-21 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef_name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Imagesss')),
                ('chef_designation', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Imagesss')),
                ('desc', models.TextField()),
                ('qty', models.IntegerField()),
                ('price_food', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Imagesss')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Specials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special_name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Imagesss')),
                ('special_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.food')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=40)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.district')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=250)),
                ('qty', models.IntegerField()),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.district')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_app.food')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='food_app.place')),
            ],
        ),
    ]
