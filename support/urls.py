from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('send_message/', views.send_message, name='send_message'),
    path('report_incident/', views.report_incident, name='report_incident'),
    path('review_incidents/', views.review_incidents, name='review_incidents'),
    path('update_incident/<int:incident_id>/', views.update_incident, name='update_incident'),
    path('view_incidents/', views.view_incidents, name='view_incidents'),
    path('', views.home, name='home'),
    path('resource1/', views.resource1, name='resource1'),
    path('resource2/', views.resource2, name='resource2'),
    path('resource3/', views.resource3, name='resource3'),
    path('resource4/', views.resource4, name='resource4'),
    path('resource5/', views.resource5, name='resource5'),
    path('story1/', views.story1, name='story1'),
    path('story2/', views.story2, name='story2'),
    path('story3/', views.story3, name='story3'),
]

