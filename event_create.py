from start import cal_service
import csv


def main():
   
   #open and read the CSV file that contains the list of events

    with open("PATH TO FILE\sample_schedule.csv", encoding= "utf-8-sig", newline='') as csvfile:
        filereader = csv.reader(csvfile)
        
        for row in filereader:
            event_name = row[0]
            start_date = row[1]
            end_date = row[3]
            start_time = row[2]
            end_time = row[4]
            utc_start_date = str(start_date)+"T"+str(start_time)
            utc_end_date = str(end_date)+"T"+str(end_time)
            payload = {
                "summary": event_name,
                "description": 'This event was created by a python script',
                "start": {"dateTime": utc_start_date, "timeZone": 'America/Toronto'},
                "end": {"dateTime": utc_end_date, "timeZone": 'America/Toronto'},
            }
            print(payload)

            service = cal_service()

            event_result = service.events().insert(calendarId='primary',body=payload).execute()
            print("-------------------------------------------------------------------")
            print("created event")
            print("id: ", event_result['id'])
            print("summary: ", event_result['summary'])
            print("starts at: ", event_result['start']['dateTime'])
            print("ends at: ", event_result['end']['dateTime'])
            print("-------------------------------------------------------------------")

if __name__ == '__main__':
    main()
