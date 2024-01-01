TUGAS PEMROGRAMAN BERORIENTASI OBJEK PRAKTIK
LAPORAN GUI PEMESANAN TIKET PESAWAT

Disusun oleh:
1.	Sukma Indriya wati (5220411297)
2.	Syaifullah Yusuf Fadlililah (5220411293)
3.	Bayu Segara Handika (5220411296)
4.	Mahmud Isti Panggalih (5220411297)
5.	Muhammad Sirajul Huda (5220411306)

INFORMATIKA
UNIVERSITAS TEKNOLOGI YOGYAKARTA

Abstrak:

Dalam era digital yang berkembang pesat, aplikasi pemesanan tiket pesawat menjadi sarana utama untuk menyederhanakan dan mempercepat proses perjalanan udara. Faktor kunci kesuksesan aplikasi ini tidak hanya terletak pada ketersediaan tiket, tetapi juga pada Antarmuka Pengguna (GUI) yang efektif dan ramah pengguna. Penelitian ini mengusut secara mendalam pengembangan GUI pada aplikasi pemesanan tiket pesawat dengan menekankan desain responsif dan pengalaman pengguna yang memuaskan. Makalah ini dimulai dengan mendiskusikan latar belakang pentingnya GUI dalam konteks aplikasi pemesanan tiket pesawat. Dengan mobilitas yang semakin tinggi, GUI menjadi elemen krusial untuk memberikan pengalaman pengguna yang efisien dan intuitif. Selanjutnya, makalah membahas peran desain responsif dalam meningkatkan aksesibilitas aplikasi di berbagai perangkat, mulai dari smartphone hingga tablet. Studi kasus diterapkan untuk mengidentifikasi tantangan dan peluang dalam mengoptimalkan GUI. Desain yang memperhatikan kebutuhan pengguna, keterbacaan, dan navigabilitas diimplementasikan dengan tujuan mencapai tingkat kepuasan pengguna yang maksimal. Hasil analisis menunjukkan bahwa desain responsif tidak hanya meningkatkan kenyamanan pengguna tetapi juga mempercepat proses pemesanan tiket pesawat. Pentingnya pengalaman pengguna yang memuaskan menjadi fokus selanjutnya, dengan pembahasan tentang elemen-elemen seperti kejelasan informasi, sistem pembayaran yang aman, dan fitur pencarian yang efisien. Integrasi fitur-fitur ini dalam GUI bertujuan untuk memberikan pengalaman pengguna yang holistik dan tanpa hambatan. Makalah ini mengambil pendekatan holistik terhadap pengembangan GUI pada aplikasi pemesanan tiket pesawat dengan memberikan perhatian khusus pada desain responsif dan pengalaman pengguna. Diharapkan penelitian ini dapat memberikan wawasan berharga bagi pengembang aplikasi, desainer UI/UX, dan pemangku kepentingan lainnya untuk meningkatkan kualitas GUI pada aplikasi pemesanan tiket pesawat guna meraih keunggulan kompetitif di pasar yang semakin ketat.
Kata kunci: Antarmuka Pengguna, Aplikasi Pemesanan Tiket Pesawat, Desain Responsif, Pengalaman Pengguna, Studi Kasus.

