import time
import pandas as pd
import numpy as np

""" Global variables"""
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_keys = ('chicago','new york city','washington')

months = ('All','January', 'February', 'March', 'April', 'May', 'June')

weekdays = ('All','Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. User is asked to enter selections as intengers. Code uses TRY/EXCEPT to handle input exceptions 

    Returns:
        (int) city - Number of the city to analyze
        (int) month - Number of the month to filter by. Input of 0 means no month filter
        (int) day - Number of the day of week to filter by. Input of 0 means no month filter
        (int) filter_sel - Time filter selected
    """
    print("Hello! Let's explore some US bikeshare data!\n")
    # get user input for city (chicago, new york city, washington)
    while True:
        try:
            city = int(input("You may explore the following cities: 1 =Chicago, 2 =New York City, or 3 =Washington D.C. Enter your selection as a number\n"))
        except ValueError:
            print("Not a valid input. Valid location options are: 1 =Chicago, 2 =New York City, or 3 =Washington D.C. Enter your selection as a number\n")
        # if user input is an integer but outside of range, ask user to re enter selection
        if 0 < city < 4:
            break
        else:
            print("Not a valid input. Valid location options are: 1 =Chicago, 2 =New York City, or 3 =Washington D.C. Enter your selection as a number\n")
    # get user input for filter options (none, month, weekday)      
    while True:
        try:
            filter_sel = int(input("You may filter the dataset by month or weekday: 0 =No filter, 1 =By month, 2 =By weekday. Enter your selection as a number\n"))
        except ValueError:
            print("Not a valid input. Valid filter options are: 0 =No filter, 1 =By month, 2 =By weekday. Enter your selection as a number\n")
        # if user input is an integer but outside of range, ask user to re enter selection
        if 0 <= filter_sel < 3: 
            if filter_sel == 0:
                month = 0
                day = 0
            break
        else:
            print("Not a valid input. Valid filter options are: 0 =No filter, 1 =By month, 2 =By weekday. Enter your selection as a number\n")
    
    # get user input for month filter(january, february, ... , june)
    while True and filter_sel == 1:
        try: 
            month = int(input("You may filter the dataset by month: 1 =January, 2 =February, 3 =March, 4 =April, 5 =May, 6 =June. Enter your selection as a number\n"))
        except ValueError:
            print("Not a valid input. Valid month options are: 1 =January, 2 =February, 3 =March, 4 =April, 5 =May, 6 =June. Enter your selection as a number\n")   
        # if user input is an integer but outside of range, ask user to re enter selection
        if 0 < month <= 6:
                day = 0
                break
        else:
            print("Not a valid input. Valid month options are: 1 =January, 2 =February, 3 =March, 4 =April, 5 =May, 6 =June. Enter your selection as a number\n")   
    
    # get user input for weekday filter (sunday, monday, ..., saturday)
    while True and filter_sel == 2:
        try:
            day = int(input("You may filter the dataset by weekday: 1 =Sunday, 2 =Monday, 3 =Tuesday, 4 =Wednesday, 5 =Thursday, 6 =Friday, 7 =Saturday. "
                            "Enter your selection as a number\n"))
        except ValueError:
            print("Not a valid input. Valid weekday options are: 1 =Sunday, 2 =Monday, 3 =Tuesday, 4 =Wednesday, 5 =Thursday, 6 =Friday, 7 =Saturday. "
                    "Enter your selection as a number\n")
        # if user input is an integer but outside of range, ask user to re enter selection
        if 0 < day <= 7:
                month = 0
                break
        else:
             print("Not a valid input. Valid weekday options are: 1 =Sunday, 2 =Monday, 3 =Tuesday, 4 =Wednesday, 5 =Thursday, 6 =Friday, 7 =Saturday. "
                    "Enter your selection as a number\n")

    print('-'*40)
    print ("You selection is City: {}, Month: {}, Weekday: {} \n" .format(city_keys[city-1].capitalize(), months[month], weekdays[day]))
    return city, month, day, filter_sel


def load_data(city, month, day, filter_sel):

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (int) city - name of the city to analyze
        (int) month - name of the month to filter by, or "all" to apply no month filter
        (int) day - name of the day of week to filter by, or "all" to apply no day filter
        (int) filter_sel - Time filter selected
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day if applicable
    """

	# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city_keys[city-1]])
	
	# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
	
	# extract month, day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.day_name()
	
	# filter by month if applicable
    if filter_sel == 1:       
        # filter by month to create the new dataframe using a boolean expression
        df = df[df['month'] == month]
	
	# filter by day of week if applicable
    if filter_sel == 2:
        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == weekdays[day]]

    print("Dataset loaded correctly\n")
    return df

