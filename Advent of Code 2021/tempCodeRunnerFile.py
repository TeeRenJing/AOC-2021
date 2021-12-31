def relax_all_four_corners(coord:tuple,inputdict:dict):
    if (coord[0]-1,coord[1]) in inputdict:
        if inputdict[coord[current_lowest_cost_from_start]] + inputdict[]
            inputdict[(coord[0]-1,coord[1])] += 1

    if (coord[0]+1,coord[1]) in inputdict: 
        if inputdict[(coord[0],coord[1]-1)] != 0:
            inputdict[(coord[0],coord[1]-1)] += 1

    if (coord[0],coord[1]+1) in inputdict:
        if inputdict[(coord[0],coord[1]+1)] != 0:
            inputdict[(coord[0],coord[1]+1)] += 1

    if (coord[0],coord[1]-1) in inputdict:
        if inputdict[(coord[0]+1,coord[1]-1)] != 0:
            inputdict[(coord[0]+1,coord[1]-1)] += 1