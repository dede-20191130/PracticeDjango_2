from django.urls import path

from ajax_prac_1 import views

app_name = 'ajax_prac_1'
urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('ajax_add', views.ajax_post_add, name='ajax_post_add'),
    path('ajax_search', views.ajax_post_search, name='ajax_post_search'),
]
