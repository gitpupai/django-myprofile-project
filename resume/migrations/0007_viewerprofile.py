# Generated by Django 3.2.4 on 2024-01-03 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_remove_viewer_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='viewerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('profile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.profile')),
                ('viewer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.viewer')),
            ],
        ),
    ]