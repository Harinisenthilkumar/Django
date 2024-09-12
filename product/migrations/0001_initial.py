# Generated by Django 4.2.15 on 2024-08-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('gst', models.FloatField(default=0)),
                ('final_price', models.FloatField(default=0)),
            ],
        ),
    ]
