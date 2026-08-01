# Learn the rules of variable naming in Python.
#
# ## Rules
#
# 1. Make sure your variable names are descriptive
# 2. Don't have spaces between words
# 3. Don't start with numbers
# 4. Don't use special words like print or input
# 5. Choose simple words that are less likely to become typos
# 6. Check the company style guidelines if you start work at a company

n = input("What is your name? ")
l = len(n)
print(l)
###or

user_name = input("What is your name? ")
length = len(user_name)
print(length)


# Rule 2: Cannot have spaces
# user name = "Harshini"

# Rule 3: Cannot start with a number
# 1st_name = "Harshini"

# Rule 4: Cannot use reserved keywords or built-in function names
print = "Harshini"

# Descriptive and clear
user_name = "Harshini"

# Numbers allowed at the end or middle (not start)
name_1 = "Harshini"

# Multi-word variables separated by underscores
length_of_name = 6