# Generated by Django 5.1.6 on 2025-02-28 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_migrate_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='letting',
            options={'verbose_name': 'letting', 'verbose_name_plural': 'lettings'},
        ),
    ]
