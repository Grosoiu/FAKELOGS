import random
import string

def generate_timestamp(base_hour=11, base_minute=35, base_second=0, base_millisecond=0):
    # Given base times, increment randomly
    # We'll increase time by a random number of milliseconds between 500 and 60000
    increment = random.randint(500, 60000)  # in milliseconds
    total_milliseconds = ((base_hour * 3600) + (base_minute * 60) + base_second) * 1000 + base_millisecond + increment
    
    hours = (total_milliseconds // (3600 * 1000)) % 24
    total_milliseconds %= (3600 * 1000)
    minutes = total_milliseconds // (60 * 1000)
    total_milliseconds %= (60 * 1000)
    seconds = total_milliseconds // 1000
    milliseconds = total_milliseconds % 1000
    
    return hours, minutes, seconds, milliseconds

def format_timestamp(hours, minutes, seconds, milliseconds):
    # Format as HH:MM:SS (with leading zeros)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def generate_scheduled_task_id():
    # 3-digit numeric ID
    return f"{random.randint(1, 999):03d}"

def generate_background_job_id():
    # 3-letter alphabetic ID
    return ''.join(random.choices(string.ascii_lowercase, k=3))

def generate_pid():
    # random PID-like number
    return str(random.randint(10000, 99999))

def main():
    # We will generate 100 lines.
    # The requirement: a job or task should start before being finished.
    # We'll keep track of active tasks (both scheduled and background) and randomly finish them.
    
    # Parameters
    line_count = 100
    current_hour, current_minute, current_second, current_millisecond = 11, 35, 0, 0
    
    active_tasks = []  # store tuples like (type, id, pid)
    lines = []
    
    for _ in range(line_count):
        # Update timestamp
        current_hour, current_minute, current_second, current_millisecond = generate_timestamp(
            current_hour, current_minute, current_second, current_millisecond
        )
        timestamp_str = format_timestamp(current_hour, current_minute, current_second, current_millisecond)
        
        # Decide if we start a new task or finish an existing one.
        # If there are active tasks, there's a chance we finish one.
        # Otherwise, we must start a new one.
        if active_tasks and random.random() < 0.4:
            # Finish a task
            task_type, task_id, pid = random.choice(active_tasks)
            active_tasks.remove((task_type, task_id, pid))
            if task_type == "scheduled":
                line = f"{timestamp_str},scheduled task {task_id},finished,{pid}"
            else:
                line = f"{timestamp_str},background job {task_id},finished,{pid}"
        else:
            # Start a new task
            if random.random() < 0.6:
                # Scheduled task
                task_id = generate_scheduled_task_id()
                pid = generate_pid()
                active_tasks.append(("scheduled", task_id, pid))
                line = f"{timestamp_str},scheduled task {task_id},started,{pid}"
            else:
                # Background job
                task_id = generate_background_job_id()
                pid = generate_pid()
                active_tasks.append(("background", task_id, pid))
                line = f"{timestamp_str},background job {task_id},started,{pid}"
        
        lines.append(line)
    
    # Write the lines to jobs.log
    with open("jobs.log", "w") as f:
        for l in lines:
            f.write(l + "\n")

if __name__ == "__main__":
    main()
