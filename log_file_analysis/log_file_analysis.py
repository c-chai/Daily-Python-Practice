# Create a program to read a log file and extract certain information from it
# Create a simple file text named log.txt
# Entries will be in format like "[INFO] 2021-09-15 10:15:32: Task completed successfully"
# Program will open the file, read it, and count the number of INFO, WARNING, and ERROR messages 

def count_log_levels(log_file_path):
    counts = {'INFO': 0, 'WARNING': 0, 'ERROR': 0}

    with open(log_file_path, 'r') as file:
        for line in file:
            if '[INFO]' in line:
                counts['INFO'] += 1
            elif '[WARNING]' in line:
                counts['WARNING'] += 1
            elif '[ERROR]' in line:
                counts['ERROR'] += 1
    
    return counts 

# Specify path to your log file 
log_file_path = 'log.txt'

# Count log levels
log_counts = count_log_levels(log_file_path)

print(f"INFO: {log_counts['INFO']}")
print(f"WARNING: {log_counts['WARNING']}")
print(f"ERROR: {log_counts['ERROR']}")