def raw_data_display(df):
    """Displays raw data after the dataframe has been filtered based on user's inputs
    Args:
        df - filtered data frame
    """
    # Display raw data five columns at a time
    display_raw_data_request = str(input("Would you like to display raw data for your selection? Type Y for yes or any other key for no\n"))
    if display_raw_data_request.upper() == 'Y':
        row_show = 5
        print(df.iloc[0:row_show])
        while True:
            display_raw_data_request = str(input("\n Would you like to show the next five rows of data? Type Y for yes or any other key for no\n"))
            if display_raw_data_request.upper() == 'Y':                                           
                print(df.iloc[row_show:row_show+5])
                row_show = row_show + 5
            else:
                break 
    print("Raw data display completed\n")
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    Args:
        df - filtered data frame
    """

    display_stats_request = str(input("Would you like to display time-based statistics? Type Y for yes or any other key for no\n"))
    if display_stats_request.upper() == 'Y':
        print('Calculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # display the most common month
        most_common_month = df['month'].mode()[0]
        print('Based on your filter selections, the month with the most travels is: {}' .format(months[most_common_month]))

        # display the most common day of week
        most_common_day = df['weekday'].mode()[0]       
        print('Based on your filter selections, the weekday with the most travels is: {}' .format(most_common_day))

        # display the most common start hour
        most_common_hour = df['Start Time'].dt.hour.mode()[0]
        most_common_hour_formatted = time.gmtime(most_common_hour*3600)
        print('Based on your filter selections, the most common start hour is', time.strftime("%H:%M:%S",most_common_hour_formatted))

        print("\nCalculations completed in %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        df - filtered data frame
    """

    display_stats_request = str(input("Would you like to display station-based statistics? Type Y for yes or any other key for no\n"))
    if display_stats_request.upper() == 'Y':
    
        print('Calculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # display most commonly used start station
        most_common_start_station = str(df['Start Station'].mode()[0])
        print("Based on your filter selections, the most common start station is: {}" .format(most_common_start_station))

        # display most commonly used end station
        most_common_end_station = str(df['End Station'].mode()[0])
        print("Based on your filter selections, the most common end station is: {}" .format(most_common_end_station))
        
        # display most frequent combination of start station and end station trip
        df['Start-End Combo'] = (df['Start Station'] + ' > ' +  df['End Station'])
        most_common_station_combo = str(df['Start-End Combo'].mode()[0])
        print("Based on your filter selections, the most common start-end station pair is: {}\n" .format(most_common_station_combo))
        
        print("Calculations completed in %s seconds.\n" % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        df - filtered data frame
    """


    display_stats_request = str(input("Would you like to display trip duration-based statistics? Type Y for yes or any other key for no\n"))
    if display_stats_request.upper() == 'Y':

        print('Calculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        total_travel_time = df['Trip Duration'].sum()
        total_travel_time_formatted = time.gmtime(total_travel_time)
        print("Based on your filter selections, the total travel time in hours, minutes, and seconds is: ", time.strftime("%H:%M:%S",total_travel_time_formatted))

        # display mean travel time
        mean_travel_time = df['Trip Duration'].mean()
        mean_travel_time_formatted = time.gmtime(mean_travel_time)
        print("Based on your filter selections, the mean travel time in hours, minutes, and seconds is: ", time.strftime("%H:%M:%S",mean_travel_time_formatted))

        print("\nCalculations completed in %s seconds.\n" % (time.time() - start_time))
        print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        df - filtered data frame
    """

    display_stats_request = str(input("Would you like to display user-based statistics? Type Y for yes or any other key for no\n"))
    if display_stats_request.upper() == 'Y':
    
        print('Calculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_type_count = df['User Type'].value_counts().to_string()
        print("User types counts:\n", user_type_count)

        # Display counts of gender if the data is present in the dataset (i.e. NYC or Chicago)
        try:
            gender_count = df['Gender'].value_counts().to_string()
            print("User gender counts:\n", gender_count)
        except KeyError:
            print("Cannot generate gender counts. This city does not collect user gender data")

        # Display earliest, most recent, and most common year of birth if the data is present in the dataset (i.e. NYC or Chicago)
        try:
            earliest_year_of_birth = str(int(df['Birth Year'].min()))
            most_recent_year_of_birth = str(int(df['Birth Year'].max()))
            most_common_year_of_birth = str(int(df['Birth Year'].mode()[0]))
            print("Based on your filter selections, the oldest user was born in {}, the youngest user was born in {}, and the most common year of birth is " 
                "{}\n" .format(earliest_year_of_birth,most_recent_year_of_birth,most_common_year_of_birth))
        except KeyError:
            print("Cannot generate user age statistics. This city does not collect user age data")

        print("This took %s seconds." % (time.time() - start_time))
        print('-'*40)

def main():
    while True:
        city, month, day, filter_sel = get_filters()
        df = load_data(city, month, day, filter_sel)
       
        raw_data_display(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter Y for yes or any other key for no.\n')
        if restart.upper() != 'Y':
            break


if __name__ == "__main__":
	main()
