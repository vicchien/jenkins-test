import json
from modules.execute_subprocess import execute_subprocess

if __name__ == '__main__':
    json_result = []
    output_filename = "process_result.json"

    res = execute_subprocess("ps -Ao user,uid,comm,pid,pcpu --sort=-pcpu | head -n 10")
    for line in res["res"][1:]:
        split_data = line.split()
        json_result.append({
            "user": split_data[0],
            "uid": split_data[1],
            "command": split_data[2],
            "pid": split_data[3],
            "cpu_percent": split_data[4],
        })

    print("===== Top 10 CPU usage =====")
    for item in json_result:
        print(item)

    with open(output_filename, 'w') as outfile:
        outfile.write(json.dumps(json_result, indent=4))