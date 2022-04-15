import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f"Hello {sys.argv[1]} and {sys.argv[2]}")
        print(f"Goodbye {sys.argv[2]} and {sys.argv[1]}")
    else:
        print("Usage: HelloGoodbye name-1 and name-2")