from django.contrib import admin
from .models import (
    About,
    Skill,
    Service,
    Portfolio,
    Blog,
    Contact
)
# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Contact)
