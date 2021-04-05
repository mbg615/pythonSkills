
List = [1, 0, 1, 0]
i = 0
while i < len(List):
    if List[i] == 0:
        List[i] = 1 # Changes 0 to 1
    if List[i] == 1:
        List[i] = 0 # Changes 1 to 0
    i += 1
print(List)
