# Generated by Django 3.2.10 on 2022-06-21 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auditorium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditorium_name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField()),
                ('seats', models.BigIntegerField()),
                ('charge', models.BigIntegerField()),
                ('generator', models.CharField(max_length=100)),
                ('advance_charge', models.BigIntegerField()),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='chitti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('amounts', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='chitti_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('type', models.CharField(max_length=100)),
                ('chitti_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.chitti')),
            ],
        ),
        migrations.CreateModel(
            name='committee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee_name', models.CharField(max_length=100)),
                ('president', models.CharField(max_length=100)),
                ('secretary', models.CharField(max_length=100)),
                ('no_members', models.IntegerField()),
                ('phone', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=90)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('house_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('aadhar_number', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
                ('committee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.committee')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('guest', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='')),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('fathers_name', models.CharField(max_length=100)),
                ('house_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('aadhar_number', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.login')),
            ],
        ),
        migrations.AddField(
            model_name='committee',
            name='login_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.login'),
        ),
        migrations.CreateModel(
            name='committe_program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('committee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.committee')),
            ],
        ),
        migrations.CreateModel(
            name='chitti_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
                ('details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.chitti_details')),
            ],
        ),
        migrations.AddField(
            model_name='chitti_details',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.members'),
        ),
        migrations.CreateModel(
            name='bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('ifsc', models.BigIntegerField()),
                ('pin', models.BigIntegerField()),
                ('acc_no', models.BigIntegerField()),
                ('amount', models.BigIntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='auditorium_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('booking_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='templeapp.user')),
            ],
        ),
    ]