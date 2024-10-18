from django.shortcuts import render,redirect,get_object_or_404
from .models import CustomUser, Task, ToDoList,ActivityLog,Comment
from .forms import UserRegisterForm, CustomUserRegisterForm,todoListForm,NewPassword, CustomUserUpdateForm, UserUpdateForm, UserLoginForm,PasswordResetRequestForm,create_task,comment
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.utils import timezone
from django.contrib.auth import logout
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


               
def user_info(request):
    if request.user.is_authenticated:
        custom_user = CustomUser.objects.get(user= request.user)
        return {
            'user':request.user,
            'image_profile':custom_user.image_profile
        }
    else:
        return{}


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_active:
                auth_login(request, user)
                next_url = request.GET.get('next','hero')
                return redirect(next_url)
            else:
                return redirect('send_pin', pk=user.custom_user.pk)
    else:
        form = UserLoginForm()
    return render(request, 'base/login.html', {'form': form})



def hero(request):
   
    
    return render(request, 'base/base.html')

from .utils import get_icon_for_title
@login_required

# def create_todo_list(request, list_id=None):  
#     todo_list_instance = None  

#     if list_id:  
#         todo_list_instance = get_object_or_404(ToDoList, id=list_id)  

#     if request.method == 'POST':  
#         form = todoListForm(request.POST, instance=todo_list_instance)  
#         if form.is_valid():  
#             todo_list = form.save(commit=False)  
#             try:  
#                 custom_user = CustomUser.objects.get(user=request.user)  
#             except CustomUser.DoesNotExist:  
#                 raise Http404("User does not exist")  
                
#             todo_list.user = custom_user  
#             todo_list.icon = get_icon_for_title(todo_list.name)  # Use the name for the icon  
#             todo_list.save()  

#             # Log activity after saving the list  
#             activity_log(request.user, 'add', f"{todo_list.name} list")  
#             return redirect('lists_view')  

#     else:  
#         form = todoListForm(instance=todo_list_instance)  

#     # Log activity based on whether we are editing or creating  
#     if todo_list_instance and todo_list_instance.name:  # Ensure it's not None  
#         activity_log(request.user, 'edit', f"{todo_list_instance.name} list")  
   
        

#     return render(request, 'base/create_todo_list.html', {  
#         'form': form,  
#         'list': todo_list_instance,  
#         'title': 'Create List' if todo_list_instance is None else 'Edit List'  
#     })  

def create_todo_list(request):
    if request.method=='POST':
        form=todoListForm(request.POST)
        if form.is_valid():
            todo_list=form.save(commit=False)
            try:
                custom_user=CustomUser.objects.get(user=request.user)
            except CustomUser.DoesNotExist:
                raise Http404("user does not exist")
            todo_list.user=custom_user
            todo_list.icon=get_icon_for_title(todo_list.name)
            todo_list.save()
            activity_log(request.user, 'add', f"{todo_list.name} list")
    
            return redirect('lists_view')
    else:
        form=todoListForm()
    return render(request,'base/create_todo_list.html',{'form':form})

def edit_todo_list(request,list_id):
    todo_list_instance=get_object_or_404(ToDoList,id=list_id)
    if request.method=='POST':
        form=todoListForm(request.POST,instance=todo_list_instance)
        if form.is_valid():
            todo_list=form.save(commit=False)
            todo_list.icon=get_icon_for_title(todo_list.name)
            todo_list.save()
            activity_log(request.user, 'edit', f"{todo_list.name} list")
            return redirect('lists_view')
    else:
        form=todoListForm(instance=todo_list_instance)
    return render(request,'base/edit_todo_list.html',{'form':form,'title':'edit list','list':todo_list_instance,'todo_list_instance':todo_list_instance})
    
def base(request):
    return render(request, 'base/base.html')
