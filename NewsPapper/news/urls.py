from django.urls import path
from .views import * # импортируем наше представление

urlpatterns = [
    # path означает "путь". В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    #path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('<int:pk>', Post_View.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view())
]