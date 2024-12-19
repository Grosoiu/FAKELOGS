import random
import time
import datetime
import uuid

def generate_timestamp():
    # Returns a current timestamp in ISO 8601 format
    return datetime.datetime.utcnow().isoformat() + "Z"

def choose_app_name():
    # Choose an application name from a predefined list
    app_names = [
        "1C Connect for Windows",
        "AC Desktop",
        "AcrobatReader"
        "Atom",
        "Audacity",
        "Bussiness Intelligence",
        "Cmake",
        "ColdFusion",
        "EdgeWebDriver",
        "EPMMaestro",
        "EuroClear",
        "EverNote",
        "Figma",
        "Github Desktop",
        "Gitlab Runners",
        "Grafana",
        "Prometheus",
        "IAccessSolution",
        "IntellijIdea",
        "Java JDK 1.7",
        "JavaProfiler",
        "JSONViewer",
        "Lazarus",
        "LCORE",
        "Grafana Enterprise",
        "GSView",
        "HPP Printer Driver",
        "Insomnia Free",
        "Insomnia Enterprise",
        "iReport",
        "Matlab",
        "OpenStudio",
        "OpenVPN"
    ]
    return random.choice(app_names)

def choose_pid():
    # Return a pseudo-random PID
    return str(random.randint(1000, 9999))

def choose_log_level():
    # Weighted random distribution of log levels (if desired)
    levels = ["Informational", "Informational", "Informational", "Warn", "Warn", "Critical"]
    return random.choice(levels)

def generate_log_message(level, app):
    # Define separate message pools for each log level
    informational_messages = [
        "Module initialized successfully",
        "Cache refreshed without issues",
        "User session established",
        "Data synchronization completed",
        "Heartbeat signal received",
        "Metrics collected successfully",
        "Configuration loaded",
        "Periodic cleanup task finished",
        "User preferences updated",
        "Processed request in {time_spent}ms",
        # 10 additional informational messages:
        "Service uptime stable for {time_spent}ms",
        "Configuration parameter in {filename} validated",
        "Request {task_id} processed successfully",
        "Scheduled maintenance task {task_id} executed without errors",
        "Email notification dispatched (took {time_spent}ms)",
        "New user registration completed",
        "Connection pool resized: current {value} usage",
        "Resource usage remains below {metric} thresholds",
        "Report generation finished (File: {filename})",
        "Application memory footprint stable"
    ]
    
    warning_messages = [
        "Cache miss occurred; fallback to default values",
        "High memory usage detected: {value}% of {metric}",
        "Slow response time: {time_spent}ms exceeds threshold",
        "Possible inconsistent state detected in {filename}",
        "User login attempt rate unusually high",
        "Retrying connection to external service",
        "Partial data received from upstream service",
        "Background task {task_id} completed with non-fatal errors",
        "Deprecated API used by client",
        "Request queue length approaching limit",
        "Configuration parameter is missing; using fallback",
        "Network latency spike: {time_spent}ms observed",
        "Resource utilization nearing saturation point",
        "Unexpected null response encountered in function",
        "Disk space running low: 512MB remaining"
    ]
    
    critical_messages = [
        "Database connection failed unexpectedly",
        "Unrecoverable error in payment processing [Error Code: E{code}]",
        "Fatal exception: stack trace generated",
        "Application out of memory; shutting down",
        "Security breach detected: unauthorized access attempt",
        "Cluster node unreachable: potential network partition",
        "Critical data corruption detected in storage layer",
        "Severe latency spike observed: {time_spent}ms",
        "Primary service endpoint returned HTTP 500 repeatedly",
        "Data loss event: replication failed on multiple nodes",
        "Memory corruption detected in critical heap segment",
        "Irrecoverable disk I/O error on {filename}",
        "Service dependency chain broken, forced failover initiated",
        "Encryption key compromised, immediate rotation required",
        "Network isolation detected on primary cluster node",
        "Critical transaction rollback failed; data integrity at risk",
        "Major security breach: multiple user accounts compromised",
        "Zero-day exploit detected, emergency patch required",
        "Inconsistent state transition in distributed state machine",
        "Severe {metric} overload at {value}%, triggering emergency throttle"
    ]
    
    # Choose a base message depending on the level
    if level == "Informational":
        msg = random.choice(informational_messages)
    elif level == "Warn":
        msg = random.choice(warning_messages)
    else:
        msg = random.choice(critical_messages)
    
    # Introduce variable placeholders into messages
    msg = msg.replace("{time_spent}", str(random.randint(5, 3000)))
    msg = msg.replace("{metric}", random.choice(["CPU load", "memory usage", "latency"]))
    msg = msg.replace("{value}", str(round(random.uniform(40.0, 99.9), 2)))
    msg = msg.replace("{filename}", f"file_{random.randint(1,100)}.cfg")
    msg = msg.replace("{task_id}", str(uuid.uuid4()).split("-")[0])
    msg = msg.replace("{code}", str(random.randint(1000,9999)))
    
    # Add additional detail for non-informational levels
    if level == "Warn":
        msg += f" [Warning Code: W{random.randint(100,999)}]"
    elif level == "Critical":
        msg += f" [Critical Error Code: E{random.randint(1000,9999)}]"
        
    # Possibly add some user context
    if random.random() < 0.3:
        msg += f" [UserID: {random.randint(10000,99999)}]"
    
    return msg

def generate_log_line():
    timestamp = generate_timestamp()
    app_name = choose_app_name()
    pid = choose_pid()
    level = choose_log_level()
    message = generate_log_message(level, app_name)
    
    # Construct the log line
    # Format example:
    # 2024-12-19T12:34:56.789Z [AppName] [PID:1234] [Informational] Message text...
    log_line = f"{timestamp} [{app_name}] [PID:{pid}] [{level}] {message}"
    return log_line

def main():
    output_file = "fake_application.log"
    num_lines = 4000  # Number of log lines to generate
    delay_between_lines = 0  # Seconds between lines, can be 0 for no delay
    
    with open(output_file, "w", encoding="utf-8") as f:
        for _ in range(num_lines):
            line = generate_log_line()
            f.write(line + "\n")
            # Optionally print to stdout
            # print(line)
            # Delay between lines to simulate real-time logging
            time.sleep(delay_between_lines)

if __name__ == "__main__":
    main()
