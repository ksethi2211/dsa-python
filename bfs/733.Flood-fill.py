class Solution:
    def getNeighbors(self, row: int, col: int, num_rows: int, num_cols: int) -> List[List[int]]:
        neighbors = [
            [row - 1, col],
            [row + 1, col],
            [row, col - 1],
            [row, col + 1],
        ]

        filtered_neighbors = []
        for neighbor in neighbors:
            if neighbor[0] >= 0 and neighbor[0] < num_rows and neighbor[1] >= 0 and neighbor[1] < num_cols:
                filtered_neighbors.append(neighbor)
        
        return filtered_neighbors

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        position_que = deque()
        position_que.append([sr, sc])
        visited = set()
        og_color = image[sr][sc]
        num_rows = len(image)
        num_cols = len(image[0])

        while len(position_que):
            current_node = position_que.popleft()
            image[current_node[0]][current_node[1]] = color
            neighbors = self.getNeighbors(current_node[0], current_node[1], num_rows, num_cols)
            for neighbor in neighbors:
                lookup_str = f"{neighbor[0]}:{neighbor[1]}"
                if image[neighbor[0]][neighbor[1]] == og_color and not lookup_str in visited:
                    visited.add(lookup_str)
                    position_que.append(neighbor)
        
        return image