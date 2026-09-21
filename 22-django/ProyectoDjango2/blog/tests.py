from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Article, Category


class ModelosBlogTests(TestCase):

    def test_str_de_categoria_y_articulo(self):
        categoria = Category.objects.create(name='Python', description='Todo sobre Python')
        articulo = Article.objects.create(title='Mi primer artículo', content='Texto', public=True)
        self.assertEqual(str(categoria), 'Python')
        self.assertEqual(str(articulo), 'Mi primer artículo')

    def test_un_articulo_puede_tener_varias_categorias(self):
        c1 = Category.objects.create(name='Python', description='a')
        c2 = Category.objects.create(name='Django', description='b')
        articulo = Article.objects.create(title='Django y Python', content='Texto', public=True)
        articulo.categories.add(c1, c2)
        self.assertEqual(articulo.categories.count(), 2)

    def test_los_articulos_se_ordenan_del_mas_nuevo_al_mas_antiguo(self):
        antiguo = Article.objects.create(title='Antiguo', content='x', public=True)
        nuevo = Article.objects.create(title='Nuevo', content='x', public=True)
        # Se fija una fecha anterior para que el orden no dependa del reloj
        Article.objects.filter(pk=antiguo.pk).update(created_at=timezone.now() - timedelta(days=1))
        self.assertEqual(list(Article.objects.all()), [nuevo, antiguo])

    def test_los_nombres_en_plural_del_admin_estan_bien(self):
        # Evita volver a pisar verbose_name_plural con un verbose_name repetido
        self.assertEqual(Article._meta.verbose_name_plural, 'Artículos')
        self.assertEqual(Category._meta.verbose_name_plural, 'Categorías')


class VistaListaArticulosTests(TestCase):

    def test_la_lista_responde_200_y_muestra_los_articulos(self):
        Article.objects.create(title='Artículo visible en la lista', content='<p>Cuerpo</p>', public=True)
        response = self.client.get(reverse('list_articles'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/list.html')
        self.assertContains(response, 'Artículo visible en la lista')

    def test_la_lista_vacia_tambien_responde_200(self):
        response = self.client.get(reverse('list_articles'))
        self.assertEqual(response.status_code, 200)
