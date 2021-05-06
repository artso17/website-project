from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PortfolioFilterView,
    PortfolioAllView,
)

app_name = 'list'
urlpatterns = [
    path('portfolio/skill/<slug:myskill>/',
         PortfolioFilterView, name='portfolio_filter'),
    path('portfolio/all/', PortfolioAllView, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
