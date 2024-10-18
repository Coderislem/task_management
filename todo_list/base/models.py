from django.contrib.auth.models import User
from django.db import models
import uuid
from datetime import time



class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_profile = models.ImageField(upload_to='profiles/',default='profiles/avatar.jpg', null=True, blank=True)
    confirmation_pin  = models.CharField(max_length=6, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    Boi = models.TextField(null=True,blank=True)
    location = models.TextField(null=True,blank=True)
    phone_number  =models.CharField(null=True,blank=True,max_length=13)

    def __str__(self):
        return self.user.username if self.user else "No User"

# نموذج قائمة المهام
class ToDoList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='todo_lists')
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, default='fa-list-alt')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "To-Do List"
        verbose_name_plural = "To-Do Lists"

# نموذج المهام
class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('expired','Expired'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    due_time = models.TimeField(default=time(12, 0)) 
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='not_started')
    due_date = models.DateTimeField(null=True, blank=True)
    priorities = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['status']),
        ]

# نموذج التسمية
class Label(models.Model):
    label_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label_name = models.CharField(max_length=255)

    def __str__(self):
        return self.label_name

# نموذج ربط المهام بالتسميات
class LabelTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='label_tasks')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, related_name='label_tasks')

    class Meta:
        unique_together = ('task', 'label')
        verbose_name = "Label Task"
        verbose_name_plural = "Label Tasks"

# نموذج التعليقات على المهام
class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

# نموذج القوائم المشتركة
class SharedList(models.Model):
    PERMISSION_CHOICES = [
        ('read', 'Read'),
        ('write', 'Write'),
    ]
    list_id = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='shared_lists')
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='shared_lists')
    permission = models.CharField(max_length=50, choices=PERMISSION_CHOICES)

    class Meta:
        unique_together = ('list_id', 'user_id')
        verbose_name = "Shared List"
        verbose_name_plural = "Shared Lists"

# نموذج سجل الأنشطة
class ActivityLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=255)
    related_object = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.user.username} {self.action} - {self.related_object}'

    class Meta:
        verbose_name = "Activity Log"
        verbose_name_plural = "Activity Logs"

# نموذج الإشعارات
class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='notifications')
    notification_time = models.DateTimeField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.username} on {self.task.title}'

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
        indexes = [
            models.Index(fields=['is_read']),
        ]
