from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView

# Define the app name to differentiate between different apps
app_name = 'app'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),

    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),

    path('post/', AddPostView.as_view(), name='post'),


]
