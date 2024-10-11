# Copyright © 2024 Chance Currie
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# as this was made for educational purposes and simply out of
# curiosity as OpenAI is fascinating. Please see the
# GNU General Public License for more details, or view
# <https://www.gnu.org/licenses/> for more information.


# A Python program that connects to the ChatGPT API. This program was run on a Windows machine in a Python 3.12 environment and utilizes ChatGPT 4o Mini. 
# Credits were purchased in order to test functionality of this program.

# Reference this link as needed in order to understand further how to do this: https://medium.com/@woyera/your-first-steps-in-ai-using-openais-gpt-4o-mini-with-python-e03e8d47aef7
# Second resource: https://www.linkedin.com/pulse/how-use-chatgpt-api-python-tutorialspoint-byl1c/
# This link was referenced in order to make a continuous loop of prompts and answers: https://stackoverflow.com/questions/77505030/openai-api-error-you-tried-to-access-openai-chatcompletion-but-this-is-no-lon

# Create your own Windows ChatGPT 4o Mini assistant:
# Step 1: Create an API key on OpenAI. This is secret so don't tell anyone!
# Step 2: Install the OpenAI library onto your computer. I did this through the use of Visual Studio Code's built in terminal using the command: pip install openai
# Step 3: In order to keep the secret key a secret, I made a environment variable by using PowerShell: PS> $ENV:OPENAI_API_KEY = "<your-key-value-here>", but double check by doing the following:
#         This PC -> Properties -> View Advanced System Settings -> Environment Variables -> Find/Create your environment variable, and I had to restart my VSCode environment after doing this to refresh it.
# Step 4: The following code is the implementation of how to connect to OpenAI's API:

# Importing the OpenAI library
from openai import OpenAI
# Importing the os library
import os 

# Declaring the OpenAI key through calling the environment variable that we created back in Step 3 to keep the key a secret.
api_key = os.getenv('OPENAI_API_KEY')

# Initializing the OpenAI client
client = OpenAI(api_key=api_key)

# A function that will generate a response based on what the user inputs
def chat_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages   # Send the entire conversation history as messages
    )

    return response.choices[0].message.content.strip()

# A loop that will continue to run until user enters in a keyword that ends the program
# Until the program is stopped, the user can enter in as many prompts as needed
if __name__ == "__main__":

    # Initialize the conversation history with a system message or an empty list
    conversation_history = []

    # Add a memory initialization message to remind the bot about its memory
    conversation_history.append({"role": "system", "content": "You have memory in this session. You will remember things mentioned until the session ends."})

    while True:
        user_input = input("User: ")

        # How the user quits the program
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        # Add the user's message to the history
        conversation_history.append({"role": "user", "content": user_input})

        # Get the response from the bot, including conversation history
        bot_response = chat_gpt(conversation_history)

        # Add the bot's response to the history
        conversation_history.append({"role": "assistant", "content": bot_response})

        # Print the bot's response
        print("Bot: ", bot_response)
