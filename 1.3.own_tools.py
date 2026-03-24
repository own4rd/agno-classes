from agno.agent import Agent
from agno.tools.tavily import TavilyTools
# from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()


def conversao_to_fh(temperatura_celsius: float):
    """
    Conversão de temperatura de Celsius para Fahrenheit
    args:
        temperatura_celsius: Temperatura em Celsius
    return:
        Temperatura em Fahrenheit
    """
    return f"{temperatura_celsius * 1.8 + 32}°F"

agent = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    # model=Groq(id="llama-3.3-70b-versatile"),
    tools=[TavilyTools(), conversao_to_fh],
    # debug_mode=True
)

agent.print_response("Use suas ferramentas para procurar a temperatura de hoje em Porto Alegre em Fahrenheit")
