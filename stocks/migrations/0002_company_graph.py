# Generated by Django 3.0.1 on 2020-01-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='graph',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
