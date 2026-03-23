"""
Title: The Gym Membership Cost (TCS NQT 2026 - March 20, Shift 1)
Category: Phase 1 - Basic Logic, Edge Cases, & Strict I/O

Problem Statement:
A premium gym offers membership plans for specific durations with fixed prices. 
The pricing details are strictly defined as follows:
* 1 Month = 2000
* 3 Months = 5000
* 6 Months = 9000
* 9 Months = 12000
* 12 Months = 15000

The NQT Edge Cases (Hidden Test Cases):
1. If the user requests exactly 0 months, the cost is 0.
2. If the user requests a negative number of months, or any positive number that 
   does not exactly match one of the available plans (e.g., 2, 5, 7), your program 
   must reject it and print exactly: Error

Input Format:
A single integer, N, representing the number of months. (Read from standard input).

Output Format:
* If the input is a valid plan or 0, print the exact integer cost.
* If the input is invalid, print exactly: Error

Constraints:
* -100 <= N <= 100

Sample Input 1:
6

Sample Output 1:
9000

Sample Input 2:
0

Sample Output 2:
0

Sample Input 3:
4

Sample Output 3:
Error
"""
"""
Title: The Gym Membership Cost (TCS NQT 2026 - March 20, Shift 1)
Category: Phase 1 - Basic Logic, Edge Cases, & Strict I/O
"""

import sys

def solve():
    # Read raw standard input from the NQT compiler
    input_data = sys.stdin.read().split()
    
    # Handle empty input edge case to prevent IndexError
    if not input_data:
        return
        
    n = int(input_data[0])
    
    # -----------------------------------------
    # NQT LOGIC: Dictionary Lookup (O(1) Time)
    # -----------------------------------------
    
    # Map valid months to their respective prices
    plans = {
        1: 2000, 
        3: 5000, 
        6: 9000, 
        9: 12000, 
        12: 15000
    }
    
    # Check the specific hidden Test Case 7 trap first
    if n == 0:
        print(0)
    # Check if the requested months exist in our valid plans
    elif n in plans:
        print(plans[n])
    # Handle all negative numbers and invalid positive numbers
    else:
        print("Error")

if __name__ == '__main__':
    solve()