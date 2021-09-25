# Generated by Django 3.2.5 on 2021-09-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schoolfacilities',
            options={'verbose_name_plural': 'School Facilities'},
        ),
        migrations.AlterField(
            model_name='school',
            name='class_offered',
            field=models.CharField(choices=[('Nursery - Class 12', 'Nursery - Class 12'), ('Nursery - Class 10', 'Nursery - Class 10'), ('Toddler - Class 12', 'Toddler - Class 12'), ('Pre-Nursery - Class 5', 'Pre-Nursery - Class 5'), ('Pre-Nursery - Class 8', 'Pre-Nursery - Class 8'), ('Nursery - Class 8', 'Nursery - Class 8'), ('Class 1 - Class 12', 'Class 1 - Class 12'), ('Pre-Nursery - Class 12', 'Pre-Nursery - Class 12'), ('Pre-Nursery - KG', 'Pre-Nursery - KG'), ('Nursery - UKG', 'Nursery - UKG'), ('Pre-Nursery - Class 10', 'Pre-Nursery - Class 10'), ('Class 6 - Class 12', 'Class 6 - Class 12'), ('Class 1 - Class 8', 'Class 1 - Class 8'), ('Pre-Nursery - UKG', 'Pre-Nursery - UKG'), ('Nursery - KG', 'Nursery - KG'), ('Pre-School (Nursery) - Class 12', 'Pre-School (Nursery) - Class 12'), ('LKG - Class 12', 'LKG - Class 12'), ('Nursery - Class 3', 'Nursery - Class 3'), ('Pre-Nursery - Class 7', 'Pre-Nursery - Class 7'), ('Play Group - Class 1', 'Play Group - Class 1'), ('Nursery - Class 11', 'Nursery - Class 11'), ('Nursery - Class 7', 'Nursery - Class 7'), ('Nursery - Class 9', 'Nursery - Class 9'), ('Pre-School (Nursery) - Class 5', 'Pre-School (Nursery) - Class 5'), ('LKG - Class 10', 'LKG - Class 10'), ('Pre-School (Nursery) - Class 10', 'Pre-School (Nursery) - Class 10'), ('Pre-Nursery - Class 2', 'Pre-Nursery - Class 2'), ('Pre-Nursery - Prep', 'Pre-Nursery - Prep'), ('KG - Class 12', 'KG - Class 12'), ('Pre-School (Nursery) - Class 1', 'Pre-School (Nursery) - Class 1'), ('Nursery - Class 5', 'Nursery - Class 5'), ('LKG - Class 9', 'LKG - Class 9'), ('Nursery - Class 2', 'Nursery - Class 2'), ('UKG - Class 12', 'UKG - Class 12'), ('Class 1 - Class 11', 'Class 1 - Class 11'), ('Play Way - Class 12', 'Play Way - Class 12'), ('Pre-School (Nursery) - Pre-Primary (KG)', 'Pre-School (Nursery) - Pre-Primary (KG)'), ('Play Group - UKG', 'Play Group - UKG'), ('Pre-Nursery - Class 6', 'Pre-Nursery - Class 6'), ('UKG - Class 4', 'UKG - Class 4'), ('KG - Class 10', 'KG - Class 10'), ('Play Way - Class 10', 'Play Way - Class 10'), ('KG - Class 8', 'KG - Class 8'), ('Play School - Class 8', 'Play School - Class 8'), ('Class 1 - Class 5', 'Class 1 - Class 5'), ('Pre-Nursery - Class 9', 'Pre-Nursery - Class 9'), ('Class 6 - Class 10', 'Class 6 - Class 10'), ('Play Group - Class 5', 'Play Group - Class 5'), ('Nursery - Class 1', 'Nursery - Class 1'), ('Nursery - Class 6', 'Nursery - Class 6'), ('Pre-Nursery - Class 3', 'Pre-Nursery - Class 3'), ('Class 3 - Class 12', 'Class 3 - Class 12'), ('Class 1 - Class 10', 'Class 1 - Class 10'), ('Class 6 - Class 8', 'Class 6 - Class 8'), ('UKG - Class 10', 'UKG - Class 10'), ('Class 1 - Class 6', 'Class 1 - Class 6'), ('LKG - Class 8', 'LKG - Class 8'), ('Pre-Nursery - Nursery', 'Pre-Nursery - Nursery'), ('UKG - Class 5', 'UKG - Class 5'), ('Class 1 - Class 7', 'Class 1 - Class 7'), ('LKG - Class 5', 'LKG - Class 5'), ('Class 9 - Class 12', 'Class 9 - Class 12'), ('Play Group - Class 8', 'Play Group - Class 8'), ('Play Group - Class 10', 'Play Group - Class 10'), ('UKG - Class 8', 'UKG - Class 8')], max_length=100),
        ),
    ]
