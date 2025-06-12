# Format Prompting

**Descrição:** Especifica o formato exato em que a resposta deve ser apresentada.

**Quando usar:**
- Para integração com outros sistemas (JSON, XML)
- Quando precisar de respostas estruturadas
- Para limitar o tamanho ou estilo da resposta
- Em relatórios ou documentação padronizada

**Exemplo 1:**

Analise o seguinte código e responda no formato JSON:

Código:
```python
def calcular_media(numeros):
    return sum(numeros) / len(numeros)
```

Responda no formato:
```json
{
  "complexidade": "O(1)",
  "tipo": "função",
  "parametros": ["lista de números"],
  "retorno": "número",
  "observacoes": []
}
```

**Exemplo 2:**

Analise o texto abaixo e responda em tópicos:

Texto: "O novo sistema de pagamentos reduziu o tempo de processamento em 40%, aumentou a satisfação dos clientes e diminuiu os custos operacionais."

Responda em tópicos:
- Pontos positivos
- Impactos
- Recomendações 

---

[Anterior: Role Prompting](04_role_prompt.md) | [Próximo: Multi-step Prompting](06_multi_step.md) | [Voltar ao Índice](../README.md) 