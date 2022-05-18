# Lintcode 2261//Naive

# Description
# In this problem we will provide a list list_1 and we have written the delete_list_element function in solution.py for you. The list_1 of this function represents our initial list and the function will eventually return a list of elements that you need to delete from the 4th to the 7th element and return.

# Write the relevant Python code in solution.py to return the list after the elements have been removed.

# Example
# The evaluation opportunity executes your code by executing the command python main.py {list_1}, and passing in list_1 as a command line parameter, you can learn how the code runs in main.py. For different list_1, your code should also print different results.

# Example one

# When the input list is:

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# The print result is:

# [1, 2, 3, 7, 8, 9]
# Example two

# When the input list is:

# [23, 24, 30]
# The print result is:

# [23, 24, 30]
# Sample three

# When the input list is:

# ['a','b','c','d','e','f','g','h','i','j','k','l', ' m','n']
# The print result is:

# ['a','b','c','g','h','i','j','k','l','m','n']
# ``` 34, 5356, 78787]
# Hide Hint
# For the specific content of this question, please refer to the del statement in Python official documentation for learning.

# SOLUTION 1
def del_list_element(list_1:list) -> list:
    '''
    :param list_1: Input List
    :return: The list after deleting the specified element
    '''
    # -- write your code here --
    cnt = 0
    while len(list_1) > 3 and cnt < 3:
        list_1.pop(3)
        cnt += 1
    return list_1

# TODO SOLUTION 2: del
