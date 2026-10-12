# log-file-analyzer
# Overview

A Python-based cybersecurity application designed to parse and analyze system log files, identify suspicious authentication activity, and generate security alerts through a graphical user interface (GUI).

The application processes log entries, extracts relevant information such as timestamps, IP addresses, usernames, and event severity levels, and uses time-based detection logic to identify potential brute-force login attempts.

This project was developed to strengthen my practical experience with Python programming, log analysis, threat detection, and security monitoring concepts commonly used in Security Operations Centers (SOCs).

# Key Features

- Log File Parsing: Uses regular expressions (Regex) to extract timestamps, IP addresses, usernames, event messages, and severity levels.

- Event Classification: Categorizes log entries by severity (INFO, WARNING, ERROR) and generates a summary of event counts.

- Brute-Force Detection: Identifies potential brute-force attacks when five or more failed login attempts originate from the same IP address within five minutes.

- Incident Grouping: Groups related failed login attempts into a single incident until more than five minutes pass between consecutive failures, reducing duplicate alerts.

- Security Alert Generation: Produces alerts containing the originating IP address, number of failed attempts, and incident start/end timestamps.

- Graphical User Interface: Provides a Tkinter-based interface for selecting log files, running analysis, reviewing event statistics, and viewing security alerts.

# Technologies Used

- Python

- Tkinter: Graphical user interface

- Regular Expressions (re): Log parsing and pattern matching

- datetime: Timestamp processing and time-based threat detection

- File I/O: Reading and processing log files

# How It Works

- The user selects a log file through the graphical interface.

- The backend reads and parses each log entry.

- Relevant information is extracted and stored in structured Python dictionaries.

- The application calculates event severity counts and organizes failed login attempts by IP address.

- A sliding-window algorithm identifies suspicious authentication activity within a five-minute period.

- Related failed login attempts are grouped into incidents to avoid generating overlapping alerts.

- The application displays the analysis summary and detected security alerts in the GUI.
