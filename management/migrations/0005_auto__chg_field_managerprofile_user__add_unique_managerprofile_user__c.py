# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ManagerProfile.user'
        db.alter_column('management_managerprofile', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, null=True))
        # Adding unique constraint on 'ManagerProfile', fields ['user']
        db.create_unique('management_managerprofile', ['user_id'])


        # Changing field 'ManagerProfile.location'
        db.alter_column('management_managerprofile', 'location_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['directory.Location']))
        # Adding unique constraint on 'ManagerProfile', fields ['location']
        db.create_unique('management_managerprofile', ['location_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'ManagerProfile', fields ['location']
        db.delete_unique('management_managerprofile', ['location_id'])

        # Removing unique constraint on 'ManagerProfile', fields ['user']
        db.delete_unique('management_managerprofile', ['user_id'])


        # Changing field 'ManagerProfile.user'
        db.alter_column('management_managerprofile', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True))

        # Changing field 'ManagerProfile.location'
        db.alter_column('management_managerprofile', 'location_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['directory.Location']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'directory.location': {
            'Meta': {'object_name': 'Location'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.LocationCategory']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'default': "'Menomonie'", 'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django_thumbs.db.models.ImageWithThumbsField', [], {'name': "'logo'", 'sizes': '((148, 148),)', 'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'Wi'", 'max_length': '2'}),
            'street': ('django.db.models.fields.TextField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'default': "'54751'", 'max_length': '5'})
        },
        'directory.locationcategory': {
            'Meta': {'object_name': 'LocationCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '45'})
        },
        'management.bizpost': {
            'Meta': {'object_name': 'BizPost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'post_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'urltext': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'})
        },
        'management.managerprofile': {
            'Meta': {'object_name': 'ManagerProfile'},
            'biz_posts': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'manager'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['management.BizPost']"}),
            'credits': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'manager'", 'unique': 'True', 'null': 'True', 'to': "orm['directory.Location']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['management']