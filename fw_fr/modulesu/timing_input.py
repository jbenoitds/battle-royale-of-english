import threading

# Function to get user input with a timeout
def timed_input(prompt, timeout):
    # This will be used to store the user input
    user_input = [None]

    def input_thread():
        user_input[0] = input(prompt)

    # Start the input thread
    thread = threading.Thread(target=input_thread)
    thread.start()

    # Wait for the specified timeout or until the input thread finishes
    thread.join(timeout)

    # If the thread is still alive after timeout, it means no input was received
    if thread.is_alive():
        # We can terminate the thread, but it's a bit tricky. Instead, we handle no input case.
        return None
    else:
        return user_input[0]