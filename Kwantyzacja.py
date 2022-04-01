import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('logo.png')
print(np.shape(img))

print(np.size(img[1, 1]))


fig, (gray1, gray2, gray3) = plt.subplots(3)


gray = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2]) / 3
gray2.imshow(gray, cmap='gray')
gray3.set_title('Uśrednienie wartości piksela')

# Wyznaczenie luminacji piksela
gray = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
gray3.imshow(gray, cmap='gray')
gray3.set_title('Wyznaczenie luminacji piksela')

plt.show()
