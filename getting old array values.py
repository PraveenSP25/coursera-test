from array import *
val= array('i',[2,4,5,7,9])
newarr=array(val.typecode, (a for a in val))
for e in newarr:
    print(e)