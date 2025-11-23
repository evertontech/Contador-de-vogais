def contar_vogais(texto):
    texto_minimo = texto.lower()

    contagem = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0 }
    for caractere in texto_minimo:
        if caractere in contagem:
            contagem[caractere] = contagem[caractere] + 1

    return contagem

resultado = contar_vogais("henrique")

print("--- Resultado da Contagem de Vogais ---")
print("--------------------------------------")
print("--------------------------------------")

for chave, valor in resultado.items():    
    print(f"A vogal '{chave.upper()}' aparece {valor} vezes.")

print("--------------------------------------")
print("--------------------------------------")
print("--------------------------------------")
