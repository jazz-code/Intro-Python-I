"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("Script name is " + (sys.argv[0]))

args = len(sys.argv) -1
print("This script is called with %i arguments" % (args))
print("The arguments are: ", str(sys.argv))
# Print out the OS platform you're using:
print("OS: ",sys.platform)
# YOUR CODE HERE
# Print out the version of Python you're using:
print("Python version ",sys.version_info[0],".", sys.version_info[1],".", sys.version_info[2])
# YOUR CODE HERE


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print("Current PID: ", os.getpgid(0))
# Print the current working directory (cwd):
# YOUR CODE HERE
print("CWD: ", os.getcwd())
# Print out your machine's login name
# YOUR CODE HERE
print("Login: ", os.getlogin())