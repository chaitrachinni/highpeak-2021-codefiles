
with open("sample_input.txt", "r") as input_file:
    lines = input_file.readlines()

no_of_employee =int(lines[0].split(':')[1])
lines = lines[4:]

goodies = []

for line in lines:
    val = line.split(":")
    goodies.append([val[0], int(val[1])])

goodies.sort(key = lambda x: x[1])

def get_min_diff(m):
    i = 0
    j = m-1
    ind = i
    min_so_far = goodies[j][1] - goodies[i][1]
    while(j<len(goodies)):
        diff = goodies[j][1] - goodies[i][1]
        if(diff < min_so_far):
            min_so_far = diff
            ind = i
        i+=1
        j+=1
    return (min_so_far, ind)

minimum, ind = get_min_diff(no_of_employee)

output = ["The goodies selected for distribution are:\n", "\n"]

for i in range(ind, ind+no_of_employee):
    val = ': '.join([goodies[i][0] , str(goodies[i][1])]) + "\n"
    output.append(val)

diff = "\n" + "And the difference between the chosen goodie with highest price and the lowest price is " + str(minimum)
output.append(diff)
with open("output.txt", "w") as opFile:
    opFile.writelines(output)
