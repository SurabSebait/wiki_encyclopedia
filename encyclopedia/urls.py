from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name = "search"),
    path("NewPage/", views.NewPage, name = "NewPage"),
    path("NewPage/save/", views.save, name = 'save'),
    path("RandomPage/", views.RandomPage, name = 'RandomPage'),
    path("<str:title>/", views.info,name = "info"),
    path("<str:title>/edit/", views.edit_page, name = "edit"),
    path("<str:title>/edit/save_edit/", views.save_edit, name = "save_edit"),
    path("wiki/<str:title>/", views.info,name = "info"),
    path("search/<str:title>/", views.info, name = "searchinfo")
    
]