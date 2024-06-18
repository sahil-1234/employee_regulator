def does_user_exist(username):
    try:
        get_users().index(username)
    except ValueError:
        return False
    else:
        return True
