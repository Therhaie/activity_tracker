import time
import tkinter as tk
import os
from datetime import datetime
from models.activity import Activity
#from views.main_view import MainView
from controllers.activity_controller import ActivityController
from database.db import create_connection, create_table, add_activity

# def work(controller):
#     controller.start_activity('Work')
#
# def end_of_act(controller):
#     controller.end_activity(controller.current_activity)
#
# def add_act(db_connection, controller):
#     add_activity(db_connection, controller.current_activity)

def main():
    # db_connection is a conn used to create connection with the database

    os.makedirs("data", exist_ok=True)
    db_connection = create_connection("data/activities.db") # connection('activities.db')
    # long terme parser to select the database
    create_table(db_connection)
    # controller.end_activity(controller.current_activity) # synthaxe pas ouf
    controller = ActivityController(db_connection)
    # act1 = Activity('act1')

    controller.current_activity = Activity('Sleep', datetime(2024, 6, 10, 6, 0), datetime(2024, 6, 10, 8, 0))

    # controller.start_activity('Break')
    # controller.end_activity(controller.current_activity)
    add_activity(db_connection, controller.current_activity)

    # work(controller)
    # #time.sleep(40)
    # end_of_act(controller)
    #
    # add_act(db_connection, controller)
    print("the activity is well added to file")
        #todo know the type of db_connection
    #todo need to create function who are aggregating the current line
    #todo need to create the function to create the plot by the data in the file 'activities.db'
    #   - plot of the planning
    #   - analysis of the task done
    #todo need to bind the GIU to the function
    # todo need to handle the case if I close the app before adding the activity -> the activity should be added before
    #  clossing / and when the app is re-run the last act should be closed and then an other can begun
    #todo perhaps adding a parser
    #todo next step is to get the data directly from what is done on the computer
    #   can be usefull to add coupled this app with other device to better track the work



    # the current architecture of the programm makes it unable to do 2 task simultaneously FIFO, FILA

    # act1.end_time()

    # root = tk.Tk()
    # app = MainView(root, controller)
    # root.mainloop()

if __name__ == "__main__":
    main()
