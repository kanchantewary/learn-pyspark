#unit test script to test sum module under my_sum

import sys

sys.path.append('/home/user/workarea/projects/learn-pyspark/jobs/samples/')

import pytest

from ex import sample1

def test_func():
    with pytest.raises(ValueError):
        sample1.func(10)
        
#sample1.func(10)
