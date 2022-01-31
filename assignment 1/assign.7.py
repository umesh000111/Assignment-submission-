def fun(value):
    if(value%5==0):
        print('true')
    else:
        print('false')




def main():
    print('enter a number')
    x = int(input())

    ret = fun(x)

if __name__=='__main__':
    main()
