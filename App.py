import csv


# ATTENTION: This method depends on the 'csv' module!
# Opens a file with the structure:
# 1;FirstName;1234
# 2;SecondName;5678
# ...
# And extracts the 'UserNames' only into a list as return value
def extract_user_names_as_list(input_file_name):
    result = []
    with open(input_file_name, 'r') as input_list:
        reader = csv.reader(input_list, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in reader:
            result.append(row[1])
    return result


# Using the method
result = extract_user_names_as_list("favorite.in")

# OPTIONAL: Print the results of your method
print(result)
