# Generated by Django 3.1.3 on 2020-11-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_number', models.IntegerField()),
                ('second_number', models.IntegerField()),
                ('summa', models.IntegerField()),
                ('division', models.IntegerField()),
                ('multiply', models.IntegerField()),
                ('minus', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Plus1',
        ),
        migrations.DeleteModel(
            name='Plus2',
        ),
    ]
