# Generated by Django 3.2.10 on 2022-07-14 06:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('templeapp', '0012_auto_20220713_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitti',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
