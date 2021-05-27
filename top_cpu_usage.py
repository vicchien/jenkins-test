import json
from modules.execute_subprocess import execute_subprocess
from modules.send_mail import send_mail
import sys

if __name__ == "__main__":
    json_result = []
    output_filename = "process_result.json"
    top_count = sys.argv[1]
    kill_or_not = sys.argv[2]

    res = execute_subprocess(f"ps -Ao user,uid,comm,pid,pcpu --sort=-pcpu | head -n {int(top_count)+1}")
    for line in res["res"][1:]:
        split_data = line.split()
        json_result.append({
            "user": split_data[0],
            "uid": split_data[1],
            "command": split_data[2],
            "pid": split_data[3],
            "cpu_percent": split_data[4],
        })

    print(f"===== Top {top_count} CPU usage =====")
    for item in json_result:
        print(item)
        if kill_or_not == "true":
            print(f"Kill process {item['pid']}")
            res = execute_subprocess(f"sudo kill {item['pid']}")

    with open(output_filename, "w") as outfile:
        outfile.write(json.dumps(json_result, indent=4))


    send_mail("gn01809864@gmail.com", json.dumps(json_result, indent=4))