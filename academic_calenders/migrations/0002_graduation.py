# Generated by Django 4.0.4 on 2022-05-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_calenders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graduation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]