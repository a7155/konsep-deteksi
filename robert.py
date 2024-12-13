import imageio
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menerapkan operator Roberts
def roberts_edge_detection(image):
    # Kernel Roberts
    kernel_x = np.array([[1, 0], [0, -1]])
    kernel_y = np.array([[0, 1], [-1, 0]])
    
    # Mendapatkan ukuran citra
    rows, cols = image.shape
    
    # Membuat citra kosong untuk hasil
    edge_image = np.zeros((rows, cols))
    
    # Menerapkan kernel Roberts
    for i in range(rows - 1):
        for j in range(cols - 1):
            gx = np.sum(kernel_x * image[i:i+2, j:j+2])
            gy = np.sum(kernel_y * image[i:i+2, j:j+2])
            edge_image[i, j] = np.sqrt(gx**2 + gy**2)
    
    # Normalisasi hasil
    edge_image = (edge_image / np.max(edge_image)) * 255
    return edge_image.astype(np.uint8)

# Membaca citra
image_path = 'contoh.jpeg'  # Ganti dengan path citra Anda
image = imageio.imread(image_path)

# Mengonversi citra ke grayscale jika citra berwarna
if len(image.shape) == 3:
    image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # Menggunakan rumus luminance

# Menerapkan deteksi tepi dengan operator Roberts
edges = roberts_edge_detection(image)

# Menampilkan citra asli dan citra hasil deteksi tepi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Citra Asli')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Deteksi Tepi (Roberts)')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()