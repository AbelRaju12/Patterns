from collections import deque

def rottenoranges(grid):
    q = deque()
    time, fresh = 0, 0
    
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])
                
    directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft() #not pop() because it will opo the recently added items and end of the loop
            for dr, dc in directions:
                row, col = dr + r, dc + c #moving in directions
                if(row < 0 or row == len(grid)
                   or col < 0 or col == len(grid[0])
                   or grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        time += 1
                
    return time if fresh == 0 else -1       

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

result = rottenoranges(grid)
print(f"Time = {result} units")