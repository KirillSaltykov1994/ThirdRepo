# Generated by Django 4.1.7 on 2023-02-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('uid', models.CharField(max_length=100)),
                ('strain', models.CharField(max_length=100)),
                ('cannabinoid_abbreviation', models.CharField(max_length=100)),
                ('cannabinoid', models.CharField(max_length=100)),
                ('terpene', models.CharField(max_length=100)),
                ('medical_use', models.CharField(max_length=100)),
                ('health_benefit', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('buzzword', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
    ]
