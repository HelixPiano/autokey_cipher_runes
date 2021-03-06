import numpy as np


def get_divinity_text():
    return np.array(
        [1, 28, 21, 15, 12, 0, 5, 4, 12, 1, 6, 13, 28, 28, 0, 7, 14, 16, 5, 20, 28, 26, 19, 28, 12, 16, 5, 9, 25, 21,
         19, 27, 27, 19, 19, 7, 25, 13, 23, 21, 27, 4, 3, 28, 27, 19, 10, 0, 0, 18, 1, 21, 12, 1, 25, 26, 13, 4, 25, 10,
         13, 25, 5, 25, 25, 9, 7, 17, 14, 19, 23, 4, 27, 10, 0, 13, 5, 12, 12, 25, 5, 4, 2, 13, 0, 11, 19, 3, 12, 5, 7,
         27, 17, 25, 7, 17, 28, 20, 15, 4, 26, 11, 25, 4, 19, 5, 2, 12, 25, 16, 5, 13, 7, 19, 6, 12, 5, 21, 13, 1, 12,
         5, 4, 18, 7, 27, 13, 10, 17, 26, 17, 14, 0, 20, 10, 4, 4, 19, 5, 6, 17, 26, 4, 5, 0, 1, 2, 13, 27, 11, 7, 16,
         0, 28, 11, 6, 17, 25, 2, 0, 0, 28, 13, 2, 13, 0, 24, 14, 11, 19, 18, 13, 21, 15, 3, 15, 19, 7, 12, 11, 20, 7,
         14, 1, 2, 25, 7, 19, 2, 23, 26, 11, 5, 15, 27, 14, 3, 21, 4, 19, 17, 7, 4, 19, 10, 23, 26, 11, 5, 14, 8, 1, 26,
         13, 20, 11, 21, 26, 19, 0, 11, 13, 12, 1, 27, 7, 12, 11, 23, 7, 14, 1, 24, 20, 24, 15, 19, 27, 12, 14, 25, 19,
         27, 19, 10, 13, 26, 25, 19, 1, 0])


def get_cross_text():
    return np.array([15, 8, 18, 3, 6, 19, 27, 0, 15, 26, 18, 21, 5, 2, 11, 6, 25, 0, 11, 22,
                     3, 9, 2, 9, 18, 7, 17, 24, 15, 22, 12, 10, 21, 1, 9, 25, 6, 10, 2, 8, 17, 9, 27,
                     13, 17, 9, 12, 11, 2, 24, 21, 26, 14, 17, 23, 13, 18, 27, 0, 14, 6, 0,
                     15, 13, 16, 0, 13, 1, 21, 26, 21, 14, 27, 26, 8, 17, 1, 6, 3, 13, 21, 25, 2, 10,
                     25, 8, 14, 2, 13, 6, 26, 0, 21, 5, 11, 2, 24, 19, 10, 21, 10, 27, 26, 8, 12, 16, 8, 25,
                     27, 14, 26, 18, 1, 21, 5, 0, 9, 12, 2, 11, 10, 2, 2, 13, 26, 21, 28, 26, 9,
                     18, 26, 23, 14, 21, 7, 17, 5, 14, 23, 17, 0, 19, 16, 9, 18, 28, 11, 9, 20, 6,
                     17, 14, 6, 2, 26, 10, 23, 24, 21, 6, 19, 11, 4, 3, 20, 12, 26, 16, 13, 10, 2, 23, 11,
                     22, 8, 20, 28, 0, 14, 25, 13, 6, 14, 0, 20, 7, 12, 16, 25, 0, 6, 9, 19, 12, 20, 9,
                     21, 19, 0, 4, 27, 24, 15, 28, 19, 21, 14, 14, 12, 23, 17, 22, 23, 19, 3, 28,
                     12, 8, 23, 21, 6, 22, 21, 20, 1, 4, 9, 16, 25, 15, 26, 1, 8, 4, 16, 8, 5, 15, 22,
                     16, 22, 21, 1, 4, 15, 0, 3, 18, 7, 28, 22, 20, 0, 25, 19, 4, 21, 23, 24, 19, 4, 7])


