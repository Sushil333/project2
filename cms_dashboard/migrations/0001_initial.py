# Generated by Django 3.2.5 on 2021-11-04 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_date', models.DateTimeField(auto_created=True)),
                ('csv_file', models.FileField(upload_to='temp')),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
