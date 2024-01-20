# Write a function called write_file that takes in the arguments file_name and file_content.
# The file_name can be a combined file path/name, you will need to add the file extension to the file_name when opening a file.
# This function should use file_name included and file_content to write a .txt file.
def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as file:
        file.write(file_content)

# Write a append_to_file function that takes in the same parameters and appends to the .txt file.
def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as file:
        file.write(append_content)

# Write a read_file function that takes in a file name and returns the content of the .txt file.
def read_file(file_name):
    with open(f'{file_name}.txt', mode='r', encoding='utf-8') as file:
        return file.read()
