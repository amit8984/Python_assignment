#python program for 3D with dimension 3*5*8


def three_D(col1,col2,row1):
    threeD_array=[[ [0 for col in range(col1)]for col in range(col2)]for row in range(row1)]
    print(threeD_array)

if __name__=='__main__':
    three_D(3,5,8)


