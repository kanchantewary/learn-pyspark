#unit test script to test sum module under my_sum

import sys

sys.path.append('/home/user/workarea/projects/learn-pyspark/jobs/samples/')

import pytest

from calc import basic

def test_sum():
    #assert basic.sum(1,2,3)==6
    assert basic.sum([1,2,3])==6

def test_substract():
    assert basic.substract(1,2)==-1
