from dotenv import load_dotenv
from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

flow = Flow(source="my_flow.yaml")                    # Load flow
try:
    # Deploy to platform
    client.flow.deploy(flow)
except FlowError as e:
    print(f"Error occurred: {str(e)}")
