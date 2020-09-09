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

    while True:
        print ('Choose a city from chicago, new york city, or washington')
        city = input()
        city = city.lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print('Please select another city')
        else:
            break

    while True:
        print ("Choose a Month out of : january february march april may june or All")
        month = input()
        month = month.lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("invalid input. Please enter a valid input")
        else:
            break

    while True:
        print ('Choose a Day of the week or ALL')
        day = input()
        day = day.lower()
        if day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("invalid input. Please enter a valid input")
        else:
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

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print ('The Most Common Month is: ')
    print (common_month)

    common_day = df['day_of_week'].mode()[0]
    print ('The Most Common day of the Week is: ')
    print (common_day)


    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print ("THe Most Common Start is: ")
    print (common_hour)

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    common_start = df['Start Station'].mode()[0]
    print ("the Most commonly use Start Station is: ")
    print(common_start)


    common_end = df['End Station'].mode()[0]
    print ('The Most commonly used End Station is: ')
    print (common_end)


    df['combo'] = df['Start Station'] + " " + df['End Station']
    print("THe Most Commonly Combined Stations are: ")
    print (df['combo'].mode()[0])


    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print ('The Total Travel Time is: ')
    print (total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print ('The Mean Travel Time is: ')
    print (mean_travel_time)

    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("User Types equal: ")
    print (user_type)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts().to_string()
        print ('The Total Gender Count is: ')
        print('gender')
    else:
        print("Info not available")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print ('The Earliest User Birth year is: ')
        print (earliest_year)
    else:
        print ('Info Not avaiable for this city')

    if 'Birth Year' in df:
        most_recent_year = df['Birth Year'].max()
        print ('The Most recent User Birth Year is: ')
        print (most_recent_year)
    else:
        print ('info not avaiable for this city')

    if 'Birth Year' in df:
        common_year = df['Birth Year'].mode()
        print ('The Most Common user Birth Year is: ')
        print (common_year)
    else:
        print ('Info not avaiable for this city')

    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to look at the raw data? Please enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
