from random import randint
sources = 640000 # Control the total number of webpages
max_links = 30 # Control the maximum number of links that each page can have
with open("graph640000", "w") as f: # Change the name of output file here
    for i in range(sources):
        dests = ""
        num_links = randint(1,max(max_links,1))
        for _ in range(num_links):
            dest = i
            while dest == i:
                dest = randint(1, sources)
            dests += str(dest) + ","
        dests = dests[:-1]
        if i != sources - 1:
            result = "{} {}\n".format(i, dests)
        elif i == sources - 1:
            result = "{} {}".format(i, dests)
        f.write(result)