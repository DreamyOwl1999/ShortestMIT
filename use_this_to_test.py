import ps2

map_filename = "mit_map.txt"

print("Hello kiffa")
print('')
digraph = ps2.load_map(map_filename)

start = int(input("Where do you want to start on the map: "))
end = int(input("Where will you go on the map: "))
max_dist_outdoors = int(input("How much are you willing to walk outside: "))

print('')

print('The best path is: ')
print(ps2.directed_dfs(digraph, start, end, 0, max_dist_outdoors))


