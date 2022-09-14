from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.LessonListView.as_view(), name='lessons-list'),
    path('lessons/<str:slug>/', views.LessonDetailView.as_view(), name='lessons-detail'),
    path('posts/', views.PostListView.as_view(), name='posts-list'),
    path('posts/<str:slug>/', views.PostDetailView.as_view(), name='posts-detail'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews-list'),
    path('social-accounts/', views.SocialAccountListView.as_view(), name='social-account-list'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
    path('contact/', views.ContactView.as_view(), name='contact')
]