from django.test import TestCase
from django.db import models
from thxyew_note.models import Note, Author

class NoteViewsTestCase(TestCase):
    def test_index(self):
        author_1 = Author.objects.create(
            name = 'Martha Kelly',
            twitter = 'marthakelly'
        )
        note_1 = Note.objects.create(
            to_person = 'You',
            author = author_1,
            pub_date = models.DateField(auto_now=True),
            subject = 'Subject',
            note_body = 'Note Body'
        )

        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('all_notes' in resp.context)
        self.assertEqual([note.pk for note in resp.context['all_notes']], [1])

    def test_write_note(self):
        resp = self.client.get('/write-note/')
        self.assertEqual(resp.status_code, 200)