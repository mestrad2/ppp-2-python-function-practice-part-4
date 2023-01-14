pascal_tri = [[1], [1,1]]

def pascal(n):
    if n < 1:
        print("not enough rows")
    elif n == 1:
        print(pascal_tri[0])
    else:
        row_selected = 2
        while len(pascal_tri) < n:
            temp_row = []
            temp_row_before = pascal_tri[row_selected - 1]
            length = len(temp_row_before) + 1
            for i in range(length):
                if i == 0:
                    temp_row.append(1)
                elif i > 0 and i < length-1:
                    temp_row.append(pascal_tri[row_selected-1][i-1]+pascal_tri[row_selected-1][i])
                else:
                    temp_row.append(1)
            pascal_tri.append(temp_row)
            row_selected += 1
        
        for temp_row in pascal_tri:
            print(temp_row)


pascal(10)