def sidebar(request):
    custom_user = CustomUser.objects.get(user=request.user)  # Correctly retrieve the CustomUser instance
    user_last_lists = ToDoList.objects.filter(user=custom_user).order_by('-updated_at')  # Ensure the field name is correct
    print(type
          
    (user_last_lists))
    print('-5646')
    return render(request, 'base/sidebar.html',{'user_last_lists':user_last_lists})
@login_required
def header_view(request):
    # if request.user.is_authenticated:
    #     user = request.user
    #     custom_user = CustomUser.objects.get(user=user)
    #     print(custom_user.image_profile.url)  # تأكد من أن الرابط يظهر بشكل صحيح هنا
    #     return render(request, 'base/header.html', {'user': user, 'custom_user': custom_user})
    return render(request, 'base/header.html')


@login_required
def profile_view(request):
    custom_user = CustomUser.objects.get(user=request.user)
    activity_logs = ActivityLog.objects.filter(user=request.user).order_by('-update_at')[:6]
    return render(request, 'base/profile.html', {'custom_user': custom_user, 'title': 'Profile','activity_logs':activity_logs})


@login_required
def edit_profile(request):
    try:
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            custom_user_form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user.custom_user)

            if user_form.is_valid() and custom_user_form.is_valid():
                user_form.save()
                custom_user_form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            user_form = UserUpdateForm(instance=request.user)
            custom_user_form = CustomUserUpdateForm(instance=request.user.custom_user)
            print(user_form)
            print(custom_user_form)
    except Exception as e:
        print(f'the error is : {e}')

    return render(request, 'base/edit_profile.html', {
        'user_form': user_form,
        'custom_user_form': custom_user_form,
        'title': 'Edit Profile'
    })
@login_required
# def today_tasks(request):
#     custom_user = CustomUser.objects.get(user=request.user)
#     today = timezone.now().date()
#     today_tasks = Task.objects.filter(to_do_list__user=custom_user, due_date__date=today)
#     upcoming_tasks = Task.objects.filter(to_do_list__user=custom_user, due_date__date__gt=today)
#     user_lists = ToDoList.objects.filter(user=custom_user).order_by('-updated_at')
    
#     context = {
#         'today_tasks': today_tasks,
#         'today_count': today_tasks.count(),
#         'upcoming_count': upcoming_tasks.count(),
#         'user_lists': user_lists,
#         'user_tags': [],  # Implement tag functionality
#     }
#     return render(request, 'base/today.html', context)






@login_required
def add_task(request, list_id):  
    print("Entering add_task view")
    user = request.user
    print(f"User: {user}, Type: {type(user)}")
    
    try:
        todo_list = get_object_or_404(ToDoList, id=list_id)  
        print(f"ToDoList: {todo_list}")
        
        if request.method == 'POST':  
            print("POST request received")
            form_task = create_task(request.POST)  
            if form_task.is_valid():  
                print("Form is valid")
                task = form_task.save(commit=False)  
                task.to_do_list = todo_list  
                task.save()  
                print(f"Task saved: {task}")

                # Log the activity
                print("Attempting to log activity")
                activity_log(user, "add", f"{task.title} Task")  
                print("Activity logged successfully")

                return redirect('tasks_for_list', list_id)  
            else:
                print(f"Form errors: {form_task.errors}")
        else:  
            print("GET request received")
            form_task = create_task()  
        
        return render(request, 'base/add_task.html', {'form_task': form_task, 'title': todo_list.name})  
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        # You might want to handle the exception appropriately here
        raise  # Re-raise the exception after logging





def activity_log(user, action, related_object):
    print('Entering activity_log function')
    print(f"User: {user}, Type: {type(user)}")
    
    if not isinstance(user, User):
        print(f"Invalid user type: {type(user)}")
        raise ValueError("Invalid user type")

    ActivityLog.objects.create(
        user=user,
        action=action,
        related_object=related_object
    )
    print('Activity logged successfully')

