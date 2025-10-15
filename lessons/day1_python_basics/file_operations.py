"""
This module uses sys for system-specific parameters and functions.
in this case: stderr
"""
import sys

# Practice file operations and error handling
def read_config_file(filename):
    """
    This function opens, reads,
    and prints the read data from a file,
    but with error handling.
    """
    try:
        # open a file using "with".
        # "with" allows opening and closing the file
        # in a safer and cleaner way.
        with open(filename, 'r', encoding='utf-8') as file:
            print("File Opened!")
            # read a file
            for line in file:
                print(line.strip())
    # handle missing files
    except FileNotFoundError:
        print("File does not exist", file=sys.stderr)
    # handle other PermissionError errors
    except PermissionError:
        print("OS error", file=sys.stderr)
    # handle other IOError errors
    except IOError:
        print("IO error", file=sys.stderr)
    # handle other OS errors
    except OSError:
        print("OS error", file=sys.stderr)
    # handle Value Errors
    except ValueError:
        print("Value error", file=sys.stderr)
    # handle Type Errors
    except TypeError:
        print("Type error", file=sys.stderr)

# Create a sample config file and test reading it
print("\n")
print("Test (1):'123.txt'")
read_config_file("123.txt")
print("\n")

print("Test (2): '/root/home/test.txt'")
read_config_file("/root/home/test.txt")
print("\n")

print("Test (3): 123")
read_config_file(123)
print("\n")
