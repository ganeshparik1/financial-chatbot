
def simple_chatbot(user_query):
    # Predefined responses based on financial data
    if user_query.lower() == "what is the total revenue?":
        return "The total revenue is $365.82B."
    elif user_query.lower() == "what is the net income?":
        return "The net income is $94.68B."
    elif user_query.lower() == "what is the cash flow from operating activities?":
        return "The cash flow from operating activities is $104.04B."
    elif user_query.lower() == "how has revenue changed over the last year?":
        return "The revenue has increased by 10% over the last year."
    elif user_query.lower() == "how has net income changed over the last year?":
        return "The net income has increased by 8% over the last year."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Main interaction loop
if __name__ == "__main__":
    print("Welcome to the financial chatbot! You can ask me predefined queries.")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        response = simple_chatbot(user_query)
        print("Bot:", response)
