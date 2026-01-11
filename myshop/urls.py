from django.urls import path
from myshop.views import category_list, category_products

urlpatterns = [
    path('categories/', category_list, name='categories'),
    path('categories/<int:category_id>/',category_products,name='category_products'),
]
