# Generated by Django 4.0.4 on 2022-05-29 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_calenders', '0006_alter_batch_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='graduation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.graduation'),
            preserve_default=False,
        ),
    ]