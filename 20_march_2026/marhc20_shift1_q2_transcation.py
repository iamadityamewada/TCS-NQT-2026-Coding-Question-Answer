"""
Title: Fraud Transaction Detection (TCS NQT 2026 - March 20, Shift 1, Q2)
Category: Phase 3 - Dictionaries (HashMaps) & Time Complexity optimization

Problem Statement:
A bank is monitoring transactions to detect fraud. You are given a list of N 
transactions. Each transaction consists of a Sender, Receiver, Amount, and Timestamp. 

Write a program to identify the fraudulent transaction. 
A transaction is flagged as "fraud" if it perfectly matches a previous transaction's 
Sender, Receiver, and Amount, AND the absolute difference between their Timestamps 
is less than or equal to 60 minutes.

Note: It is guaranteed that at least one fraudulent transaction exists in the input. 
You need to print the details of the transaction that triggers the fraud flag 
(the later one in the sequence).

Input Format:
* Line 1: An integer N representing the number of transactions.
* Next N lines: Four space-separated values per line: 
  Sender (String), Receiver (String), Amount (Integer), Timestamp (Integer).

Output Format:
Print the fraudulent transaction details exactly as they appeared in the input.

Constraints:
* 2 <= N <= 10^4  (This constraint is why O(N^2) nested loops will fail)
* 1 <= Amount <= 10^5
* 1 <= Timestamp <= 10^9

Sample Input 1:
3
Rahul Priya 500 10
Amit Sumit 200 40
Rahul Priya 500 50

Sample Output 1:
Rahul Priya 500 50
"""

import sys

def solve():
    # Read raw standard input from the NQT compiler
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
        
    n = int(input_data[0])
    idx = 1
    
    # -----------------------------------------
    # WRITE YOUR NQT LOGIC BELOW THIS LINE
    # Hint: Use a dictionary where the key is "Sender_Receiver_Amount"
    # and the value is the Timestamp.
    # -----------------------------------------
    
    

if __name__ == '__main__':
    solve()