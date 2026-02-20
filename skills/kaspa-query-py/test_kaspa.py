import asyncio
from kaspa import Resolver, RpcClient

async def main():
    # 创建 Resolver（用于解析公共节点或自定义 URL）
    resolver = Resolver()  # 默认使用 Kaspa 的公共节点网络 (PNN)

    # 创建 RPC 客户端
    client = RpcClient(url="ws://127.0.0.1:17210")  # 本地 wRPC（WebSocket RPC），端口视你的节点配置

    # 连接到节点
    await client.connect()

    # 示例：获取服务器信息（测试连接是否成功）
    server_info = await client.get_server_info()
    print("Server Info:", server_info)

    # 其他常用 RPC 调用示例（异步）
    # block_dag_info = await client.get_block_dag_info()
    # print("Block DAG Info:", block_dag_info)

    # 断开连接（可选，程序结束时自动处理）
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())