def get_spirals_text():
    return np.array([20, 11, 12, 8, 21, 5, 2, 16, 25, 11, 16, 14, 8, 16, 1, 22, 15, 13, 4, 6,
                     26, 9, 24, 6, 12, 21, 9, 7, 0, 26, 9, 17, 28, 27, 13, 9, 26, 24, 15, 19,
                     17, 27, 28, 27, 10, 3, 17, 4, 9, 20, 28, 4, 20, 20, 18, 17, 7, 9, 8, 19, 0,
                     22, 17, 21, 4, 24, 27, 6, 22, 12, 16, 19, 14, 23, 12, 19, 26, 8, 28, 10, 20, 15, 9,
                     7, 5, 0, 13, 19, 13, 20, 28, 15, 2, 0, 22, 27, 2, 18, 26, 5, 11, 20, 5, 27, 19,
                     17, 23, 5, 12, 11, 10, 16, 22, 23, 28, 18, 27, 9, 16,
                     13, 23, 2, 12, 23, 12, 25, 20, 5, 27, 12, 28, 8, 7, 19, 26, 2,
                     1, 8, 16, 2, 4, 8, 21, 20, 21, 15, 9, 25, 28, 6, 15, 20, 15, 14,
                     3, 8, 7, 23, 19, 18, 19, 24, 0, 5, 26, 5, 25, 9, 16, 2, 6, 10, 11, 10,
                     5, 23, 27, 14, 8, 25, 25, 28, 6, 28, 21, 0, 16, 3, 4, 23, 5, 12, 0, 1,
                     14, 28, 17, 3, 14, 10, 26, 6, 15, 15, 17, 28, 3, 10, 13, 10, 11, 10, 3, 18, 8, 28, 8])


def get_branches_text():
    return np.array([14, 10, 14, 19, 1, 14, 19, 5, 2, 13, 3, 17, 27, 9, 16, 28, 14,
                     13, 4, 26, 3, 5, 28, 19, 21, 6, 14, 20, 1, 21, 10, 16, 3,
                     11, 0, 21, 15, 20, 9, 23, 3, 19, 12, 25, 4, 23, 7, 16, 11, 2,
                     26, 2, 15, 25, 26, 18, 15, 14, 22, 17, 28, 4, 12, 13, 21, 1, 13, 3, 2, 14, 24, 8,
                     22, 4, 21, 1, 18, 4, 26, 20, 14, 20, 27, 20, 4, 13, 7, 12, 9, 28, 24, 4, 14, 21,
                     26, 15, 8, 1, 20, 15, 26, 6, 9, 1, 12, 25, 9, 9, 3, 25, 18, 23, 24, 3, 11, 27, 1,
                     24, 14, 4, 14, 27, 22, 11, 19, 10, 12, 20, 28, 8, 2, 19, 28, 26, 6, 17, 5, 13,
                     14, 5, 9, 22, 22, 15, 6, 19, 13, 18, 16, 20, 9, 11, 11, 5, 21, 3, 10, 7, 20, 28, 17,
                     0, 24, 18, 16, 21, 9, 13, 28, 3, 16, 2, 8, 21, 14, 13, 8, 13, 5, 13, 4, 1, 20,
                     0, 18, 22, 6, 24, 17, 0, 10, 25, 0, 1, 22, 19, 0, 26, 21, 11, 5, 8, 16, 0, 20, 25, 18,
                     2, 15, 20, 3, 1, 25, 3, 24, 19, 22, 1, 7, 12, 17, 9, 15, 20, 21, 11, 22, 9, 19, 20, 17,
                     22, 16, 9, 23, 17, 3, 9, 2, 27, 8, 22, 4, 13, 9, 0, 13, 23, 15, 3, 10, 28, 26, 9, 12])


