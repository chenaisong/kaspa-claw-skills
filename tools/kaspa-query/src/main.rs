use kaspa_wrpc_client::{client::{KaspaRpcClient, ConnectOptions}, resolver::Resolver, WrpcEncoding};
use kaspa_consensus_core::network::{NetworkId, NetworkType};
use kaspa_wrpc_client::prelude::RpcApi;
use anyhow::Result;
use std::time::Duration;
use serde_json::json;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let url = "ws://127.0.0.1:17210";

    // 方式一：new 时传 url（推荐，简单）
    let client = KaspaRpcClient::new(
        WrpcEncoding::Borsh,                          // 或 Json，根据节点配置
        Some(url),
        None,                                         // resolver 可选
        Some(NetworkId::with_suffix(NetworkType::Testnet, 10)),
        None,
    )?;

    //println!("客户端已创建，正在连接...");

    let options = ConnectOptions {
        block_async_connect: true,                    // true = 阻塞等待连接成功
        connect_timeout: Some(Duration::from_secs(15)),
        retry_interval: Some(Duration::from_secs(3)), // 可选：失败重试间隔
        ..Default::default()
    };

    client.connect(Some(options)).await?;

    // 查询 DAG 信息
    let dag_result = client.get_block_dag_info().await;
    let node_result = client.get_info().await;

    let output = json!({
        "dag_info": match dag_result {
            Ok(info) => json!({
                "network": format!("{:?}", info.network),
                "block_count": info.block_count,
                "pruning_point_hash": info.pruning_point_hash.to_string(),
                "virtual_parents_count": info.virtual_parent_hashes.len(),
                "virtual_daa_score": info.virtual_daa_score
            }),
            Err(e) => json!({"error": e.to_string()})
        },
        "node_info": match node_result {
            Ok(info) => json!({
                "server_version": info.server_version,
                "is_synced": info.is_synced
            }),
            Err(e) => json!({"error": e.to_string()})
        }
    });

    // 只输出 JSON（无额外文本）
    println!("{}", output);

    client.disconnect().await?;
    Ok(())
}