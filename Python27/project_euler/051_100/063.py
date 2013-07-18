def p():
    ans = set()
    i = 1
    prev_count = 0
    
    while True:
        j = 1
        temp = i ** j

        while len(str(temp)) == j:
            ans.update([i**j])
            j += 1
            temp = i ** j
            #print i,j, temp
        else:
            i += 1
            
        if len(ans) != prev_count:
            print "Count = %d"%(len(ans))
            prev_count = len(ans)
        else:
            break


p()
