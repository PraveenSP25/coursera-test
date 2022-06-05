from array import *
val=array('i',[2,5,8,9,7])
newarr = array(val.typecode, (a*a for a in val))
for e in newarr:
    print(e)