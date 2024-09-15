import emoji

def emoji_to_text(emoji_str):
    text = emoji.demojize(emoji_str)
    return text


if __name__ == "__main__":
    user_input = input("Enter a text with emoji: ")
    result = emoji_to_text(user_input)
    print(f"Text with emojis converted: {result}")
