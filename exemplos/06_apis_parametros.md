# APIs e Parâmetros

## 1. Configurações de Modelos

**Descrição:** Configurações básicas que afetam o comportamento do modelo.
**Quando usar:** Ao fazer chamadas à API, para controlar a saída.

### Parâmetros Principais:
1. **Modelo**
   - gpt-4: Mais preciso, mais caro
   - gpt-3.5-turbo: Mais rápido, mais econômico
   - text-davinci-003: Bom para tarefas específicas

2. **Temperatura**
   - 0.0: Respostas determinísticas
   - 0.7: Bom equilíbrio (padrão)
   - 1.0: Mais criativo/aleatório

3. **Max Tokens**
   - Controla tamanho da resposta
   - Ajuste baseado na necessidade
   - Considere o custo

## 2. Parâmetros Importantes

### Controle de Resposta:
```python
{
    "temperature": 0.7,        # Criatividade (0-1)
    "max_tokens": 1000,        # Tamanho máximo
    "top_p": 0.9,             # Diversidade
    "frequency_penalty": 0.0,  # Evita repetições
    "presence_penalty": 0.0    # Incentiva novos tópicos
}
```

### Exemplos de Configurações:

1. **Respostas Técnicas**
```python
{
    "temperature": 0.3,        # Mais preciso
    "max_tokens": 500,         # Respostas concisas
    "top_p": 0.9,             # Termos técnicos
    "frequency_penalty": 0.1,  # Pequena redução de repetições
    "presence_penalty": 0.1    # Pequena diversidade
}
```

2. **Geração Criativa**
```python
{
    "temperature": 0.8,        # Mais criativo
    "max_tokens": 2000,        # Espaço para desenvolvimento
    "top_p": 1.0,             # Vocabulário diverso
    "frequency_penalty": 0.5,  # Evita repetições
    "presence_penalty": 0.3    # Incentiva diversidade
}
```

3. **Análise de Código**
```python
{
    "temperature": 0.2,        # Muito preciso
    "max_tokens": 1000,        # Espaço para funções
    "top_p": 0.95,            # Termos técnicos comuns
    "frequency_penalty": 0.0,  # Permite repetição de termos técnicos
    "presence_penalty": 0.0    # Foca em um aspecto
}
```

## 3. Exemplos de Uso

### 1. Chamada Básica
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Você é um assistente técnico."},
        {"role": "user", "content": "Explique o conceito de API REST."}
    ],
    temperature=0.7,
    max_tokens=500
)
```

### 2. Com Configurações Específicas
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Você é um arquiteto de software."},
        {"role": "user", "content": "Projete uma API de pagamentos."}
    ],
    temperature=0.3,
    max_tokens=1000,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1
)
```

### 3. Com Validação
```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Você é um revisor de código."},
        {"role": "user", "content": "Revise este código Python."}
    ],
    temperature=0.2,
    max_tokens=2000,
    top_p=0.95,
    frequency_penalty=0.0,
    presence_penalty=0.0
)
```

## 4. Dicas de Uso

1. **Ajuste de Parâmetros**
   - Comece com valores padrão
   - Ajuste gradualmente
   - Teste diferentes combinações
   - Documente as melhores configurações

2. **Otimização de Custo**
   - Use max_tokens adequadamente
   - Escolha o modelo certo
   - Reutilize prompts eficientes
   - Monitore o uso

3. **Boas Práticas**
   - Sempre use system prompt
   - Mantenha contexto relevante
   - Valide as respostas
   - Implemente tratamento de erros

---

[Anterior: Boas Práticas](05_boas_praticas.md) | [Voltar ao Índice](../README.md) 