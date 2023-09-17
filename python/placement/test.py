def largestRectHist(height):
    maxarea = 0
    stack = []
    
    for i, h in enumerate(height):
        start = i
        while stack and stack[-1][1] > h:
            index, heights = stack.pop()
            maxarea = max(maxarea, heights * (i - index))
            start = index
        stack.append((start, h))
        
    for i, h in stack:
        maxarea = max(maxarea, h * (len(height) - i))
        
    return maxarea

histogram = [2, 1, 5, 6, 2, 3]
result = largestRectHist(histogram)
print(f"The largest rectangle area in the histogram is: {result}")