# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BizPost'
        db.create_table('management_bizpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('post_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('management', ['BizPost'])

        # Adding field 'ManagerProfile.location'
        db.add_column('management_managerprofile', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Location'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field biz_posts on 'ManagerProfile'
        db.create_table('management_managerprofile_biz_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('managerprofile', models.ForeignKey(orm['management.managerprofile'], null=False)),
            ('bizpost', models.ForeignKey(orm['management.bizpost'], null=False))
        ))
        db.create_unique('management_managerprofile_biz_posts', ['managerprofile_id', 'bizpost_id'])


    def backwards(self, orm):
        # Deleting model 'BizPost'
        db.delete_table('management_bizpost')

        # Deleting field 'ManagerProfile.location'
        db.delete_column('management_managerprofile', 'location_id')

        # Removing M2M table for field biz_posts on 'ManagerProfile'
        db.delete_table('management_managerprofile_biz_posts')


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
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'hours_open': ('django.db.models.fields.TimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'opening_time': ('django.db.models.fields.TimeField', [], {})
        },
        'directory.locationspecial': {
            'Meta': {'object_name': 'LocationSpecial'},
            'day': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'management.bizpost': {
            'Meta': {'object_name': 'BizPost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'management.managerprofile': {
            'Meta': {'object_name': 'ManagerProfile'},
            'biz_posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['management.BizPost']", 'null': 'True', 'blank': 'True'}),
            'credits': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Location']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['management']