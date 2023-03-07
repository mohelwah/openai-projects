import json
import os

if __name__ == "__main__":
    # genrate jsonl file form premises and scripts folders
    result = []
    for premise_filename in os.listdir("premises"):
        with open("premises/%s" % premise_filename, "r", encoding="utf-8") as f1:
            premise = f1.read()
        script_filename = premise_filename.replace("premise", "script")
        with open("scripts/%s" % script_filename, "r", encoding="utf-8") as f2:
            script = f2.read()
        info = {"prompt": premise + "\n\nSCRIPT: ", "completion": " " + script}
        result.append(info)
    with open("movieScriptGenerator.jsonl", "w", encoding="utf-8") as f:
        for info in result:
            json.dump(info, f)
            f.write("\n")
