from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from urllib.request import urlopen
from urllib.error import HTTPError

import json


UX_BASE = 'http://ux:8000/'

HTTP_ERROR_404 = json.dumps({"detail": "HTTP 404 Error: File Not Found"})

def index(request):

    context = {
            "title" : "CavTutor: A Tutoring Marketplace",
            "models" : ['institutions', 'users', 'courses', 'tutors', 'tutees'],
        }

    return render(request, 'CavTutor/index.html', context)


"""
    Institutions
"""

def institution_list(request):

    json_data = urlopen(UX_BASE + 'institutions/').read().decode('utf-8')
    context = {'institutions' : json.loads(json_data) }

    return render(request, 'CavTutor/institution-list.html', context)

def institution_detail(request, inst_id):
    try: 
        json_data = urlopen(UX_BASE + 'institutions/' + inst_id).read().decode('utf-8')
        context = {'institution' : json.loads(json_data) }

        return render(request, 'CavTutor/institution-detail.html', context)

    except HTTPError as e:
        return render(request, '404.html', {
                "model": "instititution",
                "id": inst_id,
            })

"""
    Course
"""
def course_list(request):

    json_data = urlopen(UX_BASE + 'courses/').read().decode('utf-8')
    context = {'courses' : json.loads(json_data), }

    return render(request, 'CavTutor/course-list.html', context)

def course_detail(request, course_id):
    try:
        course_json_data = urlopen(UX_BASE + 'courses/' + course_id).read().decode('utf-8')
        course_data = json.loads(course_json_data)

        context = {'course' : course_data,}
        return render(request, 'CavTutor/course-detail.html', context)
    except HTTPError as e:
        return render(request, '404.html', {
                "model": "course",
                "id": course_id,
            })

"""
    Tutor
"""
def tutor_list(request):

    json_data = urlopen(UX_BASE + 'tutors/').read().decode('utf-8')
    context = {'tutors' : json.loads(json_data) }

    return render(request, 'CavTutor/tutor-list.html', context)

def tutor_detail(request, tutor_id):
    try:
        json_data = urlopen(UX_BASE + 'tutors/' + tutor_id).read().decode('utf-8')
        context = {'tutor' : json.loads(json_data) }
        return render(request, 'CavTutor/tutor-detail.html', context)
    except HTTPError as e:
        return render(request, '404.html', {
                "model": "tutor",
                "id": tutor_id,
            })

"""
    Tutee
"""
def tutee_list(request):

    json_data = urlopen(UX_BASE + 'tutees/').read().decode('utf-8')
    context = {'tutees' : json.loads(json_data) }

    return render(request, 'CavTutor/tutee-list.html', context)

def tutee_detail(request, tutee_id):
    try:
        json_data = urlopen(UX_BASE + 'tutees/' + tutee_id).read().decode('utf-8')
        context = {'tutee' : json.loads(json_data) }

        return render(request, 'CavTutor/tutee-detail.html', context)
    except HTTPError as e:
        return render(request, '404.html', {
                "model": "tutee",
                "id": tutee_id,
            })

"""
    User
"""
def user_list(request):

    json_data = urlopen(UX_BASE + 'users/').read().decode('utf-8')
    context = {'users' : json.loads(json_data) }

    return render(request, 'CavTutor/user-list.html', context)

def user_detail(request, user_id):
    try:
        json_data = urlopen(UX_BASE + 'users/' + user_id).read().decode('utf-8')
        context = {'user' : json.loads(json_data) }

        return render(request, 'CavTutor/user-detail.html', context)
    except HTTPError as e:
        return render(request, '404.html', {
                "model": "user",
                "id": user_id,
            })
