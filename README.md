# Session 8 assignment of EPAi4.0
Named Tuples
***
|Name|Email|Git ID|
|----|-----|-------|
|Rishik Dutta|rishikdutta1987@gmail.com|rishikd1987|

## File Name: session8.py
***
#### Brief Description:
Aim is to write code for 3 functionalities that demonstrate usage of "Named Tuples". Faker library to be used to get profiles as well as company names
1. Use the Faker library to get 10000 random profiles. Using namedtuple, calculate  - 
   * Largest blood type
   * mean-current_location
   * oldest_person_age
   * and average age
2. Do the same as above, but with dictionaries instead of named tuples
3. Create company names for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. 
   * Calculate and show what value the stock market started at
   * what was the highest value during the day
   * where did it end
   * Make sure your open, high, close are not totally random

#### Packages imported:
* collections
* datetime
* perf_counter
* string
* random

## Qualean class description
|Type|Name|Input parameters|Output parameters|Description|Dependency|
|----|-----|-------|-------|-------|-------|
|function|get_profiles_nt|-|namedtuple|This is the initializing function that will create the 10000 random profiles.It makes use of Faker library to generate fake profiles and stitches them into a namedtuple||
|function|largest_blood_type_nt|namedtuple|tuple|Find the most common blood type among the 10000 fake profiles using namedtuple processing|-|
|function|mean_current_location_nt|namedtuple|tuple|Find the average location among the 10000 fake profiles using namedtuple processing|-|
|function|oldest_person_age_nt|namedtuple|tuple|Find the oldest person's age among the 10000 fake profiles using namedtuple processing |-|
|function|average_age_nt|namedtuple|tuple|Find the average age among the 10000 fake profiles using namedtuple processing||
|function|get_profiles_dict|-|dictionary|This is the initializing function that will create the 10000 random profiles. It makes use of Faker library to generate fake profiles and stitches them into a dictionary||
|function|largest_blood_type_dict|dict|tuple|Find the most common blood type among the 10000 fake profiles using dictionary processing|-|
|function|mean_current_location_dict|dict|tuple|Find the average location among the 10000 fake profiles using dictionary processing|-|
|function|oldest_person_age_dict|dict|tuple|Find the oldest person's age among the 10000 fake profiles using dictionary processing |-|
|function|average_age_dict|dict|tuple|Find the average age among the 10000 fake profiles using dictionary processing||
|function|get_weights|-|tuple|generate 100 normalised weights and return as a tuple of namedtuples||
|function|stock_market|-|namedtuple|Use Faker data to create 100 companies(name, symbol) and their stock information (open, high, close) Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. We are also making sure that the open, high, close are not totally random.||
***

## File Name: test_session8.py
***
#### Brief Description:
This code is used to test the session8.py code
#### Packages imported:
* pytest
* datetime
* StringIO
* sys
* re
* time
* inspect
* os
* re


|Type|Name|Input parameters|Output parameters|Description|Dependency|
|----|-----|-------|-------|-------|-------|
|function|test_readme_exists|-|-|Check if README.md file exists|-|
|function|test_readme_contents|-|-|Check if README.md file contains atleast 500 words|-|
|function|test_readme_proper_description|-|-|Check if all functions/classes have been described in README.md file|-|
|function|test_readme_file_for_formatting|-|-|Check for formatting in README.md file |-|
|function|test_indentations|-|-|Check for misplaced indentations |-|
|function|test_function_name_had_cap_letter|-|-|Check for upper case characters in function names |-|
|function|test_getprofiles_namedtuple|-|-|Check if the get_profiles_nt function can extract and prepare 10000 profiles as namedtuples|-|
|function|test_getprofiles_dict|-|-|Check if the get_profiles_dict function can extract and prepare 10000 profiles as dictionaries|-|
|function|test_oldest_person_age_time_check|-|-|Check if the time taken by the code in calculating oldest person's age is less in case of namedtuple than in case of dictionary|-|
|function|test_average_age_time_check|-|-|Check if the time taken by the code in calculating average age is less in case of namedtuple than in case of dictionary|-|
|function|test_mean_current_location_time_check|-|-|Check if the time taken by the code in calculating mean current location is less in case of namedtuple than in case of dictionary|-|
|function|test_bloodgroup_time_check|-|-|Check if the time taken by the code in calculating most frequent blood group is less in case of namedtuple than in case of dictionary|-|
|function|test_stock_init|-|-|Check if 100 company profiles are created|-|
|function|test_stock_range|-|-|Check for correctness of values for high, low and close of the stocks|-|
|function|test_docstring|-|-|Check if docstrings are correctly placed|-|
|function|test_annotation|-|-|Check if annotations are present|-|


## Output of test in local system:
============================= test session starts =============================
platform win32 -- Python 3.7.4, pytest-5.2.1, py-1.8.0, pluggy-0.13.0 -- C:\ProgramData\Anaconda3\python.exe
cachedir: .pytest_cache
rootdir: C:\Rishik\EPAi\session-8-assignment
plugins: dash-1.16.2, Faker-9.8.2, arraydiff-0.3, doctestplus-0.4.0, openfiles-0.4.0, remotedata-0.3.2
collecting ... collected 16 items

test_session8.py::test_readme_exists PASSED                              [  6%]
test_session8.py::test_readme_contents PASSED                            [ 12%]
test_session8.py::test_readme_proper_description PASSED                  [ 18%]
test_session8.py::test_readme_file_for_formatting PASSED                 [ 25%]
test_session8.py::test_indentations PASSED                               [ 31%]
test_session8.py::test_function_name_had_cap_letter PASSED               [ 37%]
test_session8.py::test_getprofiles_namedtuple PASSED                     [ 43%]
test_session8.py::test_getprofiles_dict PASSED                           [ 50%]
test_session8.py::test_oldest_person_age_time_check PASSED               [ 56%]
test_session8.py::test_average_age_time_check PASSED                     [ 62%]
test_session8.py::test_mean_current_location_time_check PASSED           [ 68%]
test_session8.py::test_bloodgroup_time_check PASSED                      [ 75%]
test_session8.py::test_stock_init PASSED                                 [ 81%]
test_session8.py::test_stock_range PASSED                                [ 87%]
test_session8.py::test_docstring PASSED                                  [ 93%]
test_session8.py::test_annotation PASSED                                 [100%]

============================= 16 passed in 41.00s =============================

Process finished with exit code 0



