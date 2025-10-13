# Practice file operations and error handling
def read_config_file(filename):
    try:
        # open a file
        open(filename, '+')
        # read a file
        
        pass
    except FileNotFoundError:
        # Your code here: handle missing file
        pass
    except Exception as e:
        # Your code here: handle other errors
        pass

# Create a sample config file and test reading it