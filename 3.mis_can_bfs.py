from queue import deque

m = int(input("No. of Missionaires : "))
c = int(input("No. of Cannibals : "))
boat_capacity = int(input("Boat Capacity: "))
allpaths = []

def is_valid(state):
    m1, c1, n = state
    m2 = m - m1
    c2 = c - c1
    if m1 < 0  or m2 < 0 or c1 < 0 or c2 < 0:
        return False
    if  (m1 and m1 < c1)  or (m2 and m2 < c2):
        return False
    return True

def generate_successors(state):
    m, c, n = state
    successors = []

    for a in range(boat_capacity + 1):
        for b in range(boat_capacity + 1):
            if 0 < a + b <= boat_capacity:  # Ensure at least one person is on the boat
                if n == 1:
                    new_state = (m - a, c - b, 0)
                else:
                    new_state = (m + a, c + b, 1)

                if is_valid(new_state):
                    successors.append(new_state)

    return successors

def bfs():
    start_state = (m, c, 1)
    goal_state = (0, 0, 0)

    visited = set()
    q = deque([(start_state, [])])
    
    while q:
        current_state = q.popleft()
        state, path = current_state

        if state in visited:
            continue
        
        path.append(state)
        
        if state == goal_state:
            allpaths.append(path)
            continue

        visited.add(state)

        for successor in generate_successors(state):
            if successor not in visited:
                q.append((successor, path.copy()))


bfs()

if len(allpaths)==0:
    print("No Solutions")
else:
     for p in allpaths:
        print(p)