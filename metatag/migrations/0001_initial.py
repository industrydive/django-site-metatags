# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'URLMetatags'
        db.create_table('metatag_urlmetatags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='path')),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=255, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('google_pagetrack_category', self.gf('django.db.models.fields.CharField')(max_length=55, null=True, blank=True)),
            ('google_pagetrack_customvar', self.gf('django.db.models.fields.CharField')(max_length=55, null=True, blank=True)),
        ))
        db.send_create_signal('metatag', ['URLMetatags'])


    def backwards(self, orm):
        
        # Deleting model 'URLMetatags'
        db.delete_table('metatag_urlmetatags')


    models = {
        'metatag.urlmetatags': {
            'Meta': {'object_name': 'URLMetatags'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'google_pagetrack_category': ('django.db.models.fields.CharField', [], {'max_length': '55', 'null': 'True', 'blank': 'True'}),
            'google_pagetrack_customvar': ('django.db.models.fields.CharField', [], {'max_length': '55', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'path'"})
        }
    }

    complete_apps = ['metatag']
