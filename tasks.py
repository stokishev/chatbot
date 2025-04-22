import json
from config import credit_card_fees_and_rates, decimal_serializer

# Function to generate the system message content for the chatbot.
def generate_system_message():
    """
    Generates the system message content including the role definition,
    instructions, and the credit card fees and rates data in JSON format.
    """
    # Convert the structured data to a JSON string
    fees_data_json = json.dumps(credit_card_fees_and_rates, indent=2, default=decimal_serializer)

    # Define the system message content
    system_message_content = f"""You are a helpful AI assistant specializing in providing information about Standard Chartered Bank (Hong Kong) Limited Credit Card fees and rates.
You MUST ONLY use the following provided information to answer questions about these specific fees and rates. Do not use any prior knowledge or external information.
Provide concise and direct answers based *strictly* on the data provided.
If a user asks about something not covered in this data, state clearly that you cannot provide information on that topic based on the provided data.

Here is the relevant data in JSON format:
```json
{fees_data_json}
```
"""
    return system_message_content



