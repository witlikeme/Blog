from django.urls import path,re_path

from . import views

app_name = 'blog'
urlpatterns = [
#对 url 函数来说，第二个参数传入的值必须是一个函数。而 IndexView 是一个类，不能直接替代 index 函数。好在将类视图转换成函数视图非常简单，只需调用类视图的 as_view() 方法即可
    path('',views.IndexView.as_view(),name='index'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]