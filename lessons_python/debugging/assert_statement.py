import traceback
# Exceptions

"""
Create a box
********************
*                  *
*                  *
*                  *
********************
"""
def boxPrinting(symbol, width, height):
    print(symbol * width)
    if len(symbol) !=1:                             # Exception if introduce more then 1 symbol
        raise Exception('"symbol" needs to a string of length 1')
    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" need to be greater then or equal to 2.') # Exception if Width or Height i less then 2
    for i in range(height - 2):
        print(symbol +(' ' * (width - 2)) + symbol) # 15 - 2 = 13 (empty characters)
    print(symbol * width)

boxPrinting('*', 15, 5)


#!!! The traceback.format_exc() Function
try:
    raise Exception('This is the error message')
except:
    errorFile = open('error.txt', 'a') # Add new errors in txt file
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written error_log.txt')


# Assertions and the assert Statement = Sanity check
# Assertions error is kind of exaption

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)


