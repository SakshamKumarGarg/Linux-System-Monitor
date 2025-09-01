#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# === Read CSV ===
df = pd.read_csv("sysmon_report.csv", parse_dates=["timestamp"])

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# === CPU Usage Plot ===
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["cpu_usage"], label="CPU Usage (%)", color="red")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("cpu_usage.png")
print("✅ Saved cpu_usage.png")

# === Memory Usage Plot ===
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["mem_used"], label="Memory Used (MB)", color="blue")
plt.plot(df["timestamp"], df["mem_total"], label="Total Memory (MB)", linestyle="--", color="gray")
plt.xlabel("Time")
plt.ylabel("Memory (MB)")
plt.title("Memory Usage Over Time")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("memory_usage.png")
print("✅ Saved memory_usage.png")

# === Disk Usage Plot ===
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["disk_used"], label="Disk Used (GB)", color="green")
plt.plot(df["timestamp"], df["disk_total"], label="Total Disk (GB)", linestyle="--", color="gray")
plt.xlabel("Time")
plt.ylabel("Disk (GB)")
plt.title("Disk Usage Over Time")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("disk_usage.png")
print("✅ Saved disk_usage.png")

# === Network Usage Plot ===
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["rx_bytes"], label="RX Bytes", color="purple")
plt.plot(df["timestamp"], df["tx_bytes"], label="TX Bytes", color="orange")
plt.xlabel("Time")
plt.ylabel("Bytes")
plt.title("Network Usage Over Time")
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()
plt.savefig("network_usage.png")
print("✅ Saved network_usage.png")
