# Generated by Django 5.0.1 on 2024-02-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmpApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='emp',
            name='lname',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
