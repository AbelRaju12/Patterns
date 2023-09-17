def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda i: i[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= output[-1][1]:
            output[-1][1] = max(output[-1][1], end)
        else:
            output.append([start, end])
    return output
    
    
intervals = [[1, 3], [2, 6], [8, 9], [15, 18], [12, 19]]
merged_intervals = merge_intervals(intervals)
print("Merged Intervals:")
for interval in merged_intervals:
    print(interval)