#Read fixed width files using python

#using Pandas

#using Python3 FixedWidth module

import pandas as pd
from pandas import DataFrame

pdf1 = pd.read_fwf('file:/home/user/workarea/data/sample.fw',colspecs='infer',width=None)

print(pdf1)
