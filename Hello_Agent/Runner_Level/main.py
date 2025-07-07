import os
from dotenv import load_dotenv
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI,RunConfig

import rich
load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant.",
    
)

client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",

)

config = RunConfig(
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client),
    model_provider=client,
    tracing_disabled=True

)


result=Runner.run_sync(agent,"hi", run_config=config)
rich.print(result.final_output) 



