from django import forms
from django.contrib.auth.models import User
from .models import CustomUser,ToDoList,Task,Comment
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username','class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password','class':'form-control'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation','class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        return password1
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        if password2 != self.cleaned_data.get('password1'):
            raise forms.ValidationError('Password confirmation does not match')
        return password2
        
class CustomUserRegisterForm(forms.ModelForm):
    
    image_profile = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-img','id':'id_image_profile'}),required=False)
    phone_number = forms.CharField(label='phone_number',widget=forms.TextInput(attrs={'placeholder': 'Phone Number','class':'form-control'}))
    location = forms.CharField(label='location',widget=forms.TextInput(attrs={'placeholder': 'Location','class':'form-control'}))
    class Meta:
        model = CustomUser
        fields = ['image_profile','phone_number','location']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Check if user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('Invalid username or password')

        # If user exists but is not active, return user without authentication
        if not user.is_active:
            self.user_cache = user  # Store user in cache but skip authentication
            return self.cleaned_data

        # Authenticate the user (only if active)
        self.user_cache = authenticate(username=username, password=password)
        if self.user_cache is None:
            raise forms.ValidationError('Invalid username or password')

        return self.cleaned_data

    
class todoListForm(forms.ModelForm):
   is_private = forms.BooleanField(label='is private',widget=forms.CheckboxInput(attrs={'class':'is_private'}),required=False ) 
   name = forms.CharField(label='title',widget=forms.TextInput(attrs={'class':'form-control'}) ) 
   description = forms.CharField(label='description',widget=forms.Textarea(attrs={'class':'form-control'}) ) 
   class Meta:
       model =ToDoList
       fields = ['is_private', 'name', 'description'] 


class PasswordResetRequestForm(forms.Form):
    email =forms.EmailField(label='email',widget=forms.EmailInput(attrs={'placeholder': 'Enter your email...', 'class': 'form-control'} ))

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email','class':'form-control','readonly':'readonly'}))

    class Meta:
        model = User
        fields = ['username', 'email']

class CustomUserUpdateForm(forms.ModelForm):
    location = forms.CharField(label='location', widget=forms.TextInput(attrs={'placeholder': 'Location','class':'form-control',}))
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder':'Enter phone number','class':'form-control'}))
    image_profile = forms.ImageField(label='image profile', required=False)

    class Meta:
        model = CustomUser
        fields = ['image_profile', 'phone_number', 'location', 'Boi']



class NewPassword(forms.Form):
    
    new_pass = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'placeholder':'password...','class': 'form-control'}))
    repeat_new_pass = forms.CharField(label='Repeat New Password', widget=forms.PasswordInput(attrs={'placeholder':'repeat password...','class': 'form-control'}))
    
    
class NewEmail(forms.Form):
    new_email = forms.EmailField(label='New email :',widget=forms.EmailInput(attrs={'placeholder':'Email...','class':'form-control'} ))
    


class create_task(forms.ModelForm):
    title = forms.CharField(label = 'Title :',widget=forms.TextInput(attrs={'placeholder':'enter title....','class':'form-control'} ))
   
    priorities = forms.ChoiceField(label='priorities',choices=Task.PRIORITY_CHOICES,widget=forms.RadioSelect(attrs={'class':'form-control'}))
    due_date = forms.DateField(label='Select the due date :',widget=forms.DateInput(attrs={'type':'date','class':'form-control'}))
    due_time = forms.TimeField(  
        label='Select the due time:',  
        widget=forms.TimeInput(attrs={  
            'class': 'form-control',   
            'type': 'time'  # HTML5 time input  
        }),  
        input_formats=['%H:%M', '%I:%M %p']  # Add accepted time formats  
    )  

    class Meta:
        model=Task
        fields=['title', 'due_date','due_time', 'priorities']
        
        
class comment(forms.ModelForm):
    comment_text=forms.CharField(label='add comment ',widget=forms.Textarea(attrs={'placeholder':'comment ...'}))
    
    class Meta:
        model=Comment
        fields=['comment_text']