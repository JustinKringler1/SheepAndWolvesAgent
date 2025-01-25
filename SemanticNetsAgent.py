"""
File Name: SemanticNetsAgent.py
Aurthor: Justin Kringler
Last Updated: 1/24/2025

Description: Contains Function for solving mini project 1 for CS7637.

Problem: You are a shepherd tasked with getting sheep and wolves across a river for some reason. 
         If the wolves ever outnumber the sheep on either side of the river, the wolves will overpower
         and eat the sheep. You have a boat, which can only take one or two animals in it at a time,
         and must have at least one animal in it because you’ll get lonely (and because the problem
         is trivial otherwise). How do you move all the animals from one side of the river to the other?

Notes: The solve function is called from the main.py script to test out script. 

"""


##### Loading Modules -----

from collections import deque


##### SemanticNetsAgent Class -----

class SemanticNetsAgent:

    ### Solve Function ---

    def solve(self, sheep, wolves):
        # Initial state
        start_state = (sheep, wolves, 0)  # All animals on the left, boat on the left
        goal_state = (0, 0, 1)           # All animals on the right, boat on the right

        # Moves: (sheep_to_move, wolves_to_move)
        possible_moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

        # BFS queue: stores tuples of (current_state, path)
        queue = deque([(start_state, [])])
        visited = set()

        while queue:
            current_state, path = queue.popleft()

            # Unpack current state
            sheep_left, wolves_left, boat_position = current_state
            sheep_right = sheep - sheep_left
            wolves_right = wolves - wolves_left

            # Check if we reached the goal
            if current_state == goal_state:
                return path

            # Skip visited states
            if current_state in visited:
                continue
            visited.add(current_state)

            # Generate valid moves
            for move in possible_moves:
                sheep_to_move, wolves_to_move = move

                # Determine the new state based on the boat's position
                if boat_position == 0:  # Boat on the left
                    new_sheep_left = sheep_left - sheep_to_move
                    new_wolves_left = wolves_left - wolves_to_move
                    new_sheep_right = sheep_right + sheep_to_move
                    new_wolves_right = wolves_right + wolves_to_move
                    new_boat_position = 1
                else:  # Boat on the right
                    new_sheep_left = sheep_left + sheep_to_move
                    new_wolves_left = wolves_left + wolves_to_move
                    new_sheep_right = sheep_right - sheep_to_move
                    new_wolves_right = wolves_right - wolves_to_move
                    new_boat_position = 0

                # Check validity of the new state
                if (
                    0 <= new_sheep_left <= sheep
                    and 0 <= new_wolves_left <= wolves
                    and 0 <= new_sheep_right <= sheep
                    and 0 <= new_wolves_right <= wolves
                    and (new_sheep_left == 0 or new_sheep_left >= new_wolves_left)
                    and (new_sheep_right == 0 or new_sheep_right >= new_wolves_right)
                ):
                    new_state = (new_sheep_left, new_wolves_left, new_boat_position)
                    queue.append((new_state, path + [move]))

        # Return an empty list if no solution is found
        return []

