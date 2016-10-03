# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def calculate_total_cost(item_cost,state,tax = 0.05):

    """ Calculate total cost of item adding tax to it based on the state

        >>> calculate_total_cost(55.6,"CA",0.35)
        59.492

        >>> calculate_total_cost(35,"NV")
        36.75

        >>> calculate_total_cost(20.78,"MN",0.04)
        21.611

        >>> calculate_total_cost("frgde","AZ")
        Please provide item cost as a number!

    """
    try:
        if state == "CA":
            return round((item_cost + item_cost * 0.07),3)
        else:
            return round((item_cost + item_cost * tax),3) 
    except TypeError:
        print "Please provide item cost as a number!"     
   

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

def is_berry(fruit):

    """ Returns True if the fruit is "strawberry", "cherry" or "blackberry"

        >>> is_berry("strawberry")
        True

        >>> is_berry("pineapple")
        False

        >>> is_berry("cherry")
        True

    """
    return fruit == "strawberry" or fruit == "cherry" or fruit == "blackberry"

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

def shipping_cost(fruit): 

    """ Calculates shipping cost of the fruit

        >>> shipping_cost("strawberry")
        0

        >>> shipping_cost("orange")
        5

    """
    if is_berry(fruit):
        return 0
    else:
        return 5       

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.

def is_hometown(town):

    """ Evaluates to true if town is hometown "Pune"

        >>> is_hometown("California")
        False

        >>> is_hometown("Pune")
        True

        >>> is_hometown("PUNE")
        True

    """
    return town.lower() == "pune"
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.

def full_name(first_name,last_name):

    """ Returns full name from first and last names

        >>> full_name("Eshita","Thakkar")
        'Eshita Thakkar'
    """
    return first_name + " " + last_name
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.

#####################################################################

def hometown_greeting(home_town,first_name,last_name):

    """ prints a greeting based on your home town

        >>> hometown_greeting("Bombay","Sneha","Mathur")
        Hi, Sneha Mathur , Where are you from?

        >>> hometown_greeting("Pune","Alex","George")
        Hi, Alex George , we're from the same place!

    """
    print "Hi,", full_name(first_name,last_name), ",",
    if is_hometown(home_town):
        print "we're from the same place!"
    else:
        print "Where are you from?"    




# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.



def increment(x = 1):
    def add(x,y = 1): 
        return x + y




# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5) 

# Rest of the question was unclear.  (Call addfive with y = 5. Call again with y = 20. ) Need more explanation 




# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

def appended_list(number,numbers):
    """ Appends the number to the list and returns the list

        >>> appended_list(30,[3,4,5])
        [3, 4, 5, 30]

    """
    numbers += [number]
    return numbers


#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
