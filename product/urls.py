from django.urls import path
from . import views

urlpatterns = [
    path('топ 5 продуктов питания/',views.first_blog,name='first_blog'),
    path('время/',views.second_blog,name='second_blog'),
    path('фото/',views.third_blog),

    path('', views.product,name='home_page'),
    path('product_list/<int:id>/', views.product_detail),
]

