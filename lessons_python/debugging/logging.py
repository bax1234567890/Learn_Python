# ---LOG LEVELS---#
# debug (lowest)
# info
# warning
# error
# critical (highest)

import logging
# Configure logging to display debug and higher level messages
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example to disable all logs under CRITICAL level (uncomment if needed)
# logging.disable(logging.CRITICAL)

# Example to only disable INFO and DEBUG (lower severity than WARNING)
# logging.disable(logging.WARNING)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)', n)  # Use format directly within logging
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s', i, total)  # Use format directly within logging
    logging.debug('Return value is %s', total)  # Use format directly within logging
    return total

result = factorial(5)
print('Factorial result:', result)

logging.debug('End of program')
