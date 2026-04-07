# 💻 3rd April | Shift 2, Question 2: The Circular Conveyor Belt (Josephus Problem)
# This is the question that destroyed candidates in the 2nd shift.The Story: 
# A robot goes around a circular track clockwise containing $N$ slots. 
# It removes the $K$-th element, then moves to the next one and starts counting $K$ again. 
# It continues until only 1 number is left. 
# Print the winning number.Example Input: N = 5, K = 2Example 
# Process: Array is [1, 2, 3, 4, 5]. Removes 2 -> Removes 4 -> Removes 1 -> Removes 5.Winner Output: 3

import sys

def solve():
    # --- NORMAL INPUT METHOD ---
    # n, k = map(int, input().split())
    
    # --- PRO NQT INPUT ---
    data = sys.stdin.read().split()
    if not data: return
    n = int(data[0])
    k = int(data[1])
    
    # ==========================================
    # METHOD 1: RAW LOGIC (Array Simulation)
    # Easy to understand, but takes O(N^2) time.
    # Safe if N is small (which it was in some test cases).
    # ==========================================
    arr = []
    for i in range(1, n + 1):
        arr.append(i)
        
    idx = 0
    while len(arr) > 1:
        # Move idx forward by K-1. Modulo (%) keeps it circular!
        idx = (idx + k - 1) % len(arr)
        arr.pop(idx) # Remove the item
        
    print(arr[0])

    # ==========================================
    # METHOD 2: THE PRO WAY (Recursive Math)
    # O(N) Time. Instantly passes all hidden Prime/Digital test cases.
    # ==========================================
    # def josephus(n, k):
    #     if n == 1:
    #         return 1
    #     return (josephus(n - 1, k) + k - 1) % n + 1
    # print(josephus(n, k))

if __name__ == '__main__':
    solve()