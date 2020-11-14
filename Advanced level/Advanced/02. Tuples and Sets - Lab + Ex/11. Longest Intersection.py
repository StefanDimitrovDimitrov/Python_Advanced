n = int(input())

longest_intersection = set()
best_length = 0

for _ in range(n):
    ranges = input().split('-')
    first_range_start, first_range_end = [int(x) for x in ranges[0].split(",")]
    first_set = set([x for x in range(first_range_start, first_range_end+1)])

    second_range_start, second_range_end = [int(x) for x in ranges[1].split(",")]
    second_set = set([x for x in range(second_range_start, second_range_end+1)])

    intersection = first_set & second_set

    if len(intersection) > best_length:
        best_length = len(intersection)
        longest_intersection = intersection

converter = [str(x) for x in longest_intersection]

print(f"Longest intersection is [{', '.join(converter)}] with length {len(longest_intersection)}")