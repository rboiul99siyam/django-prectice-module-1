from django.shortcuts import render
from django.template import loader
import datetime 
def home(request):
    d = {

        'Name' : 'robiul',
        'Roll' : '1',
        'address' : 'Chandpur , foridgong',
        'age' : 20,
        'birthday' : datetime.datetime.now(),
        'numbers':[10,20,30],
        'blog':'In views.py you can see what the name variable looks like',
        'totalsum':41,
        'size':26214400,
        'float':10.2234345,
        'table':'Apple',
        'course': [
        {
            'c_name': 'c++',
            'fee': 1000,
            'run': '20 - 10 - 2024',
        },
        {
            'c_name': 'c',
            'fee': 200,
            'run': '20 - 10 - 2024',
        },
        {
            'c_name': 'Djanog',
            'fee': 2000,
            'run': '20 - 10 - 2024',
        },
        
],
'lst':['c is good', 'c++ is best  ', 'python is better'],

    }

    return render(request , 'index.html',d)
