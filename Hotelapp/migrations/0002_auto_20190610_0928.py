# Generated by Django 2.2 on 2019-06-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=22)),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Signup',
        ),
    ]
