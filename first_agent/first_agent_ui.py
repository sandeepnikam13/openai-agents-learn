import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Runner
from openai.types.responses import ResponseTextDeltaEvent
from agents.extensions.memory import AdvancedSQLiteSession

# Load environment variables
load_dotenv()



# Import the configured agent from first_agent.py
from first_agent import agent

@cl.on_message
async def on_message(message: cl.Message):
    # Initialize an empty message in the Chainlit UI to stream into
    msg = cl.Message(content="")
    await msg.send()

    # session
    session = AdvancedSQLiteSession(
        session_id=cl.user_session.get("id"),
        db_path="conversasations.db",
        create_tables=True
    )

    # Start the streamed runner with the user's message
    result = Runner.run_streamed(agent, message.content, session = session)

    # Iterate through the stream events and append the text delta to the UI
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            await msg.stream_token(event.data.delta)

    # Update and finalize the message in the chat
    await msg.update()
