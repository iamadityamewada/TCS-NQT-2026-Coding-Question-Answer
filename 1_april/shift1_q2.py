# 💻 April 1st | Shift 1, Question 2: 
# The Emotional State SimulationThe Story: 
# A psychological study tracks the "Happy" and "Sad" states of a group of people over time.
# You are given an integer $N$, representing the number of people who start in the Happy state (the initial Sad state is 0).
# The simulation runs for exactly 4 iterations (rounds). In each round, 
# the states transition according to these strict rules:Of the people currently Happy: 70% become Sad, and 30% remain Happy.Of 
# the people currently Sad: 50% become Happy, and 50% remain Sad.Print the final number of people in both states after 4 rounds.
# The NQT Trap: Do not calculate this using integers. If you do, Python will round down and lose the fractional people, causing your 
# final answer to fail the precision test cases.
#  You must use floats (0.3, 0.7, 0.5) and create temporary variables during the loop so you don't 
#  overwrite the current state before the math is done.Example Input:100


import sys

def solve():
    # --- NORMAL INPUT METHOD ---
    # initial_happy = float(input())
    
    # --- PRO NQT INPUT ---
    data = sys.stdin.read().split()
    if not data: return
    
    # Convert immediately to float to handle the decimal math
    happy = float(data[0])
    sad = 0.0
    
    # --- RAW LOGIC ---
    # The problem strictly states to simulate exactly 4 iterations
    for _ in range(4):
        # Calculate the new states based on the percentages
        # 30% of Happy stay Happy, 50% of Sad become Happy
        new_happy = (0.3 * happy) + (0.5 * sad)
        
        # 70% of Happy become Sad, 50% of Sad stay Sad
        new_sad = (0.7 * happy) + (0.5 * sad)
        
        # Update the main variables for the next round
        happy = new_happy
        sad = new_sad
        
    # Formatting the output to handle the float precision (usually 2 to 4 decimal places)
    print(f"Final Happy: {happy:.4f}")
    print(f"Final Sad: {sad:.4f}")

if __name__ == '__main__':
    solve()