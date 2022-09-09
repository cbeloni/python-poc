def donouts(count: int):
    return ("numero de donouts %s" % str(count)) if (count < 5) else "numero de donouts : many" 

if __name__ == '__main__':
    print (donouts(1))
    print (donouts(6))
    