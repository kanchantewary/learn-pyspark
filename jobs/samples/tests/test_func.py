#unit test script to test sum module under my_sum

import sys

sys.path.append('/home/user/workarea/projects/learn-pyspark/jobs/samples/')

import unittest
import pytest

from calc import basic

def test_func():
    assert basic.func(5)==6
