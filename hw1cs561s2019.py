from copy import copy, deepcopy
distance = [1, 2 ,3]
def calculateRank(lines, border_size):
    #distance = [1, 2, 3]
    reference = []
    table = []

    #Copy the input table from lines
    for i in range(1, border_size+1 ):
        table.append([])
        for j in range(0, border_size):
            table[len(table)-1].append(lines[i][j])

    #Test the input table is right.
    #for row in table:
    #    for element in row:
    #        print element,
    #    print
    #print
    #Preprocessed the table
    table_reference = deepcopy(table) 
    for i in range(0, border_size):
        for j in range(0, border_size):
            if table_reference[i][j] == '1':
                for shift in distance:
                    if i+shift < border_size:
                        if table[i+shift][j] == '4':
                            continue
                        elif table[i+shift][j] == '3':
                            break
                        elif table[i+shift][j] == '2':
                            table[i+shift][j] = '4'
                        elif table[i+shift][j] == '1':
                            continue
                        else:
                            table[i+shift][j] = '1'
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0:
                        if table[i-shift][j] == '4':
                            continue
                        elif table[i-shift][j] == '3':
                            break
                        elif table[i-shift][j] == '2':
                            table[i-shift][j] = '4'
                        elif table[i-shift][j] == '1':
                            continue
                        else:
                            table[i-shift][j] = '1'
                    else:
                        break
                for shift in distance:
                    if j+shift < border_size:
                        if table[i][j+shift] == '4':
                            continue
                        elif table[i][j+shift] == '3':
                            break
                        elif table[i][j+shift] == '2':
                            table[i][j+shift] = '4'
                        elif table[i][j+shift] == '1':
                            continue
                        else:
                            table[i][j+shift] = '1'
                    else:
                        break
                for shift in distance:
                    if j-shift >= 0:
                        if table[i][j-shift] == '4':
                            continue
                        elif table[i][j-shift] == '3':
                            break
                        elif table[i][j-shift] == '2':
                            table[i][j-shift] = '4'
                        elif table[i][j-shift] == '1':
                            continue
                        else:
                            table[i][j-shift] = '1'
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j+shift < border_size:
                        if table[i+shift][j+shift] == '4':
                            continue
                        elif table[i+shift][j+shift] == '3':
                            break
                        elif table[i+shift][j+shift] == '2':
                            table[i+shift][j+shift] = '4'
                        elif table[i+shift][j+shift] == '1':
                            continue
                        else:
                            table[i+shift][j+shift] = '1'
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0  and j+shift < border_size:
                        if table[i-shift][j+shift] == '4':
                            continue
                        elif table[i-shift][j+shift] == '3':
                            break
                        elif table[i-shift][j+shift] == '2':
                            table[i-shift][j+shift] = '4'
                        elif table[i-shift][j+shift] == '1':
                            continue
                        else:
                            table[i-shift][j+shift] = '1'
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j-shift >= 0:
                        if table[i+shift][j-shift] == '4':
                            continue
                        elif table[i+shift][j-shift] == '3':
                            break
                        elif table[i+shift][j-shift] == '2':
                            table[i+shift][j-shift] = '4'
                        elif table[i+shift][j-shift] == '1':
                            continue
                        else:
                            table[i+shift][j-shift] = '1'
                    else:
                        break               
                for shift in distance:
                    if i-shift >= 0 and j-shift >= 0:
                        if table[i-shift][j-shift] == '4':
                            continue
                        elif table[i-shift][j-shift] == '3':
                            break
                        elif table[i-shift][j-shift] == '2':
                            table[i-shift][j-shift] = '4'
                        elif table[i-shift][j-shift] == '1':
                            continue
                        else:
                            table[i-shift][j-shift] = '1'
                    else:
                        break
            elif table_reference[i][j] == '2':
                for shift in distance:
                    if i+shift < border_size:
                        if table[i+shift][j] == '4':
                            continue
                        elif table[i+shift][j] == '3':
                            break
                        elif table[i+shift][j] == '2':
                            continue
                        elif table[i+shift][j] == '1':
                            table[i+shift][j] = '4'
                        else:
                            table[i+shift][j] = '2'
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0:
                        if table[i-shift][j] == '4':
                            continue
                        elif table[i-shift][j] == '3':
                            break
                        elif table[i-shift][j] == '2':
                            continue    
                        elif table[i-shift][j] == '1':
                            table[i-shift][j] = '4'
                        else:
                            table[i-shift][j] = '2'
                    else:
                        break
                for shift in distance:
                    if j+shift < border_size:
                        if table[i][j+shift] == '4':
                            continue
                        elif table[i][j+shift] == '3':
                            break
                        elif table[i][j+shift] == '2':
                            continue
                        elif table[i][j+shift] == '1':
                            table[i][j+shift] = '4'
                        else:
                            table[i][j+shift] = '2'
                    else:
                        break
                for shift in distance:
                    if j-shift >= 0:
                        if table[i][j-shift] == '4':
                            continue
                        elif table[i][j-shift] == '3':
                            break
                        elif table[i][j-shift] == '2':
                            continue
                        elif table[i][j-shift] == '1':
                            table[i][j-shift] = '4'
                        else:
                            table[i][j-shift] = '2'
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j+shift < border_size:
                        if table[i+shift][j+shift] == '4':
                            continue
                        elif table[i+shift][j+shift] == '3':
                            break
                        elif table[i+shift][j+shift] == '2':
                            continue
                        elif table[i+shift][j+shift] == '1':
                            table[i+shift][j+shift] = '4'
                        else:
                            table[i+shift][j+shift] = '2'
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0  and j+shift < border_size:
                        if table[i-shift][j+shift] == '4':
                            continue
                        elif table[i-shift][j+shift] == '3':
                            break
                        elif table[i-shift][j+shift] == '2':
                            continue
                        elif table[i-shift][j+shift] == '1':
                            table[i-shift][j+shift] = '4'
                        else:
                            table[i-shift][j+shift] = '2'
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j-shift >= 0:
                        if table[i+shift][j-shift] == '4':
                            continue
                        elif table[i+shift][j-shift] == '3':
                            break
                        elif table[i+shift][j-shift] == '2':
                            continue
                        elif table[i+shift][j-shift] == '1':
                            table[i+shift][j-shift] = '4'
                        else:
                            table[i+shift][j-shift] = '2'
                    else:
                        break               
                for shift in distance:
                    if i-shift >= 0 and j-shift >= 0:
                        if table[i-shift][j-shift] == '4':
                            continue
                        elif table[i-shift][j-shift] == '3':
                            break
                        elif table[i-shift][j-shift] == '2':
                            continue
                        elif table[i-shift][j-shift] == '1':
                            table[i-shift][j-shift] = '4'
                        else:
                            table[i-shift][j-shift] = '2'
                    else:
                        break


    #Test the input table is right.
    #for row in table:
    #    for element in row:
    #        print element,
    #    print
    #print

    for i in range(0, border_size):
        for j in range(0, border_size):

            if table[i][j] == '0':
                #Emitter location
                total = 1
                detail = [0, 0, 0]
                table_buffer = deepcopy(table)
                table_buffer[i][j] = 1
                for shift in distance:
                    if i+shift < border_size:
                        if table[i+shift][j] == '4':
                            continue
                        elif table[i+shift][j] == '3':
                            break
                        elif table[i+shift][j] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i+shift][j] = '4'
                        elif table[i+shift][j] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i+shift][j] = '1'
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0:
                        if table[i-shift][j] == '4':
                            continue
                        elif table[i-shift][j] == '3':
                            break
                        elif table[i-shift][j] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i-shift][j] = '4'
                        elif table[i-shift][j] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i-shift][j] = '1'
                    else:
                        break
                for shift in distance:
                    if j+shift < border_size:
                        if table[i][j+shift] == '4':
                            continue
                        elif table[i][j+shift] == '3':
                            break
                        elif table[i][j+shift] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i][j+shift] = '4'
                        elif table[i][j+shift] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i][j+shift] = '1'
                    else:
                        break
                for shift in distance:
                    if j-shift >= 0:
                        if table[i][j-shift] == '4':
                            continue
                        elif table[i][j-shift] == '3':
                            break
                        elif table[i][j-shift] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i][j-shift] = '4'
                        elif table[i][j-shift] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i][j-shift] = '1'
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j+shift < border_size:
                        if table[i+shift][j+shift] == '4':
                            continue
                        elif table[i+shift][j+shift] == '3':
                            break
                        elif table[i+shift][j+shift] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i+shift][j+shift] = '4'
                        elif table[i+shift][j+shift] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1  
                            table_buffer[i+shift][j+shift] = '1'
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0  and j+shift < border_size:
                        if table[i-shift][j+shift] == '4':
                            continue
                        elif table[i-shift][j+shift] == '3':
                            break
                        elif table[i-shift][j+shift] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i-shift][j+shift] = '4'
                        elif table[i-shift][j+shift] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i-shift][j+shift] = '1'
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j-shift >= 0:
                        if table[i+shift][j-shift] == '4':
                            continue
                        elif table[i+shift][j-shift] == '3':
                            break
                        elif table[i+shift][j-shift] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i+shift][j-shift] = '4'
                        elif table[i+shift][j-shift] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1 
                            table_buffer[i+shift][j-shift] = '1'
                    else:
                        break               
                for shift in distance:
                    if i-shift >= 0 and j-shift >= 0:
                        if table[i-shift][j-shift] == '4':
                            continue
                        elif table[i-shift][j-shift] == '3':
                            break
                        elif table[i-shift][j-shift] == '2':
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i-shift][j-shift] = '4'
                        elif table[i-shift][j-shift] == '1':
                            continue
                        else:
                            total = total + 1
                            detail[shift-1] = detail[shift-1] + 1
                            table_buffer[i-shift][j-shift] = '1'
                    else:
                        break
                temp = (total, detail, i, j, table_buffer)
                reference.append(temp)

    reference.sort(reverse=True)    
    return reference

