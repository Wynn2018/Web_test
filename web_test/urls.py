from django.conf.urls import url
from django.contrib import admin

from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.Login.as_view()),
    url(r'^register/', views.register.as_view()),
    url(r'^onload/', views.onload.as_view()),
    url(r'^find/$',views.find_data.as_view()),
    url(r'^main/search/',views.search.as_view()),
    url(r'^main/search_null/',views.search_null.as_view()),
    url(r'^main/', views.main),
    url(r'^add_data/', views.add_data.as_view()),
    url(r'',views.index),

]