def get_mobius_text():
    return np.array([0, 1, 20, 19, 24, 28, 26, 22, 24,
                     20, 1, 21, 9, 5, 1, 17, 9, 16, 0, 21, 10, 1, 10, 1, 22, 25, 11, 0, 25, 1,
                     6, 14, 12, 13, 14, 26, 28, 20, 24, 14, 22, 14, 27, 2, 8, 28, 9,
                     24, 5, 1, 6, 9, 13, 18, 9, 2, 3, 1, 10, 27, 4, 16, 10, 17, 12, 5, 0, 6, 3,
                     2, 24, 10, 13, 8, 27, 17, 7, 13, 8, 4, 23, 14, 16, 1, 26, 17, 0, 15, 14, 1, 19, 10,
                     27, 4, 21, 1, 0, 2, 21, 13, 22, 17, 8, 6, 8, 27, 20, 3, 23, 24, 5, 2, 13, 23, 15,
                     27, 8, 12, 20, 1, 16, 15, 23, 2, 1, 23, 21, 20, 14, 21, 16, 3, 20, 24, 20, 26, 22,
                     27, 14, 26, 17, 8, 25, 11, 27, 10, 4, 2, 20, 0, 28, 9, 21, 14, 19, 17, 3, 28, 13])


def get_mayfly_text():
    return np.array([1, 24, 7, 21, 6, 14, 23, 6, 10, 17, 10, 12, 16, 17, 10, 26, 28, 6, 15, 25,
                     13, 7, 19, 28, 12, 11, 12, 7, 8, 10, 6, 28, 17, 1, 26, 8, 26,
                     21, 7, 1, 4, 15, 3, 27, 0, 27, 28, 23, 22, 2, 19, 5, 9, 14,
                     23, 2, 18, 4, 12, 5, 24, 11, 15, 22, 1, 7, 4, 16, 15, 18, 15, 16, 26, 4, 28, 25, 9,
                     23, 13, 17, 27, 15, 1, 23, 18, 26, 2, 20, 7, 22, 15, 6, 20, 11, 25, 18, 3, 5, 2, 7,
                     19, 1, 3, 6, 0, 24, 3, 27, 21, 17, 28, 2, 5, 24, 4, 27, 16, 22, 7, 0, 26, 21, 1,
                     26, 10, 20, 16, 25, 25, 24, 4, 13, 0, 19, 7, 3, 23, 28, 17, 13, 21, 22, 9, 6, 19,
                     27, 18, 3, 9, 20, 14, 21, 10, 27, 25, 19, 8, 18, 7, 19, 21, 13, 12, 19, 27, 11, 25,
                     3, 27, 0, 26, 14, 22, 25, 2, 25, 17, 3, 24, 2, 11, 4, 11, 9, 2, 27, 0, 24, 16, 9, 8, 6,
                     1, 23, 5, 2, 1, 4, 1, 22, 23, 8, 4, 6, 7, 16, 13, 18, 0, 24, 8, 28, 2])


def get_wing_tree_text():
    return np.array([19, 13, 26, 20, 15, 3, 24, 25, 8, 20, 18, 12, 10, 19, 20, 20, 15, 5, 13, 9,
                     8, 6, 1, 27, 8, 1, 17, 0, 23, 11, 1, 17, 18, 10, 25, 0, 13,
                     25, 13, 2, 4, 19, 20, 5, 17, 6, 26, 19, 28, 17, 25, 9, 2, 19, 0,
                     27, 28, 5, 17, 6, 25, 0, 18, 11, 4, 3, 13, 17, 0, 17, 3, 12, 4, 28, 4, 28, 6,
                     18, 20, 12, 4, 9, 15, 3, 3, 5, 24, 18, 26, 18, 18, 16, 4, 1, 26, 22, 11, 14,
                     28, 6, 21, 26, 16, 21, 9, 24, 16, 15, 21, 24, 11, 0, 20, 15, 1, 7, 28, 13, 10, 16,
                     10, 9, 4, 4, 21, 19, 26, 19, 0, 10, 25, 10, 24, 1, 22, 17, 7, 19, 10, 8, 26, 7, 23, 20, 22,
                     16, 23, 22, 5, 17, 27, 17, 24, 16, 7, 16, 13, 7, 28, 3, 4, 3, 18, 26, 20, 15,
                     1, 27, 4, 0, 11, 12, 4, 27, 2, 18, 1, 16, 21, 25, 9, 24, 28, 3, 24, 9, 24, 2, 6, 3,
                     25, 14, 17, 16, 18, 28, 19, 6, 4, 19, 26, 21, 0, 17, 23, 22, 23, 24, 28, 4, 5, 10,
                     13, 23, 0, 19, 21, 8, 15, 3, 23, 13, 14, 9, 22, 4, 27, 9, 5, 5, 16, 9, 13, 0])


