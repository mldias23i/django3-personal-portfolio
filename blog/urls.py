from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
    # URL pattern for displaying all blogs
    path('', views.all_blogs, name="all_blogs"),
    # URL pattern for displaying a specific blog detail
    path('<int:blog_id>/', views.detail, name="detail"),    
]
