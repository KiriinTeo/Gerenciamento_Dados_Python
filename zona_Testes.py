from pratica import numeroDePares

def teste():
    qtde, pairs = numeroDePares([4, 5, 6], [1, 2, 3])
    assert qtde == 3, f"Expected 3, but got {qtde}"
    assert pairs == [(4, 1), (5, 2), (6, 3)], f"Expected [(4, 1), (5, 2), (6, 3)], but got {pairs}"
    if pairs == [(4, 1), (5, 2), (6, 3)]:
        print(f"Teste Sucedido, Pares: {pairs}")

if __name__ == "__main__":
    teste()
    print("Testes Aprovados. Parabéns")