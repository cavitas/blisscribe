# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bliss_webapp', '0004_auto_20170902_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translationmodel',
            old_name='other_pos',
            new_name='other',
        ),
        migrations.AddField(
            model_name='translationmodel',
            name='title_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='translationmodel',
            name='fast_translate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='translationmodel',
            name='font_fam',
            field=models.CharField(choices=[(b'/Library/Fonts/Times New Roman.ttf', b'Times New Roman'), (b'/Library/Fonts/Arial.ttf', b'Arial'), (b'/Library/Fonts/Helvetica.dfont', b'Helvetica')], max_length=50),
        ),
        migrations.AlterField(
            model_name='translationmodel',
            name='font_size',
            field=models.CharField(choices=[(b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22'), (b'23', b'23'), (b'24', b'24'), (b'25', b'25'), (b'26', b'26'), (b'27', b'27'), (b'28', b'28'), (b'29', b'29'), (b'30', b'30')], max_length=2),
        ),
        migrations.AlterField(
            model_name='translationmodel',
            name='nouns',
            field=models.BooleanField(default=False),
        ),
    ]
