def greet_user(name):
    """根据用户名字生成问候语"""
    if not name or name.strip() == "":
        return "Hello! Welcome to our project!"
    else:
        return f"Hello, {name}! Welcome to our project!"

if __name__ == "__main__":
    user_name = input("Please enter your name: ")
    print(greet_user(user_name))