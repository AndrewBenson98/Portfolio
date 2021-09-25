from django.urls import path
from .views import HomeView, ProjectListView,ProjectDetailView, ResumeTemplateView,ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='portfolio-home'),
    path('projects/', ProjectListView.as_view(), name='portfolio-projects'),
    path('projects/<str:url_name>/', ProjectDetailView.as_view(), name='project-detail'),
    path('resume/', ResumeTemplateView.as_view(), name='portfolio-resume'),
    path('contact/', ContactView.as_view(), name='portfolio-contact'),

]