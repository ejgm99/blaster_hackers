# Generated by Django 3.1.4 on 2020-12-31 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20201230_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=models.CharField(default='static/images/room.jpeg', max_length=1000),
        ),
    ]
