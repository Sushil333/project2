# Generated by Django 3.2.5 on 2021-10-04 19:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=500)),
                ('school_image', models.CharField(blank=True, max_length=999)),
                ('school_logo', models.ImageField(blank=True, null=True, upload_to='school-logos')),
                ('address', models.TextField(max_length=250)),
                ('board', models.CharField(choices=[('SB', 'STATE BOARD'), ('CBSE', 'CBSE'), ('ICSE', 'ICSE'), ('CISCE', 'CISCE'), ('NIOS', 'NIOS'), ('IB', 'IB'), ('CIE', 'CIE')], default='SB', max_length=5)),
                ('co_ed_status', models.CharField(choices=[('Co-Education', 'Co-Education'), ('Girlsonly', 'Girlsonly'), ('Boysonly', 'Boysonly')], max_length=100)),
                ('ownership', models.CharField(choices=[('UN', 'UNKNOWN'), ('PR', 'PRIVATE'), ('PRA', 'PRIVATE-AIDED')], default='UN', max_length=3)),
                ('sf_ratio', models.CharField(max_length=6)),
                ('class_offered', models.CharField(choices=[('Nursery - Class 12', 'Nursery - Class 12'), ('Nursery - Class 10', 'Nursery - Class 10'), ('Toddler - Class 12', 'Toddler - Class 12'), ('Pre-Nursery - Class 5', 'Pre-Nursery - Class 5'), ('Pre-Nursery - Class 8', 'Pre-Nursery - Class 8'), ('Nursery - Class 8', 'Nursery - Class 8'), ('Class 1 - Class 12', 'Class 1 - Class 12'), ('Pre-Nursery - Class 12', 'Pre-Nursery - Class 12'), ('Pre-Nursery - KG', 'Pre-Nursery - KG'), ('Nursery - UKG', 'Nursery - UKG'), ('Pre-Nursery - Class 10', 'Pre-Nursery - Class 10'), ('Class 6 - Class 12', 'Class 6 - Class 12'), ('Class 1 - Class 8', 'Class 1 - Class 8'), ('Pre-Nursery - UKG', 'Pre-Nursery - UKG'), ('Nursery - KG', 'Nursery - KG'), ('Pre-School (Nursery) - Class 12', 'Pre-School (Nursery) - Class 12'), ('LKG - Class 12', 'LKG - Class 12'), ('Nursery - Class 3', 'Nursery - Class 3'), ('Pre-Nursery - Class 7', 'Pre-Nursery - Class 7'), ('Play Group - Class 1', 'Play Group - Class 1'), ('Nursery - Class 11', 'Nursery - Class 11'), ('Nursery - Class 7', 'Nursery - Class 7'), ('Nursery - Class 9', 'Nursery - Class 9'), ('Pre-School (Nursery) - Class 5', 'Pre-School (Nursery) - Class 5'), ('LKG - Class 10', 'LKG - Class 10'), ('Pre-School (Nursery) - Class 10', 'Pre-School (Nursery) - Class 10'), ('Pre-Nursery - Class 2', 'Pre-Nursery - Class 2'), ('Pre-Nursery - Prep', 'Pre-Nursery - Prep'), ('KG - Class 12', 'KG - Class 12'), ('Pre-School (Nursery) - Class 1', 'Pre-School (Nursery) - Class 1'), ('Nursery - Class 5', 'Nursery - Class 5'), ('LKG - Class 9', 'LKG - Class 9'), ('Nursery - Class 2', 'Nursery - Class 2'), ('UKG - Class 12', 'UKG - Class 12'), ('Class 1 - Class 11', 'Class 1 - Class 11'), ('Play Way - Class 12', 'Play Way - Class 12'), ('Pre-School (Nursery) - Pre-Primary (KG)', 'Pre-School (Nursery) - Pre-Primary (KG)'), ('Play Group - UKG', 'Play Group - UKG'), ('Pre-Nursery - Class 6', 'Pre-Nursery - Class 6'), ('UKG - Class 4', 'UKG - Class 4'), ('KG - Class 10', 'KG - Class 10'), ('Play Way - Class 10', 'Play Way - Class 10'), ('KG - Class 8', 'KG - Class 8'), ('Play School - Class 8', 'Play School - Class 8'), ('Class 1 - Class 5', 'Class 1 - Class 5'), ('Pre-Nursery - Class 9', 'Pre-Nursery - Class 9'), ('Class 6 - Class 10', 'Class 6 - Class 10'), ('Play Group - Class 5', 'Play Group - Class 5'), ('Nursery - Class 1', 'Nursery - Class 1'), ('Nursery - Class 6', 'Nursery - Class 6'), ('Pre-Nursery - Class 3', 'Pre-Nursery - Class 3'), ('Class 3 - Class 12', 'Class 3 - Class 12'), ('Class 1 - Class 10', 'Class 1 - Class 10'), ('Class 6 - Class 8', 'Class 6 - Class 8'), ('UKG - Class 10', 'UKG - Class 10'), ('Class 1 - Class 6', 'Class 1 - Class 6'), ('LKG - Class 8', 'LKG - Class 8'), ('Pre-Nursery - Nursery', 'Pre-Nursery - Nursery'), ('UKG - Class 5', 'UKG - Class 5'), ('Class 1 - Class 7', 'Class 1 - Class 7'), ('LKG - Class 5', 'LKG - Class 5'), ('Class 9 - Class 12', 'Class 9 - Class 12'), ('Play Group - Class 8', 'Play Group - Class 8'), ('Play Group - Class 10', 'Play Group - Class 10'), ('UKG - Class 8', 'UKG - Class 8')], max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=500)),
                ('webiste', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('year_of_establishment', models.CharField(max_length=500)),
                ('campus_size', models.CharField(max_length=500)),
                ('campus_type', models.CharField(max_length=500)),
                ('gallery', models.CharField(max_length=99999)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='schools.school')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(max_length=999)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_reviews', to='schools.schooldetail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'School Reviews',
            },
        ),
        migrations.CreateModel(
            name='SchoolRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=14)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_name', models.CharField(max_length=50)),
                ('fee_amount', models.IntegerField()),
                ('standard', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_refer', to='schools.school')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolFacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_classes', models.BooleanField(default=False)),
                ('smart_classes', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('boys_hostel', models.BooleanField(default=False)),
                ('girls_hostel', models.BooleanField(default=False)),
                ('auditorium_media_room', models.BooleanField(default=False)),
                ('cafeteria_canteen', models.BooleanField(default=False)),
                ('library_reading_room', models.BooleanField(default=False)),
                ('playground', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=False)),
                ('gps_bus_tracking_app', models.BooleanField(default=False)),
                ('student_tracking_app', models.BooleanField(default=False)),
                ('alumni_association', models.BooleanField(default=False)),
                ('day_care', models.BooleanField(default=False)),
                ('meals', models.BooleanField(default=False)),
                ('medical_room', models.BooleanField(default=False)),
                ('transportation', models.BooleanField(default=False)),
                ('art_and_craft', models.BooleanField(default=False)),
                ('dance', models.BooleanField(default=False)),
                ('debate', models.BooleanField(default=False)),
                ('drama', models.BooleanField(default=False)),
                ('gardening', models.BooleanField(default=False)),
                ('music', models.BooleanField(default=False)),
                ('picnics_and_excursion', models.BooleanField(default=False)),
                ('skating', models.BooleanField(default=False)),
                ('horse_riding', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('indoor_sports', models.BooleanField(default=False)),
                ('outdoor_sports', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('karate', models.BooleanField(default=False)),
                ('taekwondo', models.BooleanField(default=False)),
                ('yoga', models.BooleanField(default=False)),
                ('computer_lab', models.BooleanField(default=False)),
                ('science_lab', models.BooleanField(default=False)),
                ('robotics_lab', models.BooleanField(default=False)),
                ('ramps', models.BooleanField(default=False)),
                ('washrooms', models.BooleanField(default=False)),
                ('elevators', models.BooleanField(default=False)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
            options={
                'verbose_name_plural': 'School Facilities',
            },
        ),
        migrations.CreateModel(
            name='HallofFame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.school')),
            ],
        ),
    ]
