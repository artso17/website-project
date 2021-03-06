from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    PortfolioFilterView,
    PortfolioAllView,
    PortfolioDetailView,
    BlogAllView,
    BlogFilterView,
    BlogDetailView,
    ContactView,
)

app_name = 'list'
urlpatterns = [
    path('contact/',
         ContactView, name='contact'),
    path('blog/detail/<slug:detail_id>/',
         BlogDetailView, name='blog_detail'),
    path('blog/kategori/<slug:mykategori>/',
         BlogFilterView, name='blog_filter'),
    path('blog/all/', BlogAllView, name='blog'),
    path('portfolio/detail/<slug:detail_id>/',
         PortfolioDetailView, name='portfolio_detail'),
    path('portfolio/skill/<slug:myskill>/',
         PortfolioFilterView, name='portfolio_filter'),
    path('portfolio/all/', PortfolioAllView, name='portfolio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
