# Generated by Django 5.1.3 on 2024-11-26 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_field', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField()),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