def get_cuneiform_text():
    return np.array([23, 12, 14, 5, 0, 10, 24, 7, 8, 6, 12, 22, 0, 16, 18, 22, 28, 24,
                     27, 15, 6, 26, 28, 9, 2, 25, 4, 3, 27, 19, 7, 14, 19, 26,
                     23, 17, 16, 4, 1, 11, 8, 25, 22, 27, 21, 7, 8, 15, 0, 27, 20, 2,
                     16, 10, 7, 16, 3, 1, 9, 7, 19, 20, 15, 2, 28, 7, 11, 24, 11, 25, 6, 26, 19, 7, 23,
                     13, 27, 18, 11, 7, 18, 1, 8, 7, 21, 10, 15, 25, 6, 11, 20,
                     21, 2, 12, 10, 0, 5, 22, 12, 23, 17, 26, 27, 26, 1, 26, 9, 2, 4, 18,
                     19, 10, 12, 23, 4, 7, 14, 17, 8, 5, 11, 27, 24, 9, 7, 9, 19, 0,
                     12, 10, 12, 24, 3, 15, 17, 22, 16, 11, 13, 18, 13, 11, 3, 7, 1, 28,
                     21, 7, 19, 5, 3, 16, 16, 0, 1, 11, 23, 28, 14, 3, 14, 2, 6, 23, 17, 3, 16, 20,
                     12, 10, 17, 27, 24, 18, 0, 28, 1, 18, 13, 15, 7, 23, 23, 15, 27, 7, 2, 23, 15, 21,
                     11, 20, 6, 1, 27, 9, 14, 0, 4, 24, 26, 19, 0, 2, 8, 4, 24, 4, 25, 24, 6, 22, 23, 17])


def get_spiral_branch_text():
    return np.array([0, 9, 19, 26, 6, 23, 25, 8, 24, 13, 14, 26, 8, 12, 28, 3, 18, 16, 21,
                     28, 20, 10, 16, 2, 0, 19, 24, 5, 18, 23, 5, 16, 4, 22, 6, 28, 9,
                     25, 17, 1, 18, 17, 1, 2, 0, 22, 6, 15, 22, 10, 13, 22, 14, 15, 17, 7, 11, 17,
                     26, 19, 1, 28, 4, 10, 1, 22, 11, 10, 19, 18, 25, 4, 15, 14, 21, 28, 13, 20,
                     23, 3, 20, 10, 14, 28, 21, 18, 4, 9, 13, 18, 7, 27, 9, 11, 16, 26, 15, 3, 15,
                     16, 21, 1, 9, 12, 24, 18, 16, 24, 11, 5, 26, 22, 17, 20, 15, 17, 23, 11, 10, 21, 26, 18,
                     5, 11, 8, 20, 26, 6, 25, 20, 23, 20, 25, 20, 2, 14, 20, 18, 14, 3, 14, 10, 5, 1, 19,
                     9, 1, 3, 9, 12, 8, 27, 20, 12, 3, 25, 24, 3, 22, 3, 26, 4, 18, 0, 1, 10, 8, 22, 20,
                     9, 16, 0, 23, 4, 28, 6, 13, 3, 12, 3, 19, 28, 17, 11, 27, 15, 19, 0, 16,
                     0, 25, 3, 22, 5, 20, 23, 27, 20, 3, 5, 21, 1, 13, 7, 16, 6, 5, 15, 1, 22, 6, 2,
                     0, 14, 0, 16, 5, 15, 14, 22, 6, 0, 14, 9, 23, 17, 16, 28, 27, 13, 27])


