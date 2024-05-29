
# -------------------------------- Cresente --------------------------------

# import time

# vetor = 1000

# def selection_sort(vetor):
#     n = len(vetor)
#     for i in range(n - 1):
#         menor = i
#         for j in range(i + 1, n):
#             if vetor[j] < vetor[menor]:
#                 menor = j
#         vetor[i], vetor[menor] = vetor[menor], vetor[i]


# # Exemplo de uso:
# if __name__ == "__main__":
#     vetor = list(range(vetor))
#     print(vetor)
#     start_time = time.time()
#     selection_sort(vetor)
#     end_time = time.time()
#     execution_time = (end_time - start_time) * 1000
#     print("Tempo de execução:", execution_time, "ms")



# -------------------------------- Aleatorio --------------------------------

# import random
# import time

# TAM = 1000


# def random_integer(low, high):
#     return random.randint(low, high)

# def selection_sort(vetor):
#     n = len(vetor)
#     for i in range(n - 1):
#         menor = i
#         for j in range(i + 1, n):
#             if vetor[j] < vetor[menor]:
#                 menor = j
#         vetor[i], vetor[menor] = vetor[menor], vetor[i]


# # Exemplo de uso:
# if __name__ == "__main__":
#     vetor = [random_integer(0, TAM) for _ in range(TAM)]
#     print(vetor)
#     start_time = time.time()
#     selection_sort(vetor)
#     end_time = time.time()
#     execution_time = (end_time - start_time) * 1000
#     print("Tempo de execução:", execution_time, "ms")

# # -------------------------------- Decresente --------------------------

# import random
# import time

# TAM = 1000



# def selection_sort(vetor):
#     n = len(vetor)
#     for i in range(n - 1):
#         menor = i
#         for j in range(i + 1, n):
#             if vetor[j] < vetor[menor]:
#                 menor = j
#         vetor[i], vetor[menor] = vetor[menor], vetor[i]


# if __name__ == "__main__":
#     vetor = list(range(TAM, 0, -1))  
#     print(vetor)
#     start_time = time.time()
#     selection_sort(vetor)
#     end_time = time.time()
#     print('----------------------------------------------------------------')
#     print(vetor)
#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")