Pendahuluan 
Dalam era modern ini, mobilitas dan perjalanan udara menjadi bagian tak terpisahkan dari kehidupan sehari-hari. Seiring dengan perkembangan teknologi, proses pemesanan tiket pesawat telah mengalami transformasi signifikan melalui aplikasi pemesanan tiket pesawat berbasis mobile. Keberhasilan sebuah aplikasi pemesanan tiket pesawat tidak hanya tergantung pada ketersediaan tiket, tetapi juga pada antarmuka pengguna (GUI) yang efektif dan ramah pengguna. Antarmuka pengguna (GUI) memainkan peran yang krusial dalam menentukan keberhasilan suatu aplikasi. Pada aplikasi pemesanan tiket pesawat, GUI menjadi jendela utama bagi pengguna untuk berinteraksi dengan sistem. Dengan demikian, desain GUI yang baik tidak hanya mencakup aspek estetika, tetapi juga aspek fungsional dan pengalaman pengguna yang memadai. Perkembangan teknologi mobile telah membawa perubahan dramatis dalam cara orang memesan tiket pesawat. Proses yang sebelumnya rumit dan memakan waktu kini dapat diselesaikan dengan mudah melalui perangkat genggam, memungkinkan pengguna untuk merencanakan perjalanan mereka dengan lebih efisien. Dalam konteks ini, pengguna menuntut aplikasi pemesanan tiket pesawat yang tidak hanya cepat dan andal, tetapi juga mudah dipahami dan nyaman digunakan. Pentingnya GUI dalam konteks aplikasi pemesanan tiket pesawat menjadi fokus utama penelitian ini. Bagaimana sebuah aplikasi dapat memberikan pengalaman pengguna yang intuitif, efisien, dan menyenangkan merupakan pertanyaan sentral yang akan dijawab dalam makalah ini. Selain itu, penerapan konsep-konsep desain terkini, responsivitas, dan keamanan data juga menjadi perhatian utama dalam merancang GUI aplikasi pemesanan tiket pesawat yang komprehensif. Dengan memahami kompleksitas dan tantangan yang terkait dengan pengembangan GUI pada aplikasi pemesanan tiket pesawat, penelitian ini bertujuan untuk memberikan wawasan yang mendalam tentang faktor-faktor kunci yang perlu dipertimbangkan dalam menciptakan antarmuka yang sukses. Melalui analisis mendalam, diharapkan hasil penelitian ini dapat memberikan kontribusi pada peningkatan kualitas aplikasi pemesanan tiket pesawat yang dapat memenuhi ekspektasi dan kebutuhan pengguna secara optimal.

Rumusan Masalah:
•	Bagaimana karakteristik antarmuka pengguna (GUI) pada aplikasi pemesanan tiket pesawat saat ini dan sejauh mana kesesuaian dengan kebutuhan dan preferensi pengguna?
•	Apa saja tantangan yang dihadapi dalam pengembangan GUI aplikasi pemesanan tiket pesawat, terutama terkait dengan desain responsif dan pengalaman pengguna yang optimal?
•	Bagaimana pengaruh desain responsif terhadap aksesibilitas dan kenyamanan pengguna dalam melakukan pemesanan tiket pesawat melalui aplikasi?
•	Sejauh mana integrasi fitur-fitur seperti kejelasan informasi, sistem pembayaran yang aman, dan efisiensi fitur pencarian berkontribusi terhadap pengalaman pengguna yang memuaskan?

Tujuan Penelitian:
•	Menganalisis karakteristik GUI pada aplikasi pemesanan tiket pesawat dan mengidentifikasi potensi peningkatan untuk meningkatkan kepuasan pengguna.
•	Mengevaluasi tantangan dan hambatan yang dihadapi dalam pengembangan GUI, khususnya terkait dengan desain responsif dan pengalaman pengguna yang optimal.
•	Mengukur pengaruh positif desain responsif terhadap aksesibilitas dan kenyamanan pengguna, dengan tujuan memperbaiki elemen-elemen kritis pada GUI.
•	Mengidentifikasi kontribusi integrasi fitur-fitur tertentu dalam menciptakan pengalaman pengguna yang memuaskan dan efisien dalam proses pemesanan tiket pesawat.

Metode Implementasi:

A. Desain Sistem 

1. Merinci bagaimana antarmuka pengguna dibuat untuk memudahkan pengguna dalam melakukan pemesanan. 

a)	Pertama kita di suguhkan dengan halaman register ketika menjalan source code perogram yang berisi inpputan ‘username’ dan ‘password’ ketika user belum mempunyai akun pada aplikasi kita.

	Jika sudah registrasi maka akan muncul notifikasi di bawah ini
 
b)	Setelah membuat akun kita akan di antarkan ke menu login untuk memasukkan ‘username’ dan ‘password’ yaang pada sebelumnya kita sudah buat untuk dapat mengakses ke dalam aplikasi.
 
c)	 Setelah berhasil login akan muncul notifikasi seperti di bawah ini menunjukkan bahwa login telah berhasil.

d)	Setelah itu kita akan di antar pada menu pemesanan tiket peswat dengan inputan yang ada yaitu maskapai, jumlah penumpang, tanggal keberangkatan, tujuan,nama pemesan. Setelah itu klik submit untuk melakukan pemesanan dan akan di masukkan ke database.

e)	Setelah berhasil melakukan pemesanan akan ada notifikasi ‘pemesanan berhasiil di masukkan ke database’ agar lebih jelasnya bisa di lihat di bawah ini.

