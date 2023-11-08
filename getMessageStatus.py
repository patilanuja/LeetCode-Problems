# In this task, a basic message delivery service is to be implemented that has a rate-limiting algorithm that drops any message that has already arrived in the last k seconds.

#Given the integer k, a list of messages as an array of n strings, messages, and a sorted integer array timestamps representing the time at which the message arrived, for each message report the string "true" if the message is delivered and "false" otherwise.

def deliver_messages(k, messages, timestamps):
    delivered_messages = []
    last_delivered_timestamps = {} 

    for i, (timestamp, message) in enumerate(zip(timestamps, messages)):
        message_type = message[0]  

        if message_type not in last_delivered_timestamps or (timestamp - last_delivered_timestamps[message_type]) >= k:
            last_delivered_timestamps[message_type] = timestamp
            delivered_messages.append("true")
        else:
            delivered_messages.append("false")

    return delivered_messages



n = 6
timestamps = [1, 4, 5, 10, 11, 14]
messages = ["Hello", "Bye", "Bye", "Hello", "Bye", "Hello"]
print(deliver_messages(n, messages, timestamps))
#output = ['true', 'true', 'false', 'true', 'false', 'false']
    