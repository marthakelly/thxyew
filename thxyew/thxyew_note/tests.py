from django.test import TestCase
from django.db import models
from thxyew_note.models import Note

class NoteViewsTestCase(TestCase):
    def test_index(self):
        note_1 = Note.objects.create(
            to_person = 'You',
            from_person = 'Me',
            pub_date = models.DateField(auto_now=True),
            subject = 'Subject',
            note_body = 'Note Body'
        )
        
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('all_notes' in resp.context)
        self.assertEqual([note.pk for note in resp.context['all_notes']], [1])
        note_1 = resp.context['all_notes'][0]

    def test_write_note(self):
        resp = self.client.get('/write-note/')
        self.assertEqual(resp.status_code, 200)

    def test_good_note(self):
        d = {
            'to_person' : 'You',
            'from_person' : 'Me',
            'pub_date' : models.DateField(auto_now=True),
            'subject' : 'Subject',
            'note_body' : 'Note Body'
        }
        
        resp = self.client.post('/write-note/', d)
        self.assertEqual(resp.status_code, 200)
