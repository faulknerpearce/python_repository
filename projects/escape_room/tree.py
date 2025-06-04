
class TreeNode:
  #Initializes a new instance of a tree node with a given value. 
  def __init__(self, story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, child):
    self.choices.append(child)

  def traverse(self):
    story_node = self
    print(story_node.story_piece)

    while len(story_node.choices) > 0:

      choice = input("Enter 1 or 2 to continue the story: ")

      if choice not in ['1', '2']: 
        print('\nInvalid choice. Try again. ')

      else:
        choice_index = int(choice) -1
      
        chosen_child = story_node.choices[choice_index]

        print(chosen_child.story_piece)

        story_node = chosen_child