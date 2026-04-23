from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from miapp.forms import FormArticle
from django.contrib import messages


# MVC = Modelo Vista Controlador
# MVT = Modelo Template Vista

layout = """
<h1>Sitio web con Django | Mario</h1>
<hr/>
<ul>
    <li><a href="/inicio/">Inicio</a></li>
    <li><a href="/hola-mundo/">Hola Mundo</a></li>
    <li><a href="/pagina-pruebas/">Página de pruebas</a></li>
</ul>
<li>
    <a href="/contacto/">contacto</a>
    </li>
</ul>
<hr/>

"""



def create_full_article(request):
    form = FormArticle()
    return render(request, 'create_full_article.html', {
        'form': form
    })

def save_article(request):

    if request.method == 'POST':
        form = FormArticle(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            articulo = Article(
                title=data['title'],
                content=data['content'],
                public=True if data['public'] == "1" else False
            )
            articulo.save(request, f'Has creado correctamente el articiulo {articulo.id}')

            # Crear mensaje flash

            messages.succes()

            return HttpResponse(f"Artículo creado: {articulo.title}")

        else:
            # VOLVER A MOSTRAR EL FORMULARIO CON LOS ERRORES
            return render(request, 'create_full_article.html', {
                'form': form
            })

    return HttpResponse("Método no permitido")




def index(request):
    html = "<h1>Inicio</h1>"
    html += "<p>Años hasta el 2050:</p>"
    year = 2026
    while year <= 2050:
        html += f"<li>{year}</li>"
        year += 1
    html += "</ul>"

    year = 2026
    hasta = range(year, 2051)

    nombre = "Mario Ávila"
    lenguajes = ['JavaScript', 'Python', 'PHP', 'C']

    return render(request, 'index.html', {
        'title': 'Inicio 2',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })





def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):

  if redirigir ==1:
      return redirect('contacto', nombre="Mario", apellidos="Avila")

  return render(request, 'pagina.html')



def contacto(request, nombre="", apellidos=""):
    html = ""

    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}<h3>"

        return HttpResponse(layout+f"<h2>Contacto</h2>"+html)
    

    def articulos(request):
     
     articulos = Article.objects.filter(public=True).order_by('-id')
     return render(request, 'articulos.html', {
        'articulos': articulos
    })

"""
        articulos = Article.objects.filter(id_lte=12, title_contains=)

        articulos = Article.objets.filter(
            Q(title_contains="2") | Q(public=True)
        )
"""










def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()

    return HttpResponse(f"Articulo creado: <strong>{articulo.title} - {articulo.content}</strong>")


def save_article(request):

    if request.method == 'POST':

        title = request.POST['title']

        if len(title) <=5:
            return HttpResponse("El titulo es muy pequeño")


        content = request.POST['content']
        public = True if request.POST['public'] == "1" else False

        articulo = Article(
            title=title,
            content=content,
            public=public
        )
        articulo.save()

        return HttpResponse(
            f"Articulo creado: <strong>{articulo.title} - {articulo.content}</strong>"
        )

    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")




def create_article(request):


    return render(request, 'create_article.html',)


def create_full_article(request):
 

    if request.method =='POST':
      formulario = FormArticle(request.POST)

      if formulario.is_valid():
          data_form = formulario.cleaned_data

          title = data_form.get('title')
          content = data_form['content']
          public = data_form['public']

          articulo = Article(
              title = title,
              content = content,
              public = public
          )

          articulo.save()

          return redirect('articulos')

          #return HttpResponse(articulo.title + '-' + articulo.content + '-' + str(articulo.public))


    else:  
     formulario = FormArticle()

    return render(request, 'create_full_article.html', {
     'form': formulario
 })




def articulo(request):
    try:
        articulo = Article.objects.get(title="Superman", public=False)
        response = f"Articulo: <br/> {articulo.id}. {articulo.title}"
    except:
        response = "<h1>Articulo no encontrado</h1>"

    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} editado: <strong>{articulo.title} - {articulo.content}</strong>")

def articulos(request):
    articulos = Article.objects.all

    return render(request, 'articulos.html', {
        'articulos': articulos
    })


from django.shortcuts import get_object_or_404

def borrar_articulo(request, id):
    articulo = get_object_or_404(Article, pk=id)
    articulo.delete()
    return redirect('articulos')

