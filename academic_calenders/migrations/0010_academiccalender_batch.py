# Generated by Django 4.0.4 on 2022-05-29 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_calenders', '0009_alter_department_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='academiccalender',
            name='batch',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.batch'),
            preserve_default=False,
        ),
    ]
