# 💻 3rd April | Shift 2, Question 1: Min/Max FrequencyThe Story: Given a list of $N$ numbers, 
# you need to find the number that appears the least number of times (lowest frequency) and the
#  number that appears the most number of times (highest frequency).



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
    
    # --- RAW LOGIC ---
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    highest_freq = -1
    lowest_freq = float('inf') # Infinity to start
    
    most_frequent_num = float('inf')
    least_frequent_num = float('inf')
    
    for num, count in freq.items():
        # Find Highest
        if count > highest_freq:
            highest_freq = count
            most_frequent_num = num
        elif count == highest_freq and num < most_frequent_num:
            most_frequent_num = num
            
        # Find Lowest
        if count < lowest_freq:
            lowest_freq = count
            least_frequent_num = num
        elif count == lowest_freq and num < least_frequent_num:
            least_frequent_num = num
            
    print(f"Lowest Frequency: {least_frequent_num}")
    print(f"Highest Frequency: {most_frequent_num}")

if __name__ == '__main__':
    solve()