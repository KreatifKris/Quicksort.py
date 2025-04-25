def quick_sort(arr): #Pendefinisian fungsi quick sort pada suatu deret angka#
  if len(arr) <= 1: #Jika seluruh angka empty atau <= 1 (ex : - ). Terjadilah error code ketika kita mau membandingkan angka, karena nilai '0' adalah netral# 
    return arr #output = hanya print [ ] array kosong
  pivot = arr[len(arr) // 2] #pengisian angka acuan, bebas tapi harus strategis#
  left = [x for x in arr if x < pivot] #Jika nilai x < dari pivot, maka variabel hasil banding diletakkan sebelah kiri#
  middle = [x for x in arr if x == pivot] #Jika nilai x yang kita ambil adalah xy, maka akan diletakkan di tengah array
  right = [x for x in arr if x > pivot] #JIka nilai x pada array > pivot, maka variabel hasil diletakkan sebelah kanan array#
  return quick_sort(left) + middle + quick_sort(right) #Output : Nilai terurut gabungan dari l, m, dan r#
#Kenapa ditambah ? Karena ini merupakan hasil akumulasi perhitungan#


if __name__ == "__main__" : #Main digunakan untuk alias variabel nama (dasar listing)#
  array = [9, -3, 5, 2, 6, 8, -6, 1, 3] #Data yang harus diproses/dipertanyakan#
  sorted_array = quick_sort(array) #Pemanggilan fungsi Quick Sort#
  print("Sorted array:", sorted_array) #Output : angka terurut#