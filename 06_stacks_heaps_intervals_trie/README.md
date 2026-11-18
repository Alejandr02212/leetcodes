# Stage 6: Stacks, heaps, intervals, and tries

Choose a data structure that makes the next operation cheap.

Follow the numbered problems. Difficulty labels are relative to this course.

| # | Exercise | Difficulty | Pattern | Explained solution |
|---|---|---|---|---|
| 051 | [Valid Parentheses](051_valid_parentheses/problem.py) | Easy | Stack: match the latest unfinished opener | [Solution](051_valid_parentheses/solution.py) |
| 052 | [Simplify an Absolute Unix Path](052_simplify_unix_path/problem.py) | Medium | Stack: normalize components | [Solution](052_simplify_unix_path/solution.py) |
| 053 | [Evaluate Reverse Polish Notation](053_evaluate_rpn/problem.py) | Medium | Stack: evaluate an expression from completed operands | [Solution](053_evaluate_rpn/solution.py) |
| 054 | [Daily Temperatures](054_daily_temperatures/problem.py) | Medium | Monotonic stack of unresolved indices | [Solution](054_daily_temperatures/solution.py) |
| 055 | [Next Greater Element in a Circular Array](055_next_greater_circular/problem.py) | Medium | Monotonic stack plus virtual circular traversal | [Solution](055_next_greater_circular/solution.py) |
| 056 | [Merge Overlapping Intervals](056_merge_intervals/problem.py) | Medium | Sort then merge an active interval | [Solution](056_merge_intervals/solution.py) |
| 057 | [Insert an Interval](057_insert_interval/problem.py) | Medium | Three phases: before, overlapping, after | [Solution](057_insert_interval/solution.py) |
| 058 | [Minimum Arrows to Burst Balloons](058_minimum_arrows/problem.py) | Medium | Greedy interval stabbing: choose the earliest end | [Solution](058_minimum_arrows/solution.py) |
| 059 | [Kth Largest Element](059_kth_largest/problem.py) | Medium | Bounded min-heap: retain the best k candidates | [Solution](059_kth_largest/solution.py) |
| 060 | [Build a Prefix Dictionary](060_prefix_dictionary_trie/problem.py) | Medium | Trie: share common prefixes in a character tree | [Solution](060_prefix_dictionary_trie/solution.py) |

Checkpoint: explain one invariant or recurrence from this stage aloud, then redo two exercises without looking at your previous code.

[Return to the course](../README.md)
