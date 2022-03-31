from django.db import models
from generic.models import *
from user.models import User

# Create your models here.
STATUS_CHOICE = (
    ('NotStarted', 'NotStarted'),
    ('Pending', 'Pending'),               
    ('Completed', 'Completed')
)

class Project(BaseField):
    project_title = models.CharField(max_length=150)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    status = models.CharField(max_length=30,choices=STATUS_CHOICE)
    estimated_hourse = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)
    completion_date = models.DateTimeField() 
    class Meta():
        db_table = 'project'

    def __str__(self):
        return self.project_title


class ProjectTeam(BaseField):
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    class Meta():
        db_table = 'project_team'

class ProjectModule(BaseField):
    module_name = models.CharField(max_length=50)
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    description = models.TextField()
    estimated_hours = models.IntegerField()
    start_date = models.DateField(auto_now_add=True)

    class Meta(): 
        db_table = 'project_module'

    def __str__(self):
        return self.module_name

PRIORITY = (
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low')
)

class Task(BaseField):
    project_id = models.ForeignKey(Project,on_delete=models.CASCADE)
    project_module_id = models.ForeignKey(ProjectModule,on_delete=models.CASCADE)
    status = models.OneToOneField(ProjectModule,related_name='+',on_delete=models.CASCADE)
    task_name = models.CharField(max_length=30)
    priority = models.CharField(max_length=30,choices=PRIORITY)
    description = models.TextField()
    total_minutes = models.IntegerField()

    class Meta():
        db_table = 'task'
    
    def __str__(self):
        return self.task_name

class UserTask(BaseField):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task,on_delete=models.CASCADE)

    class Meta():
        db_table = 'user_task'
 