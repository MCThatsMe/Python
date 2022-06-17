def show_messages(og_message, done):
    while og_message:
        original = og_message.pop()
        print(original)
        done.append(original)
    
def sent_messages(sent):
    print("\nThe following message have been sent:")
    for done in sent:
        print(done)



messages = ["Hi how are you", "Good, thank you", "Okay then goodbye", "Whoah Nelly"]
sent_message = []

print(messages)
print(sent_message)

show_messages(messages, sent_message)
sent_messages(sent_message[:])