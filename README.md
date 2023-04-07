Tugas 10
1.	Penjelasan point 1 :
Program di vscode mengimpor modul random dan menggunakan fungsi randint untuk menghasilkan angka acak antara 0 dan 100. Fungsi random_number mengembalikan angka acak yang dihasilkan oleh fungsi randint. Yang dapat memanggil fungsi random_number untuk menghasilkan angka acak baru setiap kali dipanggil.

2.	Penjalasan point 2 : 
Program di vscode menggunakan tiga konstanta string dari modul string: ascii_letters, digits, dan punctuation. ascii_letters berisi semua huruf alfabet baik huruf kecil maupun huruf besar, digits berisi semua karakter numerik, dan punctuation berisi semua karakter khusus. Fungsi random_string mengambil satu parameter length yang menentukan panjang string acak yang akan dihasilkan. Fungsi ini menggunakan join untuk menggabungkan karakter-karakter acak yang dihasilkan oleh random.choice dan mengembalikan string acak yang dihasilkan. Yang dapat memanggil fungsi random_string untuk menghasilkan string acak baru setiap kali dipanggil.

3.	Penjelasan point 3 :
Program di vscode menggunakan metode split bawaan Python yang memisahkan sebuah string menjadi sebuah list, dengan delimiter atau pemisah yang ditentukan sebagai parameter. Fungsi split_string mengambil dua parameter, yaitu input_string yang merupakan string yang akan dipisahkan dan delimiter yang merupakan karakter atau string pemisah. 
Fungsi ini mengembalikan list dari string yang telah dipisahkan. Anda dapat memanggil fungsi split_string untuk memisahkan string menjadi array.
Perlu diperhatikan bahwa pemisah juga dimasukkan ke dalam list sebagai string terakhir. Jika pemisah tidak ditemukan dalam string, maka list yang dihasilkan hanya berisi satu elemen yaitu string asli.

4.	Penjelasan point 4 :
Program di vscode menggunakan aturan yang umum digunakan untuk menentukan tahun kabisat: tahun yang habis dibagi 4 adalah tahun kabisat, kecuali tahun yang habis dibagi 100, kecuali tahun yang habis dibagi 400. Fungsi is_leap_year mengambil satu parameter year yang merupakan tahun yang akan diperiksa. Fungsi ini mengembalikan True jika tahun tersebut adalah tahun kabisat dan False jika tidak. Anda dapat memanggil fungsi is_leap_year untuk memeriksa apakah sebuah tahun adalah tahun kabisat.
Bisa diperhatikan bahwa aturan untuk menentukan tahun kabisat dapat bervariasi di berbagai kalender dan sistem penanggalan.

5.	Penjelasan point 5 :
Program di atas menggunakan sebuah loop untuk mencetak setiap dictionary yang ada di dalam list data. Fungsi print_data mengambil satu parameter data yang merupakan list of dictionary yang akan dicetak. Fungsi ini mencetak setiap dictionary dengan format "Name: [nama], Age: [umur]". yang dapat memanggil fungsi print_data untuk mencetak data dari list of dictionary
Dan juga diperhatikan bahwa dalam dictionary, setiap pasangan key-value dipisahkan dengan tanda titik dua (:), dan setiap pasangan key-value dipisahkan dengan tanda koma (,) dalam list.

6.	Penjelasan point 6 :
Program di vscode menggunakan sebuah loop untuk memproses setiap dictionary yang ada di dalam list data. Fungsi group_people mengambil dua parameter: data yang merupakan list of dictionary yang akan dikelompokkan, dan job_status yang merupakan status pekerjaan yang akan dijadikan kriteria pengelompokan. Fungsi ini mengembalikan sebuah dictionary yang berisi kelompok orang berdasarkan jenis kelamin, usia, dan status perkawinan. Setiap kelompok direpresentasikan sebagai sebuah tuple yang terdiri dari tiga elemen: jenis kelamin, usia, dan status perkawinan. Nilai kunci untuk setiap kelompok adalah tuple ini, dan nilai untuk setiap kunci adalah sebuah list yang berisi nama orang-orang yang termasuk dalam kelompok tersebut. Yang dapat memanggil fungsi group_people untuk mengelompokkan orang berdasarkan kriteria yang diberikan.
Dapat diperhatikan bahwa fungsi group_people hanya mengelompokkan orang-orang yang memiliki status pekerjaan yang sesuai dengan kriteria yang diberikan. Jika tidak ada orang yang memenuhi kriteria, maka fungsi akan mengembalikan sebuah dictionary kosong.

7.	Penjelasan point 7 :
Program di vscode menggunakan fungsi count() untuk menghitung jumlah huruf "a" pada kata yang dipotong. Fungsi count_a mengambil dua parameter: word yang merupakan kata yang akan dipotong, dan n yang merupakan jumlah loop yang akan dilakukan. Fungsi ini mengembalikan sebuah bilangan bulat yang merupakan jumlah huruf "a" pada kata yang dipotong. Yang dapat memanggil fungsi count_a untuk menghitung jumlah huruf "a" pada kata yang dipotong.
Dapat diperhatikan bahwa fungsi count_a memotong kata aha menjadi ah karena jumlah loop yang diberikan adalah 3, dan mengembalikan jumlah huruf "a" pada kata yang dipotong, yaitu 2.  

NOTED. maaf sebelumnya tika program ini memakai python karena node.js dijavascript tika selalu eror saat memulai install. tapi tika tetep mengerjakan sesuai dgn tugas yang diberikan. :)
