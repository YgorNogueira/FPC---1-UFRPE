def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Variável para verificar se houve trocas nesta iteração
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos
                swapped = True
        # Se não houve trocas nesta iteração, a lista está ordenada
        if not swapped:
            break

# Exemplo de uso:
arr = [3, 6, 8, 10, 1, 2, 1]
bubble_sort(arr)
print(arr)
