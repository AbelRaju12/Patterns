def largestRectHist(heights):
    maxArea = 0
    stack = [] #store pair of values being index and height
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))
        
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i)) #len(hieghts) since it is extended  through the end of the stack
        
    return maxArea

histogram = [2, 1, 5, 6, 2, 3]
result = largestRectHist(histogram)
print(f"The largest rectangle area in the histogram is: {result}")
            