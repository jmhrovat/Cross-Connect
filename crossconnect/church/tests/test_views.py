from crossconnect.tests import GlobalTestCase
from django.urls import reverse
from users.views import *


class ChurchViewsTestCase(GlobalTestCase):

    def test_add_church_view(self):
        response = self.client.get(reverse('add_church'))
        self.assertTemplateUsed(response, 'church/add_church.html')

    def test_add_service_template_view(self):
        response = self.client.get(reverse('add_service_template'))
        self.assertTemplateUsed(response, 'church/add_service_template.html')
