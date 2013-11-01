from types import IntType
from types import LongType
from types import FloatType
from types import ComplexType

def displayNumType(num):
    print num, 'is',
    if type(num) is IntType or type(num) is LongType or type(num) is FloatType or\
       type(num) is ComplexType:
        print 'a number of type: ', type(num).__name__
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(99999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