def CalculateDif(table, score, current_max):
    #Record the max expanding area on res
    res = 0 
    border_size = len(table)
    for i in range(0, border_size):
        for j in range(0, border_size):
            if table[i][j] == '0':
                total = 1
                for shift in distance:
                    if i+shift < border_size:
                        if table[i+shift][j] == '4':
                            continue
                        elif table[i+shift][j] == '3':
                            break
                        elif table[i+shift][j] == '1':
                            total = total + 1
                        elif table[i+shift][j] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0:
                        if table[i-shift][j] == '4':
                            continue
                        elif table[i-shift][j] == '3':
                            break
                        elif table[i-shift][j] == '1':
                            total = total + 1
                        elif table[i-shift][j] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                for shift in distance:
                    if j+shift < border_size:
                        if table[i][j+shift] == '4':
                            continue
                        elif table[i][j+shift] == '3':
                            break
                        elif table[i][j+shift] == '1':
                            total = total + 1
                        elif table[i][j+shift] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                for shift in distance:
                    if j-shift >= 0:
                        if table[i][j-shift] == '4':
                            continue
                        elif table[i][j-shift] == '3':
                            break
                        elif table[i][j-shift] == '1':
                            total = total + 1
                        elif table[i][j-shift] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j+shift < border_size:
                        if table[i+shift][j+shift] == '4':
                            continue
                        elif table[i+shift][j+shift] == '3':
                            break
                        elif table[i+shift][j+shift] == '1':
                            total = total + 1
                        elif table[i+shift][j+shift] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                for shift in distance:
                    if i-shift >= 0  and j+shift < border_size:
                        if table[i-shift][j+shift] == '4':
                            continue
                        elif table[i-shift][j+shift] == '3':
                            break
                        elif table[i-shift][j+shift] == '1':
                            total = total + 1
                        elif table[i-shift][j+shift] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                for shift in distance:
                    if i+shift < border_size and j-shift >= 0:
                        if table[i+shift][j-shift] == '4':
                            continue
                        elif table[i+shift][j-shift] == '3':
                            break
                        elif table[i+shift][j-shift] == '1':
                            total = total + 1
                        elif table[i+shift][j-shift] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break               
                for shift in distance:
                    if i-shift >= 0 and j-shift >= 0:
                        if table[i-shift][j-shift] == '4':
                            continue
                        elif table[i-shift][j-shift] == '3':
                            break
                        elif table[i-shift][j-shift] == '1':
                            total = total + 1
                        elif table[i-shift][j-shift] == '2':
                            continue
                        else:
                            total = total + 1
                    else:
                        break
                #print '-----'
                #print current_max
                #print i, j
                #for row in table:
                #    for element in row:
                #        print element,
                #    print
                #print score, total
                #print '-----'
                if score - total < current_max:
                    return -1
                if total > res:
                    res = total
    return res

def main():
    f = open("output.txt", "w")
    lines = open("input.txt").read().splitlines()
    reference = calculateRank(lines, int(lines[0]))
   
    current_max = -1
    current_locate = (-1, -1)
    if len(reference) > 0:
        for element in reference:
            if element[0] > current_max:
                opponentmax = CalculateDif(element[4], element[0], current_max)
                if opponentmax != -1:
                    if element[0] - opponentmax > current_max:
                        current_max = element[0] - opponentmax
                        current_locate = (element[2], element[3])
                        
    if current_max != -1:
        #print current_max
        #print current_locate[0], current_locate[1]
        result = str(current_locate[0]) + " " + str(current_locate[1])
        print result
        f.write(current_locate[0])
        f.write(' ')
        f.write(current_locate[1])
    else:
        print "No place to put the queen"


if __name__ == '__main__':
    main()
