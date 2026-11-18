# Python Interview Playground — 100 problems

A gentle return to handwritten code, followed by a structured climb toward interview problems. Everything runs with Python 3.10+ and the standard library. No packages, account, or internet connection required.

These are original LeetCode-style exercises. Difficulty labels describe this course, rather than an official platform rating. Their contracts sometimes differ from similarly named platform questions. Learn the reusable patterns; unfamiliar problems can still require new ideas.

## Have some fun right now

1. Open [001: Add Two Numbers](01_python_reboot/001_add_two_numbers/problem.py).
2. Find `solve`, replace `raise NotImplementedError(...)` with your code, and save.
3. In Terminal, change into this folder and run:

```bash
cd ~/Documents/leetcode-python-100
python3 practice.py 1
```

Aim for problems **001–005** in your first sitting. Take your time. Type the code yourself, even when the answer seems obvious. If that feels good, continue through 010. There is no timer in the early stages.

Every numbered folder contains exactly two Python files:

- `problem.py`: task, examples, constraints, three hints, starter code, and runnable checks.
- `solution.py`: the same task, a full implementation, a correctness explanation, complexity, common mistakes, and checks.

Open the solution only when you want the explanation. You can also run either file directly with `python3 path/to/problem.py` or `python3 path/to/solution.py`. Direct runs do not update the progress tracker.

## Your route

| Stage | Problems | What you practice |
|---|---|---|
| [1. Python reboot](01_python_reboot/README.md) | 001–010 | Expressions, conditionals, loops, indices, first two-pointer invariant |
| [2. Arrays and strings](02_arrays_and_strings/README.md) | 011–020 | Write pointers, sorted merges, counts, hash maps, sets |
| [3. Hashing, prefix sums, windows](03_hashing_prefix_sums_windows/README.md) | 021–030 | Canonical keys, buckets, prefix/suffix passes, subarray sums, moving windows |
| [4. Two pointers and windows](04_two_pointers_and_windows/README.md) | 031–040 | Pair searches, triplets, fixed and variable windows, frequency constraints |
| [5. Binary search](05_binary_search/README.md) | 041–050 | Exact search, boundaries, rotations, binary search on the answer |
| [6. Data structure toolkit](06_stacks_heaps_intervals_trie/README.md) | 051–060 | Stacks, monotonic stacks, interval greediness, heaps, trie |
| [7. Linked lists and trees](07_linked_lists_and_trees/README.md) | 061–070 | Pointer updates, fast/slow pointers, DFS, BFS |
| [8. Trees and graphs](08_trees_and_graphs/README.md) | 071–080 | Tree summaries, components, graph cloning, topological order, Dijkstra, DSU |
| [9. Backtracking and DP](09_backtracking_and_dp/README.md) | 081–090 | Choose/explore/undo, state design, 1D and 2D recurrences |
| [10. Interview capstones](10_interview_capstones/README.md) | 091–100 | Subset DP, string DP, binary partition, minimum window, monotonic deque, interval DP |

**001–020:** rebuild fluency. **021–060:** build your pattern vocabulary. **061–090:** work with recursive structures and states. **091–100:** combine ideas; the final seven are hard capstones. Difficulty also depends on which patterns you already know.

## Useful commands

Run these from this folder:

```bash
python3 practice.py --next             # Find your next uncompleted exercise
python3 practice.py 19                 # Check your implementation of Two Sum
python3 practice.py 19 --solution      # Check its explained reference implementation
python3 practice.py --progress         # Count attempts with a saved pass
python3 practice.py --list             # Full list, patterns, and completion markers
python3 practice.py --all-solutions    # Audit all 100 reference implementations
```

A passing **attempt run through practice.py** records a timestamp in `.progress.json`. Running reference solutions never marks an exercise complete. Keep `.progress.json` if you move the folder. To clear history, rename that file to a backup. Run Python without `-O` or `-OO`, which disable the assert-based checks.

Tests are useful feedback; passing them is not a proof. Explain the invariant or recurrence and why it covers all valid inputs. The tracker records a practice milestone, not interview readiness.

## A practice loop that teaches the pattern

1. Say what the function receives and returns. Check whether it may mutate inputs.
2. Work one tiny example by hand, including an empty or singleton case if allowed.
3. Describe a correct brute-force approach and its cost.
4. Identify repeated work or a useful invariant. Pick a pattern from [PATTERNS.md](PATTERNS.md).
5. Write the code, then test. Explain why it is correct and state time/space costs.
6. If you used a solution, close it and recreate the approach yourself. Revisit tomorrow, then roughly a week later.

Early exercises can take two minutes or twenty. For an unfamiliar medium, try for about 20–30 focused minutes, then use one hint. For a hard problem, spend time understanding the state/invariant before coding. Reading an explanation and then reproducing it is productive practice.

At each stage checkpoint, redo two exercises without notes and explain one approach aloud. Once medium problems feel familiar, mix previously solved problems, practice 30–45 minute interview sessions, and narrate your reasoning. Return to an easier exercise when you need a confidence boost.

## When you get stuck

- **Forgot Python syntax?** Open [PYTHON_REFRESHER.md](PYTHON_REFRESHER.md).
- **Unsure which approach fits?** Open [PATTERNS.md](PATTERNS.md) and use its recognition table.
- **An assertion failed?** Read the failing test, write its expected result by hand, and trace your variables.
- **A helper class looks unfamiliar?** It models a linked node, tree node, or graph node. The helpers build test fixtures; focus on `solve` and preserve the documented identity/mutation behavior.
- **A platform version differs?** Follow this exercise's explicit contract, especially index conventions, ties, empty strings, and whether input is mutated.

You can cover a wide range of interview patterns here. There is no fixed template that guarantees a solution to every possible algorithm problem; the goal is to learn how to choose, adapt, and justify one.
