# Generated by Django 4.0.3 on 2022-04-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Okanga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=80)),
                ('item_description', models.TextField(max_length=15000)),
                ('item_image', models.TextField(default='https://image.shutterstock.com/image-vector/online-shop-logo'
                                                        '-designs-template-260nw-1709239207.jpg')), 
                ('item_amount', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
