# Generated by Django 3.0.14 on 2025-01-31 14:38

import core.utils
import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to=core.utils.resume_file_path, validators=[core.validators.validate_pdf_file])),
                ('summary', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Resumes',
            },
        ),
    ]
