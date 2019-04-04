import os

for dir in os.listdir("ExampleDataset"):
    path = "ExampleDataset/" + dir
    if os.path.isdir(path):
        for file in os.listdir(path):
            path = "ExampleDataset/" + dir + "/" + file
            print(path)
            if os.path.isfile(path) and path[-1].isdigit():
                os.rename(path, path + ".jpg")
