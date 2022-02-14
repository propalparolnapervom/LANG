###############################
# Count symbols in the message
###############################

# Set up some message
message = 'This is a test message.'

# Initialize empty dictionary
count = {}

# For each symbol in the message ...
for symbol in message:
    # ... if the symbol IS NOT present in the dictionary yet,
    # use `setdefault` to add its count as 0,
    count.setdefault(symbol, 0)

    # ... if the symbol IS already present,
    # increase its value by 1
    count[symbol] = count[symbol] + 1

# Show final dictionary
print(count)
