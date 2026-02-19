use kaspa_wrpc_client::client::{ConnectOptions, KaspaRpcClient};
use workflow_rpc::encoding::Encoding as WrpcEncoding;
use kaspa_wrpc_client::prelude::NetworkId;
use kaspa_rpc_core::api::rpc::RpcApi;
use anyhow::Result;
use std::time::Duration;

#[tokio::main]
async fn main() -> Result<()> {
    println!("正在连接 Kaspa Testnet10 通过 wRPC...");
    println!("URL: ws://127.0.0.1:17210");

    let url = "ws://127.0.0.1:17210";

    let client = KaspaRpcClient::new(
        WrpcEncoding::Borsh,
        Some(url),
        None,
        Some(NetworkId::with_suffix(kaspa_consensus_core::network::NetworkType::Testnet, 10)),
        None,
    )?;

    println!("客户端已创建，正在连接...");

    let options = ConnectOptions {
        block_async_connect: true,   // 阻塞直到连接成功
        connect_timeout: Some(Duration::from_secs(15)),
        ..Default::default()
    };

    match client.connect(Some(options)).await {
        Ok(_) => println!("连接成功！"),
        Err(e) => {
            println!("连接失败: {:?}", e);
            return Ok(());
        }
    }

    println!("尝试查询 DAG 信息...");
    match client.get_block_dag_info().await {
        Ok(dag_info) => {
            println!("DAG 信息:");
            println!("  网络类型: {:?}", dag_info.network);
            println!("  区块总数: {}", dag_info.block_count);
            println!("  修剪点哈希: {}", dag_info.pruning_point_hash);
            println!("  虚拟父节点数量: {}", dag_info.virtual_parent_hashes.len());
            println!("  虚拟 DAA 分数: {}", dag_info.virtual_daa_score);
        }
        Err(e) => {
            println!("查询失败: {:?}", e);
        }
    }

    // 示例2: 获取节点信息（使用 get_info 替代 get_node_info）
    // Example 2: Get node info (use get_info instead of get_node_info)
    match client.get_info().await {
        Ok(info) => {
            println!("\n=== 节点信息 / Node Info ===");
            println!("Node version: {}", info.server_version);
            println!("Is synced: {}", info.is_synced);
        }
        Err(e) => println!("Failed to get node info: {}", e),
    }


    client.disconnect().await?;
    Ok(())
}