# 💻 April 1st | Shift 1, Question 1: 
# The Laptop Battery FilterThe Story: 
# You are given an integer $N$ which represents the minimum battery charge required for a laptop to turn on. 
# Following that, you are given a list of battery charges for various laptops currently in the IT department.
#  Your task is to count exactly how many laptops have enough charge to turn on.
# The NQT Trap: The compiler will pass the inputs without telling you how many laptops there are in advance. 
# If you try to use for i in range(length), and you don't know the length, your code will crash. 
# Using sys.stdin completely bypasses this trap because it grabs every number on the screen at once.Input
#  Format:Line 1: An integer $N$ (Minimum charge required).
# Line 2: A sequence of integers representing the current charge of each laptop.
# Example Input:54 7 8 9 1Example Output:3 (Because 7, 8, and 9 are greater than or equal to 5).


import sys

def solve():
    # --- NORMAL INPUT METHOD (Dangerous here) ---
    # n = int(input())
    # arr = list(map(int, input().split())) # Assumes they are on one line
    
    # --- PRO NQT INPUT ---
    data = sys.stdin.read().split()
    if not data: return
    
    # The first number is the minimum required charge
    n = int(data[0])
    
    # The rest of the numbers are the laptop charges
    arr = [int(x) for x in data[1:]]
    
    # --- RAW LOGIC ---
    count = 0
    for charge in arr:
        # Check if the charge is greater than OR EQUAL to the minimum
        if charge >= n:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()