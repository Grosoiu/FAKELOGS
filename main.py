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
        "InventoryService",
        "UserAuthModule",
        "PaymentProcessor",
        "AnalyticsEngine",
        "LogAggregator",
        "MessagingQueue",
        "WorkflowOrchestrator"
    ]
    return random.choice(app_names)

def choose_pid():
    # Return a pseudo-random PID
    return str(random.randint(1000, 9999))

def choose_log_level():
    # Weighted random distribution of log levels (if desired)
    # For example, more Informational than Warn and more Warn than Critical
    levels = ["Informational", "Informational", "Informational", "Warn", "Warn", "Critical"]
    return random.choice(levels)

def generate_log_message(level, app):
    # Generate a semi-random log message.
    # Feel free to expand this with more complexity.
    
    # Some sample messages that could appear in logs:
    base_messages = [
        "Initialized module successfully",
        "Connection to database established",
        "User login attempt succeeded",
        "Cache miss occurred",
        "Processed request in {time_spent}ms",
        "Configuration value not found, using defaults",
        "File {filename} not found in directory",
        "Performance threshold exceeded: {metric} at {value}",
        "Background task {task_id} completed with warnings",
        "Reconnected to service after {retries} retries",
        "Unexpected input format encountered"
    ]
    
    msg = random.choice(base_messages)
    
    # Introduce some variable placeholders
    msg = msg.replace("{time_spent}", str(random.randint(5, 3000)))
    msg = msg.replace("{metric}", random.choice(["CPU load", "memory usage", "latency"]))
    msg = msg.replace("{value}", str(random.uniform(0.1, 99.9)))
    msg = msg.replace("{filename}", f"file_{random.randint(1,100)}.cfg")
    msg = msg.replace("{task_id}", str(uuid.uuid4()).split("-")[0])
    msg = msg.replace("{retries}", str(random.randint(1,5)))
    
    # Add extra detail depending on the log level
    if level == "Warn":
        msg += " [Warning Code: W" + str(random.randint(100,999)) + "]"
    elif level == "Critical":
        msg += " [Error Code: E" + str(random.randint(1000,9999)) + "]"
        
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
    # 2024-12-19T12:34:56.789Z [AppName] [PID:1234] [Informational] Initialized module successfully
    # You can also rearrange the order of fields if you prefer.
    log_line = f"{timestamp} [{app_name}] [PID:{pid}] [{level}] {message}"
    return log_line

def main():
    output_file = "fake_application.log"
    num_lines = 100  # Number of log lines to generate
    delay_between_lines = 0.1  # Seconds between lines, can be 0 for no delay
    
    with open(output_file, "w", encoding="utf-8") as f:
        for _ in range(num_lines):
            line = generate_log_line()
            f.write(line + "\n")
            # Optionally print to stdout
            print(line)
            # Delay between lines to simulate real-time logging
            time.sleep(delay_between_lines)

if __name__ == "__main__":
    main()
