# Generated by Django 5.0.1 on 2024-03-19 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_cargotransportinsur_fireinsur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashtransferinsura',
            name='paymentMethod',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank Transfer', 'Bank Transfer')], default='Cash', max_length=60),
        ),
    ]
