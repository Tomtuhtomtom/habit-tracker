# Generated by Django 4.1 on 2022-09-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0004_record_unique_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='entry_date',
            field=models.DateField(unique=True),
        ),
    ]
