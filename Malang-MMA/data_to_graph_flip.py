import numpy as np
import matplotlib.pyplot as plt

# Membaca data dari file numpy
data = np.load('data.npy')

# Membalik data
data2 = np.flip(data)

# Membuat grafik 2 menggunakan Matplotlib
plt.plot(data2, color='#fe6403')

# Menambahkan grid atau garis pandu pada grafik dengan warna abu-abu
plt.grid(True, color='gray', linestyle='--')  

# Menyimpan grafik tanpa grid sebagai file PNG terpisah
plt.savefig('assets/image/grafik-orange.png', format='png', transparent=True)