from collections import deque

def BFS(jug1_capacity, jug2_capacity, target):
    visited = set()
    path = []
    q = deque([(0, 0)])

    while q:
        current_state = q.popleft()
        if current_state in visited:
            continue
        visited.add(current_state)

        jug1, jug2 = current_state
        path.append(current_state)

        if jug1 == target or jug2 == target:
            if jug1 == target and jug2 != 0:
                path.append((jug1, 0))
            elif jug2 == target and jug1 != 0:
                path.append((0, jug2))

            for state in path:
                print(f"jug1: {state[0]} litres    jug2: {state[1]} litres")
            return

        q.extend([
            (jug1, jug2_capacity),   
            (jug1_capacity, jug2),   
            (0, jug2),               
            (jug1, 0),               
            (min(jug1 + jug2, jug1_capacity), max(0, jug2 - (jug1_capacity - jug1))),
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug1 + jug2, jug2_capacity))
        ])

    print("No solution")

if __name__ == '__main__':
    jug1_capacity, jug2_capacity, target = 4, 3, 2
    print("Path from initial state to solution state:")
    BFS(jug1_capacity, jug2_capacity, target)
