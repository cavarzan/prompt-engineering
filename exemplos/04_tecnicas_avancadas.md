# Técnicas Avançadas

## 1. Role Prompting
**Descrição:** Define um papel ou persona específica para o modelo assumir, influenciando o estilo e profundidade da resposta.
**Quando usar:** 
- Quando precisar de respostas especializadas
- Para simular diferentes perspectivas profissionais
- Em entrevistas técnicas ou consultorias
- Para obter respostas mais contextualizadas

Exemplo:

Você é um arquiteto de software com 20 anos de experiência. Sua especialidade é em sistemas distribuídos e microserviços. Responda como se estivesse em uma entrevista técnica.

Pergunta: Como você projetaria um sistema de registro de CCBs que precisa escalar para milhões de clientes?

## 2. Format Prompting
**Descrição:** Especifica o formato exato em que a resposta deve ser apresentada.
**Quando usar:**
- Para integração com outros sistemas (JSON, XML)
- Quando precisar de respostas estruturadas
- Para limitar o tamanho ou estilo da resposta
- Em relatórios ou documentação padronizada

Exemplo:

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

Outro exemplo:

Analise o texto abaixo e responda em tópicos:

Texto: "O novo sistema de pagamentos reduziu o tempo de processamento em 40%, aumentou a satisfação dos clientes e diminuiu os custos operacionais."

Responda em tópicos:
- Pontos positivos
- Impactos
- Recomendações

Outro exemplo:

Analise o texto abaixo e responda em 3 parágrafos concisos:

Texto: "A empresa implementou um novo sistema de gestão que automatizou processos, reduziu erros e melhorou a produtividade."

Responda em 3 parágrafos:
1. Contexto
2. Mudanças
3. Resultados

Outro exemplo:

Analise o texto abaixo e responda em no máximo 100 caracteres:

Texto: "O projeto de inovação trouxe resultados positivos, mas alguns desafios precisam ser superados para garantir o sucesso a longo prazo."

Resposta (máx. 100 caracteres):

## 3. Multi-step Prompting
**Descrição:** Divide um problema complexo em etapas sequenciais para resolução passo a passo.
**Quando usar:**
- Em problemas complexos que precisam ser decompostos
- Para garantir que todos os aspectos sejam considerados
- Em planejamento e análise de requisitos
- Para documentar processos de decisão

Exemplo:

Vamos resolver este problema em etapas:

1. Primeiro, identifique os requisitos:
   - Sistema de autenticação
   - Armazenamento de dados
   - Interface de usuário
2. Depois, sugira tecnologias para cada requisito:
   - Autenticação: [tecnologias]
   - Armazenamento: [tecnologias]
   - Interface: [tecnologias]
3. Por fim, explique como integrar estas tecnologias.

Problema: Desenvolver um sistema de gerenciamento de tarefas.

## 4. Self-Consistency
**Descrição:** Solicita múltiplas soluções para o mesmo problema e compara os resultados.
**Quando usar:**
- Para validar diferentes abordagens
- Em análise de trade-offs
- Para documentar alternativas
- Em decisões arquiteturais

Exemplo:

Resolva o problema de três maneiras diferentes e depois compare as soluções:

Problema: Implementar um sistema de cache para uma API REST.

Solução 1 (usando Redis):
[implementação]

Solução 2 (usando Memcached):
[implementação]

Solução 3 (usando cache em memória):
[implementação]

Comparação das soluções:
1. Performance
2. Complexidade
3. Manutenção
4. Custo

## 5. Recursive Prompting
**Descrição:** Decompõe um problema em subproblemas menores e mais gerenciáveis.
**Quando usar:**
- Em problemas complexos e interligados
- Para análise detalhada de componentes
- Em arquitetura de sistemas
- Para documentação técnica

Exemplo:

Vamos decompor este problema em subproblemas:

Problema Principal: Desenvolver um sistema de recomendação de produtos.

