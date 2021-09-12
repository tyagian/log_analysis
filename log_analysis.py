import sys

def analyze_logs(input_time1: float, input_time2: float, input_filename: str) -> dict:
    print ("Between time", input_time1," & ",input_time2,":")
    with open(input_filename,'r') as logs:
        lines = logs.readlines()
        log_lines = {}
        for line in lines:
            if  (float(line.split('|')[0]) > input_time1 and float(line.split('|')[0]) < input_time2):
                domain_name = str(line.split('|')[2]).strip()
                status = line.split('|')[4].strip()
                is_5xx = status.startswith('50')
                if domain_name not in log_lines:
                    log_lines[domain_name] = {
                        "total": 1,
                        "5xx" : 1 if is_5xx else 0
                    }
                else: 
                    val = log_lines[domain_name]
                    val["total"] += 1
                    val["5xx"] += 1 if is_5xx else 0
                    log_lines[domain_name] = val
    return log_lines

if __name__ == '__main__':

    if len(sys.argv) != 4:
        raise Exception("Please use readme to check the correct order of & type arguments to use")
    else:
        input_filename = sys.argv[1]
        input_time1 = float(sys.argv[2])
        input_time2 = float(sys.argv[3])
    
    log_lines = analyze_logs(input_time1, input_time2, input_filename)

    for k,v in log_lines.items():
        percent = round(v["5xx"]/v["total"],2)
        print (f"{k} returned {percent}% of 5xx errors")
