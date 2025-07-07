from dotenv import load_dotenv
from agents import Agent , Runner ,OpenAIChatCompletionsModel , AsyncOpenAI , set_tracing_disabled
import rich
import os

load_dotenv()
set_tracing_disabled(disabled=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

agent = Agent(
    name="Transalator Agent",
    instructions="You are translator agent.in urdu",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),

)

result = Runner.run_sync(agent, "I m shazia zohaib")
rich.print(result.final_output)


