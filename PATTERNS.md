# Reusable problem-solving patterns

A template is a starting structure with a reason it works. Before copying one, identify its assumptions, define what each variable means, and say what remains true after each iteration. Change the structure when the contract demands it.

## Recognition map

| Clue in the problem | Candidate pattern | Practice |
|---|---|---|
| Count matches, keep the best, or find the first | Linear scan / accumulator | 004–008, 012 |
| Find a previously seen partner or duplicate | Hash map / set | 017–023, 028 |
| Repeated range totals or exact-sum subarrays | Prefix sums, possibly with a count map | 025–027 |
| Combine everything except the current item | Prefix and suffix passes | 024 |
| Sorted pair search or two ends of a sequence | Two pointers | 010, 015, 031–034, 097 |
| A contiguous block of fixed length | Fixed sliding window | 035–036, 040 |
| Longest/shortest contiguous block under a maintainable condition | Variable sliding window | 029–030, 037–039, 096 |
| Sorted values or a monotone feasibility condition | Binary search | 041–050, 095 |
| Nested matching, undoing, or expression evaluation | Stack | 051–053 |
| Next greater/smaller value, repeated blocked candidates | Monotonic stack / deque | 054–055, 098–099 |
| Overlapping time/range segments | Sort + merge / greedy | 056–058 |
| Keep the best k items or repeatedly take the smallest | Heap | 059, 079 |
| Many prefix lookups | Trie | 060 |
| Node rewiring, middle/cycle, offset from end | Linked pointers, fast/slow, dummy node | 061–065 |
| Nested structure or connected regions | Tree/graph DFS or BFS | 066–077 |
| Dependencies and cycles | Topological sorting | 078 |
| Nonnegative weighted shortest paths | Dijkstra | 079 |
| Repeated connectivity checks | Disjoint-set union | 080 |
| Enumerate valid choices | Backtracking | 081–084 |
| Repeated subproblems with an optimal value or count | Dynamic programming | 085–094, 100 |

**Contiguous** means one uninterrupted range. A **subsequence** may skip items while keeping order. A **subset** ignores position/order except for which items are chosen. Those distinctions often decide the pattern.

## 1. Scan with an invariant

```python
best = initial_value
for value in values:
    # Update best so it summarizes the processed prefix.
    ...
return best
```

Choose the initial value from the contract: zero for a sum/count, a real element for a nonempty minimum, or `None` for an absent candidate. State the invariant: “after processing i items, best is ...”. A one-pass answer is valid only if your summary contains everything the future needs.

## 2. Hash a complement or a canonical form

```python
seen = {}
for i, value in enumerate(nums):
    needed = target - value
    if needed in seen:
        return [seen[needed], i]
    if value not in seen:
        seen[value] = i
return []
```

The map contains earlier positions only, so a number cannot use itself. For grouping, choose a canonical key: sorted characters for anagrams, a tuple of counts for a bounded alphabet, or a normalized representation appropriate to the task. Sets record membership; dictionaries can record counts, positions, or states.

Expected O(1) hash operations are the usual interview model. Sorting a key still has a cost.

## 3. Prefix sums: ranges and exact targets

```python
prefix = [0]
for value in nums:
    prefix.append(prefix[-1] + value)
# Sum of nums[left:right], with right excluded:
answer = prefix[right] - prefix[left]
```

For an exact-sum subarray, let current prefix total be `total`. An earlier prefix of `total - k` leaves a subarray of sum k:

```python
frequency = {0: 1}
total = answer = 0
for value in nums:
    total += value
    answer += frequency.get(total - k, 0)
    frequency[total] = frequency.get(total, 0) + 1
```

The initial zero counts ranges starting at index zero. Query before recording the current prefix to avoid counting an empty range. Store a **frequency**, because different earlier boundaries can have the same total. Unlike a positive-sum sliding window, this method works with negative values too.

## 4. Two pointers

For sorted pair sum:

```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        return [left, right]
    if total < target:
        left += 1
    else:
        right -= 1
return []
```

If the sum is too small, pairing the left value with any smaller right endpoint cannot help; discard that left candidate. Prove an equivalent discard rule for every two-pointer problem. For in-place compaction, a separate write pointer must never overwrite unread data. For Three Sum, sort a copy, fix one value, then use the pair template and skip duplicates.

## 5. Sliding windows

A fixed window maintains a summary when one item enters and one leaves:

