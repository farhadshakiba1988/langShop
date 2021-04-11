from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<int:pk>', views.Profile, name="profile"),
    path('item/<int:id>', views.product_detail, name='detail'),
    path('product/', views.product_grid, name='product'),
    path('youtube/', views.youtube_page, name='youtube'),
]
