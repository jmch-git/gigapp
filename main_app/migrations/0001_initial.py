# Generated by Django 4.0.2 on 2022-02-23 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=100)),
                ('mgr_name', models.CharField(max_length=50)),
                ('mgr_email', models.CharField(max_length=100)),
                ('mgr_phone', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='gig date')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.band')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
