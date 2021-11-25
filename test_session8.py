import session8
from session8 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
    "namedtuple"
    ,"tuple"
    ,"profiles"
    ,"blood"
    ,"age"
    ,"location"
    ,"person"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_getprofiles_namedtuple():
    global profiles_nt
    profiles_nt = session8.get_profiles_nt()
    assert 10000 == len(profiles_nt),"you need to create 10000 entries"

def test_getprofiles_dict():
    global profiles_dict
    profiles_dict = session8.get_profiles_dict()
    assert 10000 == len(profiles_dict),"you need to create 10000 entries"

def test_oldest_person_age_time_check():
    assert round(session8.oldest_person_age_nt(profiles_nt)[1],2) <= round(session8.oldest_person_age_dict(profiles_dict)[1],2), "Performance of namedtuple is slower than dictionary"

def test_average_age_time_check():
    assert round(session8.average_age_nt(profiles_nt)[1],2) <= round(session8.average_age_dict(profiles_dict)[1],2), "Performance of namedtuple is slower than dictionary"

def test_mean_current_location_time_check():
    assert round(session8.mean_current_location_nt(profiles_nt)[2],2) <= round(session8.mean_current_location_dict(profiles_dict)[2],2), "Performance of namedtuple is slower than dictionary"

def test_bloodgroup_time_check():
    assert round(session8.largest_blood_type_nt(profiles_nt)[1],2) <= round(session8.largest_blood_type_dict(profiles_dict)[1],2), "Performance of namedtuple is slower than dictionary"

def test_stock_init():
    global stck
    stck = session8.stock_market()
    assert 100 == len(stck),"you need to create 100 entries"
def test_stock_range():
    for _ in stck:
        assert _.high > _.low and (_.close >= _.low and _.close <= _.high), "high, low and close are not properly calculated"

def test_docstring():
    assert bool(session8.get_profiles_nt.__doc__),"Doctsring missing in get_profiles_nt"
    assert bool(session8.get_profiles_dict.__doc__),"Doctsring missing in get_profiles_dict"
    assert bool(session8.oldest_person_age_nt.__doc__),"Doctsring missing in oldest_person_age_nt"
    assert bool(session8.oldest_person_age_dict.__doc__),"Doctsring missing in oldest_person_age_dict"
    assert bool(session8.average_age_nt.__doc__),"Doctsring missing in average_age_nt"
    assert bool(session8.average_age_dict.__doc__),"Doctsring missing in average_age_dict"
    assert bool(session8.mean_current_location_nt.__doc__),"Doctsring missing in mean_current_location_nt"
    assert bool(session8.mean_current_location_dict.__doc__),"Doctsring missing in mean_current_location_dict"
    assert bool(session8.largest_blood_type_nt.__doc__),"Doctsring missing in largest_blood_type_nt"
    assert bool(session8.largest_blood_type_dict.__doc__),"Doctsring missing in largest_blood_type_dict"

def test_annotation():
    assert bool(session8.get_profiles_nt.__annotations__),"Annotation missing in get_profiles_nt"
    assert bool(session8.get_profiles_dict.__annotations__),"Annotation missing in get_profiles_dict"
    assert bool(session8.oldest_person_age_nt.__annotations__),"Annotation missing in oldest_person_age_nt"
    assert bool(session8.oldest_person_age_dict.__annotations__),"Annotation missing in oldest_person_age_dict"
    assert bool(session8.average_age_nt.__annotations__),"Annotation missing in average_age_nt"
    assert bool(session8.average_age_dict.__annotations__),"Annotation missing in average_age_dict"
    assert bool(session8.mean_current_location_nt.__annotations__),"Annotation missing in mean_current_location_nt"
    assert bool(session8.mean_current_location_dict.__annotations__),"Annotation missing in mean_current_location_dict"
    assert bool(session8.largest_blood_type_nt.__annotations__),"Annotation missing in largest_blood_type_nt"
    assert bool(session8.largest_blood_type_dict.__annotations__),"Annotation missing in largest_blood_type_dict"