from collections import deque

maze = [
    "S....E",
    ".####.",
    ".####.",
    "......"
]


# Find S or E
def find(maze, target):
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return (r, c)
    return None


# Find valid neighbours
def neighbours(maze, cell):
    rows = len(maze)
    cols = len(maze[0])

    r, c = cell
    result = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] != "#":
                result.append((nr, nc))

    return result


# BFS Function
def bfs(maze, start, goal):

    queue = deque([start])

    visited = {start}

    parent = {start: None}

    while queue:

        current = queue.popleft()

        if current == goal:
            break

        for nxt in neighbours(maze, current):

            if nxt not in visited:

                visited.add(nxt)

                parent[nxt] = current

                queue.append(nxt)

    path = []

    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    return path


# Main Program

start = find(maze, "S")
goal = find(maze, "E")

shortest = bfs(maze, start, goal)

print("BFS shortest path:", shortest)
print("Steps:", len(shortest) - 1)