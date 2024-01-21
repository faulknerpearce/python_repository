# Restaurant Explorer

Restaurant Explorer is a Python script that simulates an interactive application for exploring restaurants based on different categories. Users can traverse a tree structure to discover various types of food and specific restaurant details.

## Features

- Interactive tree traversal for exploring restaurant categories and choices.
- Information display for each restaurant, including price, rating, and address.
- User-friendly interface with delayed printing for a smoother user experience.

## Functions

`delayed_print(text, delay)`

- Prints text with a delayed effect for improved user interaction.

`delayed_input(text)`

-Prints text with a delayed effect for improved user interaction and takes user input.

`create_tree_with_categories(categories)`

- Creates a tree with a root node and adds categories as child nodes.

- Provides user input with a delayed printing effect for a more enjoyable experience.

`add_restaurants_to_categories(restaurants_tree, restaurant_selection)`

- Adds restaurant nodes to the existing tree under their respective categories.

## Classes and Methods

### `TreeNode`

Represents a node in the tree structure, specifically designed for restaurants. It includes methods for adding and removing child nodes, breadth-first search, and traversal.

#### Methods:

- `add_child()`: Adds a child node to the current node.
- `remove_child()`: Removes a child node from the current node.
- `find_by_name()`: Performs a breadth-first search to find a child node by name.
- `add_child_to_found_parent()`: Finds the parent node by name and adds the child to it.
- `print_node_information()`: Prints information about the node or a list of children's names.
- `traverse()`: Traverses the tree in a breadth-first manner, providing an interactive experience for restaurant exploration.

## Usage

Explore the script interactively to discover and learn about various restaurants. Utilize the delayed printing effect to enhance the user experience.
