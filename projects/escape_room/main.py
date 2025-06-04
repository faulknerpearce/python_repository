from tree import TreeNode

story_root = TreeNode("""\nWelcome to the enigmatic Enigma Escape Room. Dim light reveals a door to your left. Suddenly, an electronic voice echoes, 'Solve or stay trapped forever.'\n\nChoose: 1. Decode the mysterious cipher on the wall. 2. Proceed through the door and explore.\n""")

choice_a = TreeNode("""\nCracking the cipher triggers a mechanism, revealing a hidden passage. The voice commends your decoding skills.\n\nOptions: 1. Express gratitude. 2. Proceed through the revealed passage.\n""")

choice_b = TreeNode("""\nVenturing into a room with intricate locks, you find a key. The voice suggests its connection to the cipher.\n\nOptions: 1. Ask about the key's purpose. 2. Examine the locks more closely.\n""")

# Story Ends for A1 Here. 
choice_a_1 = TreeNode("""\nThe voice congratulates you on unlocking the mystery. The passage leads to freedom.\n\nESCAPE SUCCESSFUL!.\n""")

# Story ends for A2 Here. 
choice_a_2 = TreeNode("""\nYou trigger a mechanism, sealing the exit. You are trapped in the escape room with with no way out.\n\nESCAPE UNSUCCESSFUL.\n""")

choice_b_1 = TreeNode("""\nAsking the mysterious voice about the key's purpose yields a cryptic clue. Deciphering the code, you input it into the panel. The code was incorrect, the voice lied to you. The door seals shut.\n\nESCAPE UNSUCCESSFUL.\n""")

choice_b_2 = TreeNode("""\nFinding a hidden compartment, you discover another mysterious object. Proceeding with the newfound key, the door swings open, unveiling a new passageway. You step through, successfully escaping the room.\n\nCONGRATULATIONS!\n""")

# Creating the objects and adding the children nodes. 
story_root.add_child(choice_a)

story_root.add_child(choice_b)

choice_a.add_child(choice_a_1)

choice_a.add_child(choice_a_2)

choice_b.add_child(choice_b_1)

choice_b.add_child(choice_b_2)

# The game. 
story_root.traverse()  