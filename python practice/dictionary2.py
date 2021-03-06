# Dictionary practice with EDX course.

# Write a function called name_counts. name_counts will take
# as input a list of full names. Each name will be two words
# separated by a space, like "David Joyner".
#
# The function should return a dictionary. The keys to the
# dictionary will be the first names from the list, and the
# values should be the number of times that first name
# appeared.
#
# HINT: Use split() to split names into first and last.





def name_counts(name_list):
    name_list_split = []
    first_name_dictionary = {}
    for names in name_list:
        splited_name = names.split()
        name_list_split.append(splited_name)

    for i in range(0, len(name_list_split)):
        first_name = name_list_split[i][0]

        if first_name in first_name_dictionary:
            first_name_dictionary[first_name] += 1

        elif first_name not in first_name_dictionary:
            first_name_dictionary[first_name] = 1

    return first_name_dictionary


# Add your function here!


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (although the order of the keys may vary):
# {'Shelba': 5, 'Maren': 1, 'Nicol': 1, 'David': 2, 'Brenton': 2}
name_list = [
    "David Joyner",
    "David Zuber",
    "Brenton Joyner",
    "Brenton Zuber",
    "Nicol Barthel",
    "Shelba Barthel",
    "Shelba Crowley",
    "Shelba Fernald",
    "Shelba Odle",
    "Shelba Fry",
    "Maren Fry",
]
print(name_counts(name_list))
