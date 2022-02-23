from django.test import TestCase


class TestBagViews(TestCase):
    ''' Test Bag Views '''

    def test_view_bag(self):
        '''Testing the view_bag view'''

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
