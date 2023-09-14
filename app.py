# chainlit run app.py  -w
import chainlit as cl


# continuously on a loop
@cl.on_message
def main(message:str):
    # Your logic will be here
    result = message.capitalize()

    if "file" in message:
        file = None
        while file == None:
            file = cl.ask_for_file(title="Please upload a text file to analyse",accept=["text/plain"])

        # Decode bytes to text
        text = file.content.decode("utf-8")
        # Send a message to the user
    else:
        # LLM 

        # send a response back to the user 
        pass



@cl.on_chat_start
async def start():
    content = "Hello this is SmartGPT which has internet access and criticise itself"
    await cl.Message(content=content).send()