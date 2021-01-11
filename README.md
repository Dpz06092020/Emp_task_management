Api to register new employee 'api/v1/auth/register', register_view, name='register'
Api to login 'api/v1/auth/login', TokenObtainPairView.as_view(), name='token'
Api to create refresh token: 'api/v1/auth/refresh', TokenRefreshView.as_view(), name='refresh'
Api to add new task by the employee:'api/v1/tasks/addTask', add_task_view, name='addTask'
Api to review task: 'api/v1/tasks/reviewTask', review_task_view, name='reviewTask'
Api to fetch all employee list:'api/v1/tasks/fetchAll', FetchAllTasks.as_view(), name='FetchTasks
