def read_file(filename):
    """Read the contents of a file and return it."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
        return None

def write_file(filename, content):
    """Write content to a new file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Modified content has been written to '{filename}'.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be written.")

def main():
    input_filename = input("Please enter the filename to read: ")
    content = read_file(input_filename)
    
    if content is not None:
        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()
        
        output_filename = input("Please enter the filename to write the modified content to: ")
        write_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
