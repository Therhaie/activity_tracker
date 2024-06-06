from models.activity import Activity
from controllers.activity_controller import ActivityController
from database.db import create_connection, create_table, add_activity, retrieve_data
import os

## file for data analysis
# reading data from the database OK


def main():
    # path to the data file
    cwd = os.getcwd()
    parent = os.path.dirname(cwd) # get the parent directory
    print(parent)
    path_to_data = os.path.join(parent, "data")
    print(path_to_data)
    final_path = os.path.join(path_to_data, "activities.db")
    print(final_path)

    db_connection = create_connection(final_path)
    create_table(db_connection)
    controller = ActivityController(db_connection)
    raw_data = retrieve_data(db_connection, 'Work')
    print(raw_data)

    #time spend on a task



if __name__ == "__main__":
    main()

