# Generated by Django 3.2.10 on 2022-08-26 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('templeapp', '0016_remove_chitti_payment_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chitti',
            name='committee',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='templeapp.committee'),
            preserve_default=False,
        ),
    ]