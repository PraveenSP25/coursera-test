a=5
b=3     ## we give b =0 then print exception part
try:
    print("resource open")
    print(a/b)
except Exception as e:###########  only print if any error comes
    print("hey praveen",e)
finally:                  ### it print if any error comes or not
    print("resoure close")
