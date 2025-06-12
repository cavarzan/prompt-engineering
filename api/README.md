# Parâmetros de API para LLMs

## Configuração do Ambiente

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Edite o arquivo `.env` com suas credenciais:
```bash
# Configurações da API OpenAI
OPENAI_API_KEY=sua-chave-api-aqui

# Configurações opcionais
OPENAI_MODEL=gpt-4  # ou gpt-3.5-turbo
OPENAI_ORG_ID=seu-org-id-aqui  # opcional
```

3. Para obter sua chave API:
   - Acesse https://platform.openai.com
   - Crie uma conta ou faça login
   - Vá para "API Keys"
   - Clique em "Create new secret key"
   - Copie a chave gerada

4. Teste a configuração:
```bash
python exemplo_api.py
```

## Parâmetros Principais

### Temperature (Temperatura)
- Controla o quão "criativa" ou "previsível" será a resposta
- Funciona como um termostato de criatividade:
  - 0.0 = respostas sempre iguais, muito previsíveis
  - 1.0 = respostas mais variadas e criativas
- Exemplos práticos:
  - 0.2-0.3: Ideal para código (queremos respostas precisas)
  - 0.7-0.8: Bom para textos criativos (histórias, ideias)
  - 0.5-0.6: Uso geral (equilíbrio entre precisão e criatividade)

### Max Tokens (Máximo de Tokens)
- Controla o tamanho da resposta
- Token = unidade de texto (aproximadamente 4 caracteres em português)
- Considerações importantes:
  - Cada token tem custo
  - Respostas muito longas podem ser caras
  - Respostas muito curtas podem ser incompletas
- Exemplos:
  - 100 tokens ≈ 1 parágrafo curto
  - 500 tokens ≈ 1 página
  - 2000 tokens ≈ 4 páginas

### Top P (Núcleo de Probabilidade)
- Controla a diversidade das palavras usadas
- Funciona como um filtro de palavras:
  - 0.95 = usa palavras mais comuns e previsíveis
  - 1.0 = permite usar palavras menos comuns
- Exemplo prático:
  - 0.95: "O gato está na casa"
  - 1.0: "O felino está na residência"

### Frequency Penalty (Penalidade de Frequência)
- Evita repetição de palavras
- Funciona como um corretor de redundância:
  - 0.0 = pode repetir palavras
  - 2.0 = evita ao máximo repetições
- Exemplo:
  - Com 0.0: "O sistema é rápido, o sistema é eficiente"
  - Com 2.0: "O sistema é rápido e eficiente"

### Presence Penalty (Penalidade de Presença)
- Incentiva o uso de tópicos diferentes
- Funciona como um guia de diversidade:
  - 0.0 = foca em um tópico
  - 2.0 = explora vários tópicos
- Exemplo:
  - Com 0.0: Foca em um aspecto do problema
  - Com 2.0: Aborda múltiplos aspectos

## Configurações Recomendadas

### Para Geração de Código
```python
{
    "temperature": 0.2,  # Respostas precisas e consistentes
    "max_tokens": 1000,  # Espaço suficiente para funções
    "top_p": 0.95,       # Usa termos técnicos comuns
    "frequency_penalty": 0.0,  # Permite repetição de termos técnicos
    "presence_penalty": 0.0    # Foca em um aspecto do código
}
```

### Para Texto Criativo
```python
{
    "temperature": 0.8,  # Respostas mais criativas
    "max_tokens": 2000,  # Espaço para desenvolvimento
    "top_p": 1.0,        # Permite vocabulário diverso
    "frequency_penalty": 0.5,  # Evita repetições
    "presence_penalty": 0.3    # Incentiva diversidade
}
```

### Para Respostas Técnicas
```python
{
    "temperature": 0.3,  # Respostas mais diretas
    "max_tokens": 500,   # Respostas concisas
    "top_p": 0.9,        # Usa termos técnicos
    "frequency_penalty": 0.1,  # Pequena redução de repetições
    "presence_penalty": 0.1    # Pequena diversidade
}
```

## Dicas de Uso

1. Comece com valores padrão e ajuste conforme necessário
2. Teste diferentes combinações para seu caso específico
3. Documente as configurações que funcionam bem
4. Monitore o custo das chamadas
5. Ajuste os parâmetros baseado no feedback dos usuários

## Exemplos de Uso

### Para Documentação Técnica
- Temperature: 0.3 (precisão)
- Max Tokens: 1000 (espaço para detalhes)
- Top P: 0.9 (termos técnicos)
- Frequency Penalty: 0.1 (alguma repetição é aceitável)
- Presence Penalty: 0.1 (foco no tópico)

### Para Brainstorming
- Temperature: 0.9 (criatividade)
- Max Tokens: 2000 (espaço para ideias)
- Top P: 1.0 (diversidade de ideias)
- Frequency Penalty: 0.5 (evita repetições)
- Presence Penalty: 0.5 (explora diferentes aspectos) 