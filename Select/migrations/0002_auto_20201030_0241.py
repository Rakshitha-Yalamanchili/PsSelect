# Generated by Django 3.0.7 on 2020-10-29 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Select', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taken',
            name='tNo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teamNum', to='Select.Team'),
        ),
    ]
