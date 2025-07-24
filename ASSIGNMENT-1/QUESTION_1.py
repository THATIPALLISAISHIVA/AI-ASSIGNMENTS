from collections import deque

class State:
    def __init__(self, config):
        self.config = config

    def goal_test(self):
        return self.config == ('W','W','W','_','E','E','E')

    def move_gen(self):
        children = []
        i = self.config.index('_')
        c = list(self.config)

        if i-1 >= 0 and c[i-1] == 'E':
            nxt = c.copy()
            nxt[i], nxt[i-1] = nxt[i-1], '_'
            children.append(State(tuple(nxt)))
        if i+1 < len(c) and c[i+1] == 'W':
            nxt = c.copy()
            nxt[i], nxt[i+1] = nxt[i+1], '_'
            children.append(State(tuple(nxt)))

        if i-2 >= 0 and c[i-2] == 'E' and c[i-1] in ('E','W'):
            nxt = c.copy()
            nxt[i], nxt[i-2] = nxt[i-2], '_'
            children.append(State(tuple(nxt)))
        if i+2 < len(c) and c[i+2] == 'W' and c[i+1] in ('E','W'):
            nxt = c.copy()
            nxt[i], nxt[i+2] = nxt[i+2], '_'
            children.append(State(tuple(nxt)))

        return children

    def __eq__(self, other):
        return isinstance(other, State) and self.config == other.config

    def __hash__(self):
        return hash(self.config)

    def __str__(self):
        return ''.join(self.config)


def removeSeen(children, OPEN, CLOSED):
    open_states   = [node for node, _ in OPEN]
    closed_states = [node for node, _ in CLOSED]
    return [c for c in children if c not in open_states and c not in closed_states]


def reconstructPath(node_pair, CLOSED):
    parent_map = { node: parent for node, parent in CLOSED }
    N, parent = node_pair
    path = [N]
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    path.reverse()
    print(" ->\n ".join(str(s) for s in path))
    return path


def bfs(start):
    OPEN   = [(start, None)]
    CLOSED = []
    while OPEN:
        node, parent = OPEN.pop(0)
        CLOSED.append((node, parent))

        if node.goal_test():
            print("BFS found goal!")
            return reconstructPath((node, parent), CLOSED)

        children = node.move_gen()
        new_nodes = removeSeen(children, OPEN, CLOSED)
        OPEN += [(c, node) for c in new_nodes]

    print("BFS: No solution.")
    return []


def dfs(start):
    OPEN   = [(start, None)]
    CLOSED = []
    while OPEN:
        node, parent = OPEN.pop(0)
        CLOSED.append((node, parent))

        if node.goal_test():
            print("DFS found goal!")
            return reconstructPath((node, parent), CLOSED)

        children = node.move_gen()
        new_nodes = removeSeen(children, OPEN, CLOSED)
        OPEN = [(c, node) for c in new_nodes] + OPEN

    print("DFS: No solution.")
    return []


if __name__ == "__main__":
    start = State(('E','E','E','_','W','W','W'))
    bfs(start)
    print()
    dfs(start)
