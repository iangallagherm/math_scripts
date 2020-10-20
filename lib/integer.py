import sys

class Integer:
    def __init__(self, number):
        self.is_pos = number > 0
        self.abs_val = abs(number)
    def __eq__(self, other):
        return self.is_pos == other.is_pos and self.abs_val == other.abs_val
    def __repr__(self):
        if self.is_pos:
            return str(self.abs_val)
        else:   
            return str(-self.abs_val)
def add_ints(obj_x, obj_y):
    return Integer(int(str(obj_x)) + int(str(obj_y)))

int1 = Integer(-5)
int2 = Integer(7)

print(add_ints(int(sys.argv[1]), int(sys.argv[2])))
