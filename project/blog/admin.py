from django.contrib import admin
from .models import (
    About,
    Skill,
    Service,
    Portfolio,
    Blog,
    Contact,
)


class read_only(admin.ModelAdmin):
    readonly_fields = ['published']


# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Blog, read_only)
admin.site.register(Contact)
