meals = ["pasta", "pizza", "salad"]

for whatever in meals:
    print(whatever.title())


#the print for the command has to be the variable (whatever, x, n, meal, etc) that will give the list.
#if you do meals.title() you get "AttributeError: 'list' object has no attribute 'title'"
#if you take out the meals= line and add "" around the in variable, you will get M E A L S all on a new line