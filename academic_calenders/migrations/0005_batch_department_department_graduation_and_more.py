# Generated by Django 4.0.4 on 2022-05-29 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_calenders', '0004_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='graduation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.graduation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]