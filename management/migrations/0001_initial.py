# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ManagerProfile'
        db.create_table('management_managerprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('credits', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
        ))
        db.send_create_signal('management', ['ManagerProfile'])


    def backwards(self, orm):
        # Deleting model 'ManagerProfile'
        db.delete_table('management_managerprofile')


    models = {
        'management.managerprofile': {
            'Meta': {'object_name': 'ManagerProfile'},
            'credits': ('django.db.models.fields.IntegerField', [], {'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['management']