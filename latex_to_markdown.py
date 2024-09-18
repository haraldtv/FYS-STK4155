#
# Simple script to convert my latex notes to markdown used in the jupyter notebooks
#

FILENAME = "/Users/harald/Documents/GitHub/FYS-STK4155/Week38/ltm.txt"

f = open(FILENAME, "r")
# output = open(FILENAME+".md", "rw")

def findEndOfCommand(text, open_index, OpenSymbol="{", CloseSymbol="}"):
    open = 1
    close = 0
    for i in range(open_index, len(text)):
        if text[i] == OpenSymbol:
            open += 1
        elif text[i] == CloseSymbol:
            close += 1
        if open == close:
            return i
    return False

def checkAndReplaceEv(text, i):
    if (text[i] + text[i+1] + text[i+2] + text[i+3]) == "\\ev{":
        index = findEndOfCommand(text, i, "{", "}")
    return False


latex_file = f.read()
latex_file = latex_file.replace("\begin{equation}", "$$")
latex_file = latex_file.replace("\end{equation}", "$$")
latex_file = latex_file.replace("\Tilde{", "\tilde{")
# latex_arr = latex_file.replace("\n", " ")
#latex_arr = latex_file.split(' ')
for i in range(len(latex_file)):
    print(latex_file[i])
    if latex_file[i] == '\\':
        update = checkAndReplaceEv(latex_file, i)
        if update == 1:
            i = update
            break

print(latex_file)
        

#print(latex_file)

f.close()