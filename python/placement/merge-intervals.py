def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals by their start values
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for interval in intervals[1:]:
        current_interval = merged[-1]

        if interval[0] <= current_interval[1]:
            # If the current interval overlaps with the previous one, merge them
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            # If there is no overlap, add the current interval to the merged list
            merged.append(interval)

    return merged

# Test the merge_intervals function
intervals = [[1, 3], [2, 6], [8, 9], [15, 18], [12, 19]]
merged_intervals = merge_intervals(intervals)

print("Merged Intervals:")
for interval in merged_intervals:
    print(interval)