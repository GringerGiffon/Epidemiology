import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from datetime import datetime

def convert_diff(rand_list):
    sorted_list = []
    length = len(rand_list)
    for i in range(length - 1):
        if (rand_list[i + 1] - rand_list[i]) < 0: # To avoid deviation and error in observation
            sorted_list.append(0)
        else:
            sorted_list.append(rand_list[i + 1] - rand_list[i])

    return sorted_list

total_cases_sierra_leone = [
    14122, 14122, 14104, 14078, 14066, 14052, 14031, 13999, 
    13992, 13978, 13956, 13941, 13928, 13894, 13823, 13785, 
    13756, 13701, 13683, 13638, 13603, 13582, 13538, 13518, 
    13489, 13484, 13465, 13426, 13406, 13387, 13290, 13284, 
    13262, 13250, 13209, 13209, 13201, 13169, 13155, 13135, 
    13119, 13093, 13059, 12990, 12962, 12911, 12884, 12850, 
    12816, 12735, 12666, 12593, 12536, 12519, 12470, 12440, 
    12398, 12371, 12313, 12267, 12256, 12223, 12201, 12170, 
    12138, 12022, 11974, 11889, 11841, 11619, 11301, 10934, 
    10518, 10124, 9446, 8356, 7312, 6599, 6073, 5368, 4759, 
    5235, 3706, 3252, 2789, 2304, 1940, 1673, 1424, 1261, 910, 
    848, 783, 717, 574, 525, 442, 337, 252, 158, 117, 81, 16, 0, 0]

total_death_cases_sierra_leone = [
    3955, 3955, 3955, 3955, 3955, 3955, 3955, 3955, 3955, 
    3955, 3955, 3955, 3955, 3955, 3955, 3955, 3953, 3953, 
    3953, 3953, 3953, 3952, 3952, 3952, 3952, 3951, 3951,
    3951, 3951, 3951, 3951, 3951, 3949, 3949, 3947, 3947, 
    3946, 3941, 3940, 3935, 3932, 3931, 3928, 3922, 3919, 
    3917, 3913, 3912, 3911, 3911, 3907, 3906, 3904, 3904, 
    3904, 3903, 3901, 3899, 3886, 3877, 3872, 3865, 3857, 
    3842, 3831, 3810, 3799, 3773, 3747, 3629, 3461, 3341, 
    3199, 3062, 2758, 2085, 1583, 1398, 1250, 1169, 1070, 
    1500, 1359, 1183, 879, 622, 597, 562, 524, 491, 392, 
    365, 334, 298, 252, 224, 206, 142, 101, 34, 19, 7, 5, 0, 0]

# Revert the  list back to order
data2_infected = total_cases_sierra_leone[::-1]
data2_death = total_death_cases_sierra_leone[::-1]

# Show the difference (ie how many people were infected since the last report) 
infection_data = convert_diff(data2_infected)
death_data = convert_diff(data2_death)

# List of dates
who_report_dates = [
    '11/12/2015', '11/9/2015', '11/5/2015', '11/2/2015', '10/29/2015', '10/26/2015', '10/22/2015', '10/19/2015',
    '10/15/2015', '10/12/2015', '10/8/2015', '10/5/2015', '10/1/2015', '9/28/2015', '9/22/2015', '9/18/2015',
    '9/15/2015', '9/11/2015', '9/8/2015', '9/3/2015', '8/31/2015', '8/27/2015', '8/24/2015', '8/20/2015', '8/17/2015',
    '8/13/2015', '8/10/2015', '8/6/2015', '8/4/2015', '7/31/2015', '7/29/2015', '7/27/2015', '7/23/2015', '7/21/2015',
    '7/17/2015', '7/15/2015', '7/13/2015', '7/9/2015', '7/5/2015', '7/3/2015', '6/30/2015', '6/24/2015', '6/21/2015',
    '6/16/2015', '6/13/2015', '6/9/2015', '6/6/2015', '6/4/2015', '5/30/2015', '5/26/2015', '5/20/2015', '5/16/2015',
    '5/12/2015', '5/9/2015', '5/5/2015', '5/3/2015', '4/29/2015', '4/26/2015', '4/22/2015', '4/19/2015', '4/18/2015',
    '4/16/2015', '4/14/2015', '4/10/2015', '4/8/2015', '4/2/2015', '3/31/2015', '3/27/2015', '3/25/2015', '3/11/2015',
    '2/25/2015', '2/11/2015', '1/28/2015', '1/14/2015', '12/31/2014', '12/17/2014', '12/3/2014', '11/26/2014',
    '11/19/2014', '11/12/2014', '11/5/2014', '10/29/2014', '10/22/2014', '10/15/2014', '10/8/2014', '10/1/2014',
    '9/24/2014', '9/18/2014', '9/12/2014', '9/6/2014', '8/22/2014', '8/19/2014', '8/13/2014', '8/8/2014', '8/3/2014',
    '7/28/2014', '7/21/2014', '7/14/2014', '7/7/2014', '6/24/2014', '6/11/2014', '6/5/2014', '5/28/2014', '5/23/2014'
]

dates_list = []

# Convert date strings to datetime objects
dates_to_convert = [datetime.strptime(date_str, "%m/%d/%Y") for date_str in who_report_dates]

# Initial date
initial_date_str = "3/25/2014"
initial_date = datetime.strptime(initial_date_str, "%m/%d/%Y")

# Calculate and print days elapsed for each date from the initial date
for date in dates_to_convert:
    days_elapsed = (date - initial_date).days
    dates_list.append(days_elapsed)
    
dates = dates_list[::-1]

data2_death.remove(0)

def plot():
    # Scatter plot
    plt.scatter(dates, infection_data, s = 4, marker='o', color='blue', label='Infected People')
    plt.scatter(dates, data2_death, s = 4, marker='o', color='red', label='Deaths')

    plt.xlabel('Time (days)')
    plt.ylabel('People')
    plt.title('Infected / Death cases of Ebola in Sierra Leone')
    plt.legend()
    plt.show()  

if  __name__ == "__main__":
    plot()
    
