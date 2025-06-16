def print_morning():
    
    events = ["Turn off the alarm", "Open my eyes", "Sit up in my bed", "Stand up", 
              "Walk in to the bathroom", "Use the toilet", "Flush the toilet",
              "Wash my hands", "Use the towel"]
    
    number = 1

    for event in events:
        x = input()
        print("Step " + str(number) + " " + event)
        number = number + 1

print_morning()