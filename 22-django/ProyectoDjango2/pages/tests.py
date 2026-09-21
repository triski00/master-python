from django.test import TestCase
from django.urls import reverse

from pages.models import Page


class PageModelTests(TestCase):

    def test_el_slug_se_genera_a_partir_del_titulo_si_esta_vacio(self):
        page = Page.objects.create(title='Sobre mí', content='<p>Hola</p>', visible=True, slug='')
        self.assertEqual(page.slug, 'sobre-mi')

    def test_no_se_pisa_un_slug_indicado_a_mano(self):
        page = Page.objects.create(title='Contacto', content='x', visible=True, slug='mi-contacto')
        self.assertEqual(page.slug, 'mi-contacto')

    def test_str_devuelve_el_titulo(self):
        page = Page.objects.create(title='Contacto', content='x', visible=True, slug='contacto')
        self.assertEqual(str(page), 'Contacto')


class PageViewsTests(TestCase):

    def setUp(self):
        self.visible = Page.objects.create(
            title='Sobre mí', content='<p>Contenido de prueba</p>', visible=True, slug='sobre-mi')
        self.oculta = Page.objects.create(
            title='Página oculta', content='x', visible=False, slug='oculta')

    def test_pagina_existente_responde_200_y_muestra_su_contenido(self):
        response = self.client.get(reverse('page', args=['sobre-mi']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contenido de prueba')

    def test_slug_inexistente_devuelve_404(self):
        response = self.client.get(reverse('page', args=['no-existe']))
        self.assertEqual(response.status_code, 404)

    def test_el_menu_solo_muestra_las_paginas_visibles(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Sobre mí')
        self.assertNotContains(response, 'Página oculta')
