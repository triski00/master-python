from django.test import TestCase
from django.urls import reverse


class MainappViewsTests(TestCase):

    def test_index_responde_200_y_usa_su_plantilla(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/index.html')

    def test_inicio_es_otra_ruta_de_la_misma_vista(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_hola_mundo_responde_200(self):
        response = self.client.get(reverse('hola_mundo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainapp/hola_mundo.html')
