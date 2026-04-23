from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name = "Título")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(default='null', verbose_name = "Miniatura", upload_to="articles")
    public = models.BooleanField(verbose_name = "¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name = "Editado")

class Meta:
 verbose_name = "Artículo"
 verbose_name_plural = "Artículos"
 ordering = ['create_at']

 def __str__(self):
    if self.public:
       
        public = "(publicado)"
    else:
      public = "(privado)"

    return f"{self.title} {public}"
 

 
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)


class Meta:
    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"


    def __str__(self):
     return self.name


