# # Radom

# import random
# import time

# TAM = 1000


# def insertion_sort(pVetor):
#     for vAux in range(1, len(pVetor)):
#         vTemp = vAux
#         while vTemp > 0 and pVetor[vTemp] < pVetor[vTemp-1]:
#             pVetor[vTemp], pVetor[vTemp-1] = pVetor[vTemp-1], pVetor[vTemp]
#             vTemp -= 1


# if __name__ == "__main__":
#     vetor = [random.randint(0, TAM) for _ in range(TAM)]
#     print(vetor)
#     start_time = time.time()
#     insertion_sort(vetor)
#     end_time = time.time()

#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")

# # Cresente

# import time

# vetor = 1000


# def insertion_sort(pVetor):
#     for vAux in range(1, len(pVetor)):
#         vTemp = vAux
#         while vTemp > 0 and pVetor[vTemp] < pVetor[vTemp-1]:
#             pVetor[vTemp], pVetor[vTemp-1] = pVetor[vTemp-1], pVetor[vTemp]
#             vTemp -= 1


# if __name__ == "__main__":
#     vetor = list(range(vetor))
#     print(vetor)
#     start_time = time.time()
#     insertion_sort(vetor)
#     end_time = time.time()

#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")


## Decresente

# import time

# TAM = 1000


# def insertion_sort(pVetor):
#     for vAux in range(1, len(pVetor)):
#         vTemp = vAux
#         while vTemp > 0 and pVetor[vTemp] < pVetor[vTemp-1]:
#             pVetor[vTemp], pVetor[vTemp-1] = pVetor[vTemp-1], pVetor[vTemp]
#             vTemp -= 1


# if __name__ == "__main__":
#     vetor = list(range(TAM, 0, -1))
#     print(vetor)
#     start_time = time.time()
#     insertion_sort(vetor)
#     end_time = time.time()
#     print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
#     print(vetor)
#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")
