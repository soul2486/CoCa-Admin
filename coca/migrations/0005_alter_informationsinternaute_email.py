# Generated by Django 5.0.1 on 2024-02-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coca', '0004_remove_type_panneau_panneau_remove_type_panneau_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationsinternaute',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
