num_rooms = int(input("Enter number of rooms: "))

dungeon = [[0] * num_rooms for _ in range(num_rooms)]
for i in range(num_rooms):
    for j in range(i + 1, num_rooms):
        time = int(input(f"Time from Room {i} to {j} (0 if blocked): "))
        dungeon[i][j] = time
        dungeon[j][i] = time

# 2. Dijkstra's Setup
visited = [False] * num_rooms
times = [9999] * num_rooms  # Stores the best time
parent = [-1] * num_rooms   # Stores where we came from to show the PATH
times[0] = 0

for _ in range(num_rooms):
    # Find the closest unvisited room
    min_time = 9999
    u = -1 #current room
    for j in range(num_rooms):
        if not visited[j] and times[j] < min_time:
            min_time = times[j]
            u = j
            
    if u == -1: break
    visited[u] = True
    
    # Check neighbors and update their paths
    for v in range(num_rooms):
        travel_time = dungeon[u][v]
        if travel_time > 0 and not visited[v]:
            new_time = times[u] + travel_time
            if new_time < times[v]:
                times[v] = new_time
                parent[v] = u # Remember that we reached 'v' through 'u'

# 3. Print Results and Paths
print("\n--- Final Escape Results ---")
for i in range(num_rooms):
    if times[i] == 9999:
        print(f"Room {i}: Unreachable (-1)")
    else:
        # Build the path by tracing back through 'parent'
        path = []
        curr = i
        while curr != -1:
            path.insert(0, str(curr)) # Add to the front of the list
            curr = parent[curr]
            
        print(f"Room {i} | Time: {times[i]} | Path: {' -> '.join(path)}")
