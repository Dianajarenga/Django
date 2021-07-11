# Generated by Django 3.2.5 on 2021-07-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('unit', models.CharField(max_length=10)),
                ('duration', models.DurationField()),
            ],
        ),
    ]
