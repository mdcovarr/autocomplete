"""
    Example building a Segment tree
"""
from math import ceil, log2


def get_mid(s, e):
    return s + (e - s) // 2


def construct_st_util(arr, ss, se, st, si):
    """
        A recursive function that constructs
        Segment Tree for array [ss.. se].
        si is index of current node in segment tree
        st
    """
    """
        If there is one element in array,
        store it in current node of
        segment tree and return
    """
    if (ss == se):
        st[si] = arr[ss]
        return arr[ss]

    """
        If there are more than one elements,
        then recur for left and right subtrees
        and store the sum of values in this node
    """
    mid = get_mid(ss, se)

    left_max = construct_st_util(arr, ss, mid, st, si * 2 + 1)
    right_max = construct_st_util(arr, mid + 1, se, st, si * 2 + 2)

    if left_max > right_max:
        st[si] = left_max
    else:
        st[si] = right_max

    return st[si]


def construct_st(arr, n):
    # Height of segment tree
    x = (int)(ceil(log2(n)))
    # Maximum size of segment tree
    max_size = 2 * (int)(2 ** x) - 1
    # Allocate memory
    st = [None] * max_size
    # Fill the allocated memory st
    construct_st_util(arr, 0, n - 1, st, 0)

    # Return the constructed segment tree
    return st


def main():
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)

    # Build segment tree
    st = construct_st(arr, n)

    print(st)



if __name__ == "__main__":
    main()

    """
                 36
            9          27
         4    5     16    11
       1  3        7  9



                11
          5           11
        3   5       9    11
      1  3         7 9
    """