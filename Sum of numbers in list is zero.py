def check_sum(num_list):
    a = len(num_list)
    for i in range(a):
        for j in range(i+1, a):
            if num_list[j] + num_list[i]==0:
                return True
    return False        
    
    
    
    
list = [4,5,6,-85]
print(check_sum(list))