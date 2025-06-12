"""
Exemplo prático de uso da API OpenAI com diferentes configurações
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do cliente
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

# Modelo padrão ou do .env
DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

def criar_prompt_base() -> str:
    return """
    Você é um assistente especializado em desenvolvimento de software.
    Responda de forma técnica e objetiva.
    """

def configurar_parametros(
    temperatura: float = 0.7,
    max_tokens: int = 1000,
    top_p: float = 1.0,
    frequency_penalty: float = 0.0,
    presence_penalty: float = 0.0
) -> Dict[str, Any]:
    return {
        "temperature": temperatura,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty
    }

# Configurações pré-definidas
config_criativa = configurar_parametros(
    temperatura=0.9,
    max_tokens=2000,
    frequency_penalty=0.5
)

config_tecnica = configurar_parametros(
    temperatura=0.3,
    max_tokens=500,
    presence_penalty=0.1
)

config_codigo = configurar_parametros(
    temperatura=0.2,
    max_tokens=1000,
    top_p=0.95
)

def chamar_api(
    prompt: str,
    config: Dict[str, Any],
    system_prompt: str = None,
    model: str = DEFAULT_MODEL
) -> str:
    """
    Faz uma chamada à API com o prompt e configuração especificados
    
    Args:
        prompt: O prompt do usuário
        config: Configurações da API
        system_prompt: Prompt do sistema (opcional)
        model: Modelo a ser usado (opcional)
    
    Returns:
        str: Resposta da API
    """
    messages = []
    
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    messages.append({"role": "user", "content": prompt})
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            **config
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na chamada da API: {str(e)}"

# Exemplos de uso
if __name__ == "__main__":
    print("\nEscolha um exemplo para executar:")
    print("1 - Explicação técnica")
    print("2 - Geração de código")
    print("3 - Transformação para JSON")
    print("4 - Brainstorming")
    print("0 - Sair")
    
    opcao = input("\nDigite o número do exemplo (0-4): ")
    
    if opcao == "1":
        print("================================================")
        print("\n\n\nExemplo 1: Explicação técnica")
        resposta_tecnica = chamar_api(
            prompt="Explique o conceito de herança em POO.",
            config={
                "temperature": 0.3,  # Respostas mais diretas
                "max_tokens": 500,   # Respostas concisas
                "top_p": 0.9,        # Usa termos técnicos
                "frequency_penalty": 0.1,  # Pequena redução de repetições
                "presence_penalty": 0.1    # Pequena diversidade
            },
            system_prompt="Você é um professor de programação."
        )
        print("Resposta Técnica:", resposta_tecnica)
        
    elif opcao == "2":
        print("================================================")
        print("\n\n\nExemplo 2: Geração de código")
        resposta_codigo = chamar_api(
            prompt="Escreva uma função em Java com o design pattern Strategy.",
            config={
                "temperature": 0.2,  # Respostas precisas e consistentes
                "max_tokens": 1000,  # Espaço suficiente para funções
                "top_p": 0.95,       # Usa termos técnicos comuns
                "frequency_penalty": 0.0,  # Permite repetição de termos técnicos
                "presence_penalty": 0.0    # Foca em um aspecto do código
            },
            system_prompt="Você é um desenvolvedor sênior."
        )
        print("\nResposta Código:", resposta_codigo)
        
    elif opcao == "3":
        print("================================================")
        print("\n\n\nExemplo 3: Transformação para JSON")
        resposta_json = chamar_api(
            prompt="Transforme o seguinte CSV em JSON: nome;idade;cidade\nJoão;25;São Paulo\nMaria;30;Rio de Janeiro\nPedro;28;Belo Horizonte",
            config={
                "temperature": 0.1,  # Respostas extremamente precisas
                "max_tokens": 500,   # Espaço para JSON
                "top_p": 0.1,        # Resposta muito focada
                "frequency_penalty": 0.0,  # Mantém estrutura consistente
                "presence_penalty": 0.0    # Mantém formato exato
            },
            system_prompt="Você é um especialista em transformação de dados. Retorne APENAS o JSON, sem explicações adicionais."
        )
        print("\nResposta JSON:", resposta_json)
        
    elif opcao == "4":
        print("================================================")
        print("\n\n\nExemplo 4: Brainstorming")
        resposta_criativa = chamar_api(
            prompt="Sugira 5 ideias inovadoras para um app de produtividade.",
            config={
                "temperature": 0.8,  # Respostas mais criativas
                "max_tokens": 2000,  # Espaço para desenvolvimento
                "top_p": 1.0,        # Permite vocabulário diverso
                "frequency_penalty": 0.5,  # Evita repetições
                "presence_penalty": 0.3    # Incentiva diversidade
            },
            system_prompt="Você é um arquiteto de software criativo."
        )
        print("\nResposta Criativa:", resposta_criativa)
        
    elif opcao == "0":
        print("Saindo...")
        
    else:
        print("Opção inválida!") 