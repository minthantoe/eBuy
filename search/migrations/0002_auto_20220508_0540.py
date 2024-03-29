# Generated by Django 3.2.13 on 2022-05-08 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=220, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='ebay',
            new_name='Finding',
        ),
    ]