@login_required  
def add_task(request, list_id):  
    print("Entering add_task view")
    user = request.user
    print(f"User: {user}, Type: {type(user)}")
    
    try:
        todo_list = get_object_or_404(ToDoList, id=list_id)  
        print(f"ToDoList: {todo_list}")
        
        if request.method == 'POST':  
            print("POST request received")
            form_task = create_task(request.POST)  
            if form_task.is_valid():  
                print("Form is valid")
                task = form_task.save(commit=False)  
                task.to_do_list = todo_list  
                task.save()  
                print(f"Task saved: {task}")

                # Log the activity
                print("Attempting to log activity")
                activity_log(user, "add", task.title)  
                print("Activity logged successfully")

                return redirect('tasks_for_list', list_id)  
            else:
                print(f"Form errors: {form_task.errors}")
        else:  
            print("GET request received")
            form_task = create_task()  
        
        return render(request, 'base/add_task.html', {'form_task': form_task, 'title': todo_list.name})  
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        # You might want to handle the exception appropriately here
        raise  # Re-raise the exception after logging
def logout_view(request):
    logout(request)
    return redirect('login')


def generate_pin():
    return random.randint(100000, 999999)

def send_confirmation_email(email, pin):
    send_mail(
        'Confirm Your Registration',
        f'Your confirmation pin is {pin}',
        'todo.list.alg@gmail.com',
        [email],
        fail_silently=False,
    )
