# ☀️ April 3rd | Shift 1, Question 2: The Maximum Subarray 
# (Kadane's Algorithm)The Story: You are given an integer array that contains both positive and negative numbers. 
# Find the contiguous subarray (a sequence of numbers side-by-side) that has the maximum sum.
#  You must print both the maximum sum AND the exact subarray elements.The NQT Trap: Finding just the sum is easy.
#   The trap is that you have to track the start and end indices so you can print the actual subarray at the end. 
#   Brute force ($O(N^2)$) will fail here. You must use Kadane's 
# Algorithm ($O(N)$).Example Input:9-2 1 -3 4 -1 2 1 -5 4Example Output:Max Sum: 6Subarray: 4 -1 2 1


import sys

def solve():
    # --- NORMAL INPUT METHOD ---
    # n = int(input())
    # arr = list(map(int, input().split()))
    
    # --- PRO NQT INPUT ---
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    
    # --- RAW LOGIC (Kadane's Algorithm with Index Tracking) ---
    max_sum = float('-inf')
    current_sum = 0
    
    start_idx = 0
    end_idx = 0
    temp_start = 0  # Used to track the start of a fresh sequence
    
    for i in range(n):
        current_sum += arr[i]
        
        # If we hit a new highest sum, update max_sum and lock in the indices
        if current_sum > max_sum:
            max_sum = current_sum
            start_idx = temp_start
            end_idx = i
            
        # If our running sum drops below zero, it's useless for future numbers.
        # Reset it to 0 and assume the next number will be the start of a new subarray.
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
            
    print(max_sum)
    
    # Print the actual subarray elements using the locked indices
    for i in range(start_idx, end_idx + 1):
        print(arr[i], end=" ")

if __name__ == '__main__':
    solve()