def coordinate_permutation(x, y, z, n):
    """Returns a list of the permutations of x, y, z

    It is given three integers x, y, and z, representing a cuboid's dimensions 
    and an integer n. The function returns a list of all  possible coordinates 
    given by (i, j, k) on 3D grid where the sum of i + j + k is not equal to n.
    The list of coordinates is sorted lexicographic increasing order.

    Args:
        x :  
        y :
        z :

    Returns:
        
    """

    # generate all coordinates for cuboid.
    coordinates = [[xx, yy, zz] for zz in range(z + 1) \
            for yy in range(y + 1) \
            for xx in range(x + 1)]

    # filter out coordinates whose the sum of x, y, and z is less than n. 
    coordinates = [coordinate for coordinate in coordinates if sum(coordinate) < n]

    # sort the list in lexograhic increasing order.
    return sorted(coordinates)

if __name__ = '__main__':
    print(coordinate_permutation(1, 1, 1, 2))
