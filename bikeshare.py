import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # Get user input for city (chicago, new york city, washington).
    while True:
        city = input("Please enter the name of the city(chicago, new york city, washington): ").lower()
        if city in ("chicago", "new york city", "washington"):
            break
        

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month (all, january, february, ... , june): ").lower()
        if month in ("all", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"):
            break

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day of week (all, monday, tuesday, ... sunday): ").lower()
        if day in ("all", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"):
            break

    print('-'*40)
    return city, month, day


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
    
    # Reading the city file and converting the date to a dateframe. Also, creating new columns.
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name    
            
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int        
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    print("The most common month is: ", months[df['month'].mode()[0] - 1].title())

    # Display the most common day of week
    print("The most common day of week is: ", df['day_of_week'].mode()[0])

    # Display the most common start hour
	df['hour'] = df['Start Time'].dt.hour
    print("The most start hour is: ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    print("The most commonly used start station is: ", df['Start Station'].mode()[0])

    # Display most commonly used end station
    print("The most commonly used end station is: ", df['End Station'].mode()[0])

    # Display most frequent combination of start station and end station trip
    tripMode = df[['Start Station', 'End Station']].mode()    
    print("The most frequent combination of start station and end station trip is: ", tripMode['Start Station'][0], " to ", tripMode['End Station'][0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    print("Total travel time is: ", df['Trip Duration'].sum())

    # Display mean travel time
    print("Total travel time is: ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print("Number of counts for each user type:")
    print(user_types)
    print()

    # Display counts of gender
    gender = df['Gender'].value_counts()
    print("Number of counts for each gender:")
    print(gender)
    print()
    
    # Display earliest, most recent, and most common year of birth
    print("Earliest year of birth: ", df['Birth Year'].min())
    print("Most recent year of birth: ", df['Birth Year'].max())
    print("Most Common year of birth: ", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)

        # Display first 5 lines of raw data
        while True:
            raw_answer = input("Do you want to see 5 lines of raw data? (yes or no): ").lower()
            if raw_answer == "yes":
                print(df.head())
                
            if raw_answer in ("yes", "no"):
                break                                
            
        restart = input('\nWould you like to restart? Type yes to continue...\n')
        if restart.lower() != 'yes':
            break
		
		print("Thank you for using our program!!")

if __name__ == "__main__":
	main()
