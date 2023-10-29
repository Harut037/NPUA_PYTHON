def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"File Content:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return False
    except ValueError:
        print("Error: Invalid file name. Please provide a valid filename.")
        return False
    return True


def write_to_file(file_name, new_file=False):
    try:
        mode = 'w' if new_file else 'a'
        with open(file_name, mode) as file:
            if new_file:
                content = input("Enter content to write to the file: ")
            else:
                content = input("Enter additional content: ")

            file.write(content)
            print("Writing to file successful.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print(f"File '{file_name}' closed.")


def main():
    valid_file = False
    while not valid_file:
        file_name = input("Enter the name of the text file you want to open: ")

        try:
            valid_file = read_file(file_name)
        except ValueError:
            print("Error: Invalid file name. Please provide a valid filename.")

    write_option = input("Do you want to write to this file? (yes/no): ")
    if write_option.lower() == 'yes':
        new_file_option = input("Do you want to write to a new file? (yes/no): ")
        if new_file_option.lower() == 'yes':
            new_file_name = input("Enter the name of the new file: ")
            write_to_file(new_file_name, new_file=True)
        else:
            write_to_file(file_name)


if __name__ == "__main__":
    main()
