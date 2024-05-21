

def get_create_task_query(title, description, user_fk):
    insert_query = '''INSERT INTO tasks (
            title, description, user_fk
        ) VALUES
        (:title, :description, :user_fk)'''
    insert_params = {'title': title, 'description': description, 'user_fk': user_fk}

    return insert_query, insert_params

def get_task_list_query(user_fk):
    select_query = '''SELECT * FROM tasks WHERE user_fk = :user_fk'''
    select_params = {'user_fk': user_fk}

    return select_query, select_params

def get_task_detail_query(task_pk):
    select_query = 'SELECT * FROM tasks WHERE task_pk = :task_pk;'
    select_params = {'task_pk': task_pk}

    return select_query, select_params

def get_update_task_query(task_pk, title, description, status, deleted):
    update_query = '''UPDATE tasks
        SET title = :title,
            description = :description,
            status = :status,
            deleted = :deleted,
            updated_at = NOW()
        WHERE task_pk = :task_pk;'''
    update_params = {
        'task_pk': task_pk,
        'title': title,
        'description': description,
        'status': status,
        'deleted': deleted
    }

    return update_query, update_params

def get_delete_task_query(task_pk):
    delete_query = 'DELETE FROM tasks WHERE task_pk = :task_pk;'
    delete_param = {'task_pk': task_pk}

    return delete_query, delete_param