Subproblema 1: Coleta de Dados
- Quais dados precisamos?
- Como coletar?
- Como armazenar?

Subproblema 2: Processamento
- Como processar os dados?
- Quais algoritmos usar?
- Como validar?

Subproblema 3: Interface
- Como apresentar as recomendações?
- Como coletar feedback?
- Como melhorar continuamente?

Para cada subproblema, forneça uma solução detalhada.

## 6. Contrastive Prompting
**Descrição:** Compara e contrasta diferentes abordagens ou soluções.
**Quando usar:**
- Para análise de alternativas
- Em decisões arquiteturais
- Para documentar trade-offs
- Em avaliação de tecnologias

Exemplo:

Compare e contraste estas duas abordagens:

Abordagem 1: Monolito
- Vantagens
- Desvantagens
- Casos de uso ideais

Abordagem 2: Microserviços
- Vantagens
- Desvantagens
- Casos de uso ideais

Conclusão: Em quais cenários cada abordagem é mais adequada?

## 7. Chain-of-Thought com Validação
**Descrição:** Solicita raciocínio passo a passo com validação em cada etapa.
**Quando usar:**
- Em problemas complexos que precisam de verificação
- Para documentar processos de decisão
- Em análise de performance
- Para debugging e otimização

Exemplo:

Resolva o problema e valide cada passo:

Problema: Otimizar uma query SQL que está lenta.

Passo 1: Análise da Query
Query atual:
```sql
SELECT p.nome, c.valor, c.data
FROM pedidos p
JOIN clientes cl ON p.cliente_id = cl.id
JOIN compras c ON p.id = c.pedido_id
WHERE c.data BETWEEN '2023-01-01' AND '2023-12-31'
AND cl.estado = 'SP'
ORDER BY c.valor DESC;
```
- Problemas identificados: [lista]
- Validação: [como confirmar os problemas]

Passo 2: Proposta de Otimização
- Alterações sugeridas: [lista]
- Justificativa: [explicação]
- Validação: [como testar as alterações]

Passo 3: Implementação
- Código otimizado: [query]
- Métricas de melhoria: [números]
- Validação final: [como confirmar a melhoria]

## 8. Chain-of-Thought Interativo
**Descrição:** Permite interação passo a passo com o modelo, aguardando confirmação.
**Quando usar:**
- Em sessões de debugging
- Para validação de requisitos
- Em análise de problemas complexos
- Para tutoriais interativos

Exemplo:

Vamos resolver este problema passo a passo. Após cada passo, aguarde minha confirmação antes de prosseguir.

```markdown
Problema: Em uma sala de aula, há 24 alunos. O professor precisa formar grupos de 4 alunos para um trabalho. Quantos grupos serão formados?
```

## 9. Chain-of-Thought Automático
**Descrição:** Solicita raciocínio completo sem interrupções.
**Quando usar:**
- Para documentação de processos
- Em análise de problemas
- Para explicações detalhadas
- Em relatórios técnicos

Exemplo:

Resolva o seguinte problema mostrando seu raciocínio passo a passo:

Problema: Uma loja vende camisetas por R$ 45,00 cada. Se um cliente comprar 3 camisetas, receberá 10% de desconto no valor total. Quanto o cliente pagará? Mostre seu raciocínio.

Resposta esperada:

1. Primeiro, calculamos o valor total sem desconto:
   3 camisetas × R$ 45,00 = R$ 135,00
2. Depois, calculamos o desconto de 10%:
   R$ 135,00 × 0,10 = R$ 13,50
3. Por fim, subtraímos o desconto do valor total:
   R$ 135,00 - R$ 13,50 = R$ 121,50

Portanto, o cliente pagará R$ 121,50.

---

[Anterior: Chain-of-Thought Prompting](03_chain_of_thought.md) | [Próximo: Boas Práticas](05_boas_praticas.md) | [Voltar ao Índice](../README.md)
