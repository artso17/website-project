from django.contrib import admin
from .models import (
    About,
    Skill,
)
# Register your models here.
admin.site.register(About)
admin.site.register(Skill)
