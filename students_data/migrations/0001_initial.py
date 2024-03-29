# Generated by Django 4.0.4 on 2022-05-29 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_calenders', '0004_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_url', models.URLField(max_length=1000)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.batch')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.department')),
                ('graduation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_calenders.graduation')),
            ],
        ),
    ]
