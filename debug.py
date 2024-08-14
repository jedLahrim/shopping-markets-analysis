import numpy as np

# Set print options to display full numbers
# np.set_printoptions(suppress=True, precision=2, linewidth=100)

# Step 1: Read the CSV file using pandas
shopping_data = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True)
shopping_data

shopping_data
nan_shopping_data = np.isnan(shopping_data)
nan_shopping_data
temporary_mean = np.nanmean(shopping_data, axis=0)
temporary_fill = np.nanmax(shopping_data) + 1
temporary_max = np.nanmax(shopping_data, axis=0)
temporary_min = np.nanmin(shopping_data, axis=0)
temporary_mean
len(temporary_mean)
temporary_status = np.array([temporary_min, temporary_mean, temporary_max])
temporary_status
string_columns = np.argwhere(np.isnan(temporary_mean)).squeeze()
print(string_columns)
numeric_columns = np.argwhere(np.isnan(temporary_mean) == False).squeeze()
print(numeric_columns)
shopping_data_string = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True,
                                     usecols=string_columns,
                                     dtype=np.str_)

shopping_data_string
shopping_data_numeric = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True,
                                      usecols=numeric_columns, filling_values=temporary_fill, dtype=str)

shopping_data_numeric
get_full_header = np.genfromtxt('data/retailcenter.csv', delimiter=';',
                                autostrip=True,
                                skip_footer=shopping_data.shape[0],
                                dtype=np.str_)
get_full_header
header_string, header_numeric = get_full_header[string_columns], get_full_header[numeric_columns]
header_numeric
from tools.checkpoint import checkpoint

