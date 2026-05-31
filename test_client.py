import asyncio
import websockets
import sys

async def connect(player_id: str):
    uri = f"ws://127.0.0.1:8000/ws/{player_id}"
    try:
        async with websockets.connect(uri) as websocket:
            print(f"Connected as {player_id}.")
            
            # Receive welcome message
            welcome = await websocket.recv()
            print(welcome)
            
            async def receive_messages():
                try:
                    while True:
                        msg = await websocket.recv()
                        print(f"\n{msg}\n> ", end="")
                except websockets.ConnectionClosed:
                    print("\nConnection closed.")

            # Start receiver task
            asyncio.create_task(receive_messages())
            
            # Input loop
            while True:
                cmd = await asyncio.to_thread(input, "> ")
                if cmd.lower() in ["quit", "exit"]:
                    break
                await websocket.send(cmd)
                await asyncio.sleep(0.1) # Small delay to let recv print first
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    player = sys.argv[1] if len(sys.argv) > 1 else "player1"
    asyncio.run(connect(player))
