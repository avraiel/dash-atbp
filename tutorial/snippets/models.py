from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.db.models.functions import Now

# from django.contrib.auth.models import AbstractBaseUser, PermissionMixin, BaseUserManager

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])
EMPLOYEE_STATUS_CHOICES = {
    "full-time": "Full-time", 
    "suspended": "Suspended",
    "on-probation": "Probation",
}   

ROLE_STATUS_CHOICES = {
    "active": "Active", 
    "inactive": "Inactive",
    "deleted": "Deleted",
}   

''' 
To anyone reading this, these models will be serialized using serializers.py. Serializing means that these each object in the Django reference table will be parsed into a json object. This json object can be fed through different frontends. 
'''
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

class Employee(models.Model):
    employee_id = models.AutoField(primary_key = True)
    employee_first_name = models.CharField(max_length = 50)
    employee_middle_name = models.CharField(max_length = 50)
    employee_last_name = models.CharField(max_length = 50)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)
    started_on = models.DateTimeField()
    ended_on = models.DateTimeField(default = None, null = True, blank = True)
    last_edited_on = models.DateTimeField(auto_now_add=True)
    employee_status = models.CharField(choices = EMPLOYEE_STATUS_CHOICES, default='full-time', max_length = 50)

    def __str__(self):
        return self.employee_first_name + " " + self.employee_last_name

class Role(models.Model):
    role_id = models.AutoField(primary_key = True)
    role_name = models.CharField(max_length = 100)
    role_description = models.CharField(max_length = 1000)
    division = models.CharField(max_length = 100)
    added_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="+")
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(default = None, null = True, blank = True)
    role_status = models.CharField(choices = ROLE_STATUS_CHOICES, default='active', max_length = 50)

    def __str__(self):
        return self.role_name


# class User(AbstractBaseUser, PermissionMixin):


