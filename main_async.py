from agents import Agent, ItemHelpers, Runner, function_tool
from simple_agent.simple_agent import create_simple_agent
from dotenv import load_dotenv
import asyncio
from openai.types.responses import ResponseTextDeltaEvent

async def main():

    result =  Runner.run_streamed(create_simple_agent(), "what is change in open interest for stcoks?")

    print("=== Run starting ===")

    async for event in result.stream_events():
     

        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

         # When the agent updates, print that
        elif event.type == "agent_updated_stream_event":
            print(f"Agent updated: {event.new_agent.name}")
            continue
        # When items are generated, print them
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print("-- Tool was called")
            elif event.item.type == "tool_call_output_item":
                print(f"-- Tool output: {event.item.output}")
            elif event.item.type == "message_output_item":
                continue
                #print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")
            else:
                pass  # Ignore other event types
       
    
    print("\n=== Run complete ===")

if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())