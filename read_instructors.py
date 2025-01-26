# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from crud.models import *
from datetime import date


# Your code starts from here:
instructor_yan = Instructor.objects.get(first_name="Yan")
print("1. Найдите одного инструктора с именем `Yan`")
print(instructor_yan)

print("\n")
# Обратите внимание, что инструктора с именем `Andy` нет
# Поэтому менеджер вызовет исключение
try:
    instructor_andy = Instructor.objects.get(first_name="Andy")
except Instructor.DoesNotExist:
    print("2. Попробуйте найти несуществующего инструктора с именем `Andy`")
    print("Инструктор Andy не существует")

print("\n")
part_time_instructors = Instructor.objects.filter(full_time=False)
print("3. Найдите всех инструкторов на неполный рабочий день: ")
print(part_time_instructors)

print("\n")
full_time_instructors = Instructor.objects.exclude(full_time=False).filter(total_learners__gt=30000).\
        filter(first_name__startswith='Y')
print("4. Найдите всех инструкторов на полный рабочий день с именем, начинающимся на `Y`, и количеством учащихся более 30000")
print(full_time_instructors)

print("\n")
full_time_instructors = Instructor.objects.filter(full_time=True, total_learners__gt=30000,
                                                      first_name__startswith='Y')
print("5. Найдите всех инструкторов на полный рабочий день с именем, начинающимся на `Y`, и количеством учащихся более 30000")
print(full_time_instructors)

 # Найти студентов с фамилией "Smith"
learners_smith = Learner.objects.filter(last_name="Smith")
print("1. Найти студентов с фамилией `Smith`:")
print(learners_smith)
print("\n")
# Упорядочить по дате рождения по убыванию и выбрать первые два объекта
learners = Learner.objects.order_by('-dob')[0:2]
print("2. Найти двух самых молодых студентов:")
print(learners)