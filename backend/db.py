import sqlite3

class db():
    def __init__(self) -> None:
        con = sqlite3.connect("alarm.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS alarms('alarm_id' INTEGER PRIMARY KEY AUTOINCREMENT, 'dt' TEXT)")
        con.commit()
    # initialize the table if not exist

    def deleteAlarm(self, time):
        con = sqlite3.connect("alarm.db")
        cursor = con.cursor()
        cursor.execute('DELETE FROM alarms WHERE "dt"= ?', (time,))
        con.commit()
        return
    def addAlarm(self, time):
        con = sqlite3.connect("alarm.db")
        cursor = con.cursor()
        sPath = "./backend/sounds/"
        cursor.execute("INSERT INTO alarms('dt') VALUES(?)", [time,])
        con.commit()
    
    def getAlarms(self):
        con = sqlite3.connect("alarm.db")
        cursor = con.cursor()
        alarmList = []
        alarmList = list(cursor.execute("SELECT dt FROM alarms"))
        if not alarmList:
            return []
        return alarmList
