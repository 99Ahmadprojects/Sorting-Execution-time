import time

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# Test arrays
arrays = {
    5:   list(range(1, 6)),
    10:  list(range(1, 11)),
    50:  list(range(1, 51)),
    100: list(range(1, 101))
}

print("— Selection Sort —")
for n, arr in arrays.items():
    start_ns = time.perf_counter_ns()
    selection_sort(arr)
    elapsed_ms = (time.perf_counter_ns() - start_ns) / 1e6
    print(f"For N = {n:<3} → Time = {elapsed_ms:.3f} ms")