def confirm_registration(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        try:
            custom_user = CustomUser.objects.get(confirmation_pin=pin)
            custom_user.is_active = True
            custom_user.confirmation_pin = None
            custom_user.save()
            custom_user.user.is_active = True
            custom_user.user.save()
            messages.success(request, 'Your account has been activated. You can now log in.')
            return redirect('login')
        except CustomUser.DoesNotExist:
            messages.error(request, 'Invalid confirmation pin.')
    return render(request, 'base/confirm_registration.html')


def register_1(request):
    if request.method == 'POST':
         user_form = UserRegisterForm(request.POST)
        # custom_user_form = CustomUserRegisterForm(request.POST, request.FILES)
         if user_form.is_valid():
             request.session['basic_info']=user_form.cleaned_data
             return redirect('register_step2')
            # user = user_form.save(commit=False)
            # user.is_active = False
            # user.save()
            # custom_user = custom_user_form.save(commit=False)
            # custom_user.user = user
            # custom_user.save()
            # return redirect('send_pin', pk=custom_user.pk)
    else:
        user_form = UserRegisterForm()
        # custom_user_form = CustomUserRegisterForm()
    return render(request, 'base/register.html', {'user_form': user_form})
def register_2(request):
    
    if 'basic_info' not in request.session:
        redirect('register_step1')
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        custom_user = None
        if form.is_valid():
            basic_info = request.session.get('basic_info')
            print(basic_info)
            user = User.objects.create_user(
                username=   basic_info['username'],
                email = basic_info['email'],
                password=basic_info['password1']
            )
            user.is_active=False
            user.save()
            custom_user = form.save(commit=False)
            custom_user.user = user
            custom_user.save()
            del request.session['basic_info']
            return redirect('send_pin',pk=custom_user.pk)
    else :
        form = CustomUserRegisterForm()
    return render(request, 'base/register_2.html', {'form': form})
        
def send_pin(request, pk):
    custom_user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        pin = generate_pin()
        custom_user.confirmation_pin = pin
        custom_user.save()
        try:
            send_confirmation_email(custom_user.user.email, pin)
        except:
            print('there is somthing wrong')
        
        return redirect('confirm_registration')
    return render(request, 'base/send_pin.html', {'email': custom_user.user.email})


def password_reset_request(request):
    if request.method =='POST':
        form = PasswordResetRequestForm(data = request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                customer_user = User.objects.get(email=email)
                Customer_profile = CustomUser.objects.get(user=customer_user)
                pin = generate_pin()
                Customer_profile.confirmation_pin = pin
                Customer_profile.save()
                send_confirmation_email(email,pin)
                messages.success(request,'Send pin in your email successfully ') 
                return redirect('password_reset_confirm')
            except CustomUser.DoesNotExist:
                    messages.error(request,'the email not found')
    else:
        form = PasswordResetRequestForm()
    return render(request,'base/Reset_password_request.html',{'form':form})
           

def password_reset_confirmation(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        new_password = request.POST.get('new_password')
        try:
            customer_user = CustomUser.objects.get(confirmation_pin=pin)  # Get user by pin
            customer_user.user.set_password(new_password)  # Set the new password
            customer_user.confirmation_pin = None  # Clear the pin after use
            customer_user.user.save()  # Save the user
            customer_user.save()  # Save the custom user
            messages.success(request, 'The password has been changed successfully.')
            return redirect('login')  # Redirect to login after successful change
        except CustomUser.DoesNotExist:
            messages.error(request, 'The pin is incorrect or has expired.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')  # General error handling
    return render(request, 'base/password_reset_confirm.html')  # Render the confirmation page

@login_required
def reset_pass_edit_profile(request):
    if request.method == 'POST':
        user = request.user
        form = NewPassword(request.POST)
        if form.is_valid():
            new_pass = form.cleaned_data.get('new_pass')
            user.set_password(new_pass)
            user.save()
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = NewPassword()

    return render(request, 'base/reset_pass_in_edit.html', {'form': form, 'title': 'Reset Password'})

from .forms import NewEmail
@login_required
def NewEmail_view(request):
    if request.method =='POST':
        user = request.user
        form = NewEmail(request.POST)   
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            request.session['new_email'] = str(new_email)
           
            return redirect('confirm_email_edit')
    else:
        form = NewEmail()
    return render(request,'base/change_email.html',{'form':form,'title':'Change Email'} )
@login_required
def confirm_email_edit(request):
    new_email = request.session.get('new_email')
    if request.method == 'GET':
           pin = generate_pin()
           request.session['pin'] = pin  # حفظ الـ pin في الجلسة
           send_confirmation_email(new_email, pin)
    if request.method == 'POST':
        confirm_pin = request.POST.get('pin')  # جلب الـ pin المدخل من الفورم
        print(request.session.get('pin'))
        print(type(confirm_pin))
        print(type(request.session.get('pin')))
        if confirm_pin == str(request.session.get('pin')):
            
            # تحديث البريد الإلكتروني
            request.user.email = new_email
            request.user.save()  # حفظ المستخدم بعد التعديل
            del request.session['new_email']
            del request.session['pin']  # حذف الـ pin بعد الاستخدام
            messages.success(request, 'Your email has been updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'The PIN is incorrect. Please try again.')
    
    return render(request,'base/confirm_email_with_pin.html',{'title':'Confirm Email '})

@login_required
def lists_view(request):
    custom_user = CustomUser.objects.get(user = request.user)
    search_query = request.GET.get('search','')
    if search_query:
        user_lists = ToDoList.objects.filter(user = custom_user,name__icontains=search_query).order_by('-updated_at')
    else:
        user_lists = ToDoList.objects.filter(user = custom_user).order_by('-updated_at')
   
    if user_lists.exists():
       return render(request,'base/user_lists.html',{'user_lists':user_lists,'title':' My Lists','search_query':search_query} )
    else:
        messages.info(request,'There is no lists')
    return render(request,'base/user_lists.html',{'user_lists':user_lists} )



def tasks_for_list(request, list_id):
    custom_user = CustomUser.objects.get(user=request.user)
    to_do_list = ToDoList.objects.get(id=list_id)
    search_query = request.GET.get('search', '')
    filter_query = request.GET.get('filter', '')

    # Start with all tasks for the to_do_list
    tasks = Task.objects.filter(to_do_list=to_do_list)

    # Apply filter if provided
    if filter_query:
        if filter_query == 'low':
            tasks = tasks.filter(priorities='low')
        elif filter_query == 'medium':
            tasks = tasks.filter(priorities='medium')
        elif filter_query == 'high':
            tasks = tasks.filter(priorities='high')

    # Apply search if provided
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    return render(request, 'base/tasks_for_list.html', {'tasks': tasks, 'title': f'Tasks for List {to_do_list}', 'search_query': search_query, 'list_id': list_id})

def change_task_status(request,task_id):
    task = get_object_or_404(Task,task_id = task_id)
    
    if task.status =='not_started':
        task.status ='in_progress'
    elif task.status =='in_progress':
        task.status ='completed'
    else:
        task.status =='not_started'
        
    task.save()
    return redirect('tasks_for_list',list_id=task.to_do_list_id)
    
@login_required
def remove_task(request, task_id):
    try:
        task = get_object_or_404(Task, task_id=task_id)
        list_id = task.to_do_list_id
        task.delete()
        activity_log(request.user,'remove',task.title)
        messages.success(request, 'Task deleted successfully.')
    except Task.DoesNotExist:
        messages.error(request, 'Task not found.')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
    return redirect('tasks_for_list', list_id=list_id)

@login_required
def remove_list(request, list_id):
    to_do_list = get_object_or_404(ToDoList, id=list_id)
    to_do_list.delete()
    activity_log(request.user,'remove',to_do_list.name)
    messages.success(request, 'To-do list deleted successfully.')
    return redirect('lists_view')

@login_required
def today_tasks(request):
    custom_user = CustomUser.objects.get(user=request.user)
    today = timezone.now().date()
    tasks = Task.objects.filter(
        to_do_list__user=custom_user,
        due_date__date=today
    ).exclude(status='completed').order_by('due_time')
    return render(request, 'base/today_tasks.html', {'tasks': tasks, 'title': 'Today\'s Tasks'})

def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, task_id=task_id)
        task.status = 'completed'
        task.save()
        messages.success(request, f'Task "{task.title}" marked as completed.')
    return redirect('today_tasks')  # Redirect to the today's tasks page

def ignore_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, task_id=task_id)
        task.status = 'ignored'
        task.save()
        messages.success(request, f'Task "{task.title}" ignored.')
    return redirect('today_tasks')  # Redirect to the today's tasks page

def complete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, task_id=task_id)
        task.status = 'completed'
        task.save()
        messages.success(request, f'Task "{task.title}" marked as completed.')
    return redirect('today_tasks')

def ignore_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, task_id=task_id)
        task.status = 'ignored'
        task.save()
        messages.success(request, f'Task "{task.title}" ignored.')
    return redirect('today_tasks')

