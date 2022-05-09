# Generated by Django 3.2.13 on 2022-05-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20220508_0540'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostWatchedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidCount', models.FloatField(blank=True, null=True)),
                ('buyItNowPrice', models.FloatField(blank=True, null=True)),
                ('currentPrice', models.FloatField(blank=True, null=True)),
                ('imageURL', models.URLField(blank=True, null=True)),
                ('itemId', models.CharField(blank=True, max_length=220, null=True)),
                ('primaryCategoryName', models.CharField(blank=True, max_length=220, null=True)),
                ('primaryCategoryId', models.CharField(blank=True, max_length=220, null=True)),
                ('shippingCost', models.FloatField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('viewItemURL', models.URLField(blank=True, null=True)),
                ('watchCount', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
