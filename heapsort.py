def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  # Inicializa o maior como o índice do nó raiz
        left = 2 * i + 1
        right = 2 * i + 2

        # Verifica se o filho esquerdo existe e é maior que o nó raiz
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Verifica se o filho direito existe e é maior que o nó raiz
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Troca o nó raiz se necessário
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Troca
            heapify(arr, n, largest)

    n = len(arr)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos um por um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca o maior elemento para o final
        heapify(arr, i, 0)

# Exemplo de uso:
arr = [3, 6, 8, 10, 1, 2, 1]
heap_sort(arr)
print(arr)
