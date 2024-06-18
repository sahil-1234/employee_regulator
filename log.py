def write_file(keys):
    global numbers_of_clicks
    with open("file.txt", "w") as f:
        for key in keys:
            numbers_of_clicks+=1
            f.write(str(numbers_of_clicks))
