# Generated by Django 4.0.3 on 2023-01-13 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_alter_ashokleyland_id_alter_bse_id_alter_cipla_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ashokleyland',
            options={'verbose_name_plural': 'AshokLeyland'},
        ),
        migrations.AlterModelOptions(
            name='bse',
            options={'verbose_name_plural': 'BSE'},
        ),
        migrations.AlterModelOptions(
            name='cipla',
            options={'verbose_name_plural': 'Cipla'},
        ),
        migrations.AlterModelOptions(
            name='eichermotors',
            options={'verbose_name_plural': 'EicherMotors'},
        ),
        migrations.AlterModelOptions(
            name='nse',
            options={'verbose_name_plural': 'NSE'},
        ),
        migrations.AlterModelOptions(
            name='reliance',
            options={'verbose_name_plural': 'Reliance'},
        ),
        migrations.AlterModelOptions(
            name='tatasteel',
            options={'verbose_name_plural': 'TataSteel'},
        ),
    ]
