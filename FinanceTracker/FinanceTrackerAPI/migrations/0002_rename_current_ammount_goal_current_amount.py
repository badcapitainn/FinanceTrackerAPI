# Generated by Django 5.0.7 on 2024-07-12 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FinanceTrackerAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='current_ammount',
            new_name='current_amount',
        ),
    ]