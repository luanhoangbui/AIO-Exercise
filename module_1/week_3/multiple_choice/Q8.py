from module_1.week_3.multiple_choice.Q7 import Doctor

### Your Code Here
def count_doctor(self):
    count = 0
    for p in self.__list_people:
        if isinstance(p, Doctor):
            count += 1
    return count
### End Code Here
