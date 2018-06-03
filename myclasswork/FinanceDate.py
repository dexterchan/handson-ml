import re
from datetime import *

from dateutil.relativedelta import *
import numpy as np
from IPython.core.debugger import set_trace
from enum import Enum


class DATETYPE(Enum):
    DAY=0
    WEEK=1
    MONTH=2
    YEAR=3
def FinanceDate(date, genericdate):
    #set_trace()
    #from dateutil.relativedelta import *
    matchformat=re.match( "([+-]?)(\d+)([A-Za-z])",genericdate.lower())
    if(matchformat is None):
        raise Exception('Date format cannot be handled')
    
    num = int(matchformat.group(2))
    st = matchformat.group(3)
    num = (num * (-1)) if (matchformat.group(1)=="-") else num
    dd=date
    
    if(st == "d"):
        dd=date + relativedelta(days=num)
    elif(st == "w"):
        dd=date + relativedelta(weeks=num)
    elif(st=="m"):
        dd=date + relativedelta(months=num)
    elif(st=="y"):
        dd=date #+ relativedelta(years=num)
    return dd
    