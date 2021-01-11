import json
from json.decoder import JSONDecodeError

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from task.forms import CreateUserForm
from task.models import TaskSheet
from task.serializers import FetchTasksSerializer
from task.validations import task_validation
import logging
from django.contrib.auth.models import User

logger = logging.getLogger('taskmanager.logger')
JSON_PARAMS = {'indent': 2}


def landing_view(request):
    logger.info("Home Page Accessed: /")
    return HttpResponse("<h1>Service Up & Running !!</h1>")


@csrf_exempt
@api_view(['POST', ])
def register_view(request):
    try:
        request_data = json.loads(request.body)
        logger.info("Register API Accessed: /")
        form = CreateUserForm(request_data)
        if form.is_valid():
            form.save()
            return HttpResponse('User Registered')
        else:
            msg = []
            for m in form.errors:
                msg.append(m)
            logger.error('Error in Registration : ' + ','.join(msg))
            return HttpResponse('Error in Registration: ' + ','.join(msg))
    except json.decoder.JSONDecodeError as e:
        logger.error('Error in Registration : Malformed Request Body ' + str(e.args[0]))
        return HttpResponse('Malformed request body ' + str(e.args[0]))


# Task Code
@csrf_exempt
@api_view(['PUT', ])
@permission_classes([IsAuthenticated])
def add_task_view(request):
    """
    Function to add new Person
    """
    # Predefined structure for response object.
    response_data = {'status': '', 'code': None, 'message': None, 'data': []}
    logger.info('Task Add Endpoint Accessed : /api/v1/addTask')

    if request.method == 'PUT':
        try:
            models = json.loads(request.body)
            user_obj = User.objects.get(id=request.user.id)
            if not user_obj:
                raise ValidationError("User not found for Authorization Token")

            # Verify all data before Insertion, Fail if any one data is corrupted
            record_count = 0
            for m in models:
                record_count = record_count + 1
                valid_status = task_validation.validate_add(m)
                if not valid_status[0]:
                    raise ValidationError(valid_status[1])

            for task_model in models:
                employee_name = task_model.get('employee_name')
                task = task_model.get('task')
                time = task_model.get('time')

                task_sheet_obj = TaskSheet(employee_name=employee_name, task=task, time=time, user=user_obj)
                try:
                    task_sheet_obj.save()
                    response_data['status'] = True
                    response_data['code'] = 200
                    response_data['message'] = 'Task Sheet Added for User=' + str(request.user.username)
                    response_data['data'] = models
                    logger.info('Task Sheet Added => ' + str(task_sheet_obj.get_dict()))

                except ValueError as e:
                    response_data['status'] = False
                    response_data['code'] = 500
                    response_data['message'] = 'TaskSheet Creation in DB Failed'
                    logger.error('TaskSheet Creation in DB Failed')

        except JSONDecodeError as e:
            response_data['status'] = False
            response_data['code'] = 400
            response_data['message'] = "JSON Error = " + str(e.args[0])
            logger.error('JSON Decode Error in /api/v1/addTask')
        except ValidationError as e:
            response_data['status'] = False
            response_data['code'] = 400
            response_data['message'] = e.args[0]
            logger.error('addTask Validation Failed in /api/v1/addTask ' + str(e.args[0]))
    else:
        response_data['status'] = False
        response_data['code'] = 400  # Bad Request
        response_data['message'] = "Method not supported"
        response_data['data'] = []
        logger.error('Method not Supported in /api/v1/addTask')

    return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)


@csrf_exempt
@api_view(['POST', ])
@permission_classes([IsAuthenticated & IsAdminUser])
def review_task_view(request):
    """
    Function to review task sheet
    """
    # Predefined structure for response object.
    response_data = {'status': '', 'code': None, 'message': None, 'data': []}
    logger.info('Task Review Endpoint Accessed : /api/v1/tasks/reviewTask')
    if request.method == 'POST':
        try:
            models = json.loads(request.body)
            reviewer_obj = User.objects.get(id=request.user.id)
            if not reviewer_obj:
                raise ValidationError("User not found for Authorization Token")

            record_count = 0
            for m in models:
                record_count = record_count + 1
                valid_status = task_validation.validate_review(m)
                if not valid_status[0]:
                    raise ValidationError(valid_status[1])

            for task_model in models:
                task_id = task_model.get('task_id')
                review_status = task_model.get('review_status', False)
                review_comment = task_model.get('review_comment', '')
                try:
                    task_sheet_obj = TaskSheet.objects.get(id=task_id)
                    task_sheet_obj.review_status = review_status
                    task_sheet_obj.review_comment = review_comment
                    task_sheet_obj.reviewer = reviewer_obj
                    task_sheet_obj.save()
                    response_data['status'] = True
                    response_data['code'] = 200
                    response_data['message'] = 'Task Sheet Reviewed for User =' + str(request.user.username)
                    response_data['data'] = models
                    logger.info('Task Sheet Updated => ' + str(task_sheet_obj.get_dict()))

                except ValueError as e:
                    response_data['status'] = False
                    response_data['code'] = 500
                    response_data['message'] = 'TaskSheet Review in DB Failed'
                    logger.error('TaskSheet Review in DB Failed')

        except JSONDecodeError as e:
            response_data['status'] = False
            response_data['code'] = 400
            response_data['message'] = "JSON Error = " + str(e.args[0])
            logger.error('JSON Decode Error in /api/v1/tasks/reviewTask')
        except ValidationError as e:
            response_data['status'] = False
            response_data['code'] = 400
            response_data['message'] = e.args[0]
            logger.error('addTask Validation Failed in /api/v1/tasks/reviewTask ' + str(e.args[0]))
    else:
        response_data['status'] = False
        response_data['code'] = 400  # Bad Request
        response_data['message'] = "Method not supported"
        response_data['data'] = []
        logger.error('Method not Supported in /api/v1/tasks/reviewTask')

    return JsonResponse(response_data, json_dumps_params=JSON_PARAMS)


@permission_classes([IsAuthenticated & IsAdminUser])
class FetchAllTasks(ListAPIView):
    queryset = TaskSheet.objects.all().order_by("id")
    pagination_class = PageNumberPagination
    serializer_class = FetchTasksSerializer
