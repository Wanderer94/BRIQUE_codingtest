import asyncio

# 클라이언트 연결을 처리하는 비동기 함수
async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Connected by {addr}")

    count = 0  # 메시지 수를 세기 위한 카운터
    
    while True:
        data = await reader.read(100)  # 클라이언트로부터 데이터 읽기
        if not data:
            break
        message = data.decode()
        count += 1
        print(f"Received({count}): {message}")
        if message == "Ping":
            response = f"Pong ({count})"
        else:
            response = f"{message} ({count})"
        await asyncio.sleep(3)  # 3초 대기
        writer.write(response.encode())
        await writer.drain()  # 버퍼 비우기
        print(f"Send: {response}")
    
    writer.close()  # 클라이언트와 연결 종료
    await writer.wait_closed()  # 연결 종료 대기

# 서버 시작을 위한 비동기 함수
async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 65432)
    print("Server started and listening")

    async with server:
        await server.serve_forever()

# 이 스크립트가 직접 실행될 때만 main() 함수를 실행
if __name__ == "__main__":
    asyncio.run(main())
