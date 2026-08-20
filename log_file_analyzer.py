## log file analyzer ##
import re # regex

## variables ##
info_count = 0
warning_count = 0
error_count = 0
failed_login_count = 0

log_entries = []

with open("sample.log", "r") as file:
    for line in file:
        if line.startswith("#"):
            continue
        # debugging the blank line error when trying to pull parts 
        if not line.strip():
            continue

        ## .split() - separates a line of text into parts, by default at every blank space
        ## positional parts starting from 0 and ascending can be printed out
        parts = line.split() 
        date = parts[0]
        timestamp = parts[1]
        severity = parts[2]
        event_message = " ".join(parts[3:]) ## "separator".join(list[index])

        ## matching IP addresses
        ## word boundary > 1-3 digits + period > repeat 3 more times > end word boundary
        ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line) 
        if ip_match:
            ip_address = ip_match.group()
            print(ip_address)

        log_entries.append({
            "date": date,
            "timestamp": timestamp,
            "severity": severity,
            "event_message": event_message
        })

        if severity == "INFO":
            info_count += 1
        elif severity == "WARNING":
            warning_count += 1
        elif severity == "ERROR":
            error_count += 1

        if "Failed login attempt" in event_message:
            failed_login_count += 1
        print(line.strip())  # prints the lines, the .strip() function eliminates the newline characters in each line


    
#print(f"Failed login attempts {failed_login_count}")
#print(f"Info {info_count}")
#print(log_entries)



