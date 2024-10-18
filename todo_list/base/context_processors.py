from .models import CustomUser,ToDoList
from django.db.models import Count
def user_info(request):
    if request.user.is_authenticated:
        try:
            user_profile = CustomUser.objects.get(user = request.user)
            return {
                'user':user_profile,
                'image_profile':user_profile.image_profile
                
            }
        except:
            print('there is error ')
    return{}
         
def side_bare_links(request):
    if request.user.is_authenticated:
        custom_user = CustomUser.objects.get(user=request.user)
        user_last_lists = ToDoList.objects.filter(user=custom_user).annotate(task_count=Count('tasks')).order_by('-updated_at')[:3]
        return {'custom_user': custom_user, 'user_last_lists': user_last_lists}
    return {'custom_user': None, 'user_last_lists': []}