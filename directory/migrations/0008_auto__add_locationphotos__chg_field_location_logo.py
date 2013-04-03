# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationPhotos'
        db.create_table('directory_locationphotos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='location_photos', to=orm['directory.Location'])),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('image', self.gf('django_thumbs.db.models.ImageWithThumbsField')(max_length=100, name='image', sizes=((280, 280),))),
        ))
        db.send_create_signal('directory', ['LocationPhotos'])


        # Changing field 'Location.logo'
        db.alter_column('directory_location', 'logo', self.gf('django_thumbs.db.models.ImageWithThumbsField')(name='logo', sizes=((148, 148),), max_length=100, null=True))

    def backwards(self, orm):
        # Deleting model 'LocationPhotos'
        db.delete_table('directory_locationphotos')


        # Changing field 'Location.logo'
        db.alter_column('directory_location', 'logo', self.gf('django_thumbs.db.models.ImageWithThumbsField')(max_length=100, null=True, name='logo'))

    models = {
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationCategory']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            'highlights': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.LocationHighlight']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django_thumbs.db.models.ImageWithThumbsField', [], {'name': "'logo'", 'sizes': '((148, 148),)', 'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
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
        'directory.locationphotos': {
            'Meta': {'object_name': 'LocationPhotos'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django_thumbs.db.models.ImageWithThumbsField', [], {'max_length': '100', 'name': "'image'", 'sizes': '((280, 280),)'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_photos'", 'to': "orm['directory.Location']"})
        },
        'directory.locationspecial': {
            'Meta': {'object_name': 'LocationSpecial'},
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'location_special'", 'to': "orm['directory.Location']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['directory']