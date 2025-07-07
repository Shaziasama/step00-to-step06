from dotenv import load_dotenv
from agents import Agent,Runner

import rich
load_dotenv()

agent = Agent(
    name="My Agent",
    instructions="you are a helpful assistant",
    model="LitellmModel"
)
result = Runner.run_sync(agent, "Hi")
rich.print(result.final_output)

