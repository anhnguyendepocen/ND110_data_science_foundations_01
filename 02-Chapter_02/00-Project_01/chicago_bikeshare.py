##############################################################################################
#                                                                               VERSION: 2.0 #
#  Author:   Anderson Hitoshi Uyekita                                                        #
#  Project:  Explore Chicago Bikeshare Data                                                  #
#  Date:     09/12/2018                                                                      #
#  COD:      ND110                                                                           #
#  Tags:     Udacity, Data Science, Python                                                   #
#                                                                                            #
##############################################################################################

##############################################################################################
#                                                                                            #
#  VERSION 1.1:                                                                              #
#      Submited: 08/12/2018                                                                  #
#                                                                                            #
#      Issues:                                                                               #
#             1) Loops and conditional statements are used to process the data correctly.    #
#                                                                                            #
#                  a) In some tasks , we expect that you don't use pyhton functions like     #
#                     sum or count to process the data.                                      #
#                                                                                            #
#                     Reply: I have written my own summation function called sum_ahu and     #
#                            count_ahu.                                                      #
#                                                                                            #
#                  b) Loops and conditional statements should be used to process the data    #
#                     correctly.                                                             #
#                                                                                            #
#                     Reply: OK.                                                             #
#                                                                                            #
#                  c) Also, the median is being calculated incorrectly.                      #
#                                                                                            #
#                     Reply: I fix it defining a function median_ahu.                        #
#                                                                                            #
#             2) Comments, function and variable names enable readability of the code.       #
#                                                                                            #
#                  a) All variables of your code should have descriptive names.              #
#                                                                                            #
#                     Reply: I got it! No more a simple "i" to iterate any for() loop.       #
#                                                                                            #
#                  b) I added more information and suggestions about it on the Code Review   #
#                     tab.                                                                   #
#                                                                                            #
#                     Reply: OK! Thank you!                                                  #
#                                                                                            #
##############################################################################################

# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

for row in data_list[:20]:   # The first 20 rows - The first row in the header and the other 19 rows were observations
    print(row)               # Printing
                             # Now in "Pythonic" way.

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

for row in data_list[:20]:       # The first 20 rows
    print(row[6])                # The second index 6 means gender's column
                                 # Now in Pythonic way.

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, column):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function selects a specific column (defined as column) of a data frame (here called      |
    |     as data, but probabily will be data_list).                                                    |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     data       list   The imported dataset of the Chicago Bikeshare, a 1551506 x 8 data frame     |
    |                       stored in a list.                                                           |
    |                                                                                                   |
    |     column     int    The desireable column to be selected.                                       |
    |                           0: Start Time                                                           |
    |                           1: End Time                                                             |
    |                           2: Trip Duration                                                        |
    |                           3: Start Station                                                        |
    |                           4: End Station                                                          |
    |                           5: User Type                                                            |
    |                           6: Gender                                                               |
    |                           7: Birth Year                                                           |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE      TYPE   DESCRIPTION                                                              |
    |                                                                                                   |
    |     column_list   list   The Selected column from the data input.                                 |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    column_list = [] # Local variable
    
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for row in data:                     # Iterates each row of data
        column_list.append(row[column])  # select a specific element (column) of the row and append it
    return column_list                   # Now in "Pythonic" way.


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.

