from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


    path('', views.blog_index, name='blogIndex'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('article/update/<int:article_id>', views.update, name='update'),
    path('article/delete/<int:article_id>', views.delete, name='delete'),
    path('article/create', views.create, name='create'),
]
