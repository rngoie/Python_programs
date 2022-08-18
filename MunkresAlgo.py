from munkres import Munkres, print_matrix, make_cost_matrix
m = Munkres()
def Munkress(Mtrx):
    indexes = m.compute(matrix)
    total = 0
    for row, column in indexes: 
        value = matrix[row][column]
        total += value   
    return total
