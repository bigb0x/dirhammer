""""
dirhammer.py version: 1.0.0
Author: Mohamed Ali (https://twitter.com/MohamedNab1l)


Description

The dirhammer.py is a multi-threads brute-force Python script that searches for sensitive directories on a target website.
dirhammer.py can also run multiple threads to speed up the search process. The user can specify the number of threads to use. Each thread handles searching for directories in a separate process, which allows the script to search for directories more quickly.

Disclaimer

dirhammer.py is for testing purposes only and should only be used on websites that you have permission to test. The author of this script is not responsible for any damage done to any website as a result of using this script.

Minimum Requirements

To run the dirhammer.py script, you will need the following:

    Python 3.6 or later installed on your system
    The requests library for Python (you can install it via pip: pip install requests)
    The termcolor library for Python (you can install it via pip: pip install termcolor)

"""

import requests
import threading
from termcolor import colored

# Get user input for the target website and directories file
print ("dirhammer.py version:1.0 by @MohamedNab1l")
target_website = input("Enter the target website URL: ")
directories_file = input("Enter the path to the directories file: ")
num_threads = int(input("Enter the number of threads to use: "))

# Read directories from the file
with open(directories_file) as f:
    directories = [line.strip() for line in f]

# Define a function to handle each thread
def search_directories():
    # Loop through directories and search for each one
    while True:
        # Get the next directory to search
        try:
            directory = directories.pop(0)
        except IndexError:
            # If there are no more directories, exit the thread
            return
        
        # Construct the full URL
        url = target_website + "/" + directory
        
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            print(colored("Directory found: {}".format(url), "green"))
    
        # If the status code is not 200, continue searching
        else:
            #print("Directory not found: {}".format(url))
            print(colored("Directory not found: {}".format(url), "red"))

# Create a list of threads and start them
threads = []
for i in range(num_threads):
    t = threading.Thread(target=search_directories)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Print any remaining directories that were not found
if directories:
    print("The following directories were not found:")
    for directory in directories:
        print(directory)

