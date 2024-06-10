import os
import subprocess

# Specify the directory containing your Python scripts
directory = '/Users/ionbota/PycharmProjects/Learn_Python/lessons_python/apendix_B'

# Path to the output log file
log_file = '/Users/ionbota/PycharmProjects/Learn_Python/output.log'

# Function to log messages
def log_message(message):
    with open(log_file, 'a') as f:
        f.write(message + '\n')

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a Python script
    if filename.endswith('.py'):
        filepath = os.path.join(directory, filename)
        log_message(f"\n\n--- Running {filename} ---\n\n")
        print(f"Running {filepath}")
        # Run the Python script using the specified Python interpreter and append output to log file
        result = subprocess.run(
            ['/Library/Frameworks/Python.framework/Versions/3.11/bin/python3', filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Log standard output
        if result.stdout:
            log_message(result.stdout)
        # Log standard error
        if result.stderr:
            log_message(f"\n--- Errors in {filename} ---\n")
            log_message(result.stderr)
        # Log return code
        if result.returncode == 0:
            log_message(f"\n--- {filename} completed successfully ---\n")
        else:
            log_message(f"\n--- {filename} failed with return code {result.returncode} ---\n")
