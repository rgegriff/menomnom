# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.location'
        db.add_column('events_event', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['events.EventLocation']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.location'
        db.delete_column('events_event', 'location_id')


    models = {
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationCategory']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'highlights': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.LocationHighlights']", 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationHours']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management.ManagerProfile']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'specials': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.LocationSpecials']", 'null': 'True', 'blank': 'True'}),
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
        'directory.locationhighlights': {
            'Meta': {'object_name': 'LocationHighlights'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'directory.locationhours': {
            'Meta': {'object_name': 'LocationHours'},
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'hours_open': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_time': ('django.db.models.fields.TimeField', [], {})
        },
        'directory.locationspecials': {
            'Meta': {'object_name': 'LocationSpecials'},
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'attending': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['profiles.UserProfile']", 'symmetrical': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.EventCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.EventLocation']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'events.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'events.eventlocation': {
            'Meta': {'object_name': 'EventLocation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'dir_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'management.managerprofile': {
            'Meta': {'object_name': 'ManagerProfile'},
            'credits': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management.ManagerProfile']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']