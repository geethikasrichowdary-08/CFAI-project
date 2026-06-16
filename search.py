from collections import deque
import heapq


graph = {
    "A": {"B": 4, "C": 2},
    "B": {"D": 5},
    "C": {"D": 1},
    "D": {}
}


def bfs(start, goal):

    queue = deque([[start]])

    visited = set()

    while queue:

        path = queue.popleft()

        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:

                new_path = list(path)

                new_path.append(neighbor)

                queue.append(new_path)


def dfs(start, goal):

    stack = [[start]]

    visited = set()

    while stack:

        path = stack.pop()

        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:

                new_path = list(path)

                new_path.append(neighbor)

                stack.append(new_path)


def ucs(start, goal):

    pq = [(0, start, [start])]

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node].items():

            heapq.heappush(
                pq,
                (
                    cost + weight,
                    neighbor,
                    path + [neighbor]
                )
            )


heuristic = {
    "A": 5,
    "B": 4,
    "C": 2,
    "D": 0
}


def astar(start, goal):

    pq = [(0, start, [start])]

    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node].items():

            f = cost + weight + heuristic[neighbor]

            heapq.heappush(
                pq,
                (
                    f,
                    neighbor,
                    path + [neighbor]
                )
            )


if __name__ == "__main__":

    print("BFS:", bfs("A", "D"))

    print("DFS:", dfs("A", "D"))

    print("UCS:", ucs("A", "D"))

    print("A* :", astar("A", "D"))