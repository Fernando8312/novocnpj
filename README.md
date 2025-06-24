🔍 𝗩𝗼𝗰𝗲̂ 𝗷𝗮́ 𝗼𝘂𝘃𝗶𝘂 𝗳𝗮𝗹𝗮𝗿 𝘀𝗼𝗯𝗿𝗲 𝗼 𝗻𝗼𝘃𝗼 𝗖𝗡𝗣𝗝 𝗔𝗹𝗳𝗮𝗻𝘂𝗺𝗲́𝗿𝗶𝗰𝗼?

A Receita Federal anunciou a modernização do modelo atual de 𝗖𝗡𝗣𝗝, que passará a aceitar 𝗹𝗲𝘁𝗿𝗮𝘀 𝗲 𝗻𝘂́𝗺𝗲𝗿𝗼𝘀 em sua composição, mantendo os 14 caracteres. Essa mudança tem como principal objetivo ampliar a quantidade de combinações possíveis, evitando o esgotamento do formato atual (numérico).
Com mais de 58 milhões de CNPJs registrados até setembro de 2024, o modelo exclusivamente numérico se tornou insustentável. A nova estrutura amplia  as possibilidades de combinações, garantindo a continuidade da emissão de CNPJs.  

✅ Pontos importantes:  
• Os CNPJs atuais continuam válidos — nada muda para quem já possui um número registrado.  
• O 𝗠𝗘𝗜 seguirá com o CNPJ numérico, sem alterações.  

📅 A previsão é que os primeiros CNPJs nesse novo padrão comecem a ser emitidos em julho de 2026.  

📌 Estrutura do novo CNPJ  
•  Composto por 12 caracteres alfanuméricos + 2 dígitos verificadores numéricos.  
• Total de 14 posições, como no formato atual.  
• EX. 12.ABC.345/01DE-35  

🔢 Como calcular os dígitos verificadores (DV)?  

1️⃣ Primeiro Dígito Verificador (DV1)  
  1. Converter os caracteres para valores numéricos, usando a tabela ASCII, subtraindo 48 do valor de cada caractere.  
  Ex:  
  ▪ Letra A → ASCII 65 → 65 - 48 = 17,  
  ▪ Letra B → ASCII 66 → 66 - 48 = 18,   
  ▪ Letra C → ASCII 67 → 67 - 48 = 19, e assim por diante.  
  
Ex. CNPJ 12.ABC.345/01DE – (DV)  

![novocnpj](https://github.com/Fernando8312/novocnpj/blob/main/Telas/01.png)

  2. Aplicar pesos de 2 a 9, da direita para a esquerda, reiniciando após o oitavo caractere:  

![novocnpj](https://github.com/Fernando8312/novocnpj/blob/main/Telas/02.png)
![novocnpj](https://github.com/Fernando8312/novocnpj/blob/main/Telas/03.png)

🧮 E depois?  
  1. Multiplica cada valor pelo peso  
  2. Soma tudo  
  3. Divide por 11  
  4. Aplica a regra:  
    ◦ Se o resto = 0 ou 1 → DV = 0  
    ◦ Senão → DV = 11 - resto  
![novocnpj](https://github.com/Fernando8312/novocnpj/blob/main/Telas/04.png)

  No exemplo: Resto da divisão 459/11 = 8  
  1º DV = 3 (resultado de 11-8)  

2️⃣ Segundo Dígito Verificador (DV2)  
  1. Acrescentar o DV1 ao final do número-base (agora são 13 caracteres).  
  2. Repetir o processo:  
    ◦ Aplicar novos pesos, agora começando em 6 e indo até 2.  
  3. Repetir os passos de conversão, multiplicação, soma e divisão.  
  4. Calcular o segundo DV com a mesma regra:  
    ◦ Se resto = 0 ou 1 → DV = 0  
    ◦ Senão → DV = 11 - resto  
![novocnpj](https://github.com/Fernando8312/novocnpj/blob/main/Telas/05.png)

Somatório (6+10+...+6) = 424  
Resto da divisão 424/11 = 6  
2º DV = 5 (resultado de 11-6)  
Resultado final: 12.ABC.345/01DE-35  