from itertools import combinations
#used for generating all possible combinations of 2 family members

class State:
    
    def __init__(self,amogh,ameya,grandmother,grandfather,umbrella,mpp,time):
        #0 means left side of the river, 1 means right side of the river
        # amogh, ameya, grandmother, grandfather are the family members
        self.pos = {
            'amogh':      amogh,
            'ameya':      ameya,
            'grandmother': grandmother,
            'grandfather': grandfather
        }
        self.mpp = mpp  # mpp stands for the time taken by the each family member
        self.umbrella = umbrella
        self.time = time
    
    def goal_test(self):
        if (self.pos["amogh"] == 1 and 
            self.pos["ameya"] == 1 and 
            self.pos["grandmother"] == 1 and 
            self.pos["grandfather"] == 1 and 
            self.time >= 0):
            return True
        else:
            return False
        

    def move_gen(self):
        children=[]
        current_side = self.umbrella

        #who are in the current side of the umbrella
        here = [p for p, side in self.pos.items() if side == current_side]

        #if umbrella on the left side move 2 people to the right side

        if current_side == 0:
            for pair in combinations(here,2):
                #move 2 people to the right side
                cost=max(self.mpp[p] for p in pair)
                new_time=self.time-cost

                if new_time < 0:
                    continue
                
                new = State(
                    amogh      = 1 if 'amogh' in pair else self.pos['amogh'],
                    ameya      = 1 if 'ameya' in pair else self.pos['ameya'],
                    grandmother= 1 if 'grandmother' in pair else self.pos['grandmother'],
                    grandfather= 1 if 'grandfather' in pair else self.pos['grandfather'],
                    umbrella   = 1,
                    mpp        = self.mpp,
                    time       = new_time
                )
                children.append(new)
        else:
            #if umbrella on the right side move the one person to the left side of the bridge
            for person in here:
                cost=self.mpp[person]
                new_time=self.time-cost
                if new_time < 0:
                    continue
                new = State(
                    amogh      = 0 if person == 'amogh' else self.pos['amogh'],
                    ameya      = 0 if person == 'ameya' else self.pos['ameya'],
                    grandmother= 0 if person == 'grandmother' else self.pos['grandmother'],
                    grandfather= 0 if person == 'grandfather' else self.pos['grandfather'],
                    umbrella   = 0,
                    mpp        = self.mpp,
                    time       = new_time
                )
                children.append(new)
        return children
    
    def __eq__(self, other):
        return (
            self.pos        == other.pos and
            self.umbrella   == other.umbrella and
            self.time       == other.time
        )

    
    def __hash__(self):
        return hash((self.pos['amogh'], self.pos['ameya'], self.pos['grandmother'], self.pos['grandfather'], self.umbrella, self.time))
    
    def __str__(self):
        left=[p for p,s in self.pos.items() if s==0]
        right=[p for p,s in self.pos.items() if s==1]
        return f"Left: {left}, Right: {right}, Time left: {self.time}, Umbrella on: {'Left' if self.umbrella == 0 else 'Right'}"

def removeSeen(children,OPEN,CLOSED):
    #removes the children that are already in OPEN or CLOSED
    open_nodes  = [node for node, parent in OPEN]
    closed_nodes = [node for node, parent in CLOSED]
    new_nodes = [node for node in children if node not in open_nodes and node not in closed_nodes]
    return new_nodes

def reconstructPath(node_pair, CLOSED):
    parent_map = {} 
    for node, parent in CLOSED:
        parent_map[node] = parent    
    N, parent = node_pair
    path = [N]
    
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    
    path.reverse()
    print(" -> \n ".join([str(e) for e in path]))
    
    return path

def bfs(start):
    OPEN= [(start, None)]  # (node, parent)
    CLOSED = []  # (node, parent)

    while OPEN:
        node, parent = OPEN.pop(0)
        CLOSED.append((node, parent))

        if node.goal_test():
            print("Goal found!")
            return reconstructPath((node, parent), CLOSED)

        children = node.move_gen()
        children = removeSeen(children, OPEN, CLOSED)

        new_nodes = [(child, node) for child in children]

        OPEN=OPEN+new_nodes
    print("No solution.")
    return []

def dfs(start):
    OPEN= [(start, None)]  # (node, parent)
    CLOSED = []  # (node, parent)

    while OPEN:
        node, parent = OPEN.pop(0)
        CLOSED.append((node, parent))

        if node.goal_test():
            print("Goal found!")
            return reconstructPath((node, parent), CLOSED)

        children = node.move_gen()
        children = removeSeen(children, OPEN, CLOSED)

        new_nodes = [(child, node) for child in children]

        OPEN=new_nodes+OPEN
    print("No solution.")
    return []


if __name__ == "__main__":
   
    mpp = {
        'amogh':       5,
        'ameya':      10,
        'grandmother':20,
        'grandfather':25
    }

    start = State(0,0,0,0, umbrella=0, mpp=mpp, time=60)
    dfs(start)

    



