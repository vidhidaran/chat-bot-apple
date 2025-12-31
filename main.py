#project config
import google.generativeai as genai

genai.configure(api_key="AIzaSyB7wUd5deSKXjZ5HjJJ8aakH_jISsmkCNk")

apple=genai.GenerativeModel("gemini-2.5-flash")
chat=apple.start_chat(history=[])
print("Heyy, iam chat-bot")

while True:
    user_input=input("User : ")
    if user_input.lower()=="bye":
        break

    response=chat.send_message(user_input)
    print("Apple:",response.text)
    
