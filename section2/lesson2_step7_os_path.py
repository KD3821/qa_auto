import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson1_step5.py')

print(current_dir)
print(os.path.abspath(__file__))
print(file_path)

'''
Подробнее о методах модуля os:
https://docs.python.org/3/library/os.path.html  
'''