import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sysmon_report.csv", parse_dates=["timestamp"])

# Make sure timestamp is datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Create subplots (2x2 grid → 4 plots)
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# --- Plot 1: CPU Usage ---
axs[0, 0].plot(df["timestamp"], df["cpu_usage"], label="CPU Usage (%)", color="red")
axs[0, 0].set_title("CPU Usage Over Time")
axs[0, 0].set_ylabel("CPU %")
axs[0, 0].legend()

# --- Plot 2: Memory Usage ---
axs[0, 1].plot(df["timestamp"], df["mem_used"], label="Memory Used (MB)", color="blue")
axs[0, 1].set_title("Memory Usage Over Time")
axs[0, 1].set_ylabel("Memory (MB)")
axs[0, 1].legend()

# --- Plot 3: Disk Usage ---
axs[1, 0].plot(df["timestamp"], df["disk_used"], label="Disk Used (GB)", color="green")
axs[1, 0].set_title("Disk Usage Over Time")
axs[1, 0].set_ylabel("Disk (GB)")
axs[1, 0].legend()

# --- Plot 4: Network ---
axs[1, 1].plot(df["timestamp"], df["rx_bytes"], label="RX Bytes", color="purple")
axs[1, 1].plot(df["timestamp"], df["tx_bytes"], label="TX Bytes", color="orange")
axs[1, 1].set_title("Network Usage Over Time")
axs[1, 1].set_ylabel("Bytes")
axs[1, 1].legend()

# Format layout
plt.tight_layout()

# Save to file instead of plt.show()
plt.savefig("sysmon_summary.png")

print("✅ Plots saved to sysmon_summary.png")
