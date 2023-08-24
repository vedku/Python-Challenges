import datetime


def timed_proc():
    input("type <<the lazy fox jumped over the brown dog>>:")

start_time = datetime.datetime.now()  # Starts the timer, by putting the time into start_time variable
timed_proc()  # Whatever you want to time
time_taken = datetime.datetime.now()-start_time  # Current time - start time
print("it took", time_taken, "to type <<the lazy fox jumped over the brown dog>>" )  # Printing the time it took
