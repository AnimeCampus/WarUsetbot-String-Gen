from pyrogram import Client
import os

api_id = int(os.environ.get("API_ID"))  # put your API_ID value in environment
api_hash = os.environ.get("API_HASH")  # put your API_HASH value in environment

app = Client("my_account")


async def main():
    await app.start()
    await app.send_message(
        "me",
        "**Pyrogram Session String**:\n\n"
        f"`{await app.export_session_string()}`"
    )
    await app.stop()


app.run(main())

