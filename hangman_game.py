def read_data():
    try:
        # Open data.txt from this folder
        with open("./data.txt", "r", encoding="utf-8") as f:
            # Strip the lines of the data
            data = [line.strip() for line in f]
        # Put it in dictionary, with enumerate function
        # This will give to each line a number, and it will be his index
        data = {key: value for key, value in enumerate(data)}
        return data
    except:
        # If can't open it, print an error and quit
        print("Can't find the data named 'data.txt', please try again")
        quit()


def run():
    pass


if __name__ == '__main__':
    print(read_data())
