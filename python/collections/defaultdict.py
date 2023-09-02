from collections import defaultdict

#it will have a default value if key not set

default_dict = defaultdict(int) #default type integer

default_dict['a'] = 1
default_dict['b'] = 2

print(default_dict['b'])

print(default_dict['c']) #integer def 0

default_dict = defaultdict(float) #default type integer

print(default_dict['c'])

#normal dict return key error
