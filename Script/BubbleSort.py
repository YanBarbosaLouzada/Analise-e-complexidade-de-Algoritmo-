# import random
# import time

# TAM = 1000


# def random_integer(low, high):
#     return random.randint(low, high)


# def bubble_sort(v):
#     for a in range(len(v)-1, 0, -1):
#         for b in range(a):
#             if v[b] > v[b+1]:
#                 v[b], v[b+1] = v[b+1], v[b]


# if __name__ == "__main__":
#     vetor = [random_integer(0, TAM) for _ in range(TAM)]

#     start_time = time.time()
#     bubble_sort(vetor)
#     end_time = time.time()

#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")


# cresente


# import time

# vetor = 1000


# def bubble_sort(v):
#     for a in range(len(v)-1, 0, -1):
#         for b in range(a):
#             if v[b] > v[b+1]:
#                 v[b], v[b+1] = v[b+1], v[b]


# if __name__ == "__main__":
#     vetor = list(range(vetor))
#     print(vetor)
#     start_time = time.time()
#     bubble_sort(vetor)
#     end_time = time.time()
#     print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#     print(vetor)
#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")


# decresente


# import time

# TAM = 10000


# def bubble_sort(v):
#     for a in range(len(v)-1, 0, -1):
#         for b in range(a):
#             if v[b] > v[b+1]:
#                 v[b], v[b+1] = v[b+1], v[b]


# if __name__ == "__main__":
#     vetor = list(range(TAM, 0, -1))
#     print(vetor)
#     start_time = time.time()
#     bubble_sort(vetor)
#     end_time = time.time()
#     print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
#     print(vetor)
#     execution_time = (end_time - start_time) * 1000

#     print("Tempo de execução:", execution_time, "ms")
