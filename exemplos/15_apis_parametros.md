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
   
   Exemplos:
   - max_tokens=50: Resposta curta, ideal para comandos simples ou respostas objetivas.
   - max_tokens=200: Resposta média, adequada para explicações rápidas ou pequenos resumos.
   - max_tokens=1000: Resposta longa, útil para análises detalhadas, geração de código ou textos extensos.

4. **Diversidade (`top_p`)**
   - Controla a variedade de palavras e ideias na resposta
   - Valores altos (ex: 1.0) permitem respostas mais criativas e variadas
   - Valores baixos (ex: 0.1) tornam a resposta mais restrita e previsível
   - Exemplo:
     - top_p=1.0: "Conte uma história sobre um dragão." → Pode gerar histórias muito diferentes a cada execução
     - top_p=0.2: "Conte uma história sobre um dragão." → Respostas mais padronizadas, com pouca variação

5. **Repetição (`frequency_penalty`)**
   - Penaliza a repetição de palavras ou frases já usadas
   - Valores altos (ex: 1.0) reduzem repetições
   - Valores baixos (ex: 0.0) permitem repetições
   - Exemplo:
     - frequency_penalty=0.0: "Fale sobre maçãs." → Pode repetir "maçã" várias vezes
     - frequency_penalty=1.0: "Fale sobre maçãs." → Evita repetir "maçã", busca sinônimos ou muda o foco

6. **Novos tópicos (`presence_penalty`)**
   - Incentiva o modelo a introduzir assuntos ou termos ainda não usados
   - Valores altos (ex: 1.0) aumentam a chance de explorar novas ideias
   - Valores baixos (ex: 0.0) mantêm o foco no mesmo tema
   - Exemplo:
     - presence_penalty=0.0: "Fale sobre IA e aprendizado de máquina." → Pode focar só em IA
     - presence_penalty=1.0: "Fale sobre IA e aprendizado de máquina." → Tende a mencionar outros conceitos relacionados, como robótica, automação, etc.

## 2. Parâmetros Importantes

### Controle de Resposta:
```python
{
    "temperature": 0.7,        # Criatividade (0-1)
    "max_tokens": 1000,        # Tamanho máximo
    "top_p": 0.9,             # Diversidade
    "frequency_penalty": 0.0,  # Permite repetições
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
    "frequency_penalty": 0.1,  # Reduz levemente repetições
    "presence_penalty": 0.1    # Pequena diversidade
}
```

2. **Geração Criativa**
```python
{
    "temperature": 0.8,        # Mais criativo
    "max_tokens": 2000,        # Espaço para desenvolvimento
    "top_p": 1.0,             # Vocabulário diverso
    "frequency_penalty": 0.5,  # Reduz repetições
    "presence_penalty": 0.3    # Incentiva diversidade
}
```

3. **Análise de Código**
```python
{
    "temperature": 0.2,        # Muito preciso
    "max_tokens": 1000,        # Espaço para funções
    "top_p": 0.95,            # Termos técnicos comuns
    "frequency_penalty": 0.0,  # Permite repetições
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

[Anterior: Boas Práticas](13_boas_praticas.md) | [Voltar ao Índice](../README.md) 