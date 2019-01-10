def count_ant(line):
    tmp=1;s=""
    if len(line)==1:
        return line[0]+"1"
    for i in range((len(line)-1)):
        if line[i]==line[i+1]:
            tmp+=1    
        else:
            s+=line[i]+str(tmp)
            tmp=1
    s+=line[-1]+str(tmp)
    return s

def cal_ant(n):
    if n==1:
        print("1")
        return "1"
    prev = cal_ant(n-1)
    s=count_ant(prev)
    print(s)
    return s

if __name__ == '__main__':
    MAX_LOOP = int(input("Enter the number of lines: "))
    cal_ant(MAX_LOOP)
