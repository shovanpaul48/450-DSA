        sum1 = sum2  = 0 
        a,b = len(l1), len(l2)

        if a == b:
            for i in range(a -1):
                sum1 = sum1 + (l1[i] * 10)
                sum2 = sum2 + (l2[i] * 10)
            
            sum1 = sum1 + l1[a-1]
            sum2 = sum2 + l2[a-1]

        