# Step 1: Initialize the stack
momo_stack = []

# Step 2: Push operations
momo_stack.append("PIN")
momo_stack.append("Amount")
momo_stack.append("Confirm")

# Step 3: Undo last two actions (pop twice)
momo_stack.pop()  # Removes "Confirm"
momo_stack.pop()  # Removes "Amount"

# Step 4: Display remaining item
print("Remaining on stack:", momo_stack)
# Step 1: Initialize the stack
ur_stack = []

# Step 2: Push lectures
ur_stack.append("Lecture1")
ur_stack.append("Lecture2")
ur_stack.append("Lecture3")

# Step 3: Pop all lectures
ur_stack.pop()  # Removes "Lecture3"
ur_stack.pop()  # Removes "Lecture2"
ur_stack.pop()  # Removes "Lecture1"

# Step 4: Display remaining stack
print("Remaining on stack:", ur_stack)
from collections import deque

# Step 1: Create the queue
rra_queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5"])

# Step 2: Serve the first client
rra_queue.popleft()

# Step 3: Identify who's now in front
print("Client now in front:", rra_queue[0])
from collections import deque

# Step 1: Create the queue
bk_queue = deque(["Client1", "Client2", "Client3", "Client4", "Client5", "Client6", "Client7", "Client8"])

# Step 2: Serve the first two clients
bk_queue.popleft()  # Client1 served
second_served = bk_queue.popleft()  # Client2 served

# Step 3: Display the second served client
print("Second client served:", second_served)
 