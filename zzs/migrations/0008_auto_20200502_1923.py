# Generated by Django 3.0.5 on 2020-05-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zzs', '0007_stat_players_stat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='event',
        ),
        migrations.AddField(
            model_name='player',
            name='event',
            field=models.ManyToManyField(related_name='event_player', to='zzs.Event', verbose_name='турниры'),
        ),
    ]