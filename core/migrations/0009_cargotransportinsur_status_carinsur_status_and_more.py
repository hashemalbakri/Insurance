# Generated by Django 5.0.1 on 2024-03-19 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cargotransportinsur_triptype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargotransportinsur',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='carinsur',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='cashsafekeepinsura',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='cashtransferinsura',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='fireinsur',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='honestyguaranteeinsur',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='notifyingcontarctorsinsur',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='transportationinsur',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
    ]
