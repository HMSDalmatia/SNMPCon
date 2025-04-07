import functions

data = []
with open('config.txt','r') as file:
    line = file.readline().strip()
    while len(line) > 0:
        if line[0] != '#':
            data.append(line)
    line = file.readline().strip()

net_addr = data[0].split(".")
mask = data[1].split(".")
to_check=[]
for i in mask:
    helper_in_count = 255-int(i)
    to_check.append(helper_in_count)

