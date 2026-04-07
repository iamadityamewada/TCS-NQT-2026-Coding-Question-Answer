#  April 3rd | Shift 1, Question 1: The Speed Converter
# The Story: You are given the distance traveled by a vehicle in kilometers and the time taken in minutes. 
# You need to convert the time into hours and calculate the speed in km/h.
# The NQT Trap: There is a strict edge case validation. 
# If the time provided is less than 1 minute or greater than 60 minutes, 
# the program must print an error (or return 0) instead of calculating.

# Input Format:

# Line 1: Distance (Integer)

# Line 2: Time in minutes (Integer)

# Example Input:
# 30
# 30
# Example Output:
# 60 (Because 30 km in 0.5 hours = 60 km/h)


import sys

def solve():
    # --- NORMAL INPUT METHOD ---
    # distance = int(input())
    # time_minutes = int(input())
    
    # --- PRO NQT INPUT ---
    data = sys.stdin.read().split()
    if len(data) < 2: return
    distance = int(data[0])
    time_minutes = int(data[1])
    
    # --- RAW LOGIC ---
    # 1. Edge Case / Error Handling
    if time_minutes < 1 or time_minutes > 60:
        print("Error")  # Or print 0 depending on exact compiler instructions
        return
        
    # 2. Formula: Speed = Distance / Time(in hours)
    # Convert minutes to hours by dividing by 60
    time_hours = time_minutes / 60.0
    speed = distance / time_hours
    
    # Print as an integer 
    print(int(speed))

if __name__ == '__main__':
    solve()