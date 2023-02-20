from django.urls import path
from webapp.views import products_view, product_view, product_add_view, product_edit_view, product_delete_view, \
    categories_view, category_add_view

urlpatterns = [
    path('', products_view, name='products'),
    path('products/<int:pk>/', product_view, name='product'),
    path('products/add/', product_add_view, name='product_add'),
    path('products/<int:pk>/edit/', product_edit_view, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete_view, name='product_delete'),
    path('categories/', categories_view, name='categories'),
    path('categories/add/', category_add_view, name='category_add'),
]


