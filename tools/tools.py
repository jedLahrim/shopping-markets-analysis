# import json
#
# import numpy as np
# import pandas as pd
#
#
# def extract_and_sum_working_hours(data_string):
#     # Replace single quotes with double quotes to handle JSON parsing
#     corrected_data_string = data_string.replace("'", '"')
#
#     # Parse the JSON string into a Python object
#     try:
#         data = json.loads(corrected_data_string)
#     except json.JSONDecodeError as e:
#         print(f"Error parsing data: {e}")
#         return 0  # Return 0 hours if there's an error
#
#     # Initialize a list to hold the working hours
#     working_hours = []
#
#     for entry in data:
#         hours = entry["hours"]
#         start_time, end_time = hours.split(" à ")
#
#         # Convert time strings to pandas datetime objects
#         start = pd.to_datetime(start_time, format="%Hh%M")
#         end = pd.to_datetime(end_time, format="%Hh%M")
#
#         # Calculate the duration in hours and append to the list
#         duration = (end - start).total_seconds() / 3600
#         working_hours.append(duration)
#
#     # Return the total hours as an integer
#     return int(sum(working_hours))
