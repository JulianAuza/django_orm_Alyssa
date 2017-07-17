import django
from apps.user_login.models import User

# Create a new user:
def new_user(first_name, last_name, email, age):
    User.objects.create(first_name=first_name, last_name=last_name, email_address=email, age=age)

# Retrieve all users:
def all_users():
    users = User.objects.all()
    for user in users:
        print user.first_name, user.last_name, "- Age:", user.age, "- Email:", user.email_address

# Retrieve the first user:
def first_user():
    user = User.objects.first()
    print user.first_name, user.last_name, "- Age:", user.age, "- Email:", user.email_address
    
# Retrieve the last user:
def last_user():
    user = User.objects.last()
    print user.first_name, user.last_name, "- Age:", user.age, "- Email:", user.email_address

# Users sorted by first name descending:
def users_desc():
    users = User.objects.order_by('-first_name')
    for user in users:
        print user.first_name, user.last_name, "- Age:", user.age, "- Email:", user.email_address

# Get a user by id and change their last name:
def change_last_name(id, new_last_name):
    user = User.objects.get(id=id)
    user.last_name = new_last_name
    user.save()
    print user.first_name, user.last_name, "- Age:", user.age, "- Email:", user.email_address

# Delete a record by id:
def delete_user(id):
    User.objects.get(id=id).delete()
