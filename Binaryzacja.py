import numpy as np
import matplotlib.pyplot as plt


# Funkcja do wyznaczenia punktu progowania
def wyznaczProg(gray_value):
    hist, big_edges = np.histogram(gray_value)
    return (np.amin(big_edges)+np.amax(big_edges)) / 2


print("Wczytuje obrazek")
img = plt.imread("rysunek.png")

print("Zamieniam obrazek na skale szarości metodą luminacji piksela")
gray_value = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]

# Pokazywanie szarego obrazka i jego histogram
fig, (gray, His1) = plt.subplots(1, 2)

gray.imshow(gray_value, cmap='gray')
gray.set_title("Obrazek w skali szarości")
His1.hist(gray_value)
His1.set_title("Histogram")
fig.tight_layout()
plt.show()

# Binaryzacja
t = wyznaczProg(gray_value)
binary_mask = gray_value < t
plt.imshow(binary_mask, cmap='gray')
plt.title("Zbinaryzowany obrazek")
plt.show()

# Segmentacja
img[binary_mask] = 0    # Nakłady maskę i dla wszystkich wartości które maska zasłania przypisujemy wartość zero
plt.title("Segmentacja")
plt.imshow(img)
plt.show()


