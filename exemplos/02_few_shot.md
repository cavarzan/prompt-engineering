# Few-Shot Prompting

**Descrição:** Técnica que fornece alguns exemplos antes da pergunta para guiar o modelo no formato e tipo de resposta esperada.
**Quando usar:**
- Para garantir um formato específico de resposta
- Quando precisar de consistência nas respostas
- Em tarefas que seguem um padrão
- Para treinar o modelo com exemplos do domínio

## 1. Classificação de Textos

```markdown
Classifique os textos abaixo como técnico ou não técnico:

Exemplo 1:
"O algoritmo de ordenação quicksort tem complexidade O(n log n) no caso médio."
Classificação: técnico

Exemplo 2:
"O dia está bonito e ensolarado."
Classificação: não técnico

Exemplo 3:
"A implementação do padrão Observer permite desacoplamento entre objetos."
Classificação: técnico

Agora classifique:
"O sistema operacional gerencia recursos do hardware."
```

## 2. Geração de Código com Padrão

```markdown
Escreva uma função que siga o mesmo padrão dos exemplos:

Exemplo 1:
def soma(a, b):
    return a + b

Exemplo 2:
def multiplica(a, b):
    return a * b

Agora escreva uma função para dividir dois números:
```

## 3. Análise de Sentimento com Contexto

```markdown
Analise o sentimento considerando o contexto:

Contexto: Avaliação de produto
"O produto é bom, mas poderia ser melhor."
Sentimento: neutro

Contexto: Avaliação de filme
"O filme é incrível, superou minhas expectativas."
Sentimento: positivo

Contexto: Avaliação de restaurante
"O atendimento foi péssimo e a comida estava fria."
Sentimento: negativo

Agora analise:
Contexto: Avaliação de aplicativo
"O aplicativo funciona bem, mas tem alguns bugs."
```

## 4. Classificação de Sentimento

```markdown
Classifique o sentimento dos textos:

Exemplo 1:
Entrada: "O produto é muito bom"
Saída: "Positivo"

Exemplo 2:
Entrada: "Serviço péssimo, não recomendo"
Saída: "Negativo"

Exemplo 3:
Entrada: "Produto ok, mas poderia ser melhor"
Saída: "Neutro"

Agora classifique:
Entrada: "Excelente atendimento, superou expectativas"
Saída: ?
```

---

[Anterior: Zero-Shot Prompting](01_zero_shot.md) | [Próximo: Chain-of-Thought Prompting](03_chain_of_thought.md) | [Voltar ao Índice](../README.md)
