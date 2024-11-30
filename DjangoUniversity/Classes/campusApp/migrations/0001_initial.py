# Generated by Django 5.1.3 on 2024-11-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CampusName', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=2)),
                ('CampusID', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
        ),
    ]