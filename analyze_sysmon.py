import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("sysmon_report.csv", parse_dates=["timestamp"])

# CPU Usage Plot
plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["cpu_usage"], label="CPU Usage (%)")
plt.axhline(80, color="r", linestyle="--", label="High Usage Threshold (80%)")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Memory Usage Plot
plt.figure(figsize=(10,5))
mem_percent = (df["mem_used"] / df["mem_total"]) * 100
plt.plot(df["timestamp"], mem_percent, label="Memory Usage (%)", color="orange")
plt.axhline(80, color="r", linestyle="--", label="High Usage Threshold (80%)")
plt.xlabel("Time")
plt.ylabel("Memory Usage (%)")
plt.title("Memory Usage Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Network Usage Plot
plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["rx_bytes"], label="RX Bytes", color="g")
plt.plot(df["timestamp"], df["tx_bytes"], label="TX Bytes", color="b")
plt.xlabel("Time")
plt.ylabel("Bytes")
plt.title("Network Usage Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
