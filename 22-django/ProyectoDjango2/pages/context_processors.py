from pages.models import Page

def get_pages(request):

    pages = Page.objects.filter(visible=True).exclude(slug__isnull=True).exclude(slug__exact='')


    return {
        'pages': pages
    }