"""
Local Variables can remain just in local scoups.
In this case can only refer to eggs inside spam function
Local variables in one function are completely separated from another function
"""
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# Global Variables
def spam():
    print(eggs)
eggs = 42
spam()

# Local variables are  prioritized
def spam():
    eggs = 'Hello'
    print(eggs)
eggs = 42
spam()
print(eggs)

# Assign global variable in local scoup
def spam():
    global eggs
    eggs = 'Hello'
    print(eggs)
eggs = 42
spam()
print(eggs)