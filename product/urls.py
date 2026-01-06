from django.urls import path
from . import views

urlpatterns = [
    path('топ 5 продуктов питания/',views.first_blog),
    path('время/',views.second_blog),
    path('фото/',views.third_blog),

    path('product_list/', views.product),
    path('product_list/<int:id>/', views.product_detail),
]