def get_54_text():
    return np.array(
        [24, 19, 21, 23, 27, 2, 14, 10, 19, 27, 23, 13, 21, 1, 7, 24, 19, 16, 24,
         21, 21, 2, 27, 7, 15, 8, 10, 5, 25, 13, 25, 6, 3, 19, 10, 24, 18, 3, 16, 7,
         3, 0, 26, 1, 16, 11, 2, 11, 28, 18, 5, 9, 28, 5, 28, 18, 4,
         3, 1, 14, 23, 7, 8, 17, 21, 0, 24, 5, 11, 1, 3, 11, 27, 28, 10, 20, 6, 8, 17, 1,
         11, 14, 24, 5, 7, 27, 19, 3, 13, 26, 23, 27, 20, 13, 12, 10, 2, 4, 26, 6, 19, 14,
         22, 6, 15, 19, 13, 11, 22, 23, 22, 16, 27, 22, 16, 21, 10, 19, 21, 26, 24, 25, 21, 4,
         26, 11, 9, 20, 1, 14, 17, 8, 13, 11, 3, 28, 6, 25, 7, 14, 15, 23, 5, 1, 16,
         22, 8, 12, 9, 13, 16, 28, 26, 17, 1, 6, 6, 24, 12, 9, 6, 3, 18, 20, 19, 17, 2, 26,
         27, 22, 12, 26, 19, 5, 22, 2, 18, 20, 4, 12, 13, 4, 23, 26, 14, 23, 21, 26, 13,
         15, 18, 14, 7, 5, 6, 0, 23, 4, 18, 23, 18, 7, 3, 12, 22, 8, 3, 22, 17, 15, 8,
         28, 24, 5, 10, 19, 14, 11, 19, 18, 19, 20, 6, 3, 16, 2, 14, 18, 28, 4, 6, 26,
         21, 25, 19, 10, 7, 15, 17, 14, 19, 15, 12, 6, 23, 2, 25, 0, 27, 24, 17, 5, 1, 7, 4, 17,
         28, 0, 14, 10, 19, 1, 5, 13, 8, 21, 20, 12, 19, 15, 23, 27, 13, 0, 17, 8, 12, 5,
         12, 18, 28, 18, 10, 6, 14, 6, 15, 18, 15, 12, 2, 2, 18, 15, 2, 22, 5, 28, 10, 19,
         5, 14, 23, 11, 1, 17, 18, 10])


