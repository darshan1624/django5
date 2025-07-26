from django.urls import path 
from product import views


urlpatterns = [
    path('product_list/', views.list_product, name='product_list'),
    path('product_add/', views.add_product, name='product_add'),
    path('product_detail/<int:id>', views.detail_product, name='product_detail'),
    path('product_edit/<int:id>', views.edit_product, name='product_edit'),
    path('product_delete/<int:id>', views.delete_product, name='product_delete'),

    
]