```python
window_sum = sum(nums[:k])       # Requires 1 <= k <= len(nums).
best = window_sum
for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]
    best = max(best, window_sum)
```

For a **longest valid** window, the usual shape is:

```python
left = 0
for right, value in enumerate(nums):
    # Add value to the window state.
    while window_is_invalid:   # Replace with a real maintained condition.
        # Remove nums[left] from the state.
        left += 1
    # The current window is valid; consider its length.
```

For a **shortest valid** window, shrink **while valid**, recording the answer before each removal. Minimum Window Substring uses required multiplicities; a set of required letters is insufficient. Each boundary advances at most n times, giving O(n) pointer moves when state updates are O(1).

A variable sum window works for positive numbers because extending increases the sum and shrinking decreases it. Negative numbers break that property; use prefix sums or another method. A longest-window template also needs validity to be repairable by moving the left boundary. State what exactly your counts mean.

## 6. Binary search: a consistent boundary convention

Lower bound finds the first index with `nums[index] >= target`:

```python
left, right = 0, len(nums)       # Search interval [left, right).
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
return left                    # May equal len(nums).
```

To find an exact target, check the returned index is in bounds and equals target. To get the first value greater than target, change the condition to `nums[mid] <= target`. Keep one interval convention throughout; prove every iteration makes the interval smaller.

For binary search on the answer, find the smallest feasible integer:

```python
left, right = lower_bound, known_feasible_upper_bound
while left < right:
    mid = (left + right) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1
return left
```

Feasibility must be monotone: once True, all larger candidates are True. In banana eating, increasing speed cannot increase required hours. In shipping, increasing capacity cannot increase required days. Cost is O(log(answer_range) * cost_of_feasible). Rotated arrays and median partition need their own justified branching rules; memorize the invariant rather than one universal condition.

## 7. Stacks, monotonic stacks, and deques

A normal stack models last-in-first-out: opening brackets, path components, or operands. For RPN, pop the **right** operand before the left.

Next greater element often uses unresolved indices:

```python
stack = []
answer = [0] * len(nums)
for i, value in enumerate(nums):
    while stack and nums[stack[-1]] < value:
        previous = stack.pop()
        answer[previous] = i - previous
    stack.append(i)
```

Here stack values are nonincreasing. Each index enters and leaves once, so total time is O(n), even with a nested while loop. Whether equal values should pop depends on the task.

A monotonic deque for window maximum holds indices with decreasing values. Remove expired indices from the front, remove dominated values from the back, append the current index, and read the front after the first full window. Indices tell you both value and expiration. Histogram area uses a popped height and the boundaries that first make that height impossible; see 098 before adapting that formula.

## 8. Greedy intervals and heaps

For merging intervals, sort by start; the current output interval contains the merged span so far. If the next interval overlaps, extend its end. Otherwise start a new output interval. Whether touching endpoints overlap depends on whether the contract uses closed or half-open intervals.

For the fewest arrows, sort by end and shoot at the earliest ending interval's end. This is an exchange argument: some shot must hit that interval; moving that shot to its end cannot hurt another interval starting before that end and ending no earlier. Skip all intervals the shot hits.

For kth largest, maintain a **min-heap of at most k** values. After each item, it contains the k largest seen so far (or all items if fewer exist). Its root is the smallest retained value, hence the kth largest once k exist. O(n log(k+1)) time and O(k) space. Use `heapq`; a plain sorted list makes repeated insertions expensive.

## 9. Trie and pointer structures

A trie stores one character per edge. Follow/create edges on insertion and mark the final node as a full word. Searching a full word needs the end marker; prefix lookup only needs the path. Empty-word/prefix behavior is a contract choice: check exercise 060.

To reverse a linked list:

```python
previous = None
current = head
while current is not None:
    following = current.next
    current.next = previous
    previous = current
    current = following
return previous
```

Save `following` before rewiring. Dummy nodes simplify changes to the head. Fast/slow pointers detect cycles or find middles; two pointers separated by n positions locate the nth node from the end. Node identity matters even when `.val` values match.

## 10. DFS and BFS

For a tree, a recursive function can return a summary of a subtree:

```python
def height(node):
    if node is None:
        return 0
    left = height(node.left)
    right = height(node.right)
    return 1 + max(left, right)
```

The call stack costs O(height), which can be O(n) for a chain. Deep Python trees may need an iterative traversal. Diameter combines two returned heights; BST validation carries bounds from **all** ancestors, not only the parent.

