
import json
import os
if os.path.exists('history.json'):
    with open('history.json', 'r') as f:
        history = json.load(f)
else:
    history = {}
try:
    i =int(list(history.keys())[-1])
except:
    i = 0
i+=1
running = True
while running:
    inputt = input()
    if inputt == 'end'.lower():
        running=False
    else:
        answer = eval(inputt)
        print(answer)
        whole = f"{inputt} = {answer}"
        history[int(i)] = whole
    i+=1
with open('history.json', 'w') as file:
    json.dump(history, file, indent=4)