from loadingMaps import load_map

from typing import List

#when given a current map in UI, prints map and players progress without showing path or solution to the game (prints '0' and '7')
def print_map(map):
   player_map = []

   for i in map:
       f = []
       for l in i:
           if l == 0 or l ==7:
               f.append(l)
           else:
               f.append(0)
       player_map.append(f)
   return player_map

#print(print_map(input()))
#
# def print_map(i)->List[int]:
#     m = []
#     if 'print' and 'map1' in i:
#         m = load_map('map1.txt')
#     else:
#         m = []
#     return m
#
# print(print_map("print map1"))