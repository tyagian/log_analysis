import timeit
from collections import defaultdict 
def analyze_logs(input_time1:float, input_time2:float, input_filename: str) -> str:

    print ("Between time", input_time1," & ",input_time2,":")
    total_request = 0
    fail_req = 0 
    with open(input_filename,'r') as logs:
        lines = logs.readlines()
        domain_status = defaultdict(int)
        http_status = 500
        for line in lines:
            #print (line)
            if  (float(line.split('|')[0]) > input_time1 and float(line.split('|')[0]) < input_time2):
                total_request += 1
                if int(line.split('|')[4]) == http_status:
                    fail_req += 1
                    domain_status[str(line.split('|')[2]).strip()] = (fail_req/total_request)*100
                #domain_status[line.split('|')[2]] += total_request
    return domain_status
input_time1 = 1493969101.639
input_time2 = 1493969101.660
input_filename = 'logs.txt'
s = analyze_logs(input_time1, input_time2, input_filename)
print (s)