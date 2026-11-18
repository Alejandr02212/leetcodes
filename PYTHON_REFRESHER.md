# Python refresher

Use this as a small reference while you type. All exercises use functions: inputs arrive as arguments, and answers leave through `return`.

```python
def count_positive(nums: list[int]) -> int:
    count = 0
    for value in nums:
        if value > 0:
            count += 1
    return count
```

Indent with four spaces. `==` compares; `=` assigns. An omitted return produces `None`. `print` displays a value but does not return it to the caller. Type hints explain the interface; Python does not enforce them automatically.

## Loops and indices

```python
for i in range(3):             # 0, 1, 2
    pass
for i in range(3, -1, -1):     # 3, 2, 1, 0
    pass
for i, value in enumerate([8, 5]):
    pass                      # (0, 8), then (1, 5)
```

Indices start at zero. `nums[-1]` is the last value. `nums[left:right]` excludes `right` and creates a new list. Indexing outside a list raises `IndexError`; slices tolerate boundaries beyond its length. Empty lists cannot be indexed.

```python
left, right = 0, len(nums) - 1
while left < right:
    left += 1
    right -= 1
```

Every while-loop iteration must make progress toward termination.

## Containers you will use

| Need | Tool | Typical cost |
|---|---|---|
| Append/remove at the end | `list.append`, `list.pop` | Amortized O(1) append, O(1) final pop |
| Membership by value | `set` | Expected O(1) |
| Value → count/index/state | `dict` | Expected O(1) lookup/update |
| FIFO queue | `collections.deque`, `popleft` | O(1) at either end |
| Smallest item repeatedly | `heapq` | O(log n) push/pop, O(1) peek |
| Ordered traversal | `sorted(values)` | O(n log n), creates a new list |

```python
seen = set()                  # {} would be a dict
seen.add(7)
counts = {}
counts['a'] = counts.get('a', 0) + 1
stack = []
stack.append(3)
last = stack.pop()

from collections import deque
queue = deque([0])
first = queue.popleft()

from heapq import heappush, heappop
heap = []
heappush(heap, 4)
smallest = heappop(heap)
```

Dictionary iteration preserves insertion order. A set does not provide sorted order. `list.pop(0)` shifts the remaining items and costs O(n); use a deque for BFS. `nums.sort()` mutates and returns `None`; `sorted(nums)` returns a new list. `.append()` also returns `None`.

## Copies, identity, and mutation

```python
a = [1, 2]
b = a                         # same object
c = a[:]                      # new outer list
assert a is b
assert a == c                 # same values
assert a is not c

rows = [[0] * 3 for _ in range(2)]  # independent rows
```

Avoid `[[0] * 3] * 2`, which shares one row. Slicing makes only a shallow copy: nested objects remain shared. Linked-list and graph problems may require node **identity** (`is`), not matching `.val` values. Changing a pointer can lose access to the remainder; save the next node first.

## Recursion, integer arithmetic, and tests

A recursive function needs a base case and a smaller subproblem. Deep recursion can exceed Python's recursion limit; use an explicit stack/queue for potentially long traversals. Backtracking often has small input limits because its output or search grows exponentially.

`//` rounds down: `-3 // 2 == -2`. Truncating toward zero would give `-1`; the RPN exercise shows an integer-only implementation. `%` gives the remainder. Python integers grow as needed, so extremely large arithmetic has costs beyond the usual fixed-width interview model.

```python
assert 2 + 3 == 5
assert [1, 2] == [1, 2]
assert None is None
```

An `AssertionError` points to a failed condition. Use the traceback to find the failing case. Do not run these exercises with optimized Python (`-O`/`-OO`) because it removes asserts. Inputs outside the stated constraints need no extra behavior unless the task explicitly requests validation.
