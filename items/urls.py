from django.urls import path
from . import views

urlpatterns = [
    path("", views.comps, name='home'),
    path("profile/<str:pk>", views.profile, name='profile'),
    path("create-product/", views.create_product, name='create-product'),
    path("login/", views.login, name='login'),
    path("error/", views.error_page, name='error'),
    path("sign-out/", views.sign_out, name='sign-out'),
    path("sign-up/", views.sign_up, name='sign-up'),
    path("product/", views.product, name='product'),
    path('company',views.company,name='superuser'),
    path('create-company',views.create_company,name='create-company'),
    path('edit-company',views.edit_company,name='edit-company'),
    path('edit-products',views.edit_products,name='edit-products'),
    path('delete-product/<str:pk>',views.delete_product,name='delete-product'),
    path('edit-product/<str:pk>',views.edit_product,name='edit-product'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about ,name='about'),

]
