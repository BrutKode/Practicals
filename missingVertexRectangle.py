#Finding coordinates of missing vertex of rectangle
x1, y1 = map(int, input("Enter the coordinates of first vertex seperated by spaces: ").split())
x2, y2 = map(int, input("Enter the coordinates of second vertex seperated by spaces: ").split())
x3, y3 = map(int, input("Enter the coordinates of third vertex seperated by spaces: ").split())

#Since rectangle is parallel to the axes, the unlike value will be the one of missing vertex
if x1 == x2:
    x4 = x3
elif x2 == x3:
    x4 = x1
else:
    x4 = x2
if y1 == y2:
    y4 = y3
elif y2 == y3:
    y4 = y1
else:
    y4 = y2

print(f"The coordinates of the fourth vertex are ({x4}, {y4})")