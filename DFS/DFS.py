maze = [
    "S....E",
    ".####.",
    ".####.",
    "......",
]


def find(maze, target):
    """Return the (row, col) of the first cell equal to target."""
    for r, row in enumerate(maze):
        for c, ch in enumerate(row):
            if ch == target:
                return (r, c)
    return None


def neighbours(maze, cell):
    """Find all valid neighbouring cells."""
    rows = len(maze)
    cols = len(maze[0])

    r, c = cell
    result = []

    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] != "#":
                result.append((nr, nc))

    return result


def dfs(maze, current, goal, visited, path):

    visited.add(current)
    path.append(current)

    if current == goal:
        return True

    for nxt in neighbours(maze, current):

        if nxt not in visited:

            if dfs(maze, nxt, goal, visited, path):
                return True

    path.pop()
    return False


# Main Program

start = find(maze, "S")
goal = find(maze, "E")

path = []

found = dfs(maze, start, goal, set(), path)

print("Path found:", found)
print("DFS Path:", path)
print("Steps:", len(path) - 1)