f)	Jika ingin menampilkan detail pemesanan bisa di klik pada menu ‘tampilkan pesanan’.

g)	Setelah mengklik ‘tampilkan pesanan’ maka pesanan pun akan di tampilkan seperti gambar berikut.
 


2. Menjelaskan bahwa data pemesanan disimpan dan dikelola dalam sebuah database.

1)	Pada hal ini kita sekelompok menggunakan ‘XAMPP’ untuk database dari aplikasi pemesanan tiket pesawat, Pertama kita membuat database dengan nama’pemesanan_tiket’ dan setelah itu di dalam databse terdapat 2 buah tabel yaitu tabel ‘pesanan’ dan ‘users’. Nah tabel pesanan ini adalah untuk menampung segala pemesanan yang di inputkan oleh user dengan catatan user tersebut sudah registrasi dan kemudian di masukkan ke database pada tabel ‘users’, agar lebih jelasnya disini kita screenshoot database yang kita miliki.

2)	Dibawah ini adalah tabel untuk ‘users’ pada databse yang berisi semua costumer yang sudah registrasi pada aplikasi pememesanan tiket pesawat yang kita buat. Dalam tabel ini bisa dilihat ada atribut id, username dan password.

3)	Sedangkan pada gambar di bawah ini adalah tabel pesanan yaitu yang berisi semua pesanan tiket pesawat yang di inputkan oleh user. Bisa dilihat pada gambar di bawah bahwasanya tiket dengan maskapai ‘garuda’  jumlah_penumpang ‘12’ tujuan ‘bali’ dengan nama_pemesan ’yuda’.

 

3.  Class Diagram

B. Keunggulan Sistem:

1.	Efisiensi Operasional:
•	Sistem ini memungkinkan pengguna untuk melakukan pemesanan tiket pesawat dengan cepat dan efisien melalui antarmuka pengguna yang ramah pengguna.
•	Proses pencarian penerbangan, pemilihan penerbangan, dan pengisian data pemesanan diintegrasikan dengan baik, mengurangi waktu yang dibutuhkan untuk menyelesaikan transaksi.
2.	Akses Real-time:
•	Keunggulan utama adalah kemampuan untuk mengakses informasi penerbangan dan ketersediaan kursi secara real-time. Ini memastikan bahwa data yang ditampilkan kepada pengguna selalu terkini.
3.	Akurasi Informasi:
•	Sistem membantu mengurangi kesalahan manusia dalam pengelolaan data dengan menyimpan dan mengelola informasi pemesanan dan jadwal penerbangan secara otomatis. Hal ini meningkatkan akurasi data dan mengurangi potensi kesalahan manusia.
4.	Manajemen Informasi yang Efisien:
•	Kemampuan sistem untuk menyimpan dan mengelola data pemesanan dan jadwal penerbangan dengan baik memungkinkan manajemen informasi yang efisien.
•	Informasi transaksi dapat dengan mudah dilacak, dan laporan dapat dihasilkan secara sistematis untuk keperluan administratif.
5.	Kemudahan Pelacakan dan Pelaporan:
•	Sistem ini menyediakan kemudahan dalam pelacakan status pemesanan dan menghasilkan laporan transaksi. Hal ini memudahkan pihak terkait untuk memantau kinerja sistem dan melacak aktivitas pemesanan.


Kesimpulan:

Dengan implementasi sistem pemesanan tiket pesawat yang terhubung ke database, dapat disimpulkan bahwa sistem ini membawa sejumlah manfaat yang signifikan. Keunggulan utama terletak pada peningkatan efisiensi operasional, akses real-time, akurasi informasi, dan manajemen informasi yang efisien.
Pengguna dapat dengan mudah mencari, memilih, dan memesan tiket pesawat tanpa mengalami hambatan yang berarti. Proses ini menjadi lebih efisien, memastikan kepuasan pelanggan dan meningkatkan produktivitas.
Sistem ini juga memungkinkan pengelolaan informasi yang lebih baik, mengurangi risiko kesalahan manusia, dan memfasilitasi pelacakan serta pelaporan transaksi. Dengan demikian, keseluruhan implementasi sistem ini memberikan dampak positif terhadap efektivitas dan efisiensi operasional dalam industri penerbangan.


