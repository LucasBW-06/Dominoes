def max_consecutive_sequence(array, extras, total): # função que calcula a maior sequencia
    max_size = 0
    left = 0

    # janela deslizante que verifica o tamanho da maior sequencia
    for right in range(total):
        while array[right] - array[left] - right - left > extras:
            left += 1
        max_size = max(max_size, right - left + 1)

    return max_size + extras

n = int(input()) # recebe inteiro n
k = int(input()) # recebe inteiro k que representa a quantidade de dominos que podem ser colocados
dominoes = [int(input()) for _ in range(n)] # recebe n dominos

amount = max_consecutive_sequence(dominoes, k, n) # recebe o tamanho da maior sequencia
print(amount)