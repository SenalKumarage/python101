## Lists []

#### append(value)
This will add an element to the end of the list

#### insert(index, value)
This will free space on the provided index and shift other elements right

#### del list[index]
This can remove an element from your list if you know the index

#### pop(index?)
This will remove the last item or the item of the provided index and return them

#### sort(reverse=True?)
This will sort the values of the list

#### sorted(reverse=True)
This will just sort the elements but wont change the original list

#### reverse()
This will just reverse the order of the list (it wont sort alphabetically).
And it will change the order of the list

#### len(list)
This will return the length of the list

#### Getting the last element of the list
`list(-1)`

#### Basic statistics min(L), max(L), sum(L)

#### Slicing
- `players[1:4]` This will give `players[1]`, `players[2]`, `players[3]`

- `players[:4]` If the first index wasn't there python will start it from the beginning.

- `players[2:]` This will give all the elements starting from the given element index

- `players[-3:]` This will return the last 3 players of the list

#### Copying a list
`new_players = players[:]`