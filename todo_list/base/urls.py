from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('hero/', views.hero, name='hero'),
    path('base/', views.base, name='base'),
    path('lists/new/', views.create_todo_list, name='create_todo_list'),
    path('lists/remove/<uuid:list_id>/', views.remove_list, name='remove_list'),
    path('lists/edit/<uuid:list_id>/', views.edit_todo_list, name='edit_todo_list'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/reset_pass', views.reset_pass_edit_profile, name='edit_rest_pass'),
    path('profile/edit/reset_email', views.NewEmail_view, name='edit_rest_email'),
    path('profile/edit/reset_email/pin', views.confirm_email_edit, name='confirm_email_edit'),
    path('my_lists/', views.lists_view, name='lists_view'),
 


    path('list/<uuid:list_id>/', views.tasks_for_list, name='tasks_for_list'),
    path('task/<uuid:task_id>/change_status/', views.change_task_status, name='change_task_status'),  
    path('task/<uuid:task_id>/remove/', views.remove_task, name='remove_task'),  
    path('list/<uuid:list_id>/create_task/', views.add_task, name='add_task'),      

    path('logout/', views.logout_view, name='logout'),
 
    path('confirm-registration/', views.confirm_registration, name='confirm_registration'),  # Add this line
    path('confirm/<str:pk>/', views.send_pin, name='send_pin'),
    path('password_rest/',views.password_reset_request,name='password_reset_request'),
    path('password_reset_confirm/',views.password_reset_confirmation,name='password_reset_confirm'),
    path('register/step1',views.register_1,name='register_step1'),
    path('register/step2',views.register_2,name='register_step2'),
    
    # today tasks:
    path("today_tasks/", views.today_tasks,name="today_tasks"),
    path('task/<uuid:task_id>/complete/', views.complete_task, name='complete_task'),
    path('task/<uuid:task_id>/ignore/', views.ignore_task, name='ignore_task'),
    
    #shared lists
    path('shared_lists/',views.shared_lists,name='shared_list'),
    path('add_comment/<uuid:list_id>/',views.add_comment,name='add comment'),
    path('comment/<uuid:list_id>/',views.comments_view,name='comments'),
    path('shared_lists/<uuid:list_id>/',views.check_shared_list,name='check_list')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
