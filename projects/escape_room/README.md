# Enigma Escape Room

Enigma Escape Room is a text-based adventure game where the player must solve puzzles and make choices to escape a mysterious room. The story unfolds through a branching narrative, and the player's decisions determine their fate.

## Features

- Interactive, text-based story with multiple endings
- Branching narrative based on player choices
- Puzzle-solving elements and hidden clues
- Simple tree structure for story progression

## Classes and Functions

### TreeNode Class

The `TreeNode` class represents a node in the story tree, with the following attributes:

- `story_segment`: The text displayed to the player at this point in the story
- `children`: A list of child nodes representing possible choices

Methods:

- `add_child(child_node)`: Adds a child node to the current node
- `traverse()`: Traverses the story tree, prompting the player for choices and displaying story segments

### Main Script

- Defines the story structure using `TreeNode` objects for each segment and choice
- Connects nodes to create a branching narrative
- Starts the game by calling `story_root.traverse()`

The main game loop is handled by the `traverse()` method of the root node, guiding the player through the escape room adventure based on their choices.
