
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/',views.Submission.as_view()),
    path('login/',views.loginUser),
    path('register/',views.registerUser),
    path('questions/',include('question.urls')),
    path('participant/',include('participant.urls')),
    path('group/',include('group.urls')),
    path('submit/',views.Submission.as_view())
]