def test_decryption():
    return np.array(
        [20, 27, 8, 14, 16, 14, 24, 5, 9, 20, 5, 10, 20, 13, 20, 28, 13, 22, 19, 26, 8, 24, 28, 25, 0, 26, 17, 18, 21,
         19, 14, 22, 12, 1, 1, 26, 10, 8, 27, 7, 25, 28, 2, 0, 28, 21, 8, 15, 12, 0, 22, 18, 27, 6, 12, 27, 28, 18, 12,
         27, 28, 2, 22, 14, 23, 3, 3, 6, 2, 14, 0, 20, 24, 5, 27, 27, 3, 13, 13, 11, 9, 5, 9, 13, 7, 26, 20, 25, 19, 7,
         28, 5, 26, 27, 18, 19, 13, 20, 18, 12, 4, 21, 5, 27, 4, 28, 13, 10, 22, 12, 26, 5, 4, 2, 19, 25, 3, 4, 7, 28,
         7, 19, 13, 4, 21, 8, 4, 21, 14, 1, 4, 26, 24, 6, 3, 5, 11, 5, 14, 24, 4, 27, 12, 24, 15, 18, 25, 7, 10, 27, 25,
         24, 16, 11, 5, 12, 18, 19, 19, 25, 19, 17, 5, 13, 15, 1, 7, 19, 6, 4, 7, 13, 10, 2, 19, 26, 28, 24, 11, 18, 4,
         17, 13, 16, 3, 20, 4, 4, 25, 24, 4, 16, 19, 5, 10, 9, 13, 0, 25, 5, 0, 4, 2, 13, 4, 25, 3, 19, 10, 28, 4, 19,
         18, 18, 3, 17, 8, 23, 5, 25, 4, 16, 5, 9, 25, 7, 5, 7, 14, 13, 6, 5, 11, 28, 5, 21, 23, 20, 2, 13, 10, 20, 23,
         7, 24, 19, 2, 13, 18, 6, 6, 23, 11, 16, 28, 17, 5, 3, 13, 0, 12, 5, 3, 22, 3, 1, 12, 27, 2, 16, 23, 11, 25, 28,
         19, 4, 22, 1, 21, 4, 5, 20, 23, 3, 0, 6, 5, 25, 9, 0, 26, 19, 23, 13, 18, 21, 9, 15, 10, 28, 3, 20, 19, 10, 19,
         2, 25, 12, 26, 6, 17, 21, 24, 4, 25, 12, 3, 10, 20, 25, 7, 18, 28, 11, 8, 11, 22, 28, 11, 9, 25, 1, 16, 19, 3,
         23, 26, 19, 3, 10, 16, 5, 19, 12, 2, 28, 27, 23, 28, 13, 0, 18, 13, 9, 13, 4, 28, 11, 27, 3, 2, 25, 20, 23, 19,
         14, 25, 13, 21, 11, 15, 8, 1, 28, 17, 20, 28, 27, 23, 18, 1, 18, 17, 4, 4, 1, 26, 6, 26, 9, 8, 18, 15, 7, 19,
         9, 21, 6, 13, 20, 23, 25, 15, 12, 1, 20, 5, 13, 23, 7, 22, 18, 23, 10, 10, 13, 17, 20, 6, 9, 4, 0, 28, 22, 9,
         19, 26, 27, 9, 2, 1, 13, 23, 7, 28, 16, 13, 19, 8, 27, 27, 11, 28, 6, 7, 5, 13, 9, 27, 28, 5, 17, 26, 23, 10,
         19, 1, 24, 21, 5, 10, 20, 25, 24, 5, 13, 13, 11, 1, 15, 10, 16, 25, 28, 13, 4, 0, 18, 9, 1, 21, 13, 0, 14, 4,
         3, 17, 12, 24, 0, 13, 27, 28, 28, 9, 13, 10, 27, 10, 20, 13, 14, 19, 18, 4, 16, 18, 20, 15, 8, 8, 26, 20, 5,
         18, 19, 23, 23, 12, 20, 21, 13, 14, 26, 24, 18, 25, 20, 2, 16, 17, 7, 18, 4, 13, 10, 0, 12, 4, 8, 4, 6, 2, 2,
         27, 19, 19, 10, 3, 11, 9, 25, 20, 15, 1, 4, 27, 25, 10, 3, 2, 25, 7, 11, 28, 18, 25, 27, 14, 23, 19, 6, 15, 4,
         25, 20, 5, 19, 8, 21, 27, 9, 23, 21, 13, 6, 2, 11, 13, 11, 23, 21, 26, 5, 1, 19, 25, 0, 14, 20, 20, 25, 7, 20,
         4, 11, 26, 28, 21, 21, 21, 21, 4, 27, 17, 28, 1, 25, 21, 7, 21, 5, 20, 14, 8, 14, 27, 13, 27, 27, 6, 4, 11, 5,
         14, 27, 10, 5, 5, 4, 17, 5, 19, 7, 4, 27, 10, 17, 12, 6, 23, 14, 7, 11, 11, 3, 25, 6, 19, 3, 25, 4, 7, 27, 9,
         8, 7, 6, 8, 13, 7, 18, 8, 15, 18, 27, 10, 13, 8, 16, 7, 26, 21, 11, 10, 13, 21, 8, 23, 13, 24, 2, 23, 7, 22, 7,
         19, 26, 0, 8, 6, 5, 1, 4, 26, 22, 22, 1, 21, 18, 11, 8, 0, 2, 12])


