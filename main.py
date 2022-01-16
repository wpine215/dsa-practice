from graph.main import main as graph_main
from tree.main import main as tree_main

from PyInquirer import prompt, Separator, print_json

scripts = {
    "tree": tree_main,
    "graph": graph_main,
}

questions = [
    {
        "type": "rawlist",
        "name": "script",
        "message": "Which script do you want to run?",
        "choices": [
            "Help",
            Separator(),
            "Tree",
            "Graph",
        ],
        'filter': lambda val: val.lower(),
        'validate': lambda val: val.lower() in scripts.keys()
    },
]

answers = prompt(questions)
print(Separator())
s = answers['script']
if s == "help":
    print("Help placeholder")
else:
    scripts[s]()
    