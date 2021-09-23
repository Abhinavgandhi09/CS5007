
def greet(name, msg = "Good morning"):
    print(msg + " " + name)


def main():
    greet("Kate")
    print()
    greet("Bruce", "How do you do")


if __name__ == "__main__":
    main()
