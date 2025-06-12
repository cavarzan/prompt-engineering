# Self-Consistency

**Descrição:** Técnica proposta por Wang et al. (2022) para substituir a decodificação gananciosa em prompts do tipo Chain-of-Thought (CoT). Consiste em gerar múltiplos caminhos de raciocínio para a mesma questão e selecionar a resposta mais frequente/consistente entre as gerações. Isso aumenta o desempenho em tarefas de raciocínio aritmético e de bom senso.

Referência: Wang, X., et al. (2022). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." https://arxiv.org/abs/2203.11171

**Quando usar:**
- Para tarefas de raciocínio aritmético ou lógico
- Quando a robustez da resposta é crítica
- Para reduzir vieses de geração única

**Exemplo:**

Resolva o problema abaixo utilizando raciocínio passo a passo. Gere pelo menos 5 cadeias de pensamento diferentes e, ao final, selecione a resposta mais frequente entre elas.

Problema: Se João tem o dobro da idade de Maria e, juntos, eles somam 36 anos, qual a idade de cada um?

---

[Anterior: Multi-step Prompting](06_multi_step.md) | [Próximo: Recursive Prompting](08_recursive.md) | [Voltar ao Índice](../README.md) 