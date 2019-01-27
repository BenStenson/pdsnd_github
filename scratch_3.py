import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the name of the city (Washington, Chicago, New York City): ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Enter the name of the month or all (January to June: ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day of the week or all: ').lower()

    print('-'*40)
    return city, month, day

#a function to extract data from the CSV
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

#a function to display time statistics
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = {1: 'January' ,2: 'February',3: 'March',4: 'April',5: 'May',6: 'June'}
    popular_month = df['month'].mode()[0]
    print("Most Popular Month: ", months[popular_month])

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day: ', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#a function to display station statistics
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The Most Popular Start Station is : ', popular_start_station)
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The Most Popular End Station is: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['start_end_combo'] = df['Start Station'] + ' to ' + df['End Station']
    start_end_combo = df['start_end_combo'].mode()[0]
    print('The Most Popular Trip is from', start_end_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#a function to display duration statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is :', total_travel_time, 'minutes')

    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print('The average travel time is :', mean_travel_time, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#a function to display user statistics
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_by = df['Birth Year'].min()
        most_recent_by = df['Birth Year'].max()
        most_common_by = df['Birth Year'].mode()[0]
        print('The Earliest Birth Year is:', earliest_by)
        print('The Most Recent Birth Year is:', most_recent_by)
        print('The Most Common Birth Year is:', most_common_by)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#a function to display everything
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Goodbye!")
            break


if __name__ == "__main__":
	main()
