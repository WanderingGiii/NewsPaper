# Generated by Django 3.2 on 2021-05-05 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cathegory',
            name='cathegory',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
