
# Task 1 - Make alternate **characters** in a string upper case or lower case

## Create a string variable
my_string = "Hi I am having fun"
print(f"Original string: {my_string}")
print("")

## Create a new variable to capture the new string that will be created
new_str = " " 

## Use for loop to iterate through characters in string 
for char in range(len(my_string)):
    if char % 2 == 0: # Make even characters in string lower case
        new_str += my_string[char].lower() 
    else:
        new_str += my_string[char].upper() # Make odd characters upper case
     
print(f"New string with alternate upper and lower cases: {new_str}")
print(" ")



# Task 2 - Make alternate **words** in original string upper and lower case

## Use split function to break up words in the string into a list
split_str = my_string.split()
print(f"The orginal string is now a list: {split_str}")
print(" ")

## Use for loop to make alternate words in list upper and lower case
for word in range(len(split_str)):
    if word % 2 == 0: 
        split_str[word] = split_str[word].upper() 
    else:
        split_str[word] = split_str[word].lower()  
     
print(f"Alternate words in my list are now upper and lower cases: {split_str}")
print(" ")


## Use join function to turn latest list back into a string
joined_str = " ".join(split_str)
print(f"My list is now a string again :): {joined_str}")
print(" ")