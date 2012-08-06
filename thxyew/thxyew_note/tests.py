from django.test import TestCase

class NoteTest(TestCase):
    #fixtures = ['thxyew_note_testdata.json']
    def text_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        #testbook = Book.objects.all()[0]
        #url = '/books/id/' + str(testbook.id)
        #response = self.client.get(url)
        #self.assertContains(response, testbook.title)
    
#index
#write_note
#submit_note
#single_note