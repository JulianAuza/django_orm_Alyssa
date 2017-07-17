import django
from apps.dojo_ninjas.models import Dojo, Ninja

# create a new dojo
def new_dojo(name, city, state):
    return Dojo.objects.create(name=name, city=city, state=state)
    
# create a new ninja
def new_ninja(first_name, last_name, dojo_name):
    dojo = Dojo.objects.get(name=dojo_name)
    return Ninja.objects.create(first_name=first_name, last_name=last_name, dojo = dojo)

# all ninjas from the first dojo
def first_dojo_ninjas():
    ninjas = Dojo.objects.first().ninjas.all()
    for ninja in ninjas:
        print ninja.first_name, ninja.last_name

# all ninjas from the last dojo
def last_dojo_ninjas():
    ninjas = Dojo.objects.last().ninjas.all()
    for ninja in ninjas:
        print ninja.first_name, ninja.last_name