from models.activity import Activity
from controllers.activity_controller import ActivityController
from database.db import create_connection, create_table, add_activity, retrieve_data, retrieve_name_activities
import os
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
    # # path to the data file
    # cwd = os.getcwd()
    # parent = os.path.dirname(cwd)  # get the parent directory
    # path_to_data = os.path.join(parent, "data")
    # final_path = os.path.join(path_to_data, f"{database}")
    # db_connection = create_connection(final_path)
    # # create_table(db_connection)
    db_connection = connection(database)
    raw_data = retrieve_data(db_connection, f'{activity}')
    return raw_data

def get_time_spend(activity):
    data = get_raw_data_task(activity)
    time = timedelta(0)
    for row in data:
        start_time = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S.%f")
        end_time = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
        time += end_time - start_time
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
    print(len(list_activities))
    act1 = list_activities[0]
    print(act1)
    act1 = str(act1)
    act1 = act1.split(",")[0]
    act1 = act1[1:]
    print(act1)

    labels, sizes = [], []

    for label in list_activities:
        #get the name of the different activities
        act = str(label)
        act = act.split("'")[1]
        labels.append(act)

        # get the times spend on the different activties
        data = get_time_spend(f'{act}')
        sizes.append(int(data.seconds))

    print("labels", labels)
    print("times,", sizes)
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1%%')
    ax.axis('equal')
    plt.show()



def main():
    # path to the data file
    # cwd = os.getcwd()
    # parent = os.path.dirname(cwd) # get the parent directory
    # print(parent)
    # path_to_data = os.path.join(parent, "data")
    # print(path_to_data)
    # final_path = os.path.join(path_to_data, "activities.db")
    # print(final_path)
    #
    # db_connection = create_connection(final_path)
    # create_table(db_connection)
    # controller = ActivityController(db_connection)
    # raw_data = retrieve_data(db_connection, 'Work')
    # print(raw_data)
    raw_data = get_raw_data_task('Work')

    #function to calculate the time spend on a task
    # time = timedelta(0)
    # for row in raw_data:
    #     # begin = row[2].split(' ')[1].split('.')[0]
    #     # end = row[3].split(' ')[1].split('.')[0]
    #     # Parse the start and end times as datetime objects
    #     start_time = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S.%f")
    #     end_time = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
    #
    #     # Calculate the duration of the activity
    #     duration = end_time - start_time
    #     time += duration
    time = get_time_spend('Work')
    print(time)
    plot_statistic()

    # convert everything into second


if __name__ == "__main__":
    main()

