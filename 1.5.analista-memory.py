from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb


load_dotenv()

db = SqliteDb(db_file="agent.db")

agent = Agent(
    # session_id="petrobras_session", # Historico de conversa mantido.
    # user_id="user_1",
    name="analista_financeiro",
    db=db,
    model=OpenAIChat(id="gpt-5-nano"),
    instructions="Você é um analista e tem diferentes clientes. Lembre-se de cada cliente e suas preferências.",
    tools=[YFinanceTools()],
    add_history_to_context=True,
    num_history_runs=3,
    enable_user_memories=True,
    add_memories_to_context=True,
    enable_agentic_memory=True #  Quando usar 1 modelo grande Ex: GPT 5 e o outro de memoria com um menor.
    # debug_mode=True
)

agent.print_response("Ola prefiro respostas em formato de tabelas, gosto de poucas informações SEMPRE coloque um QUA QUA no final.", session_id="petrobras_session_2", usuario="analista_petrobras")
agent.print_response("Ola prefiro respostas em formato de textos, gosto de bastante informações SEMPRE coloque um AU AU no final.", session_id="vale_session_2", usuario="analista_vale")

# agent.print_response("Qual a cotação da petrobras?", session_id="petrobras_session_3", usuario="analista_petrobras")
# agent.print_response("Qual a cotação da vale?", stream=True, session_id="vale_session_3", usuario="analista_vale")
# agent.print_response("Quais empresas já consultamos a cotação?", stream=True, session_id="petrobras_session", usuario="analista_empresas")
