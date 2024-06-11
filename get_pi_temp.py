import subprocess

# Define the command as a list of strings
command = ["vcgencmd", "measure_temp"]

# Execute the command and capture its output
result = subprocess.run(command, capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Print the output of the command
    print("Temperature:", result.stdout.strip())
else:
    # Print an error message
    print("Error executing command:", result.stderr)
