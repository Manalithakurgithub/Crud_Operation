# Generated by Django 5.0.1 on 2024-02-02 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0002_rename_name_emp_fname_emp_lname'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='emp_photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
