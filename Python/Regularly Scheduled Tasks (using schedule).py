import schedule
import time

def job():
    print("Job executed!")

schedule.every(10).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


#This code schedules a job to run every 10 minutes using the schedule library.