from models.activity import Activity

from controllers.activity_controller import ActivityController
from database.db import *
import os
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

## file for data analysis
# reading data from the database OK

def connection(database = 'activities.db'):
    '''
    return db_connection needed to make connection
    :param database:
    :return:
    '''
    cwd = os.getcwd()
    parent = os.path.dirname(cwd)  # get the parent directory
    path_to_data = os.path.join(parent, "data")
    final_path = os.path.join(path_to_data, f"{database}")
    db_connection = create_connection(final_path)
    return db_connection

def get_raw_data_task(activity, database = 'activities.db'):
    db_connection = connection(database)
    raw_data = retrieve_data(db_connection, f'{activity}')
    return raw_data

def get_time_spend(activity):
    data = get_raw_data_task(activity)
    time = timedelta(0)
    for row in data:
        start_time = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
        time += end_time - start_time
        print("tmime spend", time)
    return time


def plot_statistic(List = [], database = 'activities.db'):
    '''
    :param List: by default take every activities that exist
    :return: None
    Plot graph to show how much as been spend on the different activities
    '''
    db_connection = connection(database)
    list_activities = retrieve_name_activities(db_connection)
    print(list_activities)
    act1 = list_activities[0]
    act1 = str(act1)
    act1 = act1.split(",")[0]
    act1 = act1[1:]
    print(act1)

    labels, sizes = [], []

    for label in list_activities:
        # Get the name of the different activities
        act = str(label)
        act = act.split("'")[1]
        labels.append(act)

        # Get the times spend on the different activities
        data = get_time_spend(f'{act}')
        sizes.append(int(data.seconds))

    print("labels", labels)
    print("times,", sizes)

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%.1f%%')
    ax.axis('equal')
    plt.show()


def plot_planning(number_days : int, database ='activities.db') -> None:
    db_connection = connection(database)
    beginning_day = datetime.now() - timedelta(days=number_days)
    # get the data of everything between the period
    all_data = retrieve_all_data_between(db_connection, beginning_day, datetime.now())
    print(all_data)


    ##### Handling of axis
    # Create figure and axis
    fig, ax = plt.subplots()

    # Set x-axis limits for days
    ax.set_xlim(beginning_day, datetime.now() + timedelta(days=1))

    # Set x-axis ticks and labels for days
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))

    # Set y-axis limits for hours of the day
    ax.set_ylim(6, 19)
    ax.set_yticks(range(6, 20))  # Set y-ticks to every hour

    # Label y-ticks as hours
    ax.set_yticklabels([f'{hour:02d}:00' for hour in range(6, 20)])

    #todo same colors for same activities
    #

    #handle the data
    for data in all_data:
        # Define the format of the date and time string
        format = "%Y-%m-%d %H:%M:%S"

        start_time_string = data[2]
        end_time_string = data[3]
        start_time = datetime.strptime(start_time_string, format)
        end_time = datetime.strptime(end_time_string, format)
        duration = end_time - start_time
        print("type data", type(start_time))
        print("type date", type(data[2]))
        print(type(duration))
        print(duration.seconds)

        ax.bar(start_time, duration.total_seconds() / 3600, bottom=start_time.hour, width=0.5)
        ax.text(start_time, start_time.hour + duration.total_seconds() / 7200, f'{data[1]}', ha='center', va='bottom',
                color='black')

    ax.set_xlabel('Day of Month')
    ax.set_ylabel('Time of Day')

    # Show plot
    plt.show()


def main():
    raw_data = get_raw_data_task('Work')
    time = get_time_spend('Work')
    print(time)
    plot_statistic()
    plot_planning(5)

if __name__ == "__main__":
    main()