For unweighted graph reachability or shortest edge-count distance:

```python
from collections import deque
seen = {start}
queue = deque([(start, 0)])
while queue:
    node, distance = queue.popleft()
    for neighbor in adjacency[node]:
        if neighbor not in seen:
            seen.add(neighbor)
            queue.append((neighbor, distance + 1))
```

Mark visited when enqueueing, so cycles do not enqueue the same node repeatedly. O(V+E) time over reached vertices/edges, O(V) auxiliary space. Grids are graphs whose neighbors are valid adjacent cells. For cloning, map each original node to its unique clone **before** traversing its neighbors.

## 11. Dependencies, shortest paths, and connectivity

**Topological sort:** build edges prerequisite → course and indegrees. Enqueue indegree-zero vertices, remove their outgoing edges, and enqueue neighbors whose indegree becomes zero. If fewer than V vertices are processed, a directed cycle remains. O(V+E).

**Dijkstra:** keep best known distances in a map/array and candidate `(distance, node)` pairs in a min-heap. Pop the smallest distance, skip stale entries, relax outgoing edges, and push improvements. Nonnegative edge weights justify finalizing shortest distances in this order; negative edges need another algorithm. The heap implementation in 079 documents its edge-based bound, including stale entries.

**DSU:** give each element a parent; `find` follows parents to the representative, compressing the path. `union` connects two different representatives using size/rank. Already equal representatives mean the new undirected edge closes a cycle. Amortized cost per operation with both heuristics is O(alpha(V)), effectively tiny. DSU is for connectivity; it does not retain paths or solve directed cycle detection.

## 12. Backtracking: choose, explore, undo

```python
answers = []
path = []
def search(state):
    if complete(state):
        answers.append(path.copy())
        return
    for choice in allowed_choices(state):
        path.append(choice)
        search(next_state(state, choice))
        path.pop()
```

Define the state and valid next choices before coding. Each recursive branch must advance or reduce a bounded quantity. Copy paths when saving them; saving the same mutable object makes all answers change together. Word Search additionally marks a cell unavailable during one path and restores it afterward. Subsets use a starting index; permutations track used choices; Combination Sum may reuse the current index.

Exponential time can be unavoidable when enumerating exponentially many answers. Include output construction in complexity, such as O(n * 2**n) for all subsets.

## 13. Dynamic programming: define the state first

Ask five questions:

1. What precisely does `dp[state]` mean?
2. Which smaller states determine it?
3. What are the base cases, including an empty prefix?
4. Which iteration order makes dependencies available?
5. Which state contains the answer?

For stairs, `dp[i] = dp[i-1] + dp[i-2]`; `dp[0] = 1` represents one empty way. For House Robber, choose between skipping the house and taking it plus the best two positions back. For minimum coins, impossible states start at infinity; do not accidentally count combinations when the task asks for a minimum.

For 0/1 subset sum with nonnegative values, process sums **backward** for each input so it cannot be reused in the same iteration. Unbounded coin usage often processes sums **forward**. Loop direction encodes whether reuse is permitted.

For two strings, use prefix lengths as state coordinates. In LCS a match extends the diagonal; otherwise take the best of dropping one final character. In edit distance, the alternatives are insert, delete, replace, each with its own neighbor. A table's O(n*m) states times O(1) work per state gives O(n*m) time; row compression is valid only if it preserves needed neighbors.

For interval DP, identify a choice that splits the interval into independent smaller intervals. Burst Balloons chooses the **last** balloon inside `(left, right)`: at that moment its surviving neighbors are the interval boundaries. Fill intervals by increasing width. Choosing the first balloon does not give the same fixed-boundary recurrence.

Memoization caches recursive states; tabulation fills them in a valid order. Both require a correct state definition. A state that omits relevant history can cache incorrect answers.

## Check your reasoning before the code

- **Correctness:** What invariant, induction, exchange argument, or recurrence justifies every result?
- **Termination:** Which pointer, interval, queue, or state makes progress?
- **Complexity:** Count total operations across the whole algorithm. Include sorting, slicing, recursion, and output.
- **Boundaries:** Empty input if permitted, one item, duplicates, zeros, negative numbers, extreme k, disconnected graphs, skewed trees.
- **Contract:** Return type, tie order, index convention, input mutation, and object identity.

Pattern recognition gets easier through re-solving. When you finish a problem, write one sentence: “I used ___ because ___.”
