import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from backend import main

## GUI Goal ##
'''
_______________________________________________
|             Log File Analyzer                |
|                                              |
|  Log File:   [no file selected...] [Browse]  |
|                                              |
|                   [Analyze]                  |
|                                              |         
|  -----------------------------------------   |             
|                                              |  
|  Results                                     |   
|                                              |           
|  Total Entries: __                           |    
|  INFO: __                                    |     
|  WARNING: __                                 |
|  ERROR: __                                   |
|                                              |
|  Security Alerts:                            | 
|                                              |           
|______________________________________________|                                                
'''

## MAIN WINDOW ##
root = tk.Tk()
root.title("Log File Analyzer")
root.geometry("800x600")

title_label = tk.Label(root, text="Log File Analyzer", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20)

## GUI VARIABLES ##
selected_file = tk.StringVar(value="No File Selected...")
total_entries_var = tk.StringVar(value="0")
info_count_var = tk.StringVar(value="0")
warning_count_var = tk.StringVar(value="0")
error_count_var = tk.StringVar(value="0")


## FUNCTIONS ##
def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Log File",
        filetypes=[("Log Files", "*.log"), ("All Files", "*.*")]
    )

    if file_path:
        selected_file.set(file_path)

def analyze_file():
    file_path = selected_file.get()

    if file_path == "No File Selected...":
        return messagebox.showwarning(
            "Error",
            "Please select a log file to analyze."
        )

    report = main(file_path)

    total_entries_var.set(report["total_entries"])
    info_count_var.set(report["info_count"])
    warning_count_var.set(report["warning_count"])
    error_count_var.set(report["error_count"]) 

    ## Delete every thing from the beginning ("1.0") to the end (tk.END) of the text box ##
    alerts_text.delete("1.0", tk.END)

    if report["alerts"]:
        for alert in report["alerts"]:
            alerts_text.insert(
                tk.END, 
                f"ALERT: {alert['type']} detected from IP "
                f"{alert['ip_address']} with "
                f"{alert['failed_attempts']} failed attempts between " 
                f"{alert['start_time']} and {alert['end_time']}.\n\n" # < -- added a new line + space after each alert for better readability
            )
    else:
        alerts_text.insert(tk.END, "No security alerts detected.")



##########################        GUI LAYOUT            ############################


file_frame = tk.Frame(root)
file_frame.pack(pady=25)

file_label = tk.Label(file_frame, textvariable=selected_file, width=50, anchor="w")
file_label.pack(side=tk.LEFT, padx=10)

file_button = tk.Button(file_frame, text="Browse", command=browse_file)
file_button.pack(side=tk.LEFT, padx=10)

analyze_button = tk.Button(root, text="Analyze", command=analyze_file)
analyze_button.pack(pady=20)

## RESULTS FRAME ##
results_frame = tk.Frame(root)
results_frame.pack(pady=20)

results_title = tk.Label(results_frame, text="Results", font=("Arial", 14, "bold"))
results_title.pack(pady=20)


## TOTAL ENTRIES FRAME ##
total_entries_frame = tk.Frame(results_frame)
total_entries_frame.pack(pady=10)

tk.Label(total_entries_frame, 
            text="Total Entries:", 
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Label(total_entries_frame,
            textvariable=total_entries_var,
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

## INFO FRAME ##
info_frame = tk.Frame(results_frame)
info_frame.pack(pady=10)

tk.Label(info_frame,
            text="INFO Count:",
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Label(info_frame,
            textvariable=info_count_var,
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

## WARNING FRAME ##
warning_frame = tk.Frame(results_frame)
warning_frame.pack(pady=10)

tk.Label(warning_frame,
            text="WARNING Count:",
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Label(warning_frame,
            textvariable=warning_count_var,
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)

## ERROR FRAME ##
error_frame = tk.Frame(results_frame)
error_frame.pack(pady=10)

tk.Label(error_frame,
            text="ERROR Count:",
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
tk.Label(error_frame,
            textvariable=error_count_var,
            font=("Arial", 12)).pack(side=tk.LEFT, padx=5)


## SECURITY ALERTS FRAME ##

'''
Security Alerts 
______________________________________________________
| ALERT: Potential Brute Force detected from IP...   |
|                                                    |
| ALERT: Potential Brute Force detected from IP...   |
|                                                    |
|____________________________________________________|
'''

alerts_frame = tk.Frame(results_frame)
alerts_frame.pack(pady=20)

alerts_title = tk.Label(
    alerts_frame, 
    text="Security Alerts", 
    font=("Arial", 14, "bold"))

alerts_title.pack()

## ALERTS TEXT BOX ##
alerts_text = tk.Text(
    alerts_frame,
    height=10,
    width=100,
    wrap=tk.WORD,
    #state=tk.DISABLED,
    font=("Arial", 12)
)

alerts_text.pack(side=tk.LEFT, padx=10)

## SCROLLBAR ##
alerts_scrollbar = tk.Scrollbar(
    alerts_frame,
    command=alerts_text.yview
)

alerts_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

## CONFIGURE SCROLLBAR ##
alerts_text.config(yscrollcommand=alerts_scrollbar.set)












root.mainloop()

