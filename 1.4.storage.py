from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb


load_dotenv()

agent = Agent(
    # session_id="petrobras_session", # Historico de conversa mantido.
    # user_id="user_1",
    db=SqliteDb(db_file="agent.db"),
    model=OpenAIChat(id="gpt-5-nano"),
    instructions="Use tabelas para mostrar a informação final. Não inclua nenhum outro texto.",
    tools=[YFinanceTools()],
    add_history_to_context=True
    # debug_mode=True
)

agent.print_response("Qual a cotação da petrobras?", session_id="petrobras_session", usuario="analista_petrobras")
agent.print_response("Qual a cotação da vale?", stream=True, session_id="vale_session", usuario="vale_session")
agent.print_response("Quais empresas já consultamos a cotação?", stream=True, session_id="petrobras_session", usuario="analista_empresas")
