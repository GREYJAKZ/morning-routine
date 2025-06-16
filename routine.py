def print_morning():
    
    events = ["Turn off the alarm", "Open my eyes", "Sit up in my bed", "Stand up", 
              "Walk in to the bathroom", "Use the toilet", "Flush the toilet",
              "Wash my hands", "Use the towel"]
    
    for event in events:
        number = 1
        print("Step " + str(number) + " " + event)
        number = number + 1

print_morning()