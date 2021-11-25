from collections import namedtuple
from datetime import datetime,date
from time import perf_counter
from faker import Faker
from collections import Counter
import random
import string

"""
	Problem Statement:
	1. Use the Faker library to get 10000 random profiles. 
	Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, 
	and average age (add proper doc-strings). - 250 (including 5 test cases)
	2. Do the same thing above using a dictionary. Prove that namedtuple is faster. - 250 (including 5 test cases)
	3. Create fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). 
	Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day,
	and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. - 500  (including 10 test cases)
"""

def get_profiles_nt() -> namedtuple:
	"""
		This is the initializing function that will create the 10000 random profiles.
		It makes use of Faker library to generate fake profiles and stitches them into
		a namedtuple
	"""
	fake = Faker()
	profile = namedtuple('profile',fake.profile().keys())
	fullprofile = namedtuple('fullprofile',['profile'])
	fullprofile_nt = fullprofile(profile(**fake.profile()))
	for _ in range(9_999):
		prof = profile(**fake.profile())
		fullprofile_nt += fullprofile(prof)
	return fullprofile_nt

def largest_blood_type_nt(fullprofile_nt:namedtuple)->tuple:
	"""
		Find the most common blood type among the 10000 fake profiles using namedtuple processing
	"""
	start = perf_counter()
	blood_group = Counter(list(map(lambda x: x[5],fullprofile_nt))).most_common()[0][0]
	end = perf_counter()
	return blood_group,end-start

def mean_current_location_nt(fullprofile_nt:namedtuple)->tuple:
	"""
		Find the average location among the 10000 fake profiles using namedtuple processing
	"""
	start = perf_counter()
	x, y = sum(map(lambda x: x[0],map(lambda v : v[4],fullprofile_nt)))/len(fullprofile_nt),sum(map(lambda x: x[1],map(lambda v : v[4],fullprofile_nt)))/len(fullprofile_nt)
	end = perf_counter()
	return x,y,end-start

def oldest_person_age_nt(fullprofile_nt:namedtuple)->tuple:
	"""
		Find the oldest person's age among the 10000 fake profiles using namedtuple processing
	"""
	start = perf_counter()
	age = round((date.today() - min(fullprofile_nt, key=lambda x : x[-1])[-1]).days/365)
	end = perf_counter()
	return age,end-start

def average_age_nt(fullprofile_nt:namedtuple)->tuple:
	"""
		Find the average age among the 10000 fake profiles using namedtuple processing
	"""
	start = perf_counter()
	avg_age = sum(map(lambda x : ((date.today() - x[-1]).days)/365,fullprofile_nt))/len(fullprofile_nt)
	end = perf_counter()
	return round(avg_age,2),end-start

#----------------------------------------------------------------------------
def get_profiles_dict() -> dict:
	"""
		This is the initializing function that will create the 10000 random profiles.
		It makes use of Faker library to generate fake profiles and stitches them into
		a dictionary
	"""
	fake = Faker()
	profile_dict = {}

	for _ in range(10000):
		if _ == 0:
			profile_dict[_] = fake.profile()
		else:
			profile_dict[_+1] = fake.profile()
	return profile_dict

def largest_blood_type_dict(fullprofile_dict:dict)->tuple:
	"""
		Find the most common blood type among the 10000 fake profiles using dictionary processing
	"""
	start = perf_counter()
	blood_group = Counter(list(map(lambda x: x['blood_group'],fullprofile_dict.values()))).most_common()[0][0]
	end = perf_counter()
	return blood_group,end-start

def mean_current_location_dict(fullprofile_dict:dict)->tuple:
	"""
		Find the average location among the 10000 fake profiles using dictionary processing
	"""
	start = perf_counter()
	x, y = sum(map(lambda x: x[0],map(lambda v : v['current_location'],fullprofile_dict.values())))/len(fullprofile_dict.values()),sum(map(lambda x: x[1],map(lambda v : v['current_location'],fullprofile_dict.values())))/len(fullprofile_dict.values())
	end = perf_counter()
	return x,y,end-start

def oldest_person_age_dict(fullprofile_dict:dict)->tuple:
	"""
		Find the oldest person's age among the 10000 fake profiles using dictionary processing
	"""
	start = perf_counter()
	age = round((date.today() - min(fullprofile_dict.values(),key = lambda x : x['birthdate'])['birthdate']).days/365)
	end = perf_counter()
	return age,end-start

def average_age_dict(fullprofile_dict:dict)->tuple:
	"""
		Find the average age among the 10000 fake profiles using dictionary processing
	"""
	start = perf_counter()
	avg_age = sum(map(lambda x : ((date.today() - x['birthdate']).days)/365,fullprofile_dict.values()))/len(fullprofile_dict)
	end = perf_counter()
	return round(avg_age,2),end-start

def get_weights()->tuple:
	"""
		generate 100 normalised weights and return as a tuple of namedtuples
	"""
	random_weight  =  namedtuple('random_weight','weight')
	weight = random.uniform(0,1)
	r1  = random_weight(weight)
	for _ in range(99):
		weight = random.uniform(0,1)
		r1 += weight,
	sum_value = sum(r1)
	r2 = tuple(map(lambda x: x/sum_value,r1))
	return r2
def stock_market()->namedtuple:
	"""
		Use Faker data to create 100 companies(name, symbol) and their stock information (open, high, close)
		Assign a random weight to all the companies. Calculate and show what value the stock market started at, what was the highest value during the day,
		and where did it end.
		We are also making sure that the open, high, close are not totally random.
	"""
	Company = namedtuple('Company', 'name symbol open high low close')
	allcompany = namedtuple('allcompany',['Company'])
	fake = Faker()
	norm_weights = get_weights()
	for _ in range(100):
		weight = norm_weights[_]
		open_ = random.randint(1000,20000) * weight
		close = open_ * random.uniform(0.7,1.3)
		high = open_ * random.uniform(0.8,1.5)
		low = open_ * random.uniform(0.7,1)
		if high < open_:
			high = open_
		if high < close:
			high = close
		if low > high:
			if high>open_:
				low = open_
			else:
				low = close
		if close < low:
			close = low
		c1 = Company(fake.company(),''.join(random.sample(string.ascii_uppercase, 3)),open_, high, low, close)
		if _ == 0:
			comp_stock = allcompany(c1)
		else:
			comp_stock += allcompany(c1)
	return comp_stock









