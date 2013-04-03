# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field hours on 'Location'
        db.delete_table('directory_location_hours')

        # Adding field 'LocationHour.location'
        db.add_column('directory_locationhour', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='location_hour', to=orm['directory.Location']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding M2M table for field hours on 'Location'
        db.create_table('directory_location_hours', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('location', models.ForeignKey(orm['directory.location'], null=False)),
            ('locationhour', models.ForeignKey(orm['directory.locationhour'], null=False))
        ))
        db.create_unique('directory_location_hours', ['location_id', 'locationhour_id'])

        # Deleting field 'LocationHour.location'
        db.delete_column('directory_locationhour', 'location_id')


    models = {
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationCategory']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            'highlights': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.LocationHighlight']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django_thumbs.db.models.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'name': "'logo'", 'blank': 'True'}),
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
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_hour'", 'to': "orm['directory.Location']"}),
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