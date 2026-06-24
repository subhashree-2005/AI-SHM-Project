from django.contrib import admin
from django.urls import path

from app.views import (

    home,
    projects,
    dashboard,
    contact,
    predict_page,
    get_chart_data
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home),

    path('projects/', projects),

    path('dashboard/', dashboard),

    path('contact/', contact),

    path('predict-page/', predict_page),

    path(
        'chart-data/',
        get_chart_data
    ),
]