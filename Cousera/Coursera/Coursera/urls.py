"""Coursera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import home
from Curso.views import tema1, quizz, quizz2, tema2, tema3, tema4, tema5, tema6, tema7, tema8, tema9, tema10, tema11, tema12, tema13, tema14, tema15, tema16, tema17, tema18, tema19, tema20, tema21, tema22

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('organica/tema1', tema1),
    path('organica/quizz', quizz),
    path('organica/quizz2', quizz2),
    path('organica/tema2', tema2),
    path('organica/tema3', tema3),
    path('organica/tema4', tema4),
    path('organica/tema5', tema5),
    path('organica/tema6', tema6),
    path('organica/tema7', tema7),
    path('organica/tema8', tema8),
    path('organica/tema9', tema9),
    path('organica/tema10', tema10),
    path('organica/tema11', tema11),
    path('organica/tema12', tema12),
    path('organica/tema13', tema13),
    path('organica/tema14', tema14),
    path('organica/tema15', tema15),
    path('organica/tema16', tema16),
    path('organica/tema17', tema17),
    path('organica/tema18', tema18),
    path('organica/tema19', tema19),
    path('organica/tema20', tema20),
    path('organica/tema21', tema21),
    path('organica/tema22', tema22),

]
