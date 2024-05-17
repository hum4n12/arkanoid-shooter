class Node:

    def __init__(self, position: tuple[int, int], g_cost: int, h_cost: int) -> None:
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.connection: 'Node' = None
    
    @property
    def f_cost(self) -> int:
        return self.g_cost + self.h_cost

class AStarFinder:

    def __init__(self) -> None:
        self.start_point: tuple[int, int] = (0, 0)
        self.end_point: tuple[int, int] = (0, 0)

    def calculate_cost(self, p1: tuple[int, int], p2: tuple[int, int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def create_node(self, position: tuple[int, int]) -> Node:
        g_cost = self.calculate_cost(self.start_point, position)
        h_cost = self.calculate_cost(position, self.end_point)
        return Node(position, g_cost, h_cost)

    def calculate_neighbours(self, pos: tuple[int, int]) -> set[tuple[int, int]]:
        neighbors: set[tuple[int, int]] = []
        neighbors.append((pos[0], pos[1] - 1))
        neighbors.append((pos[0] - 1, pos[1]))
        neighbors.append((pos[0] + 1, pos[1]))
        neighbors.append((pos[0], pos[1] + 1))
        neighbors.append((pos[0] - 1, pos[1] - 1))
        neighbors.append((pos[0] + 1, pos[1] - 1))
        neighbors.append((pos[0] - 1, pos[1] + 1))
        neighbors.append((pos[0] + 1, pos[1] + 1))
        return neighbors

    def find_path(self, start_point: tuple[int, int], end_point: tuple[int, int], map: dict[tuple[int, int], int]) -> list[tuple[int, int]]:
        self.start_point = start_point
        self.end_point = end_point
        start: Node = self.create_node(start_point)
        to_search: dict[tuple[int, int], Node] = {start.position: start}
        processed: dict[tuple[int, int], Node] = {}

        while len(to_search) > 0:
            current: Node = None
            for node in to_search.values():
                if current is None or node.f_cost < current.f_cost:
                    current = node
                    continue

                if node.f_cost == current.f_cost:
                    if node.h_cost < current.h_cost:
                        current = node 

            to_search.pop(current.position)
            processed[current.position] = current

            if current.position == self.end_point:
                path: list[tuple[int, int]] = []
                while current.position != self.start_point:
                    path.append(current.position)
                    current = current.connection

                path.append(self.start_point)
                return path

            for n in self.calculate_neighbours(current.position):
                if n not in map or map[n] == 0:
                    continue

                if current.position[0] != n[0] and current.position[1] != n[1]:
                    if map[(current.position[0], n[1])] == 0 or map[(n[0], current.position[1])] == 0:
                        continue

                neighbour: Node = None
                in_search = False

                if n in processed:
                    continue
                
                if n in to_search:
                    neighbour = to_search[n]
                    in_search = True
                else:
                    neighbour = self.create_node(n)

                distance_to_neighbour = current.g_cost + self.calculate_cost(current.position, neighbour.position)

                if not in_search or distance_to_neighbour < neighbour.g_cost:
                    neighbour.g_cost = distance_to_neighbour
                    neighbour.connection = current

                    if not in_search:
                        to_search[n] = neighbour
        
        return []