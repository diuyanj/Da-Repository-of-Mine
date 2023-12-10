def removeIslands(matrix):
    # 1 -> black
    # 2 -> white
    
    land = {}

    # size of edges
    edges = {"Top": matrix[0],
             "Left": [i[0] for i in matrix],
             "Right": [i[-1:][0] for i in matrix],
             "Bottom": matrix[-1:][0]
             }
    edgeSize = {
             "Top": len(edges["Top"]),
             "Left": len(edges["Left"]),
             "Right": len(edges["Right"]),
             "Bottom": len(edges["Bottom"])
             }
    # could be better
    # for i in edgeSize.keys():
    #     print(f"edge {i} = {edgeSize[i]}")
    # print(matrix[-1:][0])
    # for edge in edges.keys():
    #     if len(edges[edge]) <= 2:
    #         return print("No Islands")
    
    for edge in edges.keys():
        if edge == "Top":
            index = 0
            for i in edges[edge]:
                if i == 1:
                    land[(0, index)] = True
                index += 1
            index = 0
        if edge == "Left":
            index = 0
            for i in edges[edge]:
                if i == 1:
                    land[(index, 0)] = True
                index += 1
        if edge == "Right":
            index = 0
            for i in edges[edge]:
                if i == 1:
                    land[(index, edgeSize["Top"]-1)] = True
                index += 1
        if edge == "Bottom":
            index = 0
            for i in edges[edge]:
                if i == 1:
                    land[(edgeSize["Left"]-1), index] = True
                index += 1
    
    _row = 1
    index = 0
    # Scan center area
    for r in range(1, edgeSize["Left"]-1):
        print(f"r={r}")
        for c in matrix[r]:
            if index != 0 and index != len(matrix[r])-1:
                if matrix[r][index] == 1:
                    print(r,index)
                    # Scan area surrounding a discovered '1'
                    # north                 # south                # east                 # west
                    if (r-1,index) in land or (r+1,index) in land or (r,index-1) in land or (r,index+1) in land:
                        land[r, index] = True
                    # Dont know how to do this part
                    # problem is im scanning top to bottom but oh well
                    else: matrix[r][index] = 0
            index += 1
        index = 0
        
    for i in matrix: print(i)



islands = [
    [0,1,1,0],
    [0,0,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,0]
]

removeIslands(islands)