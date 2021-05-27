import subprocess

def execute_subprocess(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, stderr=subprocess.STDOUT)
        process_stdout = []
        while True:
            line = process.stdout.readline()
            if not line:
                break
            process_stdout.append(line.rstrip().decode())
        return_code = process.wait()
        return {
            "status": return_code,
            "res": process_stdout,
        }
    except Exception as e:
        return {
            "status": False,
            "res": str(e),
        }