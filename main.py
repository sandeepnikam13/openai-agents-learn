from simple_agent.simple_agent import create_simple_agent
from dotenv import load_dotenv
from agents import Runner


def main():
    print("Hello from openai-agents-learn!")
    result = Runner.run_sync(create_simple_agent(), "What is the capital of France?")
    print(result.final_output)


if __name__ == "__main__":
    load_dotenv()
    main()
