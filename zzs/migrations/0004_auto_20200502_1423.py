# Generated by Django 3.0.5 on 2020-05-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zzs', '0003_auto_20200502_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='mvp_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zzs.MostValuablePlayer', verbose_name='MVP игрок'),
        ),
        migrations.AlterField(
            model_name='match',
            name='teams',
            field=models.CharField(default='ZZS - ', max_length=300, verbose_name='Команды'),
        ),
    ]
