def countdigit(n):
    
    count=0

    while n != 0:
          n //= 10
          count = count + 1
    return count

n = int(input("ennter number: "))

print("count is: ",countdigit(n))
