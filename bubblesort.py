import time

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Test arrays
arrays = {
    5:   list(range(1, 6)),
    10:  list(range(1, 11)),
    50:  list(range(1, 51)),
    100: list(range(1, 101))
}

print("— Bubble Sort —")
for n, arr in arrays.items():
    start_ns = time.perf_counter_ns()
    bubble_sort(arr)
    elapsed_ms = (time.perf_counter_ns() - start_ns) / 1e6
    print(f"For N = {n:<3} → Time = {elapsed_ms:.3f} ms")
