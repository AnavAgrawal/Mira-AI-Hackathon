from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})

# Create dataset
client.dataset.create("anav-agrawal/finance-bill-2025", "Finance Bill 2025")

# Add file to your dataset
client.dataset.add_source("anav-agrawal/finance-bill-2025",
                          file_path=r"C:\Users\anava\Anav\Github\Mira-AI-Hackathon\Finance_Bill.pdf")
