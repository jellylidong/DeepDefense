__author__ = 'vcoder'

attack = open("csv/output.csv", "r")
normal = open("csv/output.csv", "r")

data_labeled = open("csv/data_label.csv", "w")


for line in attack:
    newline = ""
    newline = line + " 1"
    data_labeled.write(line)

data_labeled.close
attack.close()
normal.close()
