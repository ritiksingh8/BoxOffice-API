# Generated by Django 2.2.6 on 2020-09-08 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theater', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=3)),
                ('seat_type', models.CharField(choices=[('', 'Select'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=8)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.Show')),
            ],
            options={
                'unique_together': {('no', 'show')},
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%S')),
                ('payment_type', models.CharField(choices=[('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('Net Banking', 'Net Banking'), ('Wallet', 'Wallet')], max_length=11)),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookedSeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Seat')),
            ],
            options={
                'unique_together': {('seat', 'booking')},
            },
        ),
    ]
