from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zavody/', views.FilmListView.as_view(), name='zavody'),
    #re_path(r'^films/genres/(?P<genre_name>[\w-]+)/:?(?P<order>[\w-]*)$', views.FilmListView.as_view(), name='film_genre'),
    path('films/genres/<str:genre_name>/', views.FilmListView.as_view(), name='film_genre'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
]
