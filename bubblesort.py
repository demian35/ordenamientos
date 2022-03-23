#bubblesort recibe un arreglo
def bubblesort(nums):
    #bandera es verdadera si se realiza un intercambio
    valorintercambiado = True
    while valorintercambiado:
        #La bandera cambiara si ya no hay nada que intercambiar 
        valorintercambiado = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # intercambiaos los elementos
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # se asigna la bandera a verdadero para contiunar con las iteraciones
                valorintercambiado = True

random_list_of_nums = [5, 2, 1, 8, 4,31,2,6,2,1,45,21,2,7]
bubblesort(random_list_of_nums)
print(random_list_of_nums)