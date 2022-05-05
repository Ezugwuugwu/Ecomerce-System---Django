from django.urls import path

from OkangaShopApp import views

urlpatterns = [

    path('login/>', views.project_login, name="login_project"),
    path('register/>', views.user_register, name="register_user"),

    path('create/', views.okanga_page, name="okanga_page"),
    path('get/', views.get_all_items, name="get_all_articles"),
    path('get/<int:id>', views.retrieve_project, name="retrieve_project"),
    path('delete/<int:id>', views.delete_project, name="delete_project"),
    path('update/<int:id>', views.update_project, name="update_project"),

]
