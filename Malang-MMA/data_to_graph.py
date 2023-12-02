import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file numpy
data = np.load('data.npy')

# Membuat grafik menggunakan Matplotlib
plt.plot(data, color='#59e000')

# Menambahkan grid atau garis pandu pada grafik dengan warna abu-abu
plt.grid(True, color='gray', linestyle='--')  

# Menyimpan grafik tanpa grid sebagai file PNG terpisah
plt.savefig('assets/image/grafik-hijau.png', format='png', transparent=True)

