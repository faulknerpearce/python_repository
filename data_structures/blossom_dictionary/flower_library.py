from hashmap import HashMap

#________Main Program_________ # 
if __name__ == "__main__":

    flower_definitions = [['begonia', 'cautiousness'], 
                        ['chrysanthemum', 'cheerfulness'], 
                        ['carnation', 'memories'], ['daisy', 'innocence'], 
                        ['hyacinth', 'playfulness'], ['lavender', 'devotion'], 
                        ['magnolia', 'dignity'], ['morning glory', 'unrequited love'], 
                        ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], 
                        ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]

    blossom = HashMap(len(flower_definitions))

    for flower in flower_definitions:
        blossom.assign(flower[0], flower[1])

    print(blossom.retrieve('daisy'))