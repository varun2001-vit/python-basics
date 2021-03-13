dogs=['wille','hootz','peso','goblin']
for dog in dogs:
    print('hello',dog,'!')
    print("i love these dogs")
print('these were my first dogs')
old_dogs=dogs[:2]
for old_dog in old_dogs:
    print(old_dog)
del dogs[0]
dogs.remove('peso')
print(dogs)