from copy import deepcopy


from mathlib.complex import *


if __name__ == "__main__":

    v1 = Vector(0.2, 0.3, 0.4)
    v2 = Vector(0.1, 0.3, 0.5)
    v3 = Vector(0.3, 0.1, 0.2)
    v4 = Vector(0.2, 0.2, 0.3)

    q1 = Quaternion(1.0, deepcopy(v1))
    q2 = Quaternion(0.2, deepcopy(v2))
    q3 = Quaternion(0.2, deepcopy(v3))
    q4 = Quaternion(0.1, deepcopy(v4))

    dq1 = DualQuaternion(deepcopy(q1), deepcopy(q2))
    dq2 = DualQuaternion(deepcopy(q3), deepcopy(q4))

    print(dq1, dq2)
