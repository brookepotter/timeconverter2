# import pytest library
import pytest

# import the code we want to test
from app import *

# basic smoke test
def test_smoke_test():
	assert True

# def test_it_can_convert_sec_to_hours_mins_sec():
# 	assert 

def test_it_can_convert_secs_to_dhm_list():
	assert convert_time(400000) == [4, 15, 6]
	assert convert_time(80000) == [0, 22, 13]
	assert convert_time(54) == [0, 0, 0]
	assert convert_time(300) == [0, 0, 5]


def test_it_can_get_input_of_seconds_from_user():
	given = get_time_input()
	assert isinstance(get_time_input(), int)