from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import rich

# Load .env variables
load_dotenv()

# Get the API key from the environment
OPENROUTER_API_KEY= os.getenv("OPENROUTER_API_KEY")


# Create the OpenAI-style client with correct OpenRouter key
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",  # ✅ Correct URL for OpenRouter
)

# Set up the agent with a model supported by OpenRouter
agent = Agent(
    name="My Agent",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(
        model="deepseek/deepseek-r1-0528:free",  # ✅ Use correct OpenRouter-supported model ID
        openai_client=client
    ),
)

# Run synchronously
result = Runner.run_sync(
    starting_agent=agent,
    input="Hi, who are you?"
)

# Display the result using rich
rich.print(result.final_output)

