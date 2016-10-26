# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 16:41
from __future__ import unicode_literals

import calaccess_raw.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_raw', '0008_auto_20161025_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvr2campaigndisclosurecd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvr2lobbydisclosurecd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvr2registrationcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvr2socd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvr3verificationinfocd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvrcampaigndisclosurecd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvrlobbydisclosurecd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvrregistrationcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(blank=True, db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', null=True, verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='cvrsocd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing id'),
        ),
        migrations.AlterField(
            model_name='debtcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number of the parent filing', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='expncd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='f495p2cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='f501502cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='f690p2cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lattcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lccmcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lempcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lexpcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='loancd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lobbyamendmentscd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lobbyistfirmemployer1cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lobbyistfirmemployer2cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lothcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='lpaycd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='rcptcd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='s401cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='s496cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='s497cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
        migrations.AlterField(
            model_name='s498cd',
            name='filing_id',
            field=calaccess_raw.fields.IntegerField(db_column='FILING_ID', db_index=True, help_text='Unique filing identification number', verbose_name='filing ID'),
        ),
    ]
