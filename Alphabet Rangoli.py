def print_rangoli(size):
    counter=size
    size-=1
    size+=counter
    width=size
    size-=1
    width+=size
    count=1
    list=[]
    for x in range(1,counter+1):
        str=str_maker(x,count,counter)
        count+=2
        var=str.center(width,"-")
        list.insert(0,var)
        print(var)
    for x in range(1,len(list)):
        print(list[x])

def str_maker(line_number,count,size):
    alphbet="abcdefghijklmnopqrstuvwxyz"
    string=alphbet[0:size]
    width=3
    mod=int(count/2)
    if line_number==1:
        i=len(string)-line_number
        return string[i]
    else:
        val=""
        i=len(string)-line_number
        temp=i
        temp+=1
        for x in range(mod):
            if val=="":
                val=string[i].center(width,string[temp])
                temp+=1
                width+=2
            else:
                val=val.center(width,string[temp])
                temp+=1
                width+=2

        var="-".join(val)
        return var


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
