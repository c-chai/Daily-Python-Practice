# Write a program which reads a list of filenames given by user and prints the count of each file type 

def count_file_extensions(filenames):
    extension_count = {}

    # Split the input string into individual filenames 
    files = filenames.split()

    # Process each file 
    for file in files: 
        # Extract the extension
        _, extension = os.path.splitext(file)
        extension = extension[1:].lower() # Removes dot and converts to lowercase

        # Count the extensions 
        if extension in extension_count:
            extension_count[extension] += 1 
        else: 
            extension_count[extension] = 1
    
    return extension_count
# Get the user input 
user_input = input("Please enter the filenames separated by spaces: ")

# Get the count of each file extension 
ext_count = count_file_extensions(user_input)

# Print the counts 
for ext, count in ext_count.items():
    print(f"{ext}: {count}")