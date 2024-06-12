from models.activity import Activity
from datetime import datetime
class ActivityController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.current_activity = None

    def start_activity(self,name):
        self.current_activity = Activity(name, datetime.now())

    def end_activity(self, activity): # au vue de l'implémentation pas forcément utile de mettre activity en param
        activity.end_time = datetime.now()
        #add activity to the BDD
        return activity