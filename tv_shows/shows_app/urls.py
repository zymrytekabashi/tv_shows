from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('shows/new', views.new),
    path('shows', views.shows),
    path('shows/create', views.create),
    path('shows/<int:id>', views.one_show),
    path('shows/edit/<int:id>', views.edit_show),
    path('update/<int:id>', views.update),
    path('shows/destroy/<int:id>', views.destroy)
]
