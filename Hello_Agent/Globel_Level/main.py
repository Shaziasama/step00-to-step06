import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, set_default_openai_client, AsyncOpenAI
import rich

load_dotenv()
set_tracing_disabled(disabled=True)
set_default_openai_api("chat_completions")

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

)
set_default_openai_client(client)



agent = Agent(
    name="My Agent",
    instructions="You are a helpful assistant.",
    model="gemini-2.0-flash"
)

result = Runner.run_sync(agent, "hi")
rich.print(result.final_output)
