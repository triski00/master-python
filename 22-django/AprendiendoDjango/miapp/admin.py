from django.contrib import admin
from django.utils.formats import date_format
from .models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at')
    list_display = ('title', 'formatted_created', 'formatted_updated', 'public')

    def formatted_created(self, obj):
        return date_format(
            obj.created_at,
            format="j \\d\\e F \\d\\e Y \\a \\l\\a\\s H:i",
            use_l10n=True
        )
    formatted_created.short_description = "Creado"

    def formatted_updated(self, obj):
        return date_format(
            obj.update_at,   # ← aquí también SIN “d”
            format="j \\d\\e F \\d\\e Y \\a \\l\\a\\s H:i",
            use_l10n=True
        )
    formatted_updated.short_description = "Actualizado"


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo del panel

title = "Master en Python Mario"
admin.site.site_title = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestión Mario"

