import chainlit as cl
from dotenv import load_dotenv
from agents import Runner
from openai.types.responses import ResponseTextDeltaEvent
from agents.extensions.memory import AdvancedSQLiteSession

from bank_agent import bank_agent

load_dotenv()

@cl.on_chat_start
async def start():
    # Ensure session id exists
    if not cl.user_session.get("id"):
        cl.user_session.set("id", cl.context.session.id)





@cl.on_message
async def main(message: cl.Message):

    # Main assistant message (stream target)
    msg = cl.Message(content="Using Bank Agent")
    await msg.send()

    # Session (persistent memory)    
    session_id = cl.user_session.get("id")
    if not isinstance(session_id, str):
        session_id = str(cl.context.session.id)
        cl.user_session.set("id", session_id)

    session = AdvancedSQLiteSession(
        session_id=session_id,
        db_path="memory.db",
        create_tables=True,
    )
   

    result = Runner.run_streamed(
        bank_agent,
        message.content,
        session=session
    )

    active_steps = {}
    text_buffer = ""
    thinking_step = None
    tool_running = False

    async for event in result.stream_events():


        # =========================
        # 🧠 STREAM TEXT (BUFFERED)
        # =========================
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            text_buffer += event.data.delta

        # =========================
        # 🔧 TOOL EVENTS
        # =========================
        elif event.type == "run_item_stream_event":

            # -------- TOOL CALLED --------
            if event.name == "tool_called":
                tool_running = True

                # Flush any pending text BEFORE tool UI
                if text_buffer:
                    await msg.stream_token(text_buffer)
                    text_buffer = ""


                raw_item = event.item.raw_item

                tool_name = getattr(raw_item, "name", None) or (
                    raw_item.get("name") if isinstance(raw_item, dict) else None
                )
                tool_input = getattr(raw_item, "arguments", None) or (
                    raw_item.get("arguments") if isinstance(raw_item, dict) else None
                )
                call_id = getattr(raw_item, "call_id", None) or (
                    raw_item.get("call_id") if isinstance(raw_item, dict) else None
                )

                if tool_name and call_id:
                    step = cl.Step(
                        name=f"🔧 {tool_name}",
                        type="tool",
                        parent_id=msg.id,
                        show_input=True
                    )
                    step.input = tool_input or ""
                    await step.send()

                    active_steps[call_id] = step

            # -------- TOOL OUTPUT --------
            elif event.name == "tool_output":
                raw_item = event.item.raw_item

                call_id = getattr(raw_item, "call_id", None) or (
                    raw_item.get("call_id") if isinstance(raw_item, dict) else None
                )

                output = getattr(event.item, "output", None)
                if not output and isinstance(raw_item, dict):
                    output = raw_item.get("output")

                if call_id and call_id in active_steps:
                    step = active_steps[call_id]

                    import json
                    try:
                        output_str = (
                            json.dumps(output, indent=2)
                            if not isinstance(output, str)
                            else output
                        )
                    except Exception:
                        output_str = str(output)

                    step.output = output_str
                    await step.update()

                    del active_steps[call_id]

                # If no more active tools → allow text
                if not active_steps:
                    tool_running = False


    msg = cl.Message(content = text_buffer)
    await msg.send()



@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="HDFC Bank FD rates",
            message="what is hdfc bank fd rates ?",
            icon="https://www.svgrepo.com/show/270047/bank.svg",
        ),
        cl.Starter(
            label="HDFC Bank Home Loan Interest rates",
            message="what is hdfc bank home loan interest rates?",
            icon="https://www.svgrepo.com/show/270047/bank.svg",
        ),
        cl.Starter(
            label="HDFC Bank FD and home loan rates",
            message="what is hdfc bank fd and home loan rates?",
            icon="https://www.svgrepo.com/show/270047/bank.svg",
        ),  
    ]