from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.bloglist, name='bloglist'),
    path('detail/<int:blog_id>/', blog.views.detail, name='detail'),
]
