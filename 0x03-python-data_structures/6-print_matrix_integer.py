#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(0, len(row)):
            if col != len(row)-1:
                print("{:d}".format(row[col]), end=" ")
            else:
                print("{:d}".format(row[col]))
