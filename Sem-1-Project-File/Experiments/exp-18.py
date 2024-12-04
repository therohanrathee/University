def open_file(file_path, mode):
    
    # Opens a file and returns the file object.
    
    try:
        return open(file_path, mode)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied for file '{file_path}'.")
        return None
    except Exception as e:
        print(f"Error: Unable to open the file '{file_path}' - {e}")
        return None

def read_file(file_obj):
    
    # Reads the content of the file object and returns it as a string.
    
    try:
        return file_obj.read()
    except Exception as e:
        print(f"Error: Unable to read the file - {e}")
        return None

def write_file(file_obj, content):
    
    # Writes the content to the file object.
    
    try:
        file_obj.write(content)
    except Exception as e:
        print(f"Error: Unable to write to the file - {e}")

def close_file(file_obj):
    
    # Closes the file object.
    
    try:
        file_obj.close()
    except Exception as e:
        print(f"Error: Unable to close the file - {e}")

def copy_file(source_path, destination_path):
    
    # Copies the contents of one file to another.
    
    source_file = open_file(source_path, "r")
    if not source_file:
        return

    content = read_file(source_file)
    if content is None:
        close_file(source_file)
        return

    close_file(source_file)

    destination_file = open_file(destination_path, "w")
    if not destination_file:
        return

    write_file(destination_file, content)
    close_file(destination_file)

    print(f"File '{source_path}' successfully copied to '{destination_path}'.")

# Example usage
source = "source.txt"
destination = "destination.txt"
copy_file(source, destination)
