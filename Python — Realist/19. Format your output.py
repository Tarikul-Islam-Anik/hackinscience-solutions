def list_pretty_print(items):
    for i in range(0, len(items), 5):
        print(*items[i:i+5],sep=', ')