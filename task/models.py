from django.db import models
from django.contrib.auth.models import User


class TaskSheet(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, db_column='user_id',
                             related_name='employee_id')
    employee_name = models.CharField(max_length=20, blank=False, null=False)
    task = models.CharField(max_length=30, blank=False, null=False)
    time = models.IntegerField(blank=False, null=False)
    review_status = models.BooleanField(default=False)
    review_comment = models.CharField(max_length=50, blank=True)
    reviewer = models.ForeignKey(User, null=True, on_delete=models.PROTECT, db_column='reviewer_id',
                                 related_name='manager_id')

    class Meta:
        db_table = 'tasksheet'

    def get_dict(self):
        dict_obj = {'employee_name': self.employee_name if self.employee_name else None,
                    'task': self.task if self.task else None,
                    'time': str(self.time) if self.time else None,
                    'user': self.user.id if self.user.id else None,
                    'review_status': str(self.review_status) if self.review_status else None,
                    'review_comment': str(self.review_comment) if self.review_comment else None
                    }
        return dict_obj
