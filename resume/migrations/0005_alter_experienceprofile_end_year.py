# Generated by Django 3.2.4 on 2023-12-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_experienceprofile_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experienceprofile',
            name='end_year',
            field=models.DateField(blank=True),
        ),
    ]