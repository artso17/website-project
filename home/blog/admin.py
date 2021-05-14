from django.contrib import admin
from .models import (
    About,
    Skill,
    Service,
    Portfolio,
    Blog,
    Contact,
    Kategori,
)


class read_only(admin.ModelAdmin):
    readonly_fields = ['published', 'slug']


class slug_read_only(admin.ModelAdmin):
    readonly_fields = ['slug']


# Register your models here.
admin.site.register(About)
admin.site.register(Skill, slug_read_only)
admin.site.register(Service)
admin.site.register(Portfolio, read_only)
admin.site.register(Blog, read_only)
admin.site.register(Contact)
admin.site.register(Kategori, slug_read_only)
