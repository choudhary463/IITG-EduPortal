
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView
app_name = "home"

urlpatterns = [
    path(r'add_notes/', views.add_notes, name="add_notes"),
    path(r'view_notes/', views.view_notes, name="view_notes"),
    path(r'add_club/', views.add_club, name="add_club"),
    path('display_clubs/', views.display_clubs, name='display_clubs'),
    path('addbook/',views.addbook,name='addbook'),
    path('displaybook/',views.displaybook,name='displaybook'),
    path('(?P<username>[\w.@+-]+)/(?P<book_title>[\w.@+-]+)/(?P<status>[\w.@+-]+)/requestbook/',views.requestbook, name='requestbook'),
    path('view_requests/',views.view_requests, name='view_requests'),
    path('(?P<book_title>[\w.@+-]+)/(?P<req_id>[\w.@+-]+)/(?P<req_user>[\w.@+-]+)/(?P<username>[\w.@+-]+)/updatet/', views.updatet,name='updatet'),
    path('(?P<book_title>[\w.@+-]+)/(?P<req_id>[\w.@+-]+)/(?P<req_user>[\w.@+-]+)/(?P<username>[\w.@+-]+)/updatef/', views.updatef,name='updatef'),
    path('notifications/',views.notifications,name='notifications'),
    path('notifications/delete/(?P<n_id>[\w.@+-]+)/',views.n_delete,name='n_delete'),
    path('chatrooms/',views.allchat,name='allchat'),
    path('chatroom/(?P<self>[\w.@+-]+)/(?P<other>[\w.@+-]+)/',views.chatroom,name='chatroom'),
    
    
    path('addcourse/',views.addcourse,name='addcourse'),
    path('course_list/',views.course_list,name='course_list'),
    path('addextcourse/',views.addexternalcourse,name='addextcourse'),
    path('extcourse_list/',views.external_course_list,name='extcourse_list'),
    re_path(r'(?P<coursename>[\w.@+-]+)/(?P<videoname>[\w.@+-]+)/',views.viewcourse),
    path('courses/',TemplateView.as_view(template_name='home/courses.html')),
    path('books/',TemplateView.as_view(template_name='home/books.html')),
    path('notes/',TemplateView.as_view(template_name='home/notes.html')),
    path('requests/',TemplateView.as_view(template_name='home/request.html')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


