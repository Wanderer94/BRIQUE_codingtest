import asyncio

# 메시지를 보내고 응답을 받는 비동기 함수
async def send_message(message, reader, writer, count):
    print(f"Send({count}): {message}")
    writer.write(message.encode())
    await writer.drain()  # 버퍼 비우기
    data = await reader.read(100)  # 서버로부터 데이터 읽기
    print(f"Received: {data.decode()}")

# 클라이언트 메인 함수
async def main():
    reader, writer = await asyncio.open_connection('localhost', 65432)
    
    messages = ["Ping", "Ping", "foobar"]
    await asyncio.gather(*[send_message(msg, reader, writer, i+1) for i, msg in enumerate(messages)])
    
    writer.close()  # 서버와 연결 종료
    await writer.wait_closed()  # 연결 종료 대기

# 이 스크립트가 직접 실행될 때만 main() 함수를 실행
if __name__ == "__main__":
    asyncio.run(main())