first_commit = checkpoint('data/first_commit.npz', get_full_header, shopping_data)
first_commit['data']
# examples = [
#     [{"days": "Sunday", "hours": "12h00 à 20h00"}, {"days": "Monday", "hours": "08h00 à 16h00"},
#      {"days": "Tuesday", "hours": "09h00 à 17h00"}, {"days": "Wednesday", "hours": "10h00 à 18h00"},
#      {"days": "Thursday", "hours": "11h00 à 19h00"}, {"days": "Friday", "hours": "12h00 à 20h00"},
#      {"days": "Saturday", "hours": "08h00 à 14h00"}],
#
#     [{"days": "Sunday", "hours": "10h00 à 14h00"}, {"days": "Monday", "hours": "09h00 à 17h00"},
#      {"days": "Tuesday", "hours": "08h00 à 16h00"}, {"days": "Wednesday", "hours": "11h00 à 19h00"},
#      {"days": "Thursday", "hours": "12h00 à 20h00"}, {"days": "Friday", "hours": "13h00 à 21h00"},
#      {"days": "Saturday", "hours": "09h00 à 13h00"}],
#
#     [{"days": "Sunday", "hours": "08h00 à 16h00"}, {"days": "Monday", "hours": "07h00 à 15h00"},
#      {"days": "Tuesday", "hours": "10h00 à 18h00"}, {"days": "Wednesday", "hours": "09h00 à 17h00"},
#      {"days": "Thursday", "hours": "08h00 à 16h00"}, {"days": "Friday", "hours": "11h00 à 19h00"},
#      {"days": "Saturday", "hours": "10h00 à 14h00"}],
#
#     [{"days": "Sunday", "hours": "11h00 à 17h00"}, {"days": "Monday", "hours": "12h00 à 20h00"},
#      {"days": "Tuesday", "hours": "13h00 à 21h00"}, {"days": "Wednesday", "hours": "14h00 à 22h00"},
#      {"days": "Thursday", "hours": "15h00 à 23h00"}, {"days": "Friday", "hours": "16h00 à 00h00"},
#      {"days": "Saturday", "hours": "12h00 à 20h00"}],
#
#     [{"days": "Sunday", "hours": "09h00 à 15h00"}, {"days": "Monday", "hours": "08h00 à 16h00"},
#      {"days": "Tuesday", "hours": "07h00 à 15h00"}, {"days": "Wednesday", "hours": "10h00 à 18h00"},
#      {"days": "Thursday", "hours": "11h00 à 19h00"}, {"days": "Friday", "hours": "12h00 à 20h00"},
#      {"days": "Saturday", "hours": "09h00 à 13h00"}],
#
#     [{"days": "Sunday", "hours": "12h00 à 20h00"}, {"days": "Monday", "hours": "07h00 à 15h00"},
#      {"days": "Tuesday", "hours": "09h00 à 17h00"}, {"days": "Wednesday", "hours": "10h00 à 18h00"},
#      {"days": "Thursday", "hours": "11h00 à 19h00"}, {"days": "Friday", "hours": "13h00 à 21h00"},
#      {"days": "Saturday", "hours": "08h00 à 12h00"}],
#
#     [{"days": "Sunday", "hours": "10h00 à 16h00"}, {"days": "Monday", "hours": "09h00 à 17h00"},
#      {"days": "Tuesday", "hours": "08h00 à 16h00"}, {"days": "Wednesday", "hours": "12h00 à 20h00"},
#      {"days": "Thursday", "hours": "13h00 à 21h00"}, {"days": "Friday", "hours": "14h00 à 22h00"},
#      {"days": "Saturday", "hours": "09h00 à 13h00"}],
#
#     [{"days": "Sunday", "hours": "11h00 à 19h00"}, {"days": "Monday", "hours": "10h00 à 18h00"},
#      {"days": "Tuesday", "hours": "09h00 à 17h00"}, {"days": "Wednesday", "hours": "08h00 à 16h00"},
#      {"days": "Thursday", "hours": "07h00 à 15h00"}, {"days": "Friday", "hours": "06h00 à 14h00"},
#      {"days": "Saturday", "hours": "12h00 à 20h00"}],
#
#     [{"days": "Sunday", "hours": "10h00 à 18h00"}, {"days": "Monday", "hours": "12h00 à 20h00"},
#      {"days": "Tuesday", "hours": "14h00 à 22h00"}, {"days": "Wednesday", "hours": "16h00 à 00h00"},
#      {"days": "Thursday", "hours": "18h00 à 02h00"}, {"days": "Friday", "hours": "20h00 à 04h00"},
#      {"days": "Saturday", "hours": "22h00 à 06h00"}],
#
#     [{"days": "Sunday", "hours": "06h00 à 12h00"}, {"days": "Monday", "hours": "07h00 à 13h00"},
#      {"days": "Tuesday", "hours": "08h00 à 14h00"}, {"days": "Wednesday", "hours": "09h00 à 15h00"},
#      {"days": "Thursday", "hours": "10h00 à 16h00"}, {"days": "Friday", "hours": "11h00 à 17h00"},
#      {"days": "Saturday", "hours": "12h00 à 18h00"}],
#
#     [{"days": "Sunday", "hours": "08h00 à 14h00"}, {"days": "Monday", "hours": "09h00 à 15h00"},
#      {"days": "Tuesday", "hours": "10h00 à 16h00"}, {"days": "Wednesday", "hours": "11h00 à 17h00"},
#      {"days": "Thursday", "hours": "12h00 à 18h00"}, {"days": "Friday", "hours": "13h00 à 19h00"},
#      {"days": "Saturday", "hours": "14h00 à 20h00"}],
#
#     [{"days": "Sunday", "hours": "12h00 à 20h00"}, {"days": "Monday", "hours": "14h00 à 22h00"},
#      {"days": "Tuesday", "hours": "16h00 à 00h00"}, {"days": "Wednesday", "hours": "18h00 à 02h00"},
#      {"days": "Thursday", "hours": "20h00 à 04h00"}, {"days": "Friday", "hours": "22h00 à 06h00"},
#      {"days": "Saturday", "hours": "00h00 à 08h00"}],
#
#     [{"days": "Sunday", "hours": "08h00 à 16h00"}, {"days": "Monday", "hours": "09h00 à 17h00"},
#      {"days": "Tuesday", "hours": "10h00 à 18h00"}, {"days": "Wednesday", "hours": "11h00 à 19h00"},
#      {"days": "Thursday", "hours": "12h00 à 20h00"}, {"days": "Friday", "hours": "13h00 à 21h00"},
#      {"days": "Saturday", "hours": "14h00 à 22h00"}],
#
#     [{"days": "Sunday", "hours": "06h00 à 14h00"}, {"days": "Monday", "hours": "07h00 à 15h00"},
#      {"days": "Tuesday", "hours": "08h00 à 16h00"}, {"days": "Wednesday", "hours": "09h00 à 17h00"},
#      {"days": "Thursday", "hours": "10h00 à 18h00"}, {"days": "Friday", "hours": "11h00 à 19h00"},
#      {"days": "Saturday", "hours": "12h00 à 20h00"}],
#
#     [{"days": "Sunday", "hours": "09h00 à 13h00"}, {"days": "Monday", "hours": "08h00 à 12h00"},
#      {"days": "Tuesday", "hours": "07h00 à 11h00"}, {"days": "Wednesday", "hours": "06h00 à 10h00"},
#      {"days": "Thursday", "hours": "05h00 à 09h00"}, {"days": "Friday", "hours": "04h00 à 08h00"},
#      {"days": "Saturday", "hours": "03h00 à 07h00"}],
#
#     [{"days": "Sunday", "hours": "08h00 à 12h00"}, {"days": "Monday", "hours": "09h00 à 13h00"},
#      {"days": "Tuesday", "hours": "10h00 à 14h00"}, {"days": "Wednesday", "hours": "11h00 à 15h00"},
#      {"days": "Thursday", "hours": "12h00 à 16h00"}, {"days": "Friday", "hours": "13h00 à 17h00"},
#      {"days": "Saturday", "hours": "14h00 à 18h00"}],
#
#     [{"days": "Sunday", "hours": "06h00 à 14h00"}, {"days": "Monday", "hours": "07h00 à 15h00"},
#      {"days": "Tuesday", "hours": "08h00 à 16h00"}, {"days": "Wednesday", "hours": "09h00 à 17h00"},
#      {"days": "Thursday", "hours": "10h00 à 18h00"}, {"days": "Friday", "hours": "11h00 à 19h00"},
#      {"days": "Saturday", "hours": "12h00 à 20h00"}],
# ]
# shopping_data_string[0, 23] = str(
#     [{"days": "Sunday", "hours": "12h00 à 20h00"}, {"days": "Monday", "hours": "08h00 à 16h00"},
#      {"days": "Tuesday", "hours": "09h00 à 17h00"}, {"days": "Wednesday", "hours": "10h00 à 18h00"},
#      {"days": "Thursday", "hours": "11h00 à 19h00"}, {"days": "Friday", "hours": "12h00 à 20h00"},
#      {"days": "Saturday", "hours": "08h00 à 14h00"}])

