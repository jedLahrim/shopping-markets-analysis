import numpy as np

np.set_printoptions(suppress=True, precision=0, floatmode='fixed')
shopping_data = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True)
print(shopping_data)

print(np.isnan(shopping_data))

# Set print options to display full numbers
# Step 1: Read the CSV file using pandas
shopping_data = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True)

nan_shopping_data = np.isnan(shopping_data)
temporary_mean = np.nanmean(shopping_data, axis=0)
temporary_fill = np.nanmax(shopping_data) + 1
temporary_max = np.nanmax(shopping_data, axis=0)
temporary_min = np.nanmin(shopping_data, axis=0)
len(temporary_mean)
temporary_status = np.array([temporary_min, temporary_mean, temporary_max])
string_columns = np.argwhere(np.isnan(temporary_mean)).squeeze()
print(string_columns)
numeric_columns = np.argwhere(np.isnan(temporary_mean) == False).squeeze()
print(numeric_columns)
shopping_data_string = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True,
                                     usecols=string_columns,
                                     dtype=np.str_)

shopping_data_numeric = np.genfromtxt('data/retailcenter.csv', delimiter=';', skip_header=1, autostrip=True,
                                      usecols=numeric_columns, filling_values=temporary_fill)
