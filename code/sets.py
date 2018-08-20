# demo sets on python

animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)    # false
animals.add('fish')
print('fish' in animals)    # True
print(len(animals))
animals.add('cat')
print(len(animals))
animals.remove('cat')
print(len(animals))
