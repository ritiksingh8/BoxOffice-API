# Generated by Django 2.2.6 on 2020-10-16 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0002_auto_20200908_2019'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='no',
            new_name='seat_no',
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_code',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_id',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_row',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('seat_no', 'show')},
        ),
        migrations.RemoveField(
            model_name='seat',
            name='seat_type',
        ),
    ]
