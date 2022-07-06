# Generated by Django 3.2.13 on 2022-07-05 10:33

from django.db import migrations, models
import django.utils.timezone
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('price', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('bedrooms', models.CharField(max_length=255)),
                ('bathrooms', models.CharField(max_length=255)),
                ('agent', models.CharField(max_length=255)),
                ('agent_contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('agent_email', models.EmailField(max_length=255)),
                ('agent_company', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
