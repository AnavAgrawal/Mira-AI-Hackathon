from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})


# Load flow configuration
flow = Flow(source="my_flow.yaml")

# Prepare test input
input_dict = {"income-amount": "10 lakhs",
              "query": "Do I have any tax reduction?"}
response = client.flow.test(flow, input_dict)

print(response)
