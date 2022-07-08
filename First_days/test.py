import numpy as np

name = '1,2,3,4'
print(name.split())
# A = np.array([
#     [2, -3, 1],
#     [3, 1, 1],
#     [-1, -2, -1]
# ])
# b = np.array([2, -1, 1])

# x,y,z = np.linalg.solve(A, b)
# print(x,y,z)
# # A = np.array([[1,2],[3,4]])
# # B = np.array([[-4,-3],[-2,-1]])

# # one way to matrix multiply
# #print(np.matmul(A,B))
# # another way to matrix multiply
# #A@B


# # Given
# # 2 x 3 matrix
# A = np.array([[2,3,-4], [-2, 1, -3]])
# # 2 x 3 matrix
# B = np.array([[1,-1,4], [3,-3,3]])
# # 3 x 2 matrix
# C = np.array([[1, 2], [3, 4], [5, 6]])

# print(A)
# # Calculate D = 4A - 2B
# # D = 4 * A - 2 * B
# # print(D)

# # # Calculate E = AC
# # E = A@C
# # print(E)


# # # Calculate F = CA

# # F = C@A
# # print(F)

# # angel between to vectors
# a = np.array([3, -1, 2])
# b = np.array([0, -1, 1])
# c = np.array([-2, -3, 0, 5, 1])
# print(np.dot(c, c))

# unit_vector1 = a / np.linalg.norm(a)
# unit_vector2 = a / np.linalg.norm(b)
# dot1 = np.dot(unit_vector1, unit_vector2)

# dot = np.dot(a, b)
# angle1 = np.arccos(dot1)
# denominator = np.dot(np.linalg.norm(a),np.linalg.norm(b))
# angle = np.arccos(dot / denominator)
# # print(np.arccos(np.clip(angle1, -1, 1)))
# # print(angle1)

# def unit_vector(vector):
#     """ Returns the unit vector of the vector.  """
#     return vector / np.linalg.norm(vector)

# def angle_between(v1, v2):
#     """ Returns the angle in radians between vectors 'v1' and 'v2'::

#             >>> angle_between((1, 0, 0), (0, 1, 0))
#             1.5707963267948966
#             >>> angle_between((1, 0, 0), (1, 0, 0))
#             0.0
#             >>> angle_between((1, 0, 0), (-1, 0, 0))
#             3.141592653589793
#     """
#     v1_u = unit_vector(v1)
#     v2_u = unit_vector(v2)
#     return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))