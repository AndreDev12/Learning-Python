def variable_length(*args):
    print(args)

print(variable_length())
print(variable_length('one', 'two'))
print(variable_length(None))
print(variable_length(True, 70, 'pro'))

#########################################
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))