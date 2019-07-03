from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='blog'
urlpatterns = [
    path('', login_required(views.AllPostView.as_view()), name='main'),
    path('create/', login_required(views.PostCreateView.as_view()), name='create'),
    path('detail/<int:pk>/', login_required(views.PostDetailView.as_view()), name='detail'),
    # path('detail/<int:pk>/comment', views.comment_view)
]

# urlpatterns = [
#     path('', views.main, name='main'),
#     path('login/', views.login, name='login'),
#     path('register/', views.register, name='register'),
#     path('create/', views.create, name='create'),
#     path('<int:post_id>/detail/', views.detail, name='detail'),
# ]