def test_decryption2():
    return np.array(
        [27, 24, 12, 0, 25, 0, 27, 2, 22, 6, 12, 9, 7, 24, 13, 0, 27, 21, 28, 13, 23, 15, 2, 0, 20, 25, 25, 24, 27, 11,
         25, 7, 23, 12, 26, 4, 25, 28, 4, 18, 14, 13, 21, 21, 18, 23, 10, 7, 27, 27, 8, 18, 26, 0, 9, 8, 24, 8, 21, 17,
         4, 20, 6, 4, 23, 4, 17, 0, 24, 2, 13, 22, 2, 0, 5, 19, 17, 14, 0, 13, 3, 13, 28, 3, 17, 22, 25, 6, 19, 28, 5,
         4, 9, 17, 27, 18, 10, 27, 2, 11, 18, 19, 21, 24, 2, 1, 9, 13, 10, 12, 14, 6, 3, 13, 21, 24, 11, 13, 23, 5, 4,
         8, 22, 13, 21, 13, 28, 24, 19, 7, 26, 17, 7, 19, 19, 3, 19, 8, 28, 19, 10, 12, 6, 18, 8, 10, 7, 24, 17, 27, 19,
         14, 7, 17, 21, 5, 8, 9, 11, 16, 5, 28, 25, 23, 10, 3, 2, 12, 13, 22, 21, 11, 9, 28, 14, 8, 8, 4, 17, 13, 24, 7,
         5, 8, 1, 23, 0, 23, 5, 27, 21, 21, 16, 0, 25, 13, 7, 8, 28, 7, 18, 25, 23, 11, 17, 18, 17, 23, 7, 16, 13, 25,
         12, 19, 7, 26, 20, 21, 28, 2, 12, 18, 10, 13, 4, 27, 25, 27, 27, 21, 28, 2, 9, 5, 1, 27, 5, 24, 24, 19, 27, 17,
         26, 2, 17, 14, 4, 16, 9, 19, 21, 0, 22, 1, 0, 15, 15, 0, 25, 3, 14, 4, 12, 14, 5, 2, 2, 3, 23, 4, 2, 4, 9, 17,
         9, 1, 11, 25, 23, 7, 27, 10, 13, 28, 7, 8, 13, 22, 16, 16, 13, 27, 25, 24, 7, 5, 8, 1, 18, 19, 22, 25, 12, 26,
         5, 17, 7, 0, 11, 4, 18, 0, 16, 13, 13, 25, 25, 27, 7, 19, 2, 18, 4, 20, 17, 13, 18, 4, 23, 23, 28, 14, 9, 27,
         9, 5, 3, 4, 25, 1, 5, 5, 26, 28, 20, 5, 3, 12, 7, 23, 3, 6, 20, 24, 3, 26, 21, 17, 4, 10, 22, 18, 7, 10, 28,
         23, 20, 27, 19, 2, 19, 13, 23, 18, 9, 4, 7, 14, 28, 27, 19, 25, 12, 8, 6, 2, 20, 19, 25, 20, 2, 10, 11, 27, 11,
         1, 2, 7, 6, 5, 23, 12, 17, 12, 16, 22, 6, 23, 10, 21, 14, 15, 26, 14, 5, 19, 16, 25, 28, 6, 2, 2, 28, 0, 5, 17,
         10, 26, 2, 24, 10, 9, 5, 28, 7, 11, 11, 26, 1, 11, 25, 26, 19, 26, 10, 6, 5, 3, 28, 5, 25, 10, 25, 26, 7, 1,
         10, 7, 24, 17, 14, 5, 27, 16, 19, 12, 3, 23, 7, 24, 5, 5, 25, 11, 4, 3, 28, 25, 16, 8, 1, 15, 16, 21, 5, 13,
         25, 18, 2, 24, 11, 9, 22, 4, 14, 13, 6, 10, 12, 25, 2, 24, 28, 9, 20, 12, 15, 9, 25, 13, 13, 25, 3, 26, 5, 8,
         20, 24, 17, 28, 19, 22, 28, 6, 18, 19, 17, 6, 7, 24, 0, 9, 11, 19, 22, 5, 5, 25, 28, 25, 25, 15, 5, 11, 25, 5,
         11, 18, 28, 21, 13, 17, 10, 23, 15, 26, 28, 3, 17, 8, 14, 18, 10, 17, 19, 18, 8, 14, 22, 16, 1, 8, 13, 7, 16,
         26, 11, 10, 0, 6, 21, 19, 17, 22, 13, 3, 15, 27, 11, 12, 0, 2, 26, 20, 1, 11, 5, 3, 26, 17, 25, 23, 5, 5, 12,
         11, 13, 11, 21, 14, 13, 7, 27, 23, 18, 8, 27, 20, 16, 14, 12, 6, 26, 4, 19, 13, 14, 9, 1, 26, 10, 19, 20, 23,
         26, 22, 2, 24, 25, 17, 27, 19, 27, 15, 20, 25, 11, 5, 25, 18, 6, 15, 10, 13, 11, 15, 6, 8, 9, 26, 11, 19, 5,
         28, 13, 12, 5, 24, 15, 25, 26, 5, 22, 14, 28, 19, 19, 9, 13, 15, 4, 8, 9, 27, 27, 13, 14, 3, 13, 14, 4, 25, 24,
         19, 23, 16, 5, 7, 27, 23, 6, 12, 10, 25, 7, 19, 12, 13, 4, 13, 1, 15, 13, 20, 17, 18, 5, 16, 27, 23, 20, 27,
         12, 16, 25, 7, 19, 12, 23, 3, 8, 12, 23, 1, 21, 19, 28, 25, 21, 24, 25, 20, 23, 7, 9, 3, 24, 13, 4, 24, 7, 7,
         4, 16, 19, 5, 19, 6, 14, 1, 11, 9, 4, 7, 26, 18, 19, 3, 9, 4, 25, 27, 6, 13, 24, 9, 27, 13, 19, 3, 0, 8, 8, 7,
         18, 3, 4, 10, 21, 5, 2, 6, 27, 24, 7, 24, 19, 3, 4, 10, 17, 11, 26, 10, 23, 6, 21, 3, 11, 21, 19, 10, 4, 7, 1,
         10, 17, 2, 21, 14, 24, 28, 5, 3, 28, 15, 10, 13, 15, 1, 5, 1, 9, 20, 18, 16, 13, 28, 25, 27, 17, 2, 18, 2, 24,
         28, 14, 28, 7, 13, 24, 27, 1, 11, 18, 28, 4, 5, 6, 9, 13, 3, 28, 24, 12, 18, 17, 2, 9, 10, 10, 14, 27, 27, 28,
         16, 23, 26, 10, 10, 1, 3, 15, 22, 18, 7, 22, 23, 16, 10, 16, 4, 10, 6, 9, 9, 3, 7, 24, 26, 19, 10, 9, 7, 4, 7,
         3, 7, 21, 8, 0, 13, 7, 5, 23, 4, 28, 27, 8, 0, 1, 17, 0, 13, 10, 26, 26, 4, 25, 24, 23, 2, 1, 4, 19, 23, 27,
         27, 5, 19, 16, 25, 15, 28, 27, 25, 2, 14, 24, 7, 3, 21, 18, 10, 18, 11, 13, 8, 10, 18, 7, 14, 3, 9, 27, 9, 26,
         8, 22, 8, 2, 18, 7, 5, 5, 7, 5, 25, 18, 16, 15, 12, 3, 27, 20, 13, 12, 7, 17, 11, 4, 25, 13, 10])
