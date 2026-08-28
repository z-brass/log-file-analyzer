import re # regex
from datetime import datetime, timedelta

## global variables ##
info_count = 0
warning_count = 0
error_count = 0
## max time window before brute force is detected ##
FIVE_MINS = timedelta(minutes = 5)
FAILED_ATTEMPT_THRESHOLD = 5


log_entries = []

## creating a dictionary for failed logins per ip
failed_logins_by_ip = {}

## layout ##
'''
failed_logins_by_ip = {
    "192.169.1.25": {
        "count": 5,
        "timestamps": [
        timestamp1,
        timestamp2,
        timestamp3,
        etc...
        ]
    }
}
'''
#########################


with open("sample.log", "r") as file:
    for line in file:

        if line.startswith("#"):
            continue

        # debugging the blank line error when trying to pull parts 
        if not line.strip():
            continue

########################################

        ## REGEX ##


        ## IP ADDRESSES ##
        ## word boundary > 1-3 digits + period > repeat 3 more times > end word boundary
        ip_match = re.search(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", line) 

        if ip_match:
            ip_address = ip_match.group()
            #print(ip_address)

        else:
            ip_address = "Unknown"



        ## USERNAMES (finding "user ____" ##
        ## boundary around 'user' > '/s+' = space, one or more times > '/w+' = word character, one or more (captures the username) ##
        ## .IGNORECASE debugs an issue in the case where a username might not match due to upper/lowercase characters ##
        ## group() would give us something like "user zach". With '1' as the argument it returns just the username ##
        username_match = re.search(r"\buser\s+(\w+)", line, re.IGNORECASE)

        if username_match:
            username = username_match.group(1)
            #print(username)

        else:
            username = "Unknown"



        ## EVENT MESSAGES ##
        parts = line.split()
        event_message = " ".join(parts[3:])



        ## TIMESTAMPS ##
        timestamp_match = re.search(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}", line)

        if timestamp_match:
            timestamp_text = timestamp_match.group()

            #### Converting timestamp string into actual date/time ####
            #### Converting to datetime allows us to use datetime figures with math operators ####
            timestamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")
        else:
            timestamp = None


        ## SEVERITY ##
        severity_match = re.search(r"\b(INFO|WARNING|ERROR)\b", line)
        if severity_match:
            severity = severity_match.group()
        else:
            severity = "Unknown"

#############################################################
        ### STORING LOG ENTRIES ###
        log_entries.append({
            "timestamp": timestamp,
            "severity": severity,
            "username": username,
            "ip_address": ip_address,
            "event_message": event_message
        })

        if severity == "INFO":
            info_count += 1
        elif severity == "WARNING":
            warning_count += 1
        elif severity == "ERROR":
            error_count += 1


    ### FAILED LOGINS ###

    for entry in log_entries:
        if "Failed login attempt" in entry["event_message"]:
            ip = entry["ip_address"]

            if ip not in failed_logins_by_ip:
                failed_logins_by_ip[ip] = {
                    "count": 1,
                    "timestamps": [entry["timestamp"]]
                }
            else:
                failed_logins_by_ip[ip]["count"] += 1
                failed_logins_by_ip[ip]["timestamps"].append(entry["timestamp"])

    ## .items() retrieves dictionary items ##


    for ip, data in failed_logins_by_ip.items():

        timestamps = data["timestamps"]

        for start in range(len(timestamps) - FAILED_ATTEMPT_THRESHOLD + 1):
            time_diff = timestamps[start + 4] - timestamps[start]

            if time_diff <= FIVE_MINS:
                print(
                    f"Potential brute force attempt detected from {ip}: "
                    f"{data['count']} failed attempts between {timestamps[start]} and {timestamps[start + 4]}"
                    )


#print(failed_logins_by_ip)