# for i in range(len(shopping_data_string)):
#     if i < len(shopping_data_string):
#         shopping_data_string[i, 23] = str(examples[i])
import json
from datetime import datetime, timedelta


def calculate_working_hours(json_string):
    # Parse the cleaned JSON string into a list of dictionaries
    work_hours = json.loads(json_string)

    total_hours = 0

    for entry in work_hours:
        hours = entry['hours']
        # Split the hours string into start and end times
        start_time_str, end_time_str = hours.split(' à ')

        # Convert the times into datetime objects
        start_time = datetime.strptime(start_time_str, '%Hh%M')
        end_time = datetime.strptime(end_time_str, '%Hh%M')

        # Handle cases where end time might be earlier than start time (e.g., crossing midnight)
        if end_time < start_time:
            end_time += timedelta(days=1)

        # Calculate the difference in hours
        difference = (end_time - start_time).seconds / 3600
        total_hours += difference

    # Return the total hours as an integer
    return int(total_hours) * 52


# todo create sum working hours column and add it to the dataframe
shopping_data_string
work_hours_json_strings = shopping_data_string[:, 26]
work_hours_json_strings


def get_working_hours():
    # Create a new column for sum_work_hours
    sum_work_hours = np.zeros(len(shopping_data_string), dtype=float)

    for i in range(len(work_hours_json_strings)):
        json_string = work_hours_json_strings[i]
        print(f"Processing shopping_market {i}:")

        # Remove the surrounding quotes and extra escape characters
        cleaned_json_string = json_string.replace('\\"', '"').replace('""', '"').strip('"')

        try:
            total_hours = calculate_working_hours(cleaned_json_string)
            print(f"Total working hours for shopping_market {i}: {total_hours}")

            # Add total_hours to the sum_work_hours column
            sum_work_hours[i] = total_hours
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            sum_work_hours[i] = np.nan  # Set to NaN for error cases
        except Exception as e:
            print(f"Error processing shopping_market {i}: {e}")
            sum_work_hours[i] = np.nan  # Set to NaN for error cases

    # Add the sum_work_hours column to shopping_data_string
    new_shopping_data_string = np.column_stack((shopping_data_string, sum_work_hours))

    # Update the string_columns list to include the new column name
    global string_columns
    string_columns = np.append(string_columns, 'sum_work_hours')

    return new_shopping_data_string


# Create or update the DataFrame column with total hours
#    shopping_data_string['sum_worked_hours'] = total_hours_list
# Call the function to get the updated shopping_data_string
new_shopping_data_string = get_working_hours()
# Get the index of the 'working_hours' column
working_hours_index = 26
# Get the index of the 'sum_work_hours' column (it should be the last column)
sum_work_hours_index = -1
# Create a new column order
new_order = list(range(len(string_columns)))
new_order.insert(working_hours_index + 1, new_order.pop(sum_work_hours_index))
# Reorder the columns
shopping_data_string = new_shopping_data_string[:, new_order]

# Update the string_columns list to match the new order
string_columns = string_columns[new_order]
shopping_data_string
combined_dataset = np.concatenate((shopping_data_string, shopping_data_numeric), axis=1)
combined_dataset

combined_dataset[:, 27][0] = 'sum_work_hours'
combined_dataset

# Save to CSV
np.savetxt('cleaned_dataset.csv', combined_dataset, delimiter=';', fmt='%s')
