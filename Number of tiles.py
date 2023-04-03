l_tiles = int(input("Enter the length of tiles: "))
b_tiles = int(input("Enter the breath of tiles: "))
l = int(input("Enter the length of floor: "))
b = int(input("Enter the breath of floor: "))
area_tile = l_tiles*b_tiles
area_floor = l*b
print("Number of tiles = ", area_floor//area_tile)
