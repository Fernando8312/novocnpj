def char_to_value(c):
    """Converte caractere para valor numérico conforme regra ASCII - 48"""
    return ord(c.upper()) - 48  # Garante maiúsculo para letras

def aplicar_pesos(valores, pesos):
    """Aplica os pesos e calcula o somatório"""
    return sum(v * p for v, p in zip(valores, pesos))

def calcular_dv(cnpj_base):
    """Calcula os dois dígitos verificadores do CNPJ alfanumérico"""
    # Converter caracteres para valores numéricos
    valores = [char_to_value(c) for c in cnpj_base]

    # Pesos do 1º DV (12 posições): 5 a 2, depois 9 a 2
    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma1 = aplicar_pesos(valores, pesos1)
    resto1 = soma1 % 11
    dv1 = 0 if resto1 < 2 else 11 - resto1

    # Adiciona dv1 para cálculo do segundo dígito
    valores.append(dv1)
    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma2 = aplicar_pesos(valores, pesos2)
    resto2 = soma2 % 11
    dv2 = 0 if resto2 < 2 else 11 - resto2

    return dv1, dv2

def main():
    print("🔢 Cálculo dos Dígitos Verificadores do CNPJ Alfanumérico 🔠")
    while True:
        entrada = input("Digite os 12 primeiros caracteres do CNPJ (letras e números): ").strip()
        if len(entrada) != 12 or not entrada.isalnum():
            print("⚠️ Entrada inválida. Certifique-se de digitar exatamente 12 caracteres alfanuméricos.")
            continue

        dv1, dv2 = calcular_dv(entrada)
        print(f"✅ CNPJ completo: {entrada}-{dv1}{dv2}")
        break

if __name__ == "__main__":
    main()
