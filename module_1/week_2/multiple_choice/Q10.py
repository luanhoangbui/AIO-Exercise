def my_function(integers, number=1):
    return [True if integer == number else False for integer in integers]
    # Your code here : Thuc hien duyet tung phan tu trong integers , so sanh tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
    # vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False , True , False] )


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == [False, False, False, False]

my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
