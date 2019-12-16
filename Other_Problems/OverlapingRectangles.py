class OverlappingRectangles:

    def __init__(self):
        pass

    @staticmethod
    def print_overlapping_coordinates(rectangle_a, rectangle_b):
        print("Right: {0}.".format(rectangle_a[2] > rectangle_b[0]))
        print("Left: {0}.".format(rectangle_a[0] < rectangle_b[2]))
        print("Top: {0}.".format(rectangle_a[3] > rectangle_b[1]))
        print("Bottom: {0}.".format(rectangle_a[1] < rectangle_b[3]))

        return (rectangle_a[2] > rectangle_b[0]) and \
               (rectangle_a[0] < rectangle_b[2]) and\
               (rectangle_a[3] > rectangle_b[1]) and\
               (rectangle_a[1] < rectangle_b[3])


objectOverlappingRectangles = OverlappingRectangles()
print(objectOverlappingRectangles.print_overlapping_coordinates([0, 0, 2, 2], [1, 1, 3, 3]))
print(objectOverlappingRectangles.print_overlapping_coordinates([0, 0, 0, 2], [1, 1, 3, 3]))
print(objectOverlappingRectangles.print_overlapping_coordinates([0, 0, 1, 1], [1, 0, 2, 1]))
print(objectOverlappingRectangles.print_overlapping_coordinates([5, 15, 8, 18], [0, 3, 7, 9]))

