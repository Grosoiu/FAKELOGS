import random
import time
import datetime
import uuid

def choose_app_name():
    # Choose an application name from a predefined list
    app_names = [
        "1C Connect for Windows",
        "AC Desktop",
        "AcrobatReader",
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
    # Weighted random distribution of log levels
    levels = ["Informational", "Informational", "Informational", "Warn", "Warn", "Critical"]
    return random.choice(levels)

def generate_log_message(level, app):
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
        # Additional informational messages:
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
        "Cluster node unreachable: potential network partition",
        "Severe latency spike observed: {tim-+61+e_spent}ms",
        "Primary service endpoint returned HTTP 500 repeatedly",
        "Data loss event: replication failed on multiple nodes",
        "Memory corruption detected in critical heap segment",
        "Irrecoverable disk I/O error on {filename}",
        "Service dependency chain broken, forced failover initiated",
        "Network isolation detected on primary cluster node",
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
    
    # Replace placeholders
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

def generate_simple_timestamp():
    # For the simple logs, we'll just return hh:mm:ss,xxx style from the current_time as well
    # We'll still base this on a global current_time for consistency.
    # We'll just format the current_time differently.
    global current_time_simple
    return current_time_simple.strftime("%H:%M:%S,%f")[:-3]  # %f is microseconds, so we slice to get milliseconds

def generate_simple_log_line():
    tasks = [
        "scheduled task 002", "scheduled task 947", "background job xyz", "background job abc"
    ]
    pid = random.randint(10000, 99999)
    task = random.choice(tasks)
    status = random.choice(["started", "finished"])
    duration = random.randint(1, 7000) if status == "finished" else None
    timestamp = generate_simple_timestamp()
    
    log_line = f"{timestamp}, {task} {status}, {pid}"
    if status == "finished" and duration > 5000:
        log_line += f" -- warning as over 5 seconds duration"
    return log_line

def main():
    output_file = "fake_application.log"
    num_lines = 4000  # Number of log lines to generate
    delay_between_lines = 0  # Seconds between lines, can be 0
    
    
    # We define a starting time at the beginning of November 2024
    # and we will increment it for each log line to ensure they are consecutive.
    start_time = datetime.datetime(2024, 11, 1, 0, 0, 0)
    end_time = datetime.datetime(2024, 11, 7, 23, 59, 59)
    current_time = start_time
    


    
    with open(output_file, "w", encoding="utf-8") as f:
        for _ in range(num_lines):
            # Increment current_time by a random number of seconds to ensure a random but increasing sequence
            increment_seconds = random.randint(1, 120)  # random increment between lines
            current_time += datetime.timedelta(seconds=increment_seconds)
            # Ensure we don't pass the end_time, but if we do, just break
            if current_time > end_time:
                break
            timestamp = current_time.isoformat() + "Z"
            
            app_name = choose_app_name()
            pid = choose_pid()
            level = choose_log_level()
            message = generate_log_message(level, app_name)
            
            log_line = f"{timestamp} [{app_name}] [PID:{pid}] [{level}] {message}"
            f.write(log_line + "\n")
            time.sleep(delay_between_lines)

    # with open(simple_output_file, "w", encoding="utf-8") as f:
    #     for _ in range(simple_lines):
    #         # Increment for the simple logs as well
    #         increment_seconds = random.randint(1, 60)  # smaller increments for simple logs
    #         current_time_simple += datetime.timedelta(seconds=increment_seconds)
    #         if current_time_simple > end_time:
    #             break
    #         line = generate_simple_log_line()
    #         f.write(line + "\n")
    #         time.sleep(delay_between_lines)

if __name__ == "__main__":
    main()
