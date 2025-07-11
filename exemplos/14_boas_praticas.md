# Boas Práticas de Prompting

## 1. Clareza e Especificidade

**Descrição:** Prompts claros e específicos geram respostas mais precisas e relevantes.
**Quando usar:** Sempre, em qualquer tipo de prompt.

### Exemplos:

❌ **Vago:**
```markdown
Fale sobre programação.
```

✅ **Específico:**
```markdown
Explique os conceitos fundamentais de programação orientada a objetos, focando em:
- Encapsulamento
- Herança
- Polimorfismo
- Abstração
```

❌ **Ambíguo:**
```markdown
Analise este código.
```

✅ **Claro:**
```markdown
Analise o seguinte código Python e identifique:
- Complexidade de tempo
- Possíveis bugs
- Sugestões de otimização
- Boas práticas aplicadas

Código:
[seu código aqui]
```

## 2. Formatação de Prompts

**Descrição:** Estrutura adequada do prompt facilita o entendimento e processamento.
**Quando usar:** Em prompts complexos ou que precisam de estrutura específica.

### Exemplos:

❌ **Sem Estrutura:**
```markdown
Crie uma API REST com autenticação, banco de dados e documentação.
```

✅ **Estruturado:**
```markdown
Crie uma API REST com as seguintes especificações:

1. Autenticação:
   - Método: JWT
   - Tempo de expiração: 1 hora
   - Rotas protegidas: /api/*

2. Banco de Dados:
   - Tipo: PostgreSQL
   - Tabelas necessárias: [lista]
   - Relacionamentos: [descrição]

3. Documentação:
   - Formato: Swagger/OpenAPI
   - Endpoints a documentar: todos
   - Exemplos de uso: obrigatórios
```

## 3. Evitando Problemas Comuns

**Descrição:** Conhecer e evitar armadilhas comuns melhora a qualidade das respostas.
**Quando usar:** Sempre, para garantir prompts eficientes.

### Exemplos:

❌ **Prompt Muito Longo:**
```markdown
[prompt extremamente longo com muitos detalhes desnecessários]
```

✅ **Prompt Conciso:**
```markdown
Resuma o texto abaixo em 3 tópicos principais:
[texto]
```

❌ **Múltiplas Tarefas:**
```markdown
Analise este código, otimize, documente e crie testes.
```

✅ **Tarefa Única:**
```markdown
Analise o seguinte código e sugira otimizações de performance:
[código]
```

❌ **Sem Contexto:**
```markdown
Traduza para inglês.
```

✅ **Com Contexto:**
```markdown
Traduza o seguinte texto técnico para inglês, mantendo os termos técnicos:
[texto]
```

## 4. Dicas Adicionais

1. **Use Delimitadores**
   - Para código: ```
   - Para exemplos: ---
   - Para seções: ##

   Exemplos:
   - Delimitador de código:
     ```python
     def soma(a, b):
         return a + b
     ```
   - Delimitador de exemplo:
     ---
     Exemplo de entrada: "O produto é excelente."
     Exemplo de saída: "Positivo"
     ---
   - Delimitador de seção:
     ## Nova Seção
     (Utilize para separar grandes blocos de conteúdo ou tópicos no prompt)

2. **Especifique o Formato**
   - JSON
   - Markdown
   - Lista
   - Parágrafos

3. **Defina Limites**
   - Número de palavras
   - Número de exemplos
   - Nível de detalhe

4. **Forneça Exemplos**
   - Formato esperado
   - Nível de detalhe
   - Tom da resposta

5. **Valide Entradas**
   - Verifique se o prompt está completo
   - Confirme se os parâmetros estão corretos
   - Teste o prompt antes de usar em produção 

## 5. Anti-Padrões de Prompting (O que NÃO fazer)

**Prompt "Mãe Dináh":** Esperar que a IA adivinhe o contexto que está apenas na sua cabeça.

❌ Exemplo:
"Me ajude com aquele problema."

**Prompt "Frankenstein":** Juntar várias perguntas e tarefas não relacionadas em um único prompt.

❌ Exemplo:
"Analise este código, otimize, documente e crie testes."

**Prompt "Ambíguo":** Usar palavras com duplo sentido sem esclarecer.

❌ Exemplo:
"Fale sobre o 'caixa' da empresa."

**Prompt "Sem Limites":** Pedir uma análise sem definir escopo ou formato.

❌ Exemplo:
"Faça uma análise completa do nosso app."

**Dica:** Dê nomes aos anti-padrões para facilitar a identificação e evite-os sempre que possível.

---

[Anterior: Refinamento Iterativo](13_refinamento_iterativo.md) | [Próximo: APIs e Parâmetros](15_apis_parametros.md) | [Voltar ao Índice](../README.md) 