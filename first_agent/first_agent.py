from agents import Agent, Runner
from dotenv import load_dotenv
import os   
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model= os.getenv("MODEL_NAME")
)

async def main():
    result = Runner.run_streamed(agent, "What is the capital of France")

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
