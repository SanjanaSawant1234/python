colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)
