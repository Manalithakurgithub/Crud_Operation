# Generated by Django 5.0.1 on 2024-02-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]