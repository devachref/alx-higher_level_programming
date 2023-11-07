#!/usr/bin/python3
if __name__ == "__main__":
    """print all hidden directories"""
    import hidden_4

    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
