import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge step
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged

# Test arrays
arrays = {
    5:   list(range(1, 6)),
    10:  list(range(1, 11)),
    50:  list(range(1, 51)),
    100: list(range(1, 101))
}

print("— Merge Sort —")
for n, arr in arrays.items():
    start_ns = time.perf_counter_ns()
    merge_sort(arr)
    elapsed_ms = (time.perf_counter_ns() - start_ns) / 1e6
    print(f"For N = {n:<3} → Time = {elapsed_ms:.3f} ms")
