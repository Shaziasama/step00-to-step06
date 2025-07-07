import os
from agents import Agent,  Runner , OpenAIChatCompletionsModel, AsyncOpenAI ,set_tracing_disabled
from dotenv import load_dotenv
import chainlit as cl 

load_dotenv()
set_tracing_disabled(disabled=True)
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

history = []

client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",

)
agent = Agent(
    name=" My Agent",
    instructions="you are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1-0528:free",openai_client=client)
)


@cl.on_chat_start
async def start_message():
    await cl.Message(content="How are you?").send()

@cl.on_message
async def my_message(msg: cl.Message):
    user_input = msg.content
    history.appened({"role": "user", "content": user_input})

    result  = Runner.run_sync(agent, history)
    await cl.Message(content=result.final_output).send()
    

