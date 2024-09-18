FILENAME = "/Users/harald/Documents/GitHub/FYS-STK4155/Week38/ltm.txt"

f = open(FILENAME, "r")
# output = open(FILENAME+".md", "rw")

def convertEv(word):
    if word == "\begin{equation}" or word == "\end{equation}":
        word = "$$"
    return word


latex_file = f.read()
latex_file = latex_file.replace("\begin{equation}", "$$")
latex_file = latex_file.replace("\end{equation}", "$$")
latex_file = latex_file.replace("\Tilde{", "\tilde{")
# latex_arr = latex_file.replace("\n", " ")
#latex_arr = latex_file.split(' ')

#print(latex_arr)

f.close()