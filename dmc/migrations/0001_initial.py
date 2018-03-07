# Generated by Django 2.0.2 on 2018-03-06 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_items',
            fields=[
                ('menu_item_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('menu_item_title', models.CharField(max_length=200)),
                ('menu_item_description', models.CharField(max_length=2000)),
                ('menu_item_image', models.ImageField(upload_to='')),
                ('show_in_menu', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('research_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('research_title', models.CharField(max_length=200)),
                ('research_description', models.CharField(max_length=200)),
                ('research_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('slider_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('slider_title', models.CharField(max_length=200)),
                ('slider_description', models.CharField(max_length=200)),
                ('slider_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_items',
            fields=[
                ('sub_item_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sub_item_title', models.CharField(max_length=200)),
                ('sub_item_description', models.CharField(max_length=2000)),
                ('sub_item_image', models.ImageField(upload_to='')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmc.Menu_items')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_of_sub_items',
            fields=[
                ('sub_of_sub_item_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sub_of_sub_item_title', models.CharField(max_length=200)),
                ('sub_of_sub_item_description', models.CharField(max_length=2000)),
                ('sub_of_sub_item_image', models.ImageField(upload_to='')),
                ('sub_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dmc.Sub_items')),
            ],
        ),
    ]
