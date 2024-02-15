# Create a program that reads a log file and provides a summary of its contents 

def analyze_log_file(file_path):
    log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    with open(file_path, 'r') as file:
        for line in file:
            if "INFO" in line:
                log_counts["INFO"] += 1
            elif "WARNING" in line:
                log_counts["WARNING"] += 1
            elif "ERROR" in line:
                log_counts["ERROR"] += 1

    total_logs = sum(log_counts.values())
    return log_counts, total_logs

# Example usage (replace 'server.log' with the path to your log file)
log_file_path = 'yourfilename.log'
counts, total = analyze_log_file(log_file_path)

print(f"Total log entries: {total}")
print("Entries per log level:", counts)

