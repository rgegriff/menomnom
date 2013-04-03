# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('directory_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.TextField')()),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('highlights', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.LocationHighlight'], null=True, blank=True)),
        ))
        db.send_create_signal('directory', ['Location'])

        # Adding M2M table for field category on 'Location'
        db.create_table('directory_location_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('location', models.ForeignKey(orm['directory.location'], null=False)),
            ('locationcategory', models.ForeignKey(orm['directory.locationcategory'], null=False))
        ))
        db.create_unique('directory_location_category', ['location_id', 'locationcategory_id'])

        # Adding M2M table for field hours on 'Location'
        db.create_table('directory_location_hours', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('location', models.ForeignKey(orm['directory.location'], null=False)),
            ('locationhour', models.ForeignKey(orm['directory.locationhour'], null=False))
        ))
        db.create_unique('directory_location_hours', ['location_id', 'locationhour_id'])

        # Adding M2M table for field specials on 'Location'
        db.create_table('directory_location_specials', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('location', models.ForeignKey(orm['directory.location'], null=False)),
            ('locationspecial', models.ForeignKey(orm['directory.locationspecial'], null=False))
        ))
        db.create_unique('directory_location_specials', ['location_id', 'locationspecial_id'])

        # Adding model 'LocationCategory'
        db.create_table('directory_locationcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=45)),
        ))
        db.send_create_signal('directory', ['LocationCategory'])

        # Adding model 'LocationSpecial'
        db.create_table('directory_locationspecial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('directory', ['LocationSpecial'])

        # Adding model 'LocationHighlight'
        db.create_table('directory_locationhighlight', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('directory', ['LocationHighlight'])

        # Adding model 'LocationHour'
        db.create_table('directory_locationhour', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
            ('opening_time', self.gf('django.db.models.fields.TimeField')()),
            ('closing_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal('directory', ['LocationHour'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('directory_location')

        # Removing M2M table for field category on 'Location'
        db.delete_table('directory_location_category')

        # Removing M2M table for field hours on 'Location'
        db.delete_table('directory_location_hours')

        # Removing M2M table for field specials on 'Location'
        db.delete_table('directory_location_specials')

        # Deleting model 'LocationCategory'
        db.delete_table('directory_locationcategory')

        # Deleting model 'LocationSpecial'
        db.delete_table('directory_locationspecial')

        # Deleting model 'LocationHighlight'
        db.delete_table('directory_locationhighlight')

        # Deleting model 'LocationHour'
        db.delete_table('directory_locationhour')


    models = {
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationCategory']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'highlights': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.LocationHighlight']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationHour']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'specials': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.LocationSpecial']", 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.TextField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'directory.locationcategory': {
            'Meta': {'object_name': 'LocationCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        'directory.locationhighlight': {
            'Meta': {'object_name': 'LocationHighlight'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'directory.locationhour': {
            'Meta': {'object_name': 'LocationHour'},
            'closing_time': ('django.db.models.fields.TimeField', [], {}),
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_time': ('django.db.models.fields.TimeField', [], {})
        },
        'directory.locationspecial': {
            'Meta': {'object_name': 'LocationSpecial'},
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['directory']