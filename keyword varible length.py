def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i, j)
person('praveen', age= 23, city="kumta",mob=937839878893)
