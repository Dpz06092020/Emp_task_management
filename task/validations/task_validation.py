def validate_add(model):
    msg = []
    if model.get('employee_name', None):
        if not isinstance(model.get('employee_name'), str):
            msg.append("Employee Name Invalid. Must be an String.")
    else:
        msg.append("Employee Name Missing.")

    if model.get('task', None):
        if not isinstance(model.get('task'), str):
            msg.append("Task Invalid. Must be a String.")
    else:
        msg.append("Task Missing.")

    if model.get('time', None):
        if not isinstance(model.get('time'), int):
            msg.append("Time Invalid. Must be an Integer.")
    else:
        msg.append("Time Missing.")

    if msg:
        return False, msg
    else:
        return True, msg



def validate_review(model):
    msg = []
    if model.get('task_id', None):
        if not isinstance(model.get('task_id'), int):
            msg.append("Task ID Invalid. Must be an Integer.")
    else:
        msg.append("Task ID Missing.")

    if model.get('review_status', None):
        if not isinstance(model.get('review_status'), bool):
            msg.append("Review Status Missing. Must be a Boolean.")
    else:
        msg.append("Review Status Missing.")

    if model.get('review_comment', None):
        if not isinstance(model.get('review_comment'), str):
            msg.append("Review Comments Invalid. Must be String.")
    else:
        msg.append("Review Comments Missing.")

    if msg:
        return False, msg
    else:
        return True, msg