# Creating an auxiliary function to perform the summation.
# Reason: I will use it more than twice, it's convenient for me to create this function, although this is not a task.
def sum_ahu(my_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function perform the summationof a given list.                                           |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     my_list    list   A list of integer or float.                                                 |
    |                                                                                                   |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE     TYPE           DESCRIPTION                                                       |
    |                                                                                                   |
    |     summation    float or int   Accordding to the input list.                                     |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    summation = 0 # Local variable to be updated in each iteration
    
    for index in my_list:             # Loop used to "visit" each element of the list.
        summation += index            # Accumulating the values and updating the summation.
            
    return summation # Return the summation

gender = column_to_list(data_list, -2) # Selecting the Gender's column of data_list dataframe.

# Lambda Expressions
is_male = lambda x : x == "Male"     # Check each how if the statment is True or False. Later I will coerce
is_female = lambda x : x == "Female" # True to 1 and False to 0 to count the number of each category.
is_blank = lambda x : x == ""        # I used the plt.hist(gender) function to find out the categories of
                                     # Gender's column.


male = sum_ahu(list(map(is_male, gender)))        # Applying map() (for each column) and lambdas functions
female = sum_ahu(list(map(is_female, gender)))    # I could count the number of each category. 
undefined = sum_ahu(list(map(is_blank, gender)))  # Obs.: I "coerced" boolean to integer by the using of sum_ahu().

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function counts the number of "Male" and "Female" from the Gender column of the          |
    |     data_list. This is a specific function to be used only to the purpose to calculated the       |
    |     quantity of "Male" and "Female".                                                              |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     data_list  list   The list generated after the .read() process. The original file was the     |
    |                       chicago.csv, which has a 1551506 rows and 8 columns.                        |
    |                                                                                                   |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE         TYPE   DESCRIPTION                                                           |
    |                                                                                                   |
    |     [male,female]    list   A list of two variables, the first one summarize the number of "Male" |
    |                             the second one summarize the number of "Female".                      |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |REQUIREMENT:                                                                                       |
    |                                                                                                   |
    |     NAME             SCOPE                                                                        |
    |                                                                                                   |
    |     column_to_list   Global                                                                       |
    |                                                                                                   |
    |     sum_ahu          Global                                                                       |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------    
    """
    # Selecting the Gender's column as a local variable.
    local_gender = column_to_list(data_list, -2) # Keep in mind this function has defined in the Task 3.
    
    # Based on the map() to find True or False and sum() to count.
    male = sum_ahu(list(map(lambda x : x == "Male", local_gender)))     # Simplified version, now with one step less
    female = sum_ahu(list(map(lambda x : x == "Female", local_gender))) # It's a bit clumsy but understandable (I hope so).
    
    return [male, female] # Return of the total number of male and female.


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function returns which Gender has the majority of in case of the same number returned    |
    |     Equal                                                                                         |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     data_list  list   The list generated after the .read() process. The original file was the     |
    |                       chicago.csv, which has a 1551506 rows and 8 columns.                        |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     answer     str    If the number of "Name" are greater than "Female" return "Male". If the     |
    |                       opposite was true returns "Female". In cases of draw return "Equal".        |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |REQUIREMENT:                                                                                       |
    |                                                                                                   |
    |     NAME             SCOPE                                                                        |
    |                                                                                                   |
    |     count_gender     Global                                                                       |
    |                                                                                                   |
    ----------------------------------------------------------------------------------------------------- 
    """
    # Number of Male and Female calculationg
    local_gender_total = count_gender(data_list) # local_gender_total[0] : Male
                                                 # local_gender_total[1] : Female

    if local_gender_total[0] > local_gender_total[1]:    # Is Male > Female?
        answer = "Male"                                  # If True update answer
        
    elif local_gender_total[0] == local_gender_total[1]: # Is Male == Female?
        answer = "Equal"                                 # If True update answer
        
    else:                                                # Is Female > Male
        answer = "Female"                                # If True update answer
        
    return answer # Return the answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# The same case of the summation. I will use this function a bunch of times, to save lines codes I decide
# to write an auxiliary function.
def count_ahu(my_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     Counts the number of elements of a list. It is the same of len() function.                    |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     my_list    list   Any list.                                                                   |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     counter    int    The number of elements of a list.                                           |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    """
    counter = 0 # Set the counter to zero.
    
    for element in my_list:  # Loop the list to be count
        counter += 1             # For each element add 1 to the counter

    return int(counter)          # Return the counter and ensure to be a integer.

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

# Explanation how I conduct this Task.
#
# The print(set(user_types)) give me {'Customer', 'Subscriber', 'Dependent'}, it means the dataframe has
# 3 categories, but with a deeper analisys using a straighfoward plot (plt.hist(quantity)) shows me the 
# "Dependent" are exceptions, only 4 instances of this category. For this reason I removed from the graphic
# because it is not a valueable information faced the number of "Customer" and "Subscriber".
#
# If my point of view is not correct, please, let me know. I can fix it and resubmit you as soon as possible.

# Selecting the desired column
user_types = column_to_list(data_list, -3)

# Selecting the uniques categories.
types = list(set(user_types))  # Three categories: Customer, Dependent and Subscriber

# Removing the "Dependent" as commented above
types = [sorted(types)[0], sorted(types)[-1]]

# Calculating the quantity of each of types ("Customer" and "Subscriber")
quantity = [sum_ahu(list(map(lambda x : x == types[0], user_types))),  # Due to the Task 5 requirements my function
            sum_ahu(list(map(lambda x : x == types[1], user_types)))]  # count_gender() is very specific and can not
                                                                       # deal with a generic situation like this.

# print(sum(list(map(lambda x : x == "Dependent", user_types)))) # Shows the number of Dependent category.

y_pos = list(range(count_ahu(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')              # Add the y axis
plt.xlabel('User Types')            # Add the x axis
plt.xticks(y_pos, types)            # Remove x marks
plt.title('Quantity by User Types') # Add Title
plt.show(block=True) 

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))

answer = "There are many rows with blank values in gender's column. Exactly {} rows with no values (blank)."

print("Answer:", answer.format(undefined)) # undefined was calculated in Task 4.

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().

# To be honest, I really do not know what is inside of this set of "ready functions". However, I have tried to
# do an effort to accomplish this task using different ways rather than a simple built-in function.

# Selecting the column of trip duration
trip_duration_list = column_to_list(data_list, 2)

# Defining a lambda expression to coerce str variables to float
conv_to_float = lambda x : float(x) # This is very handy!!

# Converting the elements of trip_duration_list to float
trip_dur_float = list(map(conv_to_float, trip_duration_list))

# Minimum
min_trip = round(sorted(trip_dur_float)[0]) # Could I use .sorted()?

# Maximum
max_trip = round(sorted(trip_dur_float, reverse = True)[0]) # Could I use .sorted()?

# Mean
mean_trip = round(sum_ahu(trip_dur_float)/count_ahu(trip_dur_float)) # Could I use sum()?

# Median
# I decided to encapsulated this function because I may reuse it later and I could properly document it.
def median_ahu(my_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function returns the list median.                                                        |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     my_list    list   List compounded of int or float which I want to find the median.            |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE   TYPE   DESCRIPTION                                                                 |
    |                                                                                                   |
    |     median     float  I think a convenient way is to return as float, because the average of      |
    |                       num_1 and num_2 may be a float number, and coercing to an int could led a   |
    |                       loss of information.                                                        |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |REQUIREMENT:                                                                                       |
    |                                                                                                   |
    |     NAME             SCOPE                                                                        |
    |                                                                                                   |
    |     count_ahu        Global                                                                       |
    |                                                                                                   |
    ----------------------------------------------------------------------------------------------------- 
    """
    my_list = sorted(my_list) # I must sort my_list to find the "middle".
                              # NOTE: I use the sorted() built-in function!!
    
    if (count_ahu(my_list) % 2) == 1:               # When the lenght of list is odd. I have a "middle" in my list.
        median = my_list[count_ahu(my_list) // 2]   # [0,1,2,3,4] has 5 elements and the median is located in index 2.
        return median # Return median         
    
    else:                                               # When the lenght of list is even. I do not have a single "middle" numberin my list.
        num_1 = my_list[count_ahu(my_list) // 2]        # So a need to calculated an average between two numbers, num_1 and num_2 are
        num_2 = my_list[(count_ahu(my_list) // 2) - 1]  # these two numbers.
        median = (num_1 + num_2)/2   # Calculate the mean of this two numbers, which is the median of the list.
        return float(median)         # Return the median as float.

# Median
median_trip = round(median_ahu(trip_dur_float)) # I am not using any built-in function, except the sorted().

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set() # Unique elements

# Selecting the column of Start Stations from data_list
start_stations = column_to_list(data_list, 3)

# First 20 rows to an analysis
# start_stations[0:20]

# Selecting the unique elements of start_stations list.
user_types = list(set(start_stations))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Example function with annotations.
#      Args:
#          param1: The first parameter.
#          param2: The second parameter.
#      Returns:
#          List of X values
#
#      """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    """
    -----------------------------------------------------------------------------------------------------
    |DESCRIPTION:                                                                                       |
    |                                                                                                   |
    |     This function returns which Gender has majority of in case of the same number returs Equal.   |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |INPUT:                                                                                             |
    |                                                                                                   |
    |     VARIABLE     TYPE   DESCRIPTION                                                               |
    |                                                                                                   |
    |     column_list  list   Is a list with only one variable, this is an output of column_to_list     |
    |                         function.                                                                 |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |OUTPUT:                                                                                            |
    |                                                                                                   |
    |     VARIABLE      TYPE   DESCRIPTION                                                              |
    |                                                                                                   |
    |     item_type     str    Returns all categories in the column_list.                               |
    |                                                                                                   |
    |     count_items   str    Returns the total of each category in item_type.                         |                                                                       |
    |                                                                                                   |
    -----------------------------------------------------------------------------------------------------
    |REQUIREMENT:                                                                                       |
    |                                                                                                   |
    |     NAME             SCOPE                                                                        |
    |                                                                                                   |
    |     sum_ahu        Global                                                                         |
    |                                                                                                   |
    ----------------------------------------------------------------------------------------------------- 
    """
    # Selecting unique elements from column_list
    item_types = list(set(column_list))   # set() is used to "filter" the unique values
                                          # list() to convert into a list.
    
    # Initializing coun_items
    count_items = []
    
    # Loop to calculated the total number of each element from item_types
    for i_type in item_types:
        count_items.append(sum_ahu(list(map(lambda x : x == i_type, column_list))))
        # This loop will verify for each element of the column_list the given lambda expression (True or False)
        # after that I will convert it into a list, coerce it to an int, and sum the 0 and 1 to calculate the summation.
        # Finally, I will append it in count_items as the number of instance which this item_types appears in the
        # column_list, in other words, I will counting the numbers of occurencies of each item_types in the column_list.
        
    return item_types, count_items # Return two lists


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
