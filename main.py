import class_mod as cm


first_matrix_string = "31 22; 37 43; 51 86"
second_matrix_sting = "3 5; 2 4; -1 64"


total_matrix = cm.Matrix(first_matrix_string, second_matrix_sting)
print(total_matrix)

clothes = cm.Clothes
clothes.coat_and_costume(cm.Clothes, 5, 5)
print(clothes.test_decorator)

full_cell = cm.Cell
print(full_cell.__str__(cm.Cell))
full_cell.make_order(cm.Cell)

