import numpy as np
import matplotlib.pyplot as plt


heart_img = np.array([
  [255,0,0,255,0,0,255],
  [0,255/2,255/2,0,255/2,255/2,0],
  [0,255/2,255/2,255/2,255/2,255/2,0],
  [0,255/2,255/2,255/2,255/2,255/2,0],
  [255,0,255/2,255/2,255/2,0,255],
  [255,255,0,255/2,0,255,255],
  [255,255,255,0,255,255,255]
])

# This is a helper function that makes it easy for you to show images!
# image variable is a NumPy array of RGB values
def show_image(image, name_identifier):
    plt.imshow(image, cmap="gray")
    plt.title(name_identifier)
    plt.show()

# Show heart image
#show_image(heart_img, 'Heart Image')

# Invert color
inverted_heart_img = 225 - heart_img
#show_image(inverted_heart_img, 'Inv Heart Image')

# Rotate heart
rotated_heart_img = heart_img.T
#show_image(rotated_heart_img, 'Rot Heart Image')

# Random Image
random_img = np.random.randint(0,255, (7,7))
show_image(random_img, 'Random Image')

# Solve for heart image, we want to solve the matrix that creates the original heart image
# random_img⋅x = heart_img
x = np.linalg.solve(random_img, heart_img)
solution = random_img@x
show_image(solution, 'Matrix solution')