from django.db.models import Q
def shared_lists(request):
    user = request.user
    custom_user = CustomUser.objects.get(user=user)
    lists_shared = ToDoList.objects.filter(~Q(user=custom_user), is_private=True).annotate(Count('tasks'))

    return render(request, 'base/shared_lits.html', {'title': 'Shared Lists', 'lists_shared': lists_shared})

def add_comment(request,list_id):
    list=get_object_or_404(ToDoList,id=list_id)
    if request.method=='POST':
        form = comment(request.POST)
        custom_user = CustomUser.objects.get(user = request.user)
        if form.is_valid():
            comment_save=form.save(commit=False)
            comment_save.user=custom_user
            comment_save.todo_list=list
            comment_save.save()
            return redirect('comments',list_id)
    else:
        form=comment()
    
    return render(request,'base/add_comment.html',{'form':form,'title':'add comment'})
        
def comments_view(request,list_id):
    list = get_object_or_404(ToDoList,id = list_id)
    comments = Comment.objects.filter(todo_list=list)
    return render(request,'base/comments.html',{'comments':comments,'title':'comments'})



def check_shared_list(request,list_id):
    list = get_object_or_404(ToDoList,id=list_id)
    tasks = Task.objects.filter(to_do_list=list)
    return render(request,'base/check_shared_list.html',{'tasks':tasks,'title':list.name})    