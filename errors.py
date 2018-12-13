def exit_failure(msg):
    print(msg)
    sys.exit()

def exit_usage():
    exit_failure("Usage: describe.py [csv file name]")