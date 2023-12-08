from tree import TreeNode
from restaurant_data import my_categories, my_restaurants

# Create a tree with a root node and add categories as child nodes.
def create_tree_with_categories(categories):
    root_node = TreeNode('Root', '\nWelcome to the application. Please select a type of food you would like to eat.\n\nThe types of food available are:\n')

    for name in categories:
        food_type = TreeNode(name, '\nYour available restaurant choices are:')
        root_node.add_child(food_type)
    return root_node

# Add restaurant nodes to the existing tree under their respective categories.
def add_restaurants_to_categories(restaurants_tree, restaurant_selection):
    for restaurant in restaurant_selection:
        category = restaurant[0]
        name = restaurant[1]
        information = restaurant[2:]
        
        new_restaurant = TreeNode(name, '\nThe information about your selected restaurant is:', information)
        restaurants_tree.add_child_to_found_parent(category, new_restaurant)
    return restaurants_tree

# ________Main Program_________ #
my_tree = create_tree_with_categories(my_categories)

my_restaurant_tree = add_restaurants_to_categories(my_tree, my_restaurants)

my_restaurant_tree.traverse()








