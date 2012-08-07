from django.test import TestCase
from thxyew_note.models import Note, NoteForm

class NoteTest(TestCase):
    fixtures = ['thxyew_note_testdata.json']

    def test_index(self):
        resp = self.client.get('/')
        # does the page give a 200 response
        self.assertEqual(resp.status_code, 200)
        # does the page have all_notes passed as context
        self.assertTrue('all_notes' in resp.context)

    def test_write_note(self):
        url = '/write-note/'
        resp = self.client.get(url)
        # does the page give a 200 response
        self.assertEqual(resp.status_code, 200)
        # invalid form
        invalid = self.client.post(url, {'pub_date': '2012-08-04', 'from_person': None, 'to_person': 'To Test', 'subject': 'Subject Test', 'note_body': 'Note Body Test'})
        self.assertFormError(invalid, 'form', 'from_person', 'This field is required.')
        # valid form
        # redirect = '/'
        # valid = self.client.post(url, {'pub_date': '2012-08-04', 'from_person': 'From Test', 'to_person': 'To Test', 'subject': 'Subject Test', 'note_body': 'Note Body Test'})
        # self.assertRedirects(valid, redirect)
        # self.assertContains(response, note.note_body)

    def test_submit_note(self):
        pass

    def test_single_note(self):
        note = Note.objects.all()[0]
        url = '/notes/' + str(note.pk) + '/'
        resp = self.client.get(url)
        # does the page give a 200 response
        self.assertEqual(resp.status_code, 200)
        # does the page have single_note passed as context
        self.assertTrue('single_note' in resp.context)
        # does the page have all the required fields
        # the date is formatting 'magically' in the view
        #    need to debug
        # self.assertContains(resp, note.pub_date)
        self.assertContains(resp, note.from_person)
        self.assertContains(resp, note.to_person)
        self.assertContains(resp, note.subject)
        self.assertContains(resp, note.note_body)