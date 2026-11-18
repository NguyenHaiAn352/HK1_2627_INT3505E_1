user_data = {
    "1": {
        "f": "placeholder",
        "l": "placeholder",
        "email": "placeholder",
        "first_name": "placeholder 2",
        "last_name": "placeholder 2"
    }, 
}

def get_user(uid):
    string_id = str(uid)
    return user_data.get(string_id)