## log file analyzer ##

## variables ##
info_count = 0
warning_count = 0
error_count = 0

with open("sample.log", "r") as file:
    for line in file:
        if line.startswith("#"):
            continue
        
        if "INFO" in line:
            info_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "ERROR" in line:
            error_count += 1
        print(line.strip())  # the .strip() function eliminates the newline character
    print(f"info: {info_count}")
    print(f"error: {error_count}")
    print(f"warning: {warning_count}")

