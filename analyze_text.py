My_file = "sample.txt"  # provided the sample.txt file is in the same dir as this script.

print("Line\tChars\tUppercase\t% Upper")

with open(My_file) as f:
    i = 1
    for l in f:
        total = len(l.strip())
        upper = 0
        for c in l:
            if c.isupper():
                upper += 1
        if total != 0:
            p = upper / total * 100
        else:
            p = 0
        print(str(i) + "\t" + str(total) + "\t" + str(upper) + "\t" + str(round(p, 2)) + "%")
        i += 1
