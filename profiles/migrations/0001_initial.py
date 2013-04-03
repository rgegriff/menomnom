# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('profiles_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('manager_profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['management.ManagerProfile'], null=True, blank=True)),
        ))
        db.send_create_signal('profiles', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('profiles_userprofile')


    models = {
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

    complete_apps = ['profiles']