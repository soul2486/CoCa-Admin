# Generated by Django 5.0.1 on 2024-02-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coca', '0008_alter_informationsinternaute_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='devis_appareil',
            name='power',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
