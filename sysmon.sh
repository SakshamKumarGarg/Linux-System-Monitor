#!/bin/bash
# sysmon.sh System Monitor Control

report_file="sysmon_report.csv"

if [ ! -f "$report_file" ]; then
    echo "timestamp,cpu_usage,mem_used,mem_total,disk_used,disk_total,rx_bytes,tx_bytes,uptime" > "$report_file"
fi

while true
do
    clear
    echo "===== System Monitor ====="
    echo "(Press 'q' to quit)"
    echo

    # cpu usage in %
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    if (( $(echo "$cpu_usage < 50" | bc -l) )); then
        color=$(tput setaf 2)   # Green
    elif (( $(echo "$cpu_usage < 80" | bc -l) )); then
        color=$(tput setaf 3)   # Yellow
    else
        color=$(tput setaf 1)   # Red
	echo "$(tput setaf 1)⚠️  HIGH CPU Usage Detected!$(tput sgr0)"
    fi

    echo "CPU Usage: ${color}${cpu_usage}%$(tput sgr0)"

    # Showing Memory usage
    mem_total=$(free -m | awk 'NR==2 {print $2}')
    mem_used=$(free -m | awk 'NR==2 {print $3}')
    mem_free=$(free -m | awk 'NR==2 {print $4}')
    mem_percent=$(( (mem_used * 100) / mem_total ))
    echo "Memory Usage : $mem_used MB / $mem_total MB and Free memory: $mem_free MB"
    if [ $mem_percent -gt 80 ]; then
        echo "$(tput setaf 1)⚠️  HIGH Memory Usage Detected! ($mem_percent%)$(tput sgr0)"
    fi

    # Showing Disk usage
    disk_total=$(df -BG / | awk 'NR==2 {print $2}')
    disk_used=$(df -BG / | awk 'NR==2 {print $3}')
    disk_free=$(df -BG / | awk 'NR==2 {print $4}')
    echo "Disk Usage: $disk_used / $disk_total and Available space: $disk_free"

    # Uptime
    uptime_info=$(uptime -p)
    echo "Uptime: $uptime_info"
    echo

     # === Top 5 Processes (by CPU and Memory) ===
    echo "Top 5 Processes (by CPU %):"
    ps -eo pid,comm,%cpu --sort=-%cpu | head -n 6
    echo
    echo "Top 5 Processes (by Memory %):"
    ps -eo pid,comm,%mem --sort=-%mem | head -n 6
    echo

    # === Network Usage ===
    rx_bytes=$(cat /proc/net/dev | grep "eth0" | awk '{print $2}')
    tx_bytes=$(cat /proc/net/dev | grep "eth0" | awk '{print $10}')
    echo "Network (eth0): RX = ${rx_bytes} bytes, TX = ${tx_bytes} bytes"
    echo

    timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    # === CSV Logging ===
    echo "$timestamp,$cpu_usage,$mem_used,$mem_total,$disk_used,$disk_total,$rx_bytes,$tx_bytes" >> sysmon_report.csv

    # === JSON Logging ===
    cat <<EOF >> sysmon_report.json
{
  "time": "$timestamp",
  "cpu": $cpu_usage,
  "memory": {
    "used": $mem_used,
    "total": $mem_total
  },
  "disk": {
    "used": "$disk_used",
    "total": "$disk_total"
  },
  "network": {
    "rx_bytes": $rx_bytes,
    "tx_bytes": $tx_bytes
  }
},
EOF

    echo "Refreshing in 4s... (Press 'q' + Enter to quit)"
    # Wait for 4 seconds or read input
    read -t 4 -n 1 key
    if [[ $key == "q" ]]; then
	echo
        echo "Exiting System Monitor..."
        break
    fi
done

