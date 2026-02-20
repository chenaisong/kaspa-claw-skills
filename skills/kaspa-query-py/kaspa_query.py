# kaspa_query.py
# Kaspa 测试网查询技能（纯 Python + kaspa-python 库实现）
# Kaspa testnet query skill (pure Python + kaspa-python library)

import asyncio
from kaspa import RpcClient, Resolver
from typing import Dict, Any

async def query_kaspa_rpc(query_type: str) -> Dict[str, Any]:
    """
    异步调用 Kaspa RPC 查询指定类型的信息
    Async call Kaspa RPC for specified query type
    """
    try:
        # 创建 Resolver（默认使用公共节点，如果本地不可用可 fallback）
        resolver = Resolver()

        # 优先使用本地测试网节点（你的端口 17210）
        url = "ws://127.0.0.1:17210"

        # 创建 RPC 客户端
        client = RpcClient(url=url)

        # 连接到节点
        await client.connect()

        result = {}

        if query_type == "dag-info":
            dag_info = await client.get_block_dag_info()
            print(dag_info)
            # 假设 dag_info 是 dict 类型，使用字典访问
            result = {
                "network": dag_info.get("network", "未知"),
                "block_count": dag_info.get("blockCount", "未知"),
                "pruning_point_hash": dag_info.get("pruningPointHash", "未知"),
                "virtual_parents_count": len(dag_info.get("virtualParentHashes", [])),
                "virtual_daa_score": dag_info.get("virtualDaaScore", "未知")
            }

        elif query_type == "node-info":
            node_info = await client.get_info()
            print(node_info)
            # node_info 也是 dict
            result = {
                "server_version": node_info.get("serverVersion", "未知"),
                "is_synced": node_info.get("isSynced", False)
            }

        else:
            result = {"error": "不支持的查询类型 / Unsupported query type"}

        return result

    except Exception as e:
        return {"error": f"查询失败: {str(e)} / Query failed: {str(e)}"}
    finally:
        if 'client' in locals():
            await client.disconnect()


def format_response(data: Dict[str, Any], query_type: str) -> str:
    """
    将查询结果格式化为自然语言回复（中英文双语）
    Format query result into natural language response (bilingual)
    """
    if "error" in data:
        return f"查询失败：{data['error']}"

    if query_type == "dag-info":
        return (
            f"Kaspa 测试网 DAG 状态：\n"
            f"网络类型：{data.get('network', '未知')} \n"
            f"区块总数：{data.get('block_count', '未知')} \n"
            f"修剪点哈希：{data.get('pruning_point_hash', '未知')} \n"
            f"虚拟父节点数量：{data.get('virtual_parents_count', '未知')} \n"
            f"虚拟 DAA 分数：{data.get('virtual_daa_score', '未知')} \n\n"
            f"Kaspa Testnet DAG status:\n"
            f"Network: {data.get('network', 'Unknown')} \n"
            f"Block count: {data.get('block_count', 'Unknown')} \n"
            f"Pruning point hash: {data.get('pruning_point_hash', 'Unknown')} \n"
            f"Virtual parents count: {data.get('virtual_parents_count', 'Unknown')} \n"
            f"Virtual DAA score: {data.get('virtual_daa_score', 'Unknown')}"
        )

    elif query_type == "node-info":
        return (
            f"Kaspa 节点信息：\n"
            f"服务器版本：{data.get('server_version', '未知')} \n"
            f"是否已同步：{'是' if data.get('is_synced') else '否'} \n\n"
            f"Node info:\n"
            f"Server version: {data.get('server_version', 'Unknown')} \n"
            f"Synced: {'Yes' if data.get('is_synced') else 'No'}"
        )

    return "未知查询类型 / Unknown query type"


def execute(input_text: str) -> str:
    """
    OpenClaw skill 主入口函数
    Main entry point for OpenClaw skill
    """
    input_lower = input_text.lower()

    # 根据输入判断查询类型
    if any(word in input_lower for word in ["dag", "区块", "daa", "virtual"]):
        query_type = "dag-info"
    else:
        query_type = "node-info"

    # 异步执行查询
    loop = asyncio.get_event_loop()
    raw_data = loop.run_until_complete(query_kaspa_rpc(query_type))

    # 格式化并返回回复
    return format_response(raw_data, query_type)


# 本地测试入口
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        test_input = " ".join(sys.argv[1:])
        print("测试输入:", test_input)
        print(execute(test_input))
    else:
        print(execute("查询 Kaspa DAG"))
        print("\n--- 分隔 ---")
        print(execute("Kaspa 节点状态"))