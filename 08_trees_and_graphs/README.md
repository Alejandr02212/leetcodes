# Stage 8: Trees and graphs

Transfer traversal ideas to connectivity, dependencies, and shortest paths.

Follow the numbered problems. Difficulty labels are relative to this course.

| # | Exercise | Difficulty | Pattern | Explained solution |
|---|---|---|---|---|
| 071 | [Validate a Binary Search Tree](071_validate_bst/problem.py) | Medium | DFS carrying exclusive ancestor bounds | [Solution](071_validate_bst/solution.py) |
| 072 | [Kth Smallest Value in a BST](072_kth_smallest_bst/problem.py) | Medium | Ordered traversal with an early stop | [Solution](072_kth_smallest_bst/solution.py) |
| 073 | [Diameter of a Binary Tree](073_tree_diameter/problem.py) | Medium | Bottom-up tree DP using iterative postorder | [Solution](073_tree_diameter/solution.py) |
| 074 | [Lowest Common Ancestor in a Binary Tree](074_lowest_common_ancestor/problem.py) | Medium | Parent map plus ancestor-set intersection | [Solution](074_lowest_common_ancestor/solution.py) |
| 075 | [Count Islands in a Grid](075_number_of_islands/problem.py) | Medium | Flood fill: one traversal per connected component | [Solution](075_number_of_islands/solution.py) |
| 076 | [Flood Fill](076_flood_fill/problem.py) | Easy | Grid traversal with an explicit stack | [Solution](076_flood_fill/solution.py) |
| 077 | [Clone an Undirected Graph](077_clone_graph/problem.py) | Medium | Graph traversal with an original-to-copy map | [Solution](077_clone_graph/solution.py) |
| 078 | [Can You Finish Every Course?](078_course_schedule/problem.py) | Medium | Topological sorting with indegrees (Kahn's algorithm) | [Solution](078_course_schedule/solution.py) |
| 079 | [Network Delay Time](079_network_delay_time/problem.py) | Medium | Dijkstra's shortest paths with a min-heap | [Solution](079_network_delay_time/solution.py) |
| 080 | [Find the Redundant Connection](080_redundant_connection/problem.py) | Medium | Disjoint-set union with path compression and union by size | [Solution](080_redundant_connection/solution.py) |

Checkpoint: explain one invariant or recurrence from this stage aloud, then redo two exercises without looking at your previous code.

[Return to the course](../README.md)
