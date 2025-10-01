# IMPLEMENTASI IMPROVED SQRT-COSINE SIMILARITY UNTUK PEMERINGKATAN RESUME BERDASARKAN KUALIFIKASI LOWONGAN KERJA
# SKRIPSI
Untuk memenuhi sebagian persyaratan memperoleh gelar Sarjana Komputer
Disusun oleh: Khansa Salsabila Sangdiva Laksono NIM: 215150201111068
TEKNIK INFORMATIKA DEPARTEMEN TEKNIK INFORMATIKA FAKULTAS ILMU KOMPUTER UNIVERSITAS BRAWIJAYA MALANG 2025

# PERNYATAAN ORISINALITAS
Saya menyatakan dengan sebenar-benarnya bahwa sepanjang pengetahuan saya, di  dalam naskah skripsi ini tidak terdapat karya ilmiah yang pernah diajukan oleh orang lain untuk memperoleh gelar akademik di suatu perguruan  tinggi, dan tidak terdapat karya atau pendapat yang pernah ditulis atau diterbitkan oleh orang lain, kecuali yang secara tertulis disitasi dalam naskah ini dan disebutkan dalam daftar referensi.
Apabila ternyata didalam naskah skripsi ini dapat dibuktikan terdapat unsur- unsur plagiasi, saya bersedia skripsi ini digugurkan dan gelar akademik yang telah saya peroleh (sarjana) dibatalkan, serta diproses sesuai dengan peraturan perundang-undangan yang berlaku (UU No. 20 Tahun 2003, Pasal 25 ayat 2 dan Pasal 70).
Malang, 3 Juli 2025

## Khansa Salsabila Sangdiva Laksono
# NIM: 215150201111068
iii

# PRAKATA
Puji syukur penulis panjatkan ke hadirat Allah SWT yang telah melimpahkan rahmat dan hidayah-Nya sehingga penulis dapat menyelesaikan skripsi yang berjudul “Implementasi Improved Sqrt-Cosine Similarity Untuk Pemeringkatan Resume Berdasarkan Kualifikasi Lowongan Kerja”. Penulis menyadari bahwa dalam penyusunan skripsi tidak terwujud tanpa adanya dukungan, bimbingan, arahan, serta doa yang tiada hentinya dari berbagai pihak. Pada kesempatan kali ini penulis mengucapkan terima kasih sebesar-besarnya kepada:
1.Bapak Rizal Setya Perdana, S.Kom., M.Kom., Ph.D. selaku dosen pembimbing satu yang telah menyetujui dan mengarahkan penulis sehingga dapat menyelesaikan skripsi ini.
2.Ibu Ir. Indriati, S.T., M.Kom. selaku dosen pembimbing dua yang telah menyetujui dan membimbing dalam penulisan untuk pengerjaan skripsi ini.
3.Bapak Bayu Priyambadha, S.Kom., M.Kom., Ph.D. selaku Ketua Program Studi Teknik Informatika Fakultas Ilmu Komputer Universitas Brawijaya.
4.Bapak Sabriansyah Rizqika Akbar, S.T., M.Eng., Ph.D. selaku Ketua Departemen Teknik Informatika Fakultas Ilmu Komputer Universitas Brawijaya.
5.Rajiv Maulana selaku validator dalam skripsi ini, serta seluruh rekan kerja penulis yang telah berkontribusi dalam memperluas wawasan dan pengetahuan penulis selama proses penelitian.
6.Ayah Tripinto Laksono, S.Kom. dan Bunda Dian Laksono selaku kedua orang tua penulis, Sangkaisar Laksono selaku adik penulis, dan seluruh keluarga penulis yang senantiasa memberikan dukungan, doa, dan motivasi sehingga dapat menyelesaikan skripsi ini.
7.P4OP Dinas Pendidikan Jakarta selaku penyelenggara beasiswa KJMU yang membantu penulis dalam menyelesaikan studi sarjana.
8.Seluruh teman tercinta penulis hingga saat ini yang telah menjadi teman diskusi selama proses penelitian, teman seperjuangan, serta sumber motivasi, terutama Salsabila Rachmayani, Kirana Alivia, Nathania Putri, Aidah Az Zahra, Raditya Atmaja, Roiyan Zain, Ade Arya, Nadhira Nurannisa, Saqina Salsabila, Ghania Tanziela, Gustav Ali, Emilia Putri, Farel Rakha, Aldiansyah, Dzaki Rafif, Bagas Antarino, Safia Putri, Rayshanda Yuwandina, Arkan, Alka, Faqih, Audrey, Aelissa, Dina, Kurnia, dan Zahra.
Malang, 25 Juni 2025

## Penulis
khansalaksono@gmail.com
iv

# ABSTRAK
Khansa Salsabila Sangdiva Laksono, Implementasi Improved Sqrt-Cosine Similarity Untuk Pemeringkatan Resume Berdasarkan Kualifikasi Lowongan Kerja
Pembimbing: Rizal Setya Perdana, S.Kom., M.Kom., Ph.D. dan Indriati, Ir., S.T., M.Kom.
Ketidaksesuaian antara kualifikasi pelamar dengan kebutuhan penyedia lowongan kerja dapat menjadi salah satu penyebab fenomena pengangguran. Penelitian ini menggunakan pendekatan representasi teks TF-IDF dan Word2Vec untuk implementasi perhitungan similaritas Improved Sqrt-Cosine (ISC) antara resume dengan kualifikasi lowongan kerja, memeringkat lima resume per kualifikasi lowongan kerja, dan dievaluasi hasilnya oleh seorang ahli dengan dua skenario yang melibatkan pemberian bobot pada setiap section dalam resume. Hasil penelitian ini menunjukkan keunggulan pada Word2Vec dengan ISC pada skenario tanpa bobot section dan Word2Vec dengan Cosine Similarity pada skenario dengan bobot section. TF-IDF dengan ISC menunjukkan performa terbaik dalam menghasilkan lima resume yang isiannya relevan dengan deskripsi lowongan kerja. Meskipun implementasi ISC dengan representasi teks Word2Vec unggul karena masih cukup mampu menangkap hubungan semantik kata kunci, tetap kurang disarankan karena mengaburkan hubungan semantik asli akibat nilai absolut. Jika preferensi bobot section dapat menimbulkan bias karena kurang mencerminkan variasi preferensi rekruter pada umumnya, maka implementasi ISC dengan TF-IDF lebih disarankan untuk digunakan.
Kata kunci: similaritas resume, pemeringkatan, improved sqrt-cosine, spearman
v

# ABSTRACT
Khansa Salsabila Sangdiva Laksono, The Implementation of Improved Sqrt- Cosine Similarity for Resume Ranking Based on Job Vacancy Qualifications
Supervisors: Rizal Setya Perdana, S.Kom., M.Kom., Ph.D. and Indriati, Ir., S.T., M.Kom.
The mismatch between a job applicant's qualifications and the requirements of job providers can contribute to the phenomenon of unemployment. This research employs TF-IDF and Word2Vec text representation approaches to implement the Improved Sqrt-Cosine (ISC) similarity calculation between resumes and job vacancy qualifications, ranking the top five resumes per job qualification, and evaluating the results by an expert using two scenarios involving the weighting of resume sections. The results indicate that Word2Vec with ISC performs best in the scenario without section weighting, while Word2Vec with Cosine Similarity excels in the scenario with section weighting. TF-IDF with ISC demonstrates the best performance in generating the top five resumes with content relevant to the job description. Although the implementation of ISC with Word2Vec performs best because it is still quite capable of capturing the semantic relationships of keywords, it is less recommended due to the distortion of original semantic relationships caused by absolute value transformations. If section weighting preferences introduce bias by not reflecting the general preferences of recruiters, the implementation of ISC with TF-IDF is more recommended for use.
Keywords: resume similarity, ranking, improved sqrt-cosine, spearman
vi

# DAFTAR ISI
# PENGESAHAN
# PERNYATAAN ORISINALITAS
# PRAKATA
# ABSTRAK
# ABSTRACT
# DAFTAR ISI
# DAFTAR TABEL
# DAFTAR GAMBAR
# DAFTAR LAMPIRAN
# BAB 1 PENDAHULUAN ...................................................................................... 1
## 1.1 Latar Belakang ................................................................................. 1
## 1.2 Rumusan Masalah ........................................................................... 2
## 1.3 Tujuan .............................................................................................. 2
## 1.4 Manfaat ........................................................................................... 3
## 1.5 Batasan Masalah ............................................................................. 3
## 1.6 Sistematika Pembahasan ................................................................ 3
# BAB 2 LANDASAN KEPUSTAKAAN ..................................................................... 5
## 2.1 Kajian Pustaka ................................................................................. 5
## 2.2 Dasar Teori ...................................................................................... 7
### 2.2.1 Resume .................................................................................... 7
### 2.2.2 Similaritas Teks ........................................................................ 8
### 2.2.3 Pra-pemrosesan Teks .............................................................. 9
### 2.2.4 TF-IDF .................................................................................... 10
### 2.2.5 Word2Vec .............................................................................. 12
### 2.2.6 Improved Sqrt-Cosine Similarity ............................................ 13
### 2.2.7 Cosine Similarity .................................................................... 14
### 2.2.8 Human-Level Performance .................................................... 14
### 2.2.9 Spearman Rank Correlation Coefficient (SRCC) .................... 15
# BAB 3 METODOLOGI ....................................................................................... 16
vii

## 3.1 Tipe Penelitian ............................................................................... 16
## 3.2 Strategi Penelitian ......................................................................... 16
## 3.3 Lokasi Penelitian ............................................................................ 16
## 3.4 Metode Pengumpulan Data .......................................................... 16
## 3.5 Metode Analisis Data .................................................................... 17
## 3.6 Metode Evaluasi ............................................................................ 17
## 3.7 Peralatan Pendukung .................................................................... 18
### 3.7.1 Perangkat Lunak (Software) .................................................. 18
### 3.7.2 Perangkat Keras (Hardware) ................................................. 18
## 3.8 Perancangan Algoritma ................................................................. 18
# BAB 4 PERANCANGAN .................................................................................... 20
## 4.1 Deskripsi Umum ............................................................................ 20
## 4.2 Preprocessing ................................................................................ 20
### 4.2.1 Ekstraksi Section .................................................................... 20
### 4.2.2 Preprocessing Isian Resume .................................................. 25
### 4.2.3 Preprocessing Penamaan Section ......................................... 27
### 4.2.4 Preprocessing Kualifikasi Lowongan Kerja ............................ 29
## 4.3 Perhitungan Representasi Teks ..................................................... 30
### 4.3.1 TF-IDF .................................................................................... 30
### 4.3.2 Word2Vec .............................................................................. 33
## 4.4 Perhitungan Similaritas ................................................................. 36
### 4.4.1 Improved Sqrt-Cosine Similarity ............................................ 36
### 4.4.2 Cosine Similarity .................................................................... 38
## 4.5 Perhitungan Korelasi ..................................................................... 40
## 4.6 Perhitungan Relevansi dan Senioritas........................................... 42
## 4.7 Perhitungan Manual...................................................................... 44
### 4.7.1 Data Uji .................................................................................. 44
### 4.7.2 Perhitungan Manual Ekstraksi Section .................................. 45
### 4.7.3 Perhitungan Manual Preprocessing Resume ........................ 46
### 4.7.4 Perhitungan Manual Preprocessing Kualifikasi Lowongan Kerja .................................................................................... 59
### 4.7.5 Perhitungan Manual Representasi Teks ............................... 61
viii

### 4.7.6 Perhitungan Manual Similaritas ............................................ 94
### 4.7.7 Skenario Pengujian .............................................................. 101
# BAB 5 IMPLEMENTASI................................................................................... 105
## 5.1 Implementasi Kode Program Import Libraries dan Load Dataset ..................................................................................................... 105
## 5.2 Implementasi Kode Program Preprocessing Resume ................. 108
## 5.3 Implementasi Kode Program Preprocessing Kualifikasi Lowongan Kerja ....................................................................................... 118
## 5.4 Implementasi Kode Program Representasi Teks TF-IDF ............. 120
## 5.5 Implementasi Kode Program Representasi Teks Word2Vec 121
## 5.6 Implementasi Kode Program Perhitungan Similaritas ................ 123
### 5.6.1 Implementasi Kode Program Improved Sqrt-Cosine Similarity............................................................................................. 123
### 5.6.2 Implementasi Kode Program TF-IDF dan Improved Sqrt-Cosine Similarity ......................................................................... 124
### 5.6.3 Implementasi Kode Program Word2Vec dan Cosine Similarity............................................................................................. 129
### 5.6.4 Implementasi Kode Program Word2Vec dan Improved Sqrt-Cosine Similarity ......................................................... 134
## 5.7 Implementasi Kode Program Pengujian ..................................... 139
### 5.7.1 Implementasi Kode Program Perhitungan SRCC ................ 139
### 5.7.2 Implementasi Kode Program Perhitungan Relevansi dan Senioritas ..................................................................................... 144
# BAB 6 PENGUJIAN DAN ANALISIS HASIL ....................................................... 150
## 6.1 Pengujian ..................................................................................... 150
## 6.2 Analisis Hasil ................................................................................ 156
# BAB 7 PENUTUP ............................................................................................ 165
## 7.1 Kesimpulan .................................................................................. 165
## 7.2 Saran ............................................................................................ 166
ix

# DAFTAR TABEL
Tabel 1.1 Tingkat pengangguran 7 negara ASEAN World Economic Outlook ........ 1
Tabel 2.1 Hasil eksperimen pertama penelitian oleh Ahmad Alsharef dkk. ........... 5
Tabel 2.2 Hasil eksperimen kedua penelitian oleh Ahmad Alsharef dkk. ............... 6
Tabel 4.1 Data uji resume untuk perhitungan manual ......................................... 44
Tabel 4.2 Data uji kualifikasi lowongan kerja untuk perhitungan manual ........... 45
Tabel 4.3 Hasil perhitungan manual ekstraksi section .......................................... 45
Tabel 4.4 Hasil perhitungan manual preprocessing resume bagian menghapus email ...................................................................................................................... 46
Tabel 4.5 Hasil perhitungan manual preprocessing resume bagian menghapus nomor telepon ...................................................................................................... 47
Tabel 4.6 Hasil perhitungan manual preprocessing resume bagian menghapus －berbagai tipe tanda minus (, –, —) ................................................................... 48
Tabel 4.7 Hasil perhitungan manual preprocessing resume bagian menghapus nama bulan ............................................................................................................ 48
Tabel 4.8 Hasil perhitungan manual preprocessing resume bagian menghapus kata “Present” dan “Current” ........................................................................................ 49
Tabel 4.9 Hasil perhitungan manual preprocessing resume bagian menghapus tanggal ................................................................................................................... 50
Tabel 4.10 Hasil perhitungan manual preprocessing resume bagian menghapus placeholder ............................................................................................................ 51
Tabel 4.11 Hasil perhitungan manual preprocessing resume bagian menghapus tanda baca ............................................................................................................. 52
Tabel 4.12 Hasil Perhitungan manual preprocessing resume bagian menghapus angka ..................................................................................................................... 53
Tabel 4.13 Hasil perhitungan manual preprocessing resume bagian menghapus spasi kosong berlebih ............................................................................................ 54
Tabel 4.14 Hasil perhitungan manual preprocessing resume bagian lematisasi dan menghapus stop words ......................................................................................... 54
Tabel 4.15 Hasil perhitungan manual penyetaraan nama section bagian mengonversi nama section menjadi huruf kecil (lower casing) ........................... 55
Tabel 4.16 Hasil perhitungan manual penyetaraan nama section bagian mengonversi nama section menjadi huruf kecil (lower casing) ........................... 56
Tabel 4.17 hasil perhitungan manual penyetaraan nama section bagian menyeragamkan pengelompokan section berdasarkan pemetaan ..................... 57
x
Tabel 4.18 Hasil perhitungan manual penyetaraan nama section bagian klasifikasi, penghapusan, dan pengelompokan section tidak valid ........................................ 58
Tabel 4.19 Hasil perhitungan manual penyetaraan nama section bagian mengonversi isi resume menjadi huruf kecil (lower casing) ................................ 58
Tabel 4.20 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian mengonversi isi kualifikasi lowongan kerja menjadi huruf kecil (lower casing) ................................................................................................................... 59
Tabel 4.21 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian menghapus angka ..................................................................................... 59
Tabel 4.22 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian menghapus tanda baca ............................................................................. 60
Tabel 4.23 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian menghapus spasi kosong berlebih ............................................................ 60
Tabel 4.24 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian lematisasi dan menghapus stop words ..................................................... 61
Tabel 4.25 Korpus resume untuk perhitungan manual ........................................ 61
Tabel 4.26 Perhitungan manual frekuensi term setiap resume ........................... 62
Tabel 4.27 Perhitungan manual TF korpus resume .............................................. 64
Tabel 4.28 Perhitungan manual IDF korpus resume ............................................. 66
Tabel 4.29 Perhitungan manual TF-IDF korpus resume ........................................ 68
Tabel 4.30 Perhitungan manual TF-IDF korpus resume setelah normalisasi ....... 71
Tabel 4.31 Korpus kualifikasi lowongan kerja untuk perhitungan manual........... 73
Tabel 4.32 Perhitungan manual TF korpus kualifikasi lowongan kerja ................ 73
Tabel 4.33 Perhitungan manual IDF korpus kualifikasi lowongan kerja ............... 76
Tabel 4.34 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja .......... 78
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah normalisasi ............................................................................................................ 80
Tabel 4.36 Perhitungan manual one-hot encoding ............................................... 83
Tabel 4.37 Bobot input layer-hidden layer ............................................................ 85
Tabel 4.38 Bobot hidden layer-output layer ......................................................... 86
Tabel 4.39 Bobot hidden layer-output layer ......................................................... 86
Tabel 4.40 Bobot hidden layer-output layer ......................................................... 86
Tabel 4.41 Bobot hidden layer-output layer ......................................................... 86
Tabel 4.42 Pembaharuan bobot input layer-hidden layer .................................... 91
xi
Tabel 4.43 Pembaharuan bobot input layer-output layer .................................... 92
Tabel 4.44 Pembaharuan bobot input layer-output layer .................................... 93
Tabel 4.45 Pembaharuan bobot input layer-output layer .................................... 93
Tabel 4.46 Pembaharuan bobot input layer-output layer .................................... 93
Tabel 4.47 Data sampel perhitungan manual similaritas ..................................... 94
Tabel 4.48 Vektor TF-IDF perhitungan manual Improved Sqrt-Cosine Similarity . 95
Tabel 4.49 Hasil skor similaritas resume ID 15265464 perhitungan manual Improved Sqrt-Cosine Similarity ............................................................................ 96
Tabel 4.50 Bobot section kategori industri "TEACHER" ........................................ 96
Tabel 4.51 Vektor Word2Vec perhitungan manual Cosine Similarity .................. 97
Tabel 4.52 Hasil skor similaritas resume ID 15265464 perhitungan manual Cosine Similarity................................................................................................................ 98
Tabel 4.53 Vektor Word2Vec perhitungan manual Improved Sqrt-Cosine Similarity ............................................................................................................................... 99
Tabel 4.54 Hasil skor similaritas resume ID 15265464 perhitungan manual Improved Sqrt-Cosine Similarity .......................................................................... 100
Tabel 4.55 Peringkat 1-5 resume dengan skor similaritas terbesar untuk perhitungan manual SRCC ................................................................................... 102
Tabel 4.56 Selisih peringkat 1-5 resume perhitungan manual SRCC .................. 102
Tabel 4.57 Peringkat 1-5 resume dengan hasil evaluasi relevansi dan senioritas ahli terbesar untuk perhitungan manual ................................................................... 103
Tabel 6.1 Hasil pengujian berwarna hijau skenario tanpa bobot section ........... 156
Tabel 6.2 Hasil pengujian berwarna merah skenario tanpa bobot section ........ 157
Tabel 6.3 Hasil pengujian berwarna hijau skenario dengan bobot section ........ 158
Tabel 6.4 Hasil pengujian berwarna merah skenario dengan bobot section ..... 158
Tabel 6.5 Weighted score keseluruhan pendekatan dan skenario ..................... 159
Tabel 6.6 Urutan pendekatan berdasarkan weighted score tertinggi ................ 159
Tabel 6.7 Perhitungan rata-rata parameter setiap pendekatan dan skenario ... 160
Tabel 6.8 Perhitungan similaritas antar term Word2Vec vektor nilai asli dengan vektor nilai absolut .............................................................................................. 161
xii

# DAFTAR GAMBAR
Gambar 2.1 Pengelompokan text similarity measure ............................................ 8
Gambar 2.2 Arsitektur pendekatan Skip-gram ..................................................... 12
Gambar 3.1 Struktur proses implementasi pemeringkatan similaritas resume dan kualifikasi lowongan kerja ..................................................................................... 19
Gambar 4.1 Diagram alur ekstraksi section .......................................................... 21
Gambar 4.2 Diagram alur ekstraksi section .......................................................... 22
Gambar 4.3 Diagram alur ekstraksi section .......................................................... 23
Gambar 4.4 Diagram alur ekstraksi section .......................................................... 24
Gambar 4.5 Diagram alur preprocessing isian resume ......................................... 25
Gambar 4.6 Diagram alur preprocessing isian resume ......................................... 26
Gambar 4.7 Diagram alur preprocessing penamaan section resume ................... 28
Gambar 4.8 Diagram alur preprocessing isian kualifikasi lowongan kerja ........... 29
Gambar 4.9 Diagram alur TF-IDF ........................................................................... 30
Gambar 4.10 Diagram alur TF-IDF ......................................................................... 31
Gambar 4.11 Diagram alur TF-IDF ......................................................................... 32
Gambar 4.12 Diagram alur Word2Vec .................................................................. 33
Gambar 4.13 Diagram alur Word2Vec .................................................................. 34
Gambar 4.14 Diagram alur Word2Vec .................................................................. 35
Gambar 4.15 Diagram alur Improved Sqrt-Cosine Similarity ................................ 36
Gambar 4.16 Diagram alur Improved Sqrt-Cosine Similarity ................................ 37
Gambar 4.17 Diagram alur Cosine Similarity ........................................................ 38
Gambar 4.18 Diagram alur Cosine Similarity ........................................................ 39
Gambar 4.19 Diagram alur Spearman Rank Correlation Coefficient .................... 40
Gambar 4.20 Diagram alur Spearman Rank Correlation Coefficient .................... 41
Gambar 4.21 Diagram alur relevansi dan senioritas ............................................. 42
Gambar 4.22 Diagram alur relevansi dan senioritas ........................................... 43
Gambar 4.23 Pasangan target-konteks Word2Vec Skip-gram ............................. 83
Gambar 6.1 Cuplikan template spreadsheet evaluasi ahli .................................. 150
Gambar 6.2 Cuplikan template spreadsheet evaluasi ahli .................................. 151
Gambar 6.3 Cuplikan spreadsheet hasil evaluasi ahli ......................................... 151
xiii
Gambar 6.4 Hasil descriptive statistics SPSS ....................................................... 152
Gambar 6.5 Visualisasi nilai korelasi ................................................................... 153
Gambar 6.6 Visualisasi persentase relevansi ...................................................... 154
Gambar 6.7 Visualisasi persentase senioritas ..................................................... 155
Gambar 6.8 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli dengan vektor nilai absolut .............................................................................................. 161
Gambar 6.9 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli dengan vektor nilai absolut .............................................................................................. 162
Gambar 6.10 Grafik garis tiga parameter setiap kualifikasi lowongan kerja ...... 163
xiv

# DAFTAR LAMPIRAN
# LAMPIRAN A SURAT PERNYATAAN VALIDITAS
# LAMPIRAN B BOBOT PER SECTION BERDASARKAN INDUSTRI
# LAMPIRAN C HASIL PEMERINGKATAN LIMA RESUME PER KUALIFIKASI LOWONGAN KERJA
C.1 Tanpa Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity............... 180
C.2 Tanpa Bobot - Word2Vec dan Cosine Similarity ................................ 190
C.3 Tanpa Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity ........ 201
C.4 Dengan Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity ............ 211
C.5 Dengan Bobot - Word2Vec dan Cosine Similarity ............................. 220
C.6 Dengan Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity ................................................................................................................. 231

# LAMPIRAN D GRAFIK GARIS TIGA PARAMETER SETIAP KUALIFIKASI LOWONGAN KERJA
xv

# BAB 1PENDAHULUAN
Bab pendahuluan membahas mengenai latar belakang penelitian, rumusan masalah, tujuan, manfaat, batasan masalah, serta sistematika pembahasan dari penelitian ini.
1.1Latar Belakang
Tingkat pengangguran yang tinggi merupakan salah satu tantangan utama yang dihadapi Indonesia. Masalah ini tidak hanya mempengaruhi kondisi perekonomian, tetapi juga kesejahteraan sosial masyarakat. Perkembangan ketenagakerjaan sangat penting bagi stabilitas ekonomi, dan setiap hambatan dalam aspek ini dapat berdampak negatif pada upaya meningkatkan taraf hidup masyarakat.
Tabel 1.1 Tingkat pengangguran 7 negara ASEAN World Economic Outlook

## No Negara Tingkat Pengangguran
# 1 Indonesia 5,2
# 2 Filipina 5,1
# 3 Brunei Darussalam 4,9
# 4 Malaysia 3,5
# 5 Viet Nam 2,1
# 6 Singapore 1,9
# 7 Thailand 1,1
Tabel 1.1 menunjukkan data yang diambil dari World Economic Outlook pada April 2024 oleh International Monetary Fund, di antara 7 negara ASEAN yang datanya tercantum, Indonesia memiliki tingkat pengangguran tertinggi di angka 5,2. Pengangguran bisa disebabkan oleh beberapa fenomena dan salah satunya adalah ketidaksesuaian antara karakteristik pencari kerja dengan tawaran kerja atau bisa disebut dengan pengangguran struktural (Kementerian Ketenagakerjaan RI - Badan Perencanaan dan Pengembangan Ketenagakerjaan, 2021). Sumber daya, kualifikasi, keterampilan, dan pengetahuan yang tersedia dan diperoleh oleh individu untuk memaksimalkan kemampuan kerja mereka sendiri disebut dengan human capital. Nilai-nilai ini berkontribusi pada pendapatan yang lebih tinggi, kepuasan hidup, dan kohesi sosial, sehingga juga menjadi salah satu penentu pertumbuhan ekonomi negara (Wujarso, 2022).
1
Proses mencari dan melamar pekerjaan identik dengan penggunaan curriculum vitae (CV) atau beberapa orang menyebutnya resume. Tahapan awal perekrutan adalah proses screening CV yang selanjutnya diikuti dengan proses wawancara. Rekrutmen dianggap efektif ketika mendapatkan banyak pelamar yang sesuai dengan kualifikasi untuk mendapatkan calon karyawan terbaik dari yang terbaik (Budiantoro dalam Kumaladewi, 2018).
Terdapat beberapa penelitian sebelumnya yang berkaitan dengan perhitungan similaritas teks untuk otomatisasi penyaringan resume. Pertama, penelitian oleh Ahmad Alsharef dkk. (2023) membandingkan pendekatan Cosine Similarity, Sqrt- Cosine Similarity, dan Improved Sqrt-Cosine (ISC) Similarity, menggunakan TF-IDF sebagai metode vektorisasi teks, dan menunjukkan bahwa pendekatan ISC dianggap lebih baik dibandingkan dua pendekatan lainnya. Kedua, penelitian oleh Rahul Singh Pundir dkk. (2024) mengembangkan sistem rekomendasi resume berbasis keterampilan, menggunakan Word2Vec untuk menangkap kesamaan semantik keterampilan dan Cosine Similarity untuk mengukur kesesuaian antara vektor keterampilan dengan kebutuhan pekerjaan. Merujuk pada penelitian sebelumnya, penelitian ini bertujuan untuk mengimplementasikan Improved Sqrt- Cosine (ISC) Similarity dalam memeringkat resume berdasarkan kualifikasi lowongan kerja, dengan mengeksplorasi metode representasi teks TF-IDF dan Word2Vec.

## 1.2Rumusan Masalah
Berikut ini merupakan rumusan masalah penelitian.
1.Bagaimana hasil pemeringkatan lima resume untuk setiap kualifikasi lowongan kerja menggunakan Improved Sqrt-Cosine Similarity dalam mengkalkulasikan similaritas teks? 2.Bagaimana korelasi antara peringkat hasil implementasi Improved Sqrt- Cosine Similarity dengan peringkat hasil evaluasi ahli untuk setiap kualifikasi lowongan kerja menggunakan Spearman Rank Correlation Coefficient?
1.3Tujuan
Berikut ini merupakan tujuan penelitian ini.
1.Menganalisis hasil pemeringkatan lima resume untuk setiap kualifikasi lowongan kerja menggunakan Improved Sqrt-Cosine Similarity dalam mengkalkulasikan similaritas teks. 2.Menganalisis korelasi antara peringkat hasil implementasi Improved Sqrt- Cosine Similarity dengan peringkat hasil evaluasi ahli untuk setiap kualifikasi lowongan kerja menggunakan Spearman Rank Correlation Coefficient.
2
1.4Manfaat
Berikut merupakan manfaat yang dapat diperoleh dari penelitian ini.
1.Memberikan interpretasi hasil Improved Sqrt-Cosine Similarity dalam menghasilkan perhitungan similaritas teks pada pemeringkatan lima resume untuk setiap kualifikasi lowongan kerja. 2.Memberikan pemaparan mengenai korelasi antara peringkat hasil Improved Sqrt-Cosine Similarity dengan peringkat hasil evaluasi ahli menggunakan Spearman Rank Correlation Coefficient.
1.5Batasan Masalah
Batasan masalah yang ditetapkan dalam penelitian ini sebagai berikut.
1.Penelitian ini terbatas pada dataset Kaggle dengan 2.484 resume. 2.Penelitian ini berfokus pada pemeringkatan lima resume berdasarkan nilai similaritas tertinggi untuk setiap kualifikasi lowongan kerja. 3.Penelitian ini melibatkan seorang ahli di bidang rekrutmen dalam mengevaluasi hasil pemeringkatan. 4.Kualifikasi lowongan kerja yang digunakan diambil dari 24 posisi di portal lowongan pekerjaan https://id.jobstreet.com/.

## 1.6Sistematika Pembahasan
Susunan sistematika pembahasan ditulis di bawah ini dan terdiri dari beberapa bab yang menjelaskan mengenai penelitian mengenai kalkulasi similaritas teks pada resume pelamar dengan kualifikasi lowongan kerja.

# BAB 1 PENDAHULUAN
Bab pendahuluan membahas mengenai latar belakang penelitian, rumusan masalah, tujuan, manfaat, batasan masalah, serta sistematika pembahasan dari penelitian ini.

# BAB 2 LANDASAN KEPUSTAKAAN
Bab landasan kepustakaan berisi kajian pustaka dan dasar teori. Penelitian- penelitian sebelumnya yang berhubungan dengan kalkulasi similaritas teks pada resume  dijelaskan pada kajian pustaka. Sedangkan, penjelasan teori, konsep, dan metode yang digunakan dijelaskan pada dasar teori.

# BAB 3 METODOLOGI PENELITIAN
Terdapat beberapa bagian di bab metodologi penelitian, seperti tipe penelitian, strategi penelitian, lokasi penelitian, metode pengumpulan data, metode analisis data, peralatan pendukung, dan perancangan algoritma.

# BAB 4 PERANCANGAN
Bab perancangan menjelaskan tentang perancangan algoritma dari metode- metode serta flow diagram dari setiap algoritma yang digunakan pada penelitian ini. Selain itu, bab ini juga merincikan perhitungan manual.
3

# BAB 5 IMPLEMENTASI
Bab implementasi berisi implementasi dari metode kalkulasi similaritas teks pada resume pelamar dengan kualifikasi instansi yang digunakan pada penelitian ini, seperti metode perhitungan similaritas Improved Sqrt-Cosine (ISC) dan Cosine Similarity (CosSim), serta metode representasi teks TF-IDF dan Word2Vec.

# BAB 6 PENGUJIAN DAN ANALISIS HASIL
Pemaparan hasil dari pengujian akan dijelaskan di bab pengujian, serta pembahasan dan analisa dari hasil pengujian tersebut sebagai bahan evaluasi.

# BAB 7 PENUTUP
Terakhir, kesimpulan dan saran ditulis pada bab penutup. Bagian kesimpulan memaparkan rangkuman dari hasil penelitian untuk menjawab semua rumusan masalah yang dijabarkan pada latar belakang. Sedangkan, bagian saran memaparkan masukan-masukan untuk penelitian selanjutnya agar penelitian ini dapat diperbaiki dan dikembangkan.
4

# BAB 2LANDASAN KEPUSTAKAAN
Bab landasan kepustakaan berisi kajian pustaka dan dasar teori. Penelitian- penelitian sebelumnya yang berhubungan dengan kalkulasi similaritas teks pada resume  dijelaskan pada kajian pustaka. Sedangkan, penjelasan teori, konsep, dan metode yang digunakan dijelaskan pada dasar teori.
2.1Kajian Pustaka
Terdapat beberapa penelitian yang dilakukan sebelumnya terkait perhitungan similaritas teks untuk otomatisasi penyaringan resume. Penelitian pertama dilakukan oleh Ahmad Alsharef dkk. (2023) berjudul "Exploring the Efficiency of Text-Similarity Measures in Automated Resume Screening for Recruitment" mengeksplorasi penggunaan text similarity sebagai alternatif dalam memproses resume, dengan pendekatan Cosine Similarity, Sqrt-Cosine Similarity, dan Improved Sqrt-Cosine (ISC) Similarity. Terdapat dua eksperimen dalam penelitian ini. Eksperimen pertama melibatkan 40 resume yang disandingkan dengan deskripsi pekerjaan untuk posisi manajer pengembangan bisnis di salah satu platform terkemuka untuk manajemen kepatuhan UKM di Eropa. Pada lima urutan teratas peringkat resume, dilakukan perbandingan antara peringkat yang diberikan oleh manusia dan pengukuran otomatis, hasilnya tertera pada Tabel 2.1
Tabel 2.1 Hasil eksperimen pertama penelitian oleh Ahmad Alsharef dkk.
Human ISC Sqrt-Cosine Cosine Ranking of Resumes
1 2 (0,38) 11 (28,545) 7 (43,02)
2 3 (0,345) 2 (32,732) 1 (48,44)
3 1 (0,391) 9 (28,87) 4 (44,29)
4 4 (0,344) 17 (26,749) 14 (38,5)
5 8 (0,302) 1 (32,733) 15 (38,2)
Eksperimen kedua melibatkan 30 resume yang disandingkan dengan deskripsi pekerjaan untuk posisi software engineer di salah satu perusahaan teknologi multinasional Amerika. Pada lima urutan teratas peringkat resume, dilakukan perbandingan antara peringkat yang diberikan oleh manusia dan pengukuran otomatis, yang hasilnya tertera pada Tabel 2.2.
5
Tabel 2.2 Hasil eksperimen kedua penelitian oleh Ahmad Alsharef dkk.
Human ISC Sqrt-Cosine Cosine Ranking of Resumes
1 8 (0,181) 6 (21,205) 11 (18,47)
2 1 (0,246) 4 (22,136) 1 (26,99)
3 4 (0,199) 1 (22,744) 4 (22,25)
4 3 (0,206) 2 (22,65) 10 (18,52)
5 6 (0,181)  14 (18,708) 3 (24,36)
Berdasarkan hasil kedua eksperimen, hasil dari penelitian yang dilakukan oleh Ahmad Alsharef dkk. (2023) menunjukkan bahwa peringkat Improved Sqrt-Cosine (ISC) Similarity cenderung lebih mendekati peringkat yang diberikan oleh manusia.
Penelitian kedua dilakukan oleh Rahul Singh Pundir dkk. (2024) berjudul "Enhancing Resume Recommendation System through Skill-based Similarity using Deep Learning Models" membahas cara meningkatkan rekomendasi resume dengan mempertimbangkan kesamaan keterampilan. Sistem ini menggunakan metode Word2Vec untuk mengukur kecocokan kandidat dengan kebutuhan pekerjaan berdasarkan skills dan LSTM-RNN untuk memprediksi profil pekerjaan. Skor skill similarity dari penelitian ini berkisar dari 0,447 hingga 0,790, di mana nilai yang lebih tinggi menunjukkan keterampilan kandidat lebih sesuai dengan kebutuhan pekerjaan. Pendekatan ini juga membantu kandidat memahami keterampilan tambahan yang perlu dikembangkan untuk memenuhi kualifikasi posisi yang diinginkan.
Penelitian ketiga dilakukan oleh Chirag Daryani dkk. (2020) berjudul "An Automated Resume Screening System Using Natural Language Processing and Similarity" mengembangkan sistem rekomendasi yang mengekstraksi informasi dari resume yang tidak terstruktur dan mengubahnya menjadi vektor yang mewakili fitur-fitur penting seperti pendidikan, pengalaman, dan keterampilan. Dengan menghitung kesamaan menggunakan Cosine Similarity antara resume dan deskripsi pekerjaan, sistem ini mampu menyusun peringkat kandidat terbaik yang sesuai dengan posisi pekerjaan yang ditawarkan. Hasil perhitungan Cosine Similarity antara empat resume dan query pekerjaan menunjukkan bahwa resume kandidat ke-2 menduduki peringkat pertama (0,680), diikuti resume kandidat ke- 4 di peringkat kedua (0,651), resume kandidat ke-3 di peringkat ketiga (0,498), dan resume kandidat ke-1 di peringkat terakhir (0,490).
6
Topik skripsi yang diambil memiliki beberapa kesamaan dengan penelitian sebelumnya. Pertama, penelitian ini mengimplementasikan perhitungan similaritas Improved Sqrt-Cosine (ISC), seperti pada penelitian pertama. Kedua, cara menghitung similaritas dilakukan dengan membandingkan informasi yang didapatkan dari resume dengan persyaratan atau kualifikasi posisi pekerjaan, sebagaimana dilakukan pada penelitian pertama dan ketiga. Ketiga, penelitian ini mengekstaksi informasi dari resume seperti pada penelitian ketiga, tetapi berfokus pada pengambilan informasi per bagian (section) resume sesuai standarisasi dari seorang ahli. Perbedaan dengan penelitian kedua adalah penelitian tersebut menggunakan daftar skills yang diambil dari kumpulan resume dan mengukur skill similarity-nya dengan resume yang digunakan. Sedangkan, topik skripsi ini akan mengukur similarity dari suatu resume untuk melihat apakah sesuai dengan yang dibutuhkan oleh suatu kualifikasi posisi pekerjaan. Meskipun begitu, untuk tahap representasi teks juga akan menggunakan Word2Vec seperti yang dilakukan pada penelitian kedua sebagai salah satu metode representasi teks dari penelitian ini.
2.2Dasar Teori
2.2.1Resume
Resume menurut Kamus Besar Bahasa Indonesia (KBBI) merupakan kata nominal yang berarti ikhtisar atau ringkasan. Stanford Career Education (2024) menyatakan bahwa resume merupakan ringkasan pengalaman yang dipilih oleh perekrut untuk menunjukkan kesesuaian pelamar dengan posisi yang dilamar. Resume juga sering diartikan sama dengan Curriculum Vitae (CV), keduanya pun memiliki definisi yang sama menurut Cambridge Dictionary (2024), yaitu sebuah ringkasan tertulis yang menggambarkan latar belakang pendidikan, kualifikasi, pengalaman kerja sebelumnya, serta minat pribadi seseorang dan dikirimkan kepada instansi ketika melamar pekerjaan. Di Amerika Serikat, CV umumnya digunakan saat melamar pekerjaan di bidang akademis, sedangkan resume digunakan untuk pekerjaan lainnya (Cambridge University Press & Assessment, 2024).
Perekrut hanya meluangkan kurang dari 30 detik untuk meninjau resume, sehingga penting bagi pelamar untuk secara cepat dan jelas menunjukkan bagaimana pelatihan dan pengalaman mereka dapat memberi nilai tambah bagi perusahaan, serta memaparkan keterampilan secara tepat untuk memenuhi kebutuhan perusahaan dengan format resume yang jelas, menarik, dan disesuaikan dengan konvensi yang berlaku di setiap posisi atau sektor yang dilamar (Stanford Career Education, 2018).
7
Stanford Career Education (2024) juga memberikan panduan dalam langkah- langkah membuat resume, dikatakan bahwa resume yang efektif adalah ringkasan singkat yang menyoroti pengalaman dan keterampilan yang langsung terkait dengan pekerjaan. Informasi yang ingin disampaikan kepada perekrut mengenai masing-masing pengalaman harus ditentukan dengan jelas, konten yang difokuskan tergantung pada posisi yang dilamar karena setiap perekrut mencari sekumpulan keterampilan tertentu dari pelamar yang sesuai dengan keterampilan yang diperlukan untuk menjalankan pekerjaan tertentu (Stanford Career Education, 2024). Saat mendeskripsikan keterampilan atau pencapaian yang relevan, disarankan untuk menggunakan metode C-A-R: CONTEXT mencakup apa yang dikerjakan, seperti tugas, proyek, atau tujuan keseluruhan yang tercapai, serta pihak-pihak yang terlibat, seperti tim yang berkolaborasi dan/atau populasi yang dilayani; ACTIONS menggambarkan bagaimana tugas tersebut dilaksanakan dengan menekankan keterampilan yang digunakan untuk menyelesaikan tugas, penggunaan action words sangat dianjurkan untuk mendeskripsikan tindakan yang diambil; Terakhir, RESULTS menjelaskan apa hasilnya, kuantifikasi hasil harus dilakukan jika memungkinkan, atau jika hasil tidak diketahui, penting untuk menyertakan tujuan dari tugas, proyek, atau tujuan tersebut, yang menjelaskan alasan pelaksanaan (Stanford Career Education, 2024).
2.2.2Similaritas Teks
Mengingat tujuan perekrut adalah mencari pelamar yang memiliki sekumpulan keterampilan yang dibutuhkan oleh instansi untuk melaksanakan pekerjaan tertentu, maka digunakan metode untuk menghitung similaritas antara kualifikasi yang terdapat dalam resume pelamar dengan kualifikasi yang dibutuhkan oleh instansi. Similaritas teks adalah membandingkan suatu teks dengan teks lainnya dan menemukan persamaan di antara mereka. Pada dasarnya, ini tentang menentukan tingkat kedekatan teks tersebut. Dalam pemrosesan bahasa alami, menentukan apakah makna dari dua dokumen identik adalah tugas mendasar dan luas yang memungkinkan komputer memahami bahasa manusia (He, et al., 2024).
Berbagai pendekatan telah dikembangkan untuk mengukur similaritas antara satu teks dengan teks lainnya yang terbagi menjadi empat kelompok utama, yaitu String-based, Corpus-based, Knowledge-based, dan Hybrid (Prasetya, et al., 2018).
Gambar 2.1 Pengelompokan text similarity measure
Sumber: Prasetya et al. (2018)
8
Seperti pada apa yang sudah diilustrasikan pada Gambar 2.1, String-based adalah metode pengukuran tertua, paling sederhana, tetapi paling populer dan beroperasi pada urutan string dan susunan karakter (Prasetya, et al., 2018). Corpus-based menggunakan pendekatan semantik yang mana menentukan kesamaan antara dua konsep berdasarkan informasi yang diekstraksi dari korpus yang besar (Prasetya, et al., 2018). Knowledge-based menggunakan hubungan semantik untuk mengidentifikasi tingkat kesamaan kata-kata (Prasetya, et al., 2018). Selain tiga kelompok yang telah dijelaskan sebelumnya, terdapat perhitungan similaritas secara Hybrid dengan tujuan untuk menggabungkan metode yang telah disebutkan sebelumnya, termasuk String-based, Corpus-based, dan Knowledge-based guna mencapai metrik yang lebih baik dengan mengadopsi keunggulan masing-masing metode (Prasetya, et al., 2018).
2.2.3Pra-pemrosesan Teks
Sebelum menerapkan metode similaritas teks, diperlukan proses pra- pemrosesan teks terlebih dahulu untuk menyiapkan dataset resume yang akan diolah. Penting untuk melakukan pemrosesan data ini guna memastikan bahwa data yang digunakan adalah data yang berkualitas sehingga dapat menghasilkan akurasi yang akurat (Prasetya, et al., 2024). Adapun beberapa langkah selama proses pra-pemrosesan teks, yaitu:
1.Tokenization. Proses ini untuk memecahkan kalimat menjadi kata-kata (Sohangir & Wang, 2017). Tools seperti NLTK dan spaCy biasa digunakan untuk melakukan tokenisasi (Amin, et al., 2023). 2.Lower Casing. Proses ini mengonversi semua teks menjadi huruf kecil (Alsharef, et al., 2023). 3.Stop Words. Proses ini untuk menghilangkan stop words, yaitu kata-kata umum dalam dokumen yang tidak memiliki makna signifikan dan tidak berkontribusi dalam membedakan dokumen, sehingga dapat diabaikan (Sihombing, 2022). Bahasa pemrograman Python telah menyediakan package Regular Expression (RegEx) untuk melaksanakan penghilangan stop words (Amin, et al., 2023). 4.Lemmatization. Tidak seperti stemming yang hanya mengubah kata menjadi ke bentuk dasarnya, lemmatization memanfaatkan kosakata dan morfologis yang sesuai dengan linguistik (Daryani, et al., 2020) sesuai kamus bahasa yang digunakan. Untuk bahasa Inggris, dapat memanfaatkan WordNet Lemmatizer yang tersedia melalui NLTK Python (Daryani, et al., 2020).
9

# 2.2.4TF-IDF
Term Frequency-Inverse Document Frequency (TF-IDF) adalah salah satu teknik yang digunakan untuk menghitung seberapa penting suatu kata (term) dalam sebuah dokumen terhadap keseluruhan kumpulan dokumen (Septiani & Isabela, 2022). TF-IDF didapatkan dari hasil perkalian antara Term Frequency (TF) dan Inverse Document Frequency (IDF) (Ramadhan, et al., 2023).

# 𝑇𝐹−𝐼𝐷𝐹=𝑇𝐹×𝐼𝐷𝐹       (2.1)
()𝑡,𝑑(𝑡,𝑑)(𝑡)
Adapun keterangan dari Persamaan 2.1:
𝑇𝐹−𝐼𝐷𝐹𝑡𝑑  = Bobot TF-IDF pada term ke- terhadap dokumen ke-
()𝑡,𝑑
𝑇𝐹𝑡𝑑  = Frekuensi kemunculan term ke- terhadap dokumen ke-
(𝑡,𝑑)
𝐼𝐷𝐹𝑡  = Nilai inverse dokumen yang memunculkan term ke-
(𝑡)
TF didapatkan dengan menghitung jumlah kemunculan kata dibagi dengan total kata dalam dokumen (Septiani & Isabela, 2022). IDF menghitung seberapa penting suatu kata dalam koleksi dokumen dengan membagi jumlah total dokumen dengan jumlah dokumen yang mengandung suatu term (Septiani & Isabela, 2022).
𝑓
𝑡,𝑑𝑇𝐹=         (2.2)
(𝑡,𝑑)
∑𝑓
𝑘𝑘,𝑑
Adapun keterangan dari Persamaan 2.2:
𝑇𝐹𝑡𝑑 = Frekuensi kemunculan term ke- terhadap dokumen ke-
(𝑡,𝑑)
𝑓𝑡𝑑  = Jumlah kemunculan term ke- terhadap dokumen ke-
𝑡,𝑑
∑𝑓𝑑 = Total seluruh term terhadap dokumen ke-
𝑘𝑘,𝑑
𝑁 𝐼𝐷𝐹=log()         (2.3)
(𝑡) 𝑑𝑓
Keterangan dari Persamaan 2.3:
𝐼𝐷𝐹𝑡 = Nilai inverse document frequency untuk term ke-
(𝑡)
𝑁  = Jumlah total dokumen
𝑑𝑓   = Banyaknya dokumen yang mengandung term
10
Dalam dokumentasi Scikit-learn, TF default tidak dinormalisasi dengan membagi total term. Normalisasi baru dilakukan setelah mendapatkan hasil 𝐿perkalian TF dengan IDF menggunakan  normalization, sehingga TF didapatkan

# 2 dari jumlah kemunculan (frekuensi) term terhadap suatu dokumen seperti pada Persamaan 2.4
𝑇𝐹=𝑓          (2.4)
(𝑡,𝑑)𝑡,𝑑

## Keterangan
𝑇𝐹𝑡𝑑 = Frekuensi kemunculan term ke- terhadap dokumen ke-
(𝑡,𝑑)
𝑓𝑡𝑑  = Jumlah kemunculan term ke- terhadap dokumen ke-
𝑡,𝑑
Pada dokumentasi Scikit-learn, IDF default menggunakan mekanisme smoothing dengan menambahkan konstanta "1" pada pembilang dan penyebut, seolah-olah ada dokumen tambahan yang mengandung setiap term dalam koleksi tepat satu kali sehingga mencegah pembagian oleh nol. Rumusnya menjadi seperti pada Persamaan 2.5
1+𝑁 𝐼𝐷𝐹=log()+1        (2.5)
(𝑡) 1+𝑑𝑓

## Keterangan
𝐼𝐷𝐹𝑡 = Nilai inverse document frequency untuk term ke-
(𝑡)
𝑁  = Jumlah total dokumen
𝑑𝑓   = Banyaknya dokumen yang mengandung term
Setelah mengalikan TF dan IDF, perhitungan TF-IDF dalam dokumentasi Scikit- 𝐿learn dinormalisasikan dengan  normalization atau Euclidean norm, formula dari

# 2 normalisasi ini dapat tertera pada Persamaan 2.6
𝑣𝑣 𝑣==       (2.6)
𝑛𝑜𝑟𝑚
222‖‖𝑣√𝑣+𝑣+⋯+𝑣
212𝑛

## Keterangan
𝑣 = Vektor yang telah dinormalisasi
𝑛𝑜𝑟𝑚
𝑣  = Vektor asli sebelum dinormalisasikan
‖‖𝑣𝑣  = Akar kuadrat dari jumlah kuadrat semua elemen vektor
2
11
2.2.5Word2Vec
Word2Vec adalah metode yang digunakan untuk menghasilkan word embedding dengan memanfaatkan neural networks sederhana yang dilatih untuk memahami konteks linguistik kata. Pendekatan ini menggunakan continuously sliding Skip-gram atau continuously sliding Bag-of-Words (CBOW). Word2Vec mengonversi kata-kata menjadi vektor, memungkinkan pengenalan hubungan semantik dan telah menjadi kunci dalam perkembangan berbagai aplikasi Natural Language Processing (NLP) (Kulshretha & Lodha, 2023). Pada pendekatan CBOW, suatu kata diprediksi berdasarkan konteks yang mengelilinginya di dalam sebuah kalimat. Sedangkan, pendekatan Skip-gram memprediksi konteks berdasarkan kata yang diberikan (Meyer, 2016). Mengingat tujuan utama dari penelitian ini adalah memperhitungkan similaritas teks, sehingga akan lebih fokus pada penggunaan pendekatan Skip-gram yang arsitekturnya terlampir pada Gambar 2.2
Gambar 2.2 Arsitektur pendekatan Skip-gram
Sumber: Meyer (2016)
Skip-gram bekerja dengan menggunakan kata yang sedang diproses (current word) sebagai input untuk mempelajari dan memprediksi kata-kata dalam konteks sebagai target. Proses ini mempelajari distribusi probabilitas kata-kata dalam sebuah kalimat berdasarkan jarak antara kata input dan kata-kata konteks (windows) (Ayuningtyas & Tantyoko, 2024).
12
Dalam teknik Skip-gram, proses training dan inference dilakukan secara terpisah. Selama proses training, skip-gram mempelajari konteks dari kata-kata yang muncul di sekitar kata target dalam window tertentu. Sebagai contoh, jika ukuran window adalah dua, maka kata-kata seperti 'Saya,' 'suka,' 'makan,' dan 'apel' menjadi konteks bagi kata 'apel' dalam kalimat 'Saya suka makan apel.' Metode ini digunakan untuk menghasilkan distribusi probabilitas dari semua kemungkinan konteks kata berdasarkan kata target (Dwivedi & Anand, 2023).
Pada dokumentasi Gensim, implementasinya menggunakan beberapa parameter seperti sg yang ditetapkan dengan nilai 1 untuk memakai Skip-gram, vector_size untuk menetapkan dimensi vektor-vektor kata, window untuk menetapkan jarak maksimum antara kata saat ini dan kata yang diprediksi dalam sebuah kalimat, alpha untuk menginisialisasi learning rate, dan epochs untuk menetapkan iterasi yang secara default bernilai lima.
2.2.6Improved Sqrt-Cosine Similarity
Sohangir dan Wang (2017) memperkenalkan sebuah teknik pengukuran similarity yang disebut Improved Sqrt-Cosine (ISC) similarity, yang didasarkan pada 𝐿normalisasi  (Hellinger distance) dan telah terbukti bahwa pada data berdimensi
1 𝐿𝐿tinggi, normalisasi  bekerja lebih baik daripada normalisasi  (Euclidean
12 𝐿distance). Pada persamaan ISC, alih-alih menggunakan normalisasi , digunakan

# 1 𝐿
akar kuadrat dari normalisasi (Sohangir & Wang, 2017). Sebagian besar

# 1 menganggap Cosine Similarity sebagai 'state of the art' dalam pengukuran similarity (Sohangir & Wang, 2017). Melalui eksperimen yang mendalam, diamati bahwa meskipun ISC mirip dengan Cosine Similarity dalam hal implementasi, ISC menunjukkan kinerja yang lebih baik saat dibandingkan dengan metode pengukuran kesamaan lainnya pada data berdimensi tinggi (Sohangir & Wang, 2017).
𝑚 ∑𝑥𝑦√
𝑖𝑖𝑖=1𝐼𝑆𝐶(𝑥,𝑦)=       (2.7) 𝑚𝑚∑∑√()√()𝑥𝑦
𝑖𝑖𝑖=1𝑖=1
Adapun keterangan dari Persamaan 2.7:
𝑥  = Vektor yang mewakili dokumen pertama
𝑦  = Vektor yang mewakili dokumen kedua
𝑥𝑖𝑥  = Bobot pada term ke- pada vektor
𝑖
𝑦𝑖𝑦  = Bobot pada term ke- pada vektor
𝑖
𝑖   = Indeks term dalam suatu kalimat
𝑚𝑥𝑦  = Jumlah total term dalam vektor vektor  dan
13
2.2.7Cosine Similarity
Tujuan dari Cosine Similarity adalah mendapatkan nilai similaritas dari setiap dokumen yang dibandingkan dengan mengukur kosinus sudut antara dua vektor, dengan fokus pada arah vektor daripada besarnya (Jawale, et al., 2024). Dalam kemiripan teks, setiap vektor mewakili sebuah dokumen, dan elemen-elemennya adalah frekuensi kata. (Jawale, et al., 2024).
𝑚 ∑𝑥.𝑦
𝑖𝑖𝑖=1()𝐶𝑜𝑠𝑆𝑖𝑚𝑥,𝑦=       (2.8) 𝑚𝑚22∑∑𝑥.𝑦√√
𝑖𝑖𝑖=1𝑖=1
Keterangan dari Persamaan 2.8:
𝑥  = Vektor yang mewakili dokumen pertama
𝑦  = Vektor yang mewakili dokumen kedua
𝑥𝑖𝑥  = Bobot pada term ke- pada vektor
𝑖
𝑦𝑖𝑦  = Bobot pada term ke- pada vektor
𝑖
𝑖   = Indeks term dalam suatu kalimat
𝑚𝑥𝑦  = Jumlah total term dalam vektor vektor  dan
2.2.8Human-Level Performance
Meskipun algoritma dapat menunjukkan kinerja yang sangat baik, perlu dipastikan bahwa perbandingan antara kinerja manusia dan algoritma dilakukan secara adil dan tepat agar hasil yang diperoleh dapat dipercaya (Cowley, et al., 2022). Memahami bagaimana manusia menyelesaikan tugas tertentu dapat memberikan informasi yang berguna bagi penelitian di bidang machine learning dan artificial intelligence (Cowley, et al., 2022). Penting untuk mempertimbangkan apakah suatu sistem harus mencapai kinerja setara dengan manusia untuk dianggap cerdas dan apakah mesin harus menyelesaikan masalah dengan cara yang mirip dengan manusia, sehingga dapat menunjukkan pola keberhasilan dan kesalahan yang serupa (Cowley, et al., 2022). Dengan demikian, mengetahui cara manusia menyelesaikan tugas dapat membantu dalam pengembangan algoritma yang lebih baik dan lebih efektif (Cowley, et al., 2022).
14
2.2.9Spearman Rank Correlation Coefficient (SRCC)
Spearman Rank Correlation Coefficient (SRCC) adalah versi nonparametrik dari koefisien Pearson Correlation yang digunakan untuk menyelidiki hubungan linear antara dua variabel, khususnya pada data ordinal (Temizhan, et al., 2022). SRCC cocok digunakan ketika data tidak memenuhi asumsi parametrik, ukuran sampel kecil, atau terdapat masalah outlier (Temizhan, et al., 2022). Koefisien ini dapat diinterpretasikan dalam hal variabilitas peringkat dan dapat menilai hubungan monoton, di mana satu variabel cenderung naik atau turun seiring perubahan variabel lainnya (Temizhan, et al., 2022). Meskipun nonparametrik, asumsi penting untuk menggunakan SRCC adalah data harus setidaknya bersifat ordinal dan harus ada hubungan monoton antara skor pada satu variabel dengan variabel lainnya (Temizhan, et al., 2022).
∑6𝑑
𝑖𝑆𝑅𝐶𝐶 = 1−         (2.9) 2𝑛(𝑛−1)
Adapun keterangan dari Persamaan 2.9:
𝑑𝑋−𝑌  = Selisih antara peringkat variabel, dihitung sebagai
𝑖𝑖𝑖
𝑛 = Jumlah total pasangan data yang digunakan dalam perhitungan
Rentang nilai koefisien korelasi berkisar dari -1 hingga 1 (Hermanto & Harliana, 2024). Nilai 1 menunjukkan korelasi positif sempurna, nilai -1 menunjukkan korelasi negatif sempurna, dan nilai 0 menandakan tidak ada korelasi (Hermanto & Harliana, 2024). Interpretasi koefisien korelasi pada buku oleh Robert Kurniawan (2016), koefisien korelasi berkisar antara 0,00 hingga 1,00 (Hermanto & Harliana, 2024). Nilai 0,00 hingga 0,19 menunjukkan korelasi sangat lemah; 0,20 hingga 0,39 menunjukkan korelasi lemah; 0,40 hingga 0,59 menunjukkan korelasi sedang; 0,60 hingga 0,79 menunjukkan korelasi kuat; dan 0,80 hingga 1,00 menunjukkan korelasi sangat kuat (Hermanto & Harliana, 2024).
15

# BAB 3METODOLOGI
Terdapat beberapa bagian di bab metodologi penelitian, seperti tipe penelitian, strategi penelitian, lokasi penelitian, metode pengumpulan data, metode analisis data, peralatan pendukung, dan perancangan algoritma.
3.1Tipe Penelitian
Penelitian ini merupakan penelitian non implementatif-analitik yang berarti produk yang dihasilkan berupa hasil analisis yang relevan dengan topik yang diteliti. Dalam penelitian ini, metode yang digunakan untuk menentukan resume yang paling sesuai dengan kualifikasi perekrut adalah metode perhitungan nilai similaritas tertinggi antara kualifikasi yang tercantum dalam resume dan kualifikasi yang dibutuhkan oleh perekrut sehingga dapat membantu perekrut dalam memilih 5 resume dengan tingkat kesesuaian tertinggi.
3.2Strategi Penelitian
Strategi penelitian yang dilakukan pada penelitian ini adalah penelitian eksperimen. Penelitian eksperimen adalah salah satu metode penelitian yang dapat menguji hipotesis mengenai hubungan sebab-akibat (Guritno, et al., 2011, p. 29). Kemudian, didefinisikan juga bahwa pendekatan ini merupakan penelitian untuk menguji sebab akibat antar variabel melalui langkah manipulasi, pengendalian, dan pengamatan (Musfiqon, 2016, p. 60). Penelitian eksperimen dilaksanakan dengan maksud mengetahui akibat dari suatu perlakuan melalui cara sengaja menimbulkan kejadian (eksperimen) (Effendi, 2013, p. 88).

## 3.3Lokasi Penelitian
Penelitian ini akan dilaksanakan di Fakultas Ilmu Komputer, Universitas Brawijaya, Kota Malang, Jawa Timur.
3.4Metode Pengumpulan Data
Data yang digunakan dalam penelitian ini didapatkan dari platform Kaggle, berjudul “Resume Dataset” yang dibuat oleh Snehaan Bhawal. Dataset ini terdiri dari 2.484 resume yang dikategorikan berdasarkan jenis pekerjaan yang dilamar, seperti HR, Desainer, Teknologi Informasi, Guru, dan kategori lainnya. Dataset tersebut mencakup format resume dalam bentuk string (teks) dan setiap resume diidentifikasi dengan ID unik. Informasi yang terdapat dalam dataset meliputi teks resume, data HTML hasil web scraping, dan kategori pekerjaan (Bhawal, 2021).
16
3.5Metode Analisis Data
Tujuan menganalisis data, antara lain mendapatkan perasaan terhadap data, menguji kualitas data, dan menguji hipotesis penelitian (Guritno, et al., 2011, p. 183). Menurut Cholissodin & Riyandani (2016), terdapat beberapa fase pada gambaran umum siklus hidup analitik data, seperti:
1.Discovery. Fase ini meliputi proses belajar, mencari dan menyelidiki fakta- fakta, mengidentifikasi masalah, mengembangkan konteks dan pemahaman, dan belajar tentang sumber data yang dibutuhkan, diikuti dengan perumusan hipotesis awal yang nantinya dapat diuji dengan data (Cholissodin & Riyandani, 2018, p. 22). 2.Data Preparation. Fase ini meliputi persiapan data sebelum dipakai untuk proses modelling dan evaluation yang dibagi menjadi dua bagian, yakni cleaning untuk menyeleksi beberapa fitur dan transformation untuk mengubah bentuk data ke dalam bentuk yang bisa diterima oleh algoritma (Abdusyukur, 2023). 3.Model Planning. Fase ini merupakan proses penentuan metode, teknik, dan alur kerja dengan mengeksplorasi data untuk mempelajari hubungan antara variabel yang selanjutnya memilih variabel kunci dan model yang paling cocok untuk digunakan (Cholissodin & Riyandani, 2018, p. 23). 4.Model Building. Pada fase ini, dataset dikembangkan untuk pengujian, pelatihan, dan tujuan produksi, serta mempertimangkan apakah dengan alat yanng ada akan cukup untuk menjalankan model (Cholissodin & Riyandani, 2018, p. 23). 5.Communicate Result. Pada fase ini, temuan-temuan yang didapatkan akan didiskusikan dengan para pemangku kepentingan untuk menentukan apakah hasil proyek tersebut sukses atau mengalami kegagalan (Cholissodin & Riyandani, 2018, p. 24). 6.Operationalize. Fase ini merupakan yang terakhir dengan menyerahkan laporan akhir, pengarahan, kode, dan dokumen teknis (Cholissodin & Riyandani, 2018, p. 24).
3.6Metode Evaluasi
Evaluasi metode similaritas teks dilakukan dengan menggunakan human-level performance sebagai tolak ukur untuk membandingkan korelasi antara keluaran lima resume dengan nilai similaritas tertinggi yang dihasilkan oleh implementasi metode dengan peringkat ground truth keluaran lima resume tersebut oleh seorang ahli yang memiliki pengalaman rekrutmen selama 2 tahun dan telah meninjau lebih dari 5000 resume di bidang sales, marketing, teknologi, healthcare, accounting, finance, human resources, dan legal. Evaluasi ini dilakukan untuk setiap posisi lowongan kerja dari total 24 kualifikasi lowongan kerja dan hasilnya dianalisis menggunakan tiga parameter penilaian, yakni korelasi sebagai parameter utama, serta relevansi dan senioritas sebagai parameter tambahan.
17
3.7Peralatan Pendukung
Dalam melakukan penelitian ini dari awal hingga akhir, diperlukan beberapa peralatan pendukung untuk membantu kelancaran jalannya penelitian. Peralatan pendukung tersebut meliputi perangkat lunak (software) dan perangkat keras (hardware)
3.7.1Perangkat Lunak (Software)
Perangkat lunak yang digunakan, antara lain:
1.Sistem operasi Microsoft Windows 10 Home 64-bit 2.Jupyter Notebook Versi 7.0.8 3.Bahasa pemrograman Python 3.12.4 4.Library Python Pandas Versi 2.2.3 5.Library Python BeautifulSoup4 (bs4) Versi 4.12.3 6.Library Python Gensim Versi 4.3.3 7.Library Python Numpy Versi 1.26.4 8.Library Python Scikit-learn Versi 1.6.1 9.Library Python NLTK Versi 3.9.1 10.Library Python TQDM Versi 4.67.1 11.Microsoft® Word 2016 MSO (Version 2505 Build 16.0.18827.20102) 32-bit
3.7.2Perangkat Keras (Hardware)
Perangkat keras yang digunakan, antara lain:
1.Windows 10 Home (2009) 2.Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz, 2401 Mhz, 2 Core(s), 4 Logical Processor(s) 3.Memori RAM 8,00 GB 4.SSD SanDisk Z400s 2.5 7MM 256GB
3.8Perancangan Algoritma
Pada perancangan algoritma dijabarkan proses pengimplementasian metode similaritas teks untuk otomatisasi penyaringan resume berdasarkan kualifikasi yang instansi butuhkan. Sebelumnya, dilakukan studi literatur, lalu proses implementasi ini dimulai dengan melakukan pra-pemrosesan dataset resume dan kualifikasi lowongan kerja. Kemudian, dilakukan perhitungan representasi teks untuk keduanya yang menghasilkan vektor-vektor guna menghitung similaritas antara vektor resume dengan vektor dari kualifikasi lowongan kerja. Setelah skor similaritas didapatkan, resume pun diurutkan mulai dari yang paling besar berdasarkan skor similaritasnya dan diberikan peringkat agar dapat dilakukan pengujian.
18
Gambar 3.1 Struktur proses implementasi pemeringkatan similaritas resume dan kualifikasi lowongan kerja
19

# BAB 4PERANCANGAN
Bab perancangan menjelaskan tentang perancangan algoritma dari metode- metode serta flow diagram dari setiap algoritma yang digunakan pada penelitian ini. Selain itu, bab ini juga merincikan perhitungan manual.
4.1Deskripsi Umum
Penelitian ini dilakukan dengan memeringkat lima resume dari dataset berdasarkan skor similaritas dengan kualifikasi suatu lowongan kerja dalam format CSV. Langkah pertama yang dilakukan adalah ekstraksi bagian-bagian (section) dari resume, diikuti dengan preprocessing pada dataset resume dan kualifikasi lowongan kerja. Setelah data dibersihkan, dilakukan perhitungan representasi teks untuk dataset resume dan kualifikasi lowongan kerja. Kemudian, vektor yang diperoleh dari resume dan kualifikasi lowongan kerja dilakukan perhitungan similaritas. Pemeringkatan lima resume ditentukan dengan skor similaritas tertinggi untuk setiap kualifikasi lowongan kerja. Hasil pemeringkatan diberikan ke seorang ahli untuk dievaluasi secara human-level performance.
Pada proses pemeringkatan lima resume, terdapat dua masukan, yakni dataset resume (Resume.csv)  dan kualifikasi lowongan kerja (kualifikasi_loker.csv) yang merupakan kumpulan 24 kualifikasi lowongan kerja dari situs pencarian kerja IDhttps://id.jobstreet.com/. Dalam dataset resume, terdapat kolom , Resume_strResume_htmlCategoryID, , dan . Kolom  merupakan nomor Resume_stridentifier yang dimiliki setiap resume, kolom  merupakan isi dari Resume_htmlresume, kolom  merupakan isi dari resume dengan format HTML, Categorydan kolom  merupakan pengelompokan industri atau bidang posisi pekerjaan dari setiap resume. Diketahui terdapat 24 kategori industri, yaitu: “HR”, “DESIGNER”, “INFORMATION-TECHNOLOGY”, “TEACHER”, “ADVOCATE”, “BUSINESS-DEVELOPMENT”, “HEALTHCARE”, “FITNESS”, “AGRICULTURE”, “BPO”, “SALES”, “CONSULTANT”, “DIGITAL-MEDIA”, “AUTOMOBILE”, “CHEF”, “FINANCE”, “APPAREL”, “ENGINEERING”, “ACCOUNTANT”, “CONSTRUCTION”, “PUBLIC- RELATIONS”, “BANKING, ARTS”,  dan “AVIATION”. Kategori-kategori tersebut yang dijadikan landasan untuk mencari 24 kualifikasi lowongan kerja.
4.2Preprocessing
4.2.1Ekstraksi Section
Langkah pertama adalah men-drop kolom yang tidak digunakan seperti kolom Category dan dilanjut melakukan ekstraksi bagian-bagian (section) dengan sectiontitleResume_htmlmengambil class  dari kolom . Setelah section setiap resume diketahui, isian dari setiap bagian diambil dari kolom Resume_strresume_df_1. Hasilnya adalah DataFrame  yang memiliki kolom IDResume_strResume_hmlSectionText, , , , dan . Diagram alur proses ekstraksi section tertera pada Gambar 4.1 hingga Gambar 4.4.
20
Gambar 4.1 Diagram alur ekstraksi section
21
Gambar 4.2 Diagram alur ekstraksi section
22
Gambar 4.3 Diagram alur ekstraksi section
23
Gambar 4.4 Diagram alur ekstraksi section
24
4.2.2Preprocessing Isian Resume
Setelah langkah ekstraksi section dilakukan dan menghasilkan DataFrame resume_df_1Text, selanjutnya adalah langkah preprocessing untuk kolom yang merupakan isian dari setiap section pada setiap resume. Langkah-langkah yang dilakukan mencakup penghapusan email, nomor telepon, tanggal, dan tahun. Selain itu, juga dilakukan penghapusan kata “Current”, “Present”, penghapusan istilah-istilah placeholder, penghapusan tanda baca, penghapusan tanggal, penghapusan angka, dan penghapusan spasi berlebih. Selanjutnya, dilakukan lematisasi dan penghapusan stopword agar kata-kata ditransformasikan menjadi bentuk dasar sesuai dengan kamus. Diagram alur proses preprocessing isian resume tertera pada Gambar 4.5 hingga Gambar 4.6.
Gambar 4.5 Diagram alur preprocessing isian resume
25
Gambar 4.6 Diagram alur preprocessing isian resume
26
4.2.3Preprocessing Penamaan Section
Setiap resume umumnya memiliki struktur informasi yang serupa, seperti bagian Education, Work Experience, Skills, dan Summary. Namun, penamaan atau label dari setiap bagian tersebut dapat sangat bervariasi antar resume, misalnya Work Experience bisa juga ditulis sebagai Experience. Oleh karena itu, diperlukan tahap preprocessing penamaan section untuk menyamakan atau menyeragamkan nama-nama section tersebut ke dalam satu format baku. Berikut ini merupakan daftar section standar yang digunakan.
1.Summary. Bagian yang berisi ringkasan profil, tujuan karir, atau deskripsi singkat. 2.Accomplishments/Awards. Bagian yang berisi pencapaian, penghargaan, atau prestasi yang pernah diraih. 3.Skills/Qualifications. Bagian yang berisi daftar keterampilan teknis maupun non-teknis, serta kualifikasi lainnya. 4.Education. Bagian yang berisi latar belakang pendidikan formal. 5.Experience. Bagian yang berisi pengalaman kerja atau pengalaman profesional lainnya. 6.Organization. Bagian yang berisi pengalaman dalam organisasi, kepanitiaan, atau kegiatan sosial. 7.Projects. Bagian yang berisi proyek-proyek yang pernah dikerjakan secara individu maupun kelompok. 8.Certifications. Bagian yang berisi rincian sertifikasi yang diperoleh. 9.Portfolio. Bagian yang berisi riwayat karya atau tautan ke portofolio online. 10.Others. Bagian-bagian lain yang tidak termasuk dalam section di atas, seperti referensi, hobi, atau informasi tambahan lainnya.
Diagram alur proses preprocessing penamaan section resume tertera pada Gambar 4.7.
27
Gambar 4.7 Diagram alur preprocessing penamaan section resume
28
4.2.4Preprocessing Kualifikasi Lowongan Kerja
DescriptionDilakukan preprocessing pada kolom  yang berisi kebutuhan terkait suatu posisi lowongan kerja. Langkah-langkah yang dilakukan mencakup tokenisasi dan lematisasi agar kata-kata ditransformasikan menjadi bentuk dasar sesuai dengan kamus. Diagram alur proses preprocessing isian kualifikasi lowongan kerja tertera pada Gambar 4.8.
Gambar 4.8 Diagram alur preprocessing isian kualifikasi lowongan kerja
29
4.3Perhitungan Representasi Teks

# 4.3.1TF-IDF
Pengimplementasian TF-IDF menggunakan library Scikit-learn. Meskipun proses implementasi menggunakan library, diagram alur yang menjelaskan detail perhitungan TF-IDF tertera pada Gambar 4.9 hingga Gambar 4.11.
Gambar 4.9 Diagram alur TF-IDF
30
Gambar 4.10 Diagram alur TF-IDF
31
Gambar 4.11 Diagram alur TF-IDF
32
4.3.2Word2Vec
Pengimplementasian Word2Vec menggunakan library Gensim. Meskipun proses implementasi menggunakan library, diagram alur yang menjelaskan detail perhitungan Word2Vec tertera pada Gambar 4.12 hingga Gambar 4.14.
Gambar 4.12 Diagram alur Word2Vec
33
Gambar 4.13 Diagram alur Word2Vec
34
Gambar 4.14 Diagram alur Word2Vec
35
4.4Perhitungan Similaritas
4.4.1Improved Sqrt-Cosine Similarity
Proses perhitungan Improved Sqrt-Cosine (ISC) Similarity digunakan untuk mengukur seberapa mirip antara resume dengan kualifikasi lowongan kerja. Pertama, fungsi ini memeriksa apakah kedua vektor ada. Jika tidak, hasilnya adalah 0, Selanjutnya, dihitung skor similaritas dengan menjumlahkan akar dari hasil kali elemen yang bersesuaian dalam kedua vektor sebagai pembilang. Hasil tersebut dibagi dengan hasil kali akar dari total nilai di masing-masing vektor sebagai penyebut. Terakhir, fungsi ini mengembalikan hasil pembagian yang merupakan skor kemiripan kedua vektor tersebut. Diagram alur proses perhitungan similaritas ISC tertera pada Gambar 4.15 hingga 4.16.
Gambar 4.15 Diagram alur Improved Sqrt-Cosine Similarity
36
Gambar 4.16 Diagram alur Improved Sqrt-Cosine Similarity
37
4.4.2Cosine Similarity
Meskipun dalam implementasi program digunakan library Scikit-learn untuk menghitung nilai Cosine Similarity (CosSim) antara resume dan kualifikasi lowongan kerja, proses perhitungan di balik fungsi tersebut tetap dijelaskan melalui diagram alur pada Gambar 4.17 dan 4.18. Pertama, fungsi ini akan memeriksa keberadaan kedua vektor. Jika salah satu tidak tersedia, maka akan menghasilkan pesan error. Selanjutnya, nilai CosSim dihitung dengan membagi jumlah hasil perkalian elemen-elemen bersesuaian dari kedua vektor (pembilang atau numerator) dengan hasil perkalian akar kuadrat dari jumlah kuadrat elemen pada masing-masing vektor (penyebut atau denominator). Skor akhir similaritas diperoleh dari pembagian antara pembilang dan penyebut. Diagram alur proses perhitungan CosSim tertera pada Gambar 4.17 hingga 4.18.
Gambar 4.17 Diagram alur Cosine Similarity
38
Gambar 4.18 Diagram alur Cosine Similarity
39
4.5Perhitungan Korelasi
Pada proses perhitungan korelasi, Spearman Rank Correlation Coefficient (SRCC) digunakan untuk mengukur seberapa sesuai antara dua peringkat, yaitu peringkat hasil keluaran implementasi metode dan peringkat yang disusun oleh ahli berdasarkan evaluasi terhadap hasil keluaran implementasi metode. Pertama, results_dfDataFrame  yang berisi kolom peringkat hasil implementasi metode RankResume_IDPositionSimilarity_Score(), , , , dan peringkat Rank_Expertground truth dari ahli () diinput. Selanjutnya, dihitung selisih antara peringkat hasil implementasi metode dan ahli per resume untuk setiap posisi. Selisih tersebut dikuadratkan dan dijumlahkan untuk memperoleh total deviasi peringkat. Terakhir, hasil penjumlahan tersebut  digunakan dalam rumus SRCC untuk mendapatkan nilai korelasi yang menunjukkan sejauh mana hasil implementasi metode sesuai dengan penilaian ahli. Diagram alur proses perhitungan SRCC tertera pada Gambar 4.19 hingga 4.20.
Gambar 4.19 Diagram alur Spearman Rank Correlation Coefficient
40
Gambar 4.20 Diagram alur Spearman Rank Correlation Coefficient
41
4.6Perhitungan Relevansi dan Senioritas
Pada proses perhitungan relevansi dan senioritas, digunakan persentase untuk mengukur seberapa sesuai antara resume-resume yang dihasilkan implementasi metode dengan setiap kualifikasi lowongan kerja berdasarkan penilaian ahli. results_dfPertama, DataFrame  yang berisi kolom peringkat hasil RankResume_IDPositionRelevanceimplementasi metode (), , , , dan Seniority diinput. Selanjutnya, untuk setiap kualifikasi lowongan kerja, hitung Relevanceberapa resume yang bernilai TRUE pada kolom  dan berapa resume Seniorityyang bernilai TRUE pada kolom . Kemudian, hitung persentase masing-masing relevansi dan senioritas dengan mengalikan 100 pada hasil pembagian antara jumlah resume bernilai TRUE dan jumlah total resume. Diagram alur proses perhitungan relevansi dan senioritas tertera pada Gambar 4.21 hingga 4.22.
Gambar 4.21 Diagram alur relevansi dan senioritas
42
Gambar 4.22 Diagram alur relevansi dan senioritas
43
4.7Perhitungan Manual
4.7.1Data Uji
Data uji resume yang digunakan untuk perhitungan manualisasi merupakan IDResume_strsalah satu resume yang diambil dari  dataset resume kolom , , Resume_htmldan . Rincian isi data uji resume tertera pada Tabel 4.1
Tabel 4.1 Data uji resume untuk perhitungan manual

## ID Resume_str Resume_html
# 15265464 INTERVENTION SPECIALIST <div class="fontsize fontface TEACHER OF MATH AND vmargins hmargins linespacing LANGUAGE ARTS Objective To gain pagesize" id="document"> <div the position as the resource room class="section firstsection" teacher at Howell Township Public id="SECTION_NAME537133600" Schools. Summary of style="padding-top:5px;"> <div Qualifications Demonstrated class="paragraph ability to design developmentally PARAGRAPH_NAME appropriate lessons and activities firstparagraph" allowing integration of all learning id="PARAGRAPH_537133600_1_3 styles. Highly educated in 50680747" style="padding- differentiated classrooms. top:0px;"> <div class="name Determined to maximize the thinbottomborder" educational achievement of each itemprop="name"> <span student. Trained in Developmental class="field" Reading Assessments, Common id="537133600FNAM1"> </span> Core Standards, Standard <span> </span> <span Solutions, Wonders, Anti-Bullying. class="field" Hard-working and organized. id="537133600LNAM1"> Knowledge and respect for all INTERVENTION SPECIALIST students and parental rights. TEACHER OF MATH AND Professional leadership and LANGUAGE ARTS</span> </div> management skills... <div class="myGap"> </div> <div class="lowerborder thinbottomborder"> </div> </div> </div> <div class="section" id="SECTION_SUMM537133602" style="padding-top:0px;"> <div class="heading"> <div class="sectiontitle thinbottomborder" id="SECTNAME_SUMM537133602 "> Objective</div> </div> <div class="paragraph firstparagraph" id="PARAGRAPH_537133602_1_3 50680754"...
44
Data uji kualifikasi lowongan kerja yang digunakan untuk perhitungan manualisasi merupakan salah satu kualifikasi lowongan kerja yang diambil dari PositionCompanydataset kualifikasi lowongan kerja dengan kolom , , dan Description. Rincian isi data uji kualifikasi lowongan kerja tertera pada Tabel 4.2
Tabel 4.2 Data uji kualifikasi lowongan kerja untuk perhitungan manual

## Position Company Description
Creative Director / PT Basic Entertainment Strong background in Manager event design, branding, and storytelling
Ability to lead and inspire a team of creatives and event professionals
Effectively present ideas to clients and collaborate with stakeholders
Ability to understand the project scope and requirements as outlined by clients or stakeholders.
Ensure that all designs comply with relevant industry standards
Bachelor Degree of any major..
4.7.2Perhitungan Manual Ekstraksi Section
sectiontitlePada proses ekstraksi bagian-bagian (section), diambil class Resume_htmldari kolom  menggunakan library BeautifulSoup4. Setelah section setiap resume diketahui, isian dari setiap section diambil dari kolom Resume_str seperti pada Tabel 4.3.
Tabel 4.3 Hasil perhitungan manual ekstraksi section

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles. Highly educated in differentiated classrooms...
45
Tabel 4.3 Hasil perhitungan manual ekstraksi section (lanjutan)

## Section Text
Experience Intervention Specialist Teacher of Math and Language Arts October 2013 to May －2014 Company Name  City , State Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology , December －2012 Georgian Court University  City , State GPA: Cum Laude Coursework in Psychology and Sociology Coursework in Intercultural and Group Communication...
Nicole Harrison Peters 732-513-7727 Nic_Harrison@aol.com
4.7.3Perhitungan Manual Preprocessing Resume
4.7.3.1Menghapus Email
Data uji resume yang sudah melalui proses ekstraksi section dilakukan preprocessing mulai dari menghapus email seperti pada Tabel 4.4.
Tabel 4.4 Hasil perhitungan manual preprocessing resume bagian menghapus email

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
Intervention Specialist Teacher of Math Experience and Language Arts    October 2013   to －May 2014     Company Name      City  , State      Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
46
Tabel 4.4 Hasil perhitungan manual preprocessing resume bagian menghapus email (lanjutan)

## Section Text
Education, Certifications, Endorements Bachelor of Arts   :   Psychology  , December 2012    Georgian Court －University      City  ,   State      GPA: Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...
Nicole Harrison Peters 732-513-7727
4.7.3.2Menghapus Nomor Telepon
Data uji resume yang sudah melalui preprocessing menghapus email, dilanjutkan menghapus nomor telepon seperti pada Tabel 4.5.
Tabel 4.5 Hasil perhitungan manual preprocessing resume bagian menghapus nomor telepon

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
Experience Intervention Specialist Teacher of Math and Language Arts    October 2013   to －May 2014     Company Name      City  , State      Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts   :   Psychology  , December 2012    Georgian Court －University      City  ,   State      GPA: Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
47
－ 4.7.3.3Menghapus Berbagai Tipe Tanda Minus (, –, —)
Data uji resume yang sudah melalui preprocessing menghapus nomor telepon, dilanjutkan menghapus berbagai tipe tanda minus yang kemungkinan digunakan dalam penulisan informasi seperti lokasi, tanggal, atau rentang waktu. Hasil dari proses penghapusan ini tertera pada Tabel 4.6.
Tabel 4.6 Hasil perhitungan manual preprocessing resume bagian menghapus －berbagai tipe tanda minus (, –, —)

## Section Text
To gain the position as the resource room Objective teacher at Howell Township Public Schools.
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
Experience Intervention Specialist Teacher of Math and Language Arts    October 2013   to May 2014     Company Name       City  , State      Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts   :   Psychology  , December 2012    Georgian Court University       City  ,   State      GPA:   Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.4Menghapus Nama Bulan
Data uji resume yang sudah melalui preprocessing menghapus berbagai tipe tanda minus, dilanjutkan menghapus nama bulan. Hasil dari proses penghapusan ini tertera pada Tabel 4.7.
Tabel 4.7 Hasil perhitungan manual preprocessing resume bagian menghapus nama bulan

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
48
Tabel 4.7 Hasil perhitungan manual preprocessing resume bagian menghapus nama bulan (lanjutan)

## Section Text
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
Experience Intervention Specialist Teacher of Math and Language Arts     2013   to    2014 Company Name       City  ,   State Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts   :   Psychology  ,    2012 Georgian Court University       City  , State      GPA:   Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.5Menghapus Kata “Present” dan “Current”
Data uji resume yang sudah melalui preprocessing menghapus nama bulan, dilanjutkan menghapus kata atau istilah seperti “Present” dan “Current” yang biasanya digunakan untuk menunjukkan rentang waktu. Hasil dari proses penghapusan ini tertera pada Tabel 4.8.
Tabel 4.8 Hasil perhitungan manual preprocessing resume bagian menghapus kata “Present” dan “Current”

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Demonstrated ability to design Summary of Qualifications developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
49
Tabel 4.8 Hasil perhitungan manual preprocessing resume bagian menghapus kata “Present” dan “Current” (lanjutan)

## Section Text
Experience Intervention Specialist Teacher of Math and Language Arts     2013   to    2014 Company Name       City  ,   State Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts   :   Psychology  ,    2012 Georgian Court University       City  , State      GPA:   Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.6Menghapus Tanggal
Data uji resume yang sudah melalui preprocessing menghapus kata atau istilah seperti “Present” dan “Current”, dilanjutkan dengan penghapusan format-format tanggal dan rentang waktu. Hasil dari proses penghapusan ini tertera pada Tabel 4.9.
Tabel 4.9 Hasil perhitungan manual preprocessing resume bagian menghapus tanggal

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
50
Tabel 4.9 Hasil perhitungan manual preprocessing resume bagian menghapus tanggal (lanjutan)

## Section Text
Experience Intervention Specialist Teacher of Math and Language Arts        to         Company Name       City  ,   State      Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts   :   Psychology  , Georgian Court University       City  , State      GPA:   Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.7Menghapus Placeholder
Data uji resume yang sudah melalui preprocessing menghapus tanggal, dilanjutkan menghapus placeholder yang biasanya digunakan untuk menunjukkan lokasi atau perusahaan seperti “Company Name” dan “State”. Hasil dari proses penghapusan ini tertera pada Tabel 4.10.
Tabel 4.10 Hasil perhitungan manual preprocessing resume bagian menghapus placeholder

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles.  Highly educated in differentiated classrooms...
51
Tabel 4.10 Hasil perhitungan manual preprocessing resume bagian menghapus placeholder (lanjutan)

## Section Text
Experience Intervention Specialist Teacher of Math and Language Arts        to                  , Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Bachelor of Arts   :   Psychology  ,        Education, Certifications, Endorements Georgian Court University         ,         GPA: Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.8Menghapus Tanda Baca
Data uji resume yang sudah melalui preprocessing menghapus placeholder, dilanjutkan menghapus tanda baca. Hasil dari proses penghapusan ini tertera pada Tabel 4.11.
Tabel 4.11 Hasil perhitungan manual preprocessing resume bagian menghapus tanda baca

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles  Highly educated in differentiated classrooms...
Experience Intervention Specialist Teacher of Math and Language Arts        to Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
52
Tabel 4.11 Hasil perhitungan manual preprocessing resume bagian menghapus tanda baca (lanjutan)

## Section Text
Education, Certifications, Endorements Bachelor of Arts      Psychology Georgian Court University                  GPA: Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.9Menghapus Angka
Data uji resume yang sudah melalui preprocessing menghapus tanda baca, dilanjutkan menghapus angka. Hasil dari proses penghapusan ini tertera pada Tabel 4.12.
Tabel 4.12 Hasil Perhitungan manual preprocessing resume bagian menghapus angka

## Section Text
Objective To gain the position as the resource room teacher at Howell Township Public Schools.
Demonstrated ability to design Summary of Qualifications developmentally appropriate lessons and activities allowing integration of all learning styles  Highly educated in differentiated classrooms...
Experience Intervention Specialist Teacher of Math and Language Arts        to Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Education, Certifications, Endorements Bachelor of Arts      Psychology Georgian Court University                  GPA Cum Laude      Coursework in Psychology and Sociology  Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
53
4.7.3.10Menghapus Spasi Kosong Berlebih
Data uji resume yang sudah melalui preprocessing menghapus angka, dilanjutkan menghapus spasi kosong berlebih yang biasanya muncul akibat penghapusan karakter. Hasil dari proses penghapusan ini tertera pada Tabel 4.13.
Tabel 4.13 Hasil perhitungan manual preprocessing resume bagian menghapus spasi kosong berlebih

## Section Text
To gain the position as the resource room Objective teacher at Howell Township Public Schools
Summary of Qualifications Demonstrated ability to design developmentally appropriate lessons and activities allowing integration of all learning styles Highly educated in differentiated classrooms...
Experience Intervention Specialist Teacher of Math and Language Arts to Identified students with substantial academic difficulties through evaluation using Developmental Reading Assessments and consultation with staff members of referred students...
Bachelor of Arts Psychology Georgian Education, Certifications, Endorements Court University GPA Cum Laude Coursework in Psychology and Sociology Coursework in Intercultural and Group Communication...

## Nicole Harrison Peters
4.7.3.11Lematisasi dan Menghapus Stop Words
Data uji resume yang sudah melalui preprocessing menghapus spasi kosong berlebih, dilanjutkan menghapus stop word dari dari Bahasa Inggris menggunakan daftar stop words yang tersedia pada library Natural Language Toolkit (NLTK). Hasil dari proses penghapusan ini tertera pada Tabel 4.14.
Tabel 4.14 Hasil perhitungan manual preprocessing resume bagian lematisasi dan menghapus stop words

## Section Text
Objective gain position resource room teacher Howell Township Public Schools
54
Tabel 4.14 Hasil perhitungan manual preprocessing resume bagian lematisasi dan menghapus stop words (lanjutan)

## Section Text
Summary of Qualifications Demonstrated ability design developmentally appropriate lesson activity allow integration learning style Highly educate differentiated classroom...
Experience Intervention Specialist Teacher Math Language Arts Identified student substantial academic difficulty evaluation use Developmental Reading Assessments consultation staff member referred student...
Education, Certifications, Endorements Bachelor Arts Psychology Georgian Court University GPA Cum Laude Coursework Psychology Sociology Coursework Intercultural Group Communication...

## Nicole Harrison Peters
4.7.3.12Mengonversi Nama Section Menjadi Huruf Kecil (Lower Casing)
Data uji resume yang sudah melalui preprocessing menghapus tanda koma Sectionberlebih, dilanjutkan mengonversi nama-nama section di kolom menjadi huruf kecil untuk memudahkan proses selanjutnya dalam merapikan nama-nama section. Hasil dari proses pengonversian ini tertera pada Tabel 4.15.
Tabel 4.15 Hasil perhitungan manual penyetaraan nama section bagian mengonversi nama section menjadi huruf kecil (lower casing)

## Section Text
gain position resource room teacher objective Howell Township Public Schools
Demonstrated ability design summary of qualifications developmentally appropriate lesson activity allow integration learning style Highly educate differentiated classroom...
experience Intervention Specialist Teacher Math Language Arts Identified student substantial academic difficulty evaluation use Developmental Reading Assessments consultation staff member referred student...
55
Tabel 4.15 Hasil perhitungan manual penyetaraan nama section bagian mengonversi nama section menjadi huruf kecil (lower casing) (lanjutan)

## Section Text
education, certifications, endorements Bachelor Arts Psychology Georgian Court University GPA Cum Laude Coursework Psychology Sociology Coursework Intercultural Group Communication...
nicole harrison peters
4.7.3.13Mencari Nilai Unik Section
Data uji resume yang sudah melalui preprocessing lower casing nama-nama section, dilanjutkan dengan pencarian nama-nama section yang unik untuk mengidentifikasi variasi nama section yang terdapat dalam seluruh dataset resume. Hasil dari proses pencarian nama-nama section ini tertera pada Tabel 4.16.
Tabel 4.16 Hasil perhitungan manual penyetaraan nama section bagian mengonversi nama section menjadi huruf kecil (lower casing)
Nama-Nama Section Unik
summary
highlights
accomplishments
experience
education
…
mpd projects/clients
technical projects
core compentencies
4.7.3.14Standarisasi Nama Section
Setelah mengetahui variasi nama section yang terdapat dalam seluruh dataset resume, dilakukan pemetaan nama-nama section untuk menyeragamkan agar konsisten dengan nama-nama section yang telah ditentukan pada penelitian ini, seperti “Summary”, “Accomplishments/Awards”, "Skills/Qualifications", "Education", "Experience", "Organization", "Projects", "Certifications", "Portfolio", "Others". Hasil dari proses penyetaraan nama-nama section ini untuk data uji resume tertera pada Tabel 4.17.
56
Tabel 4.17 hasil perhitungan manual penyetaraan nama section bagian menyeragamkan pengelompokan section berdasarkan pemetaan

## Section Text
Education Bachelor Arts Psychology Georgian Court University GPA Cum Laude Coursework Psychology Sociology Coursework Intercultural Group Communication...
Experience Intervention Specialist Teacher Math Language Arts Identified student substantial academic difficulty evaluation use Developmental Reading Assessments consultation staff member referred student...
Summary gain position resource room teacher Howell Township Public Schools Demonstrated ability design developmentally appropriate lesson activity allow integration learning style Highly educate differentiated classroom...
nicole harrison peters
4.7.3.15Klasifikasi, Penghapusan, dan Pengelompokan Section Tidak Valid
Setelah penyeragaman nama-nama section, dilakukan proses klasifikasi, penghapusan, dan pengelompokan section yang tidak valid. Proses ini diawali dengan mengidentifikasi section yang tidak termasuk dalam daftar nama section yang telah ditentukan. Jika ditemukan kata kunci tertentu dalam teks, seperti “years”, “experience”, atau “I am”, maka section tersebut diklasifikasikan ke dalam kategori “Summary”. Jika terdapat kata “LinkedIn”, maka dikategorikan ke dalam Section“Portfolio”. Baris data yang memiliki isian kolom  tidak sesuai dengan Textdaftar nama section yang sudah ditentukan dan kolom  tidak ada isinya, Sectionmaka dihapus. Sedangkan, isian kolom  yang tidak termasuk dalam Textdaftar nama section, tetapi memiliki isi di dalam kolom , maka dipetakan ke Textdalam section “Others”. Selain itu, seluruh baris yang isian kolom -nya kosong, hanya berisi spasi atau bernilai null juga dihapus untuk menjaga kualitas data. Hasil dari proses klasifikasi, penghapusan, dan pengelompokan section ini untuk data uji resume tertera pada Tabel 4.18.
57
Tabel 4.18 Hasil perhitungan manual penyetaraan nama section bagian klasifikasi, penghapusan, dan pengelompokan section tidak valid

## Section Text
Education Bachelor Arts Psychology Georgian Court University GPA Cum Laude Coursework Psychology Sociology Coursework Intercultural Group Communication...
Experience Intervention Specialist Teacher Math Language Arts Identified student substantial academic difficulty evaluation use Developmental Reading Assessments consultation staff member referred student...
Summary gain position resource room teacher Howell Township Public Schools Demonstrated ability design developmentally appropriate lesson activity allow integration learning style Highly educate differentiated classroom...
4.7.3.16Mengonversi Isi Resume Menjadi Huruf Kecil (Lower Casing)
TextSetelah merapikan section, dilakukan pengonversian isi kolom  menjadi huruf kecil untuk menyamakan format teks serta memudahkan proses representasi teks pada tahap selanjutnya. Hasil dari proses ini untuk data uji resume tertera pada Tabel 4.19.
Tabel 4.19 Hasil perhitungan manual penyetaraan nama section bagian mengonversi isi resume menjadi huruf kecil (lower casing)

## Section Text
Education bachelor arts psychology georgian court university gpa cum laude coursework psychology sociology coursework intercultural group communication...
Experience intervention specialist teacher math language arts identified student substantial academic difficulty evaluation use developmental reading assessments consultation staff member...
Summary gain position resource room teacher howell township public schools demonstrated ability design developmentally appropriate lesson activity allow integration learning style highly educate differentiated classroom...
58
4.7.4Perhitungan Manual Preprocessing Kualifikasi Lowongan Kerja
4.7.4.1Mengonversi Isi Kualifikasi Lowongan Kerja Menjadi Huruf Kecil (Lower Casing)
Pada proses preprocessing kualifikasi lowongan kerja, dilakukan Descriptionpengonversian isi kolom  menjadi huruf kecil untuk menyamakan format teks serta memudahkan proses preprocessing selanjutnya. Hasil dari proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.20.
Tabel 4.20 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian mengonversi isi kualifikasi lowongan kerja menjadi huruf kecil (lower casing)

## Category Position Company Description
ARTS Creative Director / PT Basic strong background Manager Entertainment  in event design, branding, and storytelling
ability to lead and inspire a team of creatives and event professionals...
4.7.4.2Menghapus Angka
DescriptionSetelah proses lower casing isi kolom , dilakukan penghapusan angka-angka. Hasil dari proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.21.
Tabel 4.21 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian menghapus angka

## Category Position Company Description
ARTS Creative Director / PT Basic strong background Manager Entertainment  in event design, branding, and storytelling
ability to lead and inspire a team of creatives and event professionals...
59
4.7.4.3Menghapus Tanda Baca
Setelah proses penghapusan angka, dilakukan penghapusan tanda baca. Hasil dari proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.22.
Tabel 4.22 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian menghapus tanda baca

## Category Position Company Description
Creative Director / PT Basic strong background ARTS Manager Entertainment  in event design branding and storytelling
ability to lead and inspire a team of creatives and event professionals...
4.7.4.4Menghapus Spasi Kosong Berlebih
Setelah proses penghapusan tanda baca, dilakukan penghapusan spasi kosong berlebih yang biasanya muncul akibat penghapusan karakter. Hasil dari proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.23.
Tabel 4.23 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian menghapus spasi kosong berlebih

## Category Position Company Description
ARTS Creative Director / PT Basic strong background in event design Manager Entertainment branding and storytelling ability to lead and inspire a team of creatives and event professionals...
60
4.7.4.5Lematisasi dan Menghapus Stop Words
Setelah proses penghapusan spasi kosong berlebih, dilakukan penghapusan stop words dari Bahasa Inggris. Hasil dari proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.24.
Tabel 4.24 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja bagian lematisasi dan menghapus stop words

## Category Position Company Description
Creative Director / PT Basic strong background ARTS Manager Entertainment  event design branding storytelling ability lead inspire team creatives event professional...
4.7.5Perhitungan Manual Representasi Teks
4.7.5.1Perhitungan Manual TF-IDF
Tujuan dari TF-IDF adalah menghitung tingkat kepentingan sebuah kata dalam suatu dokumen dibandingkan dengan keseluruhan dokumen dalam korpus. Untuk perhitungan manual pada resume, digunakan sample data dari section “Experience” dengan rincian tertera pada Tabel 4.25.
Tabel 4.25 Korpus resume untuk perhitungan manual

## Dokumen 1 Dokumen 2 Dokumen 3
demonstrated ability digital production manager acted liaison senior design developmentally responsible aspect digital business manager various appropriate lesson activity production premium global stake holder allow integration learning printing graphic design recruited analysts process style highly educate company delivering high suggest best practice differentiated classroom quality production meet effective method determined maximize client direct deadline educational achievement student trained developmental reading assessments
Tahap pertama adalah menghitung Term Frequency (TF). Pada library Scikit- learn, nilai TF merupakan jumlah kemunculan term pada setiap dokumen seperti pada Persamaan 4.1.
𝑇𝐹=𝑓           (4.1)
(𝑡,𝑑)𝑡,𝑑
61
Jumlah kemunculan (frekuensi) term setiap dokumen untuk data uji resume tertera pada Tabel 4.26.
Tabel 4.26 Perhitungan manual frekuensi term setiap resume
Term f di Dokumen 1 f di Dokumen 2 f di Dokumen 3
demonstrated 1 0 0
ability 1 0 0
design 1 1 0
developmentally 1 0 0
appropriate 1 0 0
lesson 1 0 0
activity 1 0 0
allow 1 0 0
integration 1 0 0
learning 1 0 0
style 1 0 0
highly 1 0 0
educate 1 0 0
differentiated 1 0 0
classroom 1 0 0
determined 1 0 0
maximize 1 0 0
educational 1 0 0
achievement 1 0 0
student 1 0 0
trained 1 0 0
developmental 1 0 0
reading 1 0 0
assessments 1 0 0
digital 0 2 0
production 0 3 0
manager 0 1 1
62
Tabel 4.26 Perhitungan manual frekuensi term setiap resume (lanjutan)
Term f di Dokumen 1 f di Dokumen 2 f di Dokumen 3
responsible 0 1 0
aspect 0 1 0
premium 0 1 0
printing 0 1 0
graphic 0 1 0
company 0 1 0
delivering 0 1 0
high 0 1 0
quality 0 1 0
meet 0 1 0
client 0 1 0
direct 0 1 0
deadline 0 1 0
acted 0 0 1
liaison 0 0 1
senior 0 0 1
business 0 0 1
various 0 0 1
global 0 0 1
stake 0 0 1
holder 0 0 1
recruited 0 0 1
analysts 0 0 1
process 0 0 1
suggest 0 0 1
best 0 0 1
practice 0 0 1
63
Tabel 4.26 Perhitungan manual frekuensi term setiap resume (lanjutan)
Term f di Dokumen 1 f di Dokumen 2 f di Dokumen 3
effective 0 0 1
method 0 0 1
Contoh perhitungan untuk kata “demonstrated” pada setiap dokumen tertera mulai dari Persamaan 4.2

# 𝑇𝐹=1        (4.2)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1)

# 𝑇𝐹=0        (4.3)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2)

# 𝑇𝐹=0        (4.4)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3)
Hasil perhitungan TF untuk seluruh term pada ketiga dokumen tertera pada Tabel 4.27.
Tabel 4.27 Perhitungan manual TF korpus resume
Term TF di Dokumen 1 TF di Dokumen 2 TF di Dokumen 3
demonstrated 1 0 0
ability 1 0 0
design 1 1 0
developmentally 1 0 0
appropriate 1 0 0
lesson 1 0 0
activity 1 0 0
allow 1 0 0
integration 1 0 0
learning 1 0 0
style 1 0 0
highly 1 0 0
educate 1 0 0
differentiated 1 0 0
classroom 1 0 0
determined 1 0 0
maximize 1 0 0
educational 1 0 0
64
Tabel 4.27 Perhitungan manual TF korpus resume (lanjutan)
Term TF di Dokumen 1 TF di Dokumen 2 TF di Dokumen 3
achievement 1 0 0
student 1 0 0
trained 1 0 0
developmental 1 0 0
reading 1 0 0
assessments 1 0 0
digital 0 2 0
production 0 3 0
manager 0 1 1
responsible 0 1 0
aspect 0 1 0
premium 0 1 0
printing 0 1 0
graphic 0 1 0
company 0 1 0
delivering 0 1 0
high 0 1 0
quality 0 1 0
meet 0 1 0
client 0 1 0
direct 0 1 0
deadline 0 1 0
acted 0 0 1
liaison 0 0 1
senior 0 0 1
business 0 0 1
various 0 0 1
global 0 0 1
stake 0 0 1
holder 0 0 1
recruited 0 0 1
65
Tabel 4.27 Perhitungan manual TF korpus resume (lanjutan)
Term TF di Dokumen 1 TF di Dokumen 2 TF di Dokumen 3
analysts 0 0 1
process 0 0 1
suggest 0 0 1
best 0 0 1
practice 0 0 1
effective 0 0 1
method 0 0 1
Selanjutnya menghitung Inverse Document Frequency (IDF) dengan menghitung terlebih dahulu nilai Document Frequency (DF). Nilai DF didapatkan dari menghitung jumlah dokumen yang memiliki suatu term, rumusnya tertera pada Persamaan 4.5, mulai dari Persamaan 4.6 merupakan contoh perhitungan IDF untuk term “demonstrated”.
1+𝑁 𝐼𝐷𝐹=log()+1        (4.5)
(𝑡) 1+𝑑𝑓
1+3 ()𝐼𝐷𝐹=log()+1=log2+1     (4.6)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑) 1+1

# 𝐼𝐷𝐹=0,6931471806+1=1.693147181    (4.7)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑)
Hasil IDF untuk semua term di korpus resume tertera pada Tabel 4.28.
Tabel 4.28 Perhitungan manual IDF korpus resume

## Term DF IDF
demonstrated 1 1,693147181
ability 1 1,693147181
design 2 1,287682072
developmentally 1 1,693147181
appropriate 1 1,693147181
lesson 1 1,693147181
activity 1 1,693147181
allow 1 1,693147181
integration 1 1,693147181
learning 1 1,693147181
style 1 1,693147181
highly 1 1,693147181
66
Tabel 4.28 Perhitungan manual IDF korpus resume (lanjutan)

## Term DF IDF
educate 1 1,693147181
differentiated 1 1,693147181
classroom 1 1,693147181
determined 1 1,693147181
maximize 1 1,693147181
educational 1 1,693147181
achievement 1 1,693147181
student 1 1,693147181
trained 1 1,693147181
developmental 1 1,693147181
reading 1 1,693147181
assessments 1 1,693147181
digital 1 1,693147181
production 1 1,693147181
manager 2 1,287682072
responsible 1 1,693147181
aspect 1 1,693147181
premium 1 1,693147181
printing 1 1,693147181
graphic 1 1,693147181
company 1 1,693147181
delivering 1 1,693147181
high 1 1,693147181
quality 1 1,693147181
meet 1 1,693147181
client 1 1,693147181
direct 1 1,693147181
deadline 1 1,693147181
acted 1 1,693147181
liaison 1 1,693147181
senior 1 1,693147181
67
Tabel 4.28 Perhitungan manual IDF korpus resume (lanjutan)

## Term DF IDF
business 1 1,693147181
various 1 1,693147181
global 1 1,693147181
stake 1 1,693147181
holder 1 1,693147181
recruited 1 1,693147181
analysts 1 1,693147181
process 1 1,693147181
suggest 1 1,693147181
best 1 1,693147181
practice 1 1,693147181
effective 1 1,693147181
method 1 1,693147181
Setelah mendapatkan nilai Term Frequency (TF) dan Inverse Document Frequency (IDF), nilai TF-IDF dapat didapatkan dengan mengalikan nilai TF dengan nilai IDF seperti pada Persamaan 4.8. Contoh perhitungan manual untuk term “demonstrated” tertera mulai dari Persamaan 4.9

# 𝑇𝐹−𝐼𝐷𝐹=𝑇𝐹×𝐼𝐷𝐹       (4.8)
()𝑡,𝑑(𝑡,𝑑)(𝑡)

# 𝑇𝐹−𝐼𝐷𝐹=1×1,693147181=1,693147181   (4.9)
()𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1

# 𝑇𝐹−𝐼𝐷𝐹=0×1,693147181=0    (4.10)
()𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2

# 𝑇𝐹−𝐼𝐷𝐹=0×1,693147181=0    (4.11)
()𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3
Hasil TF-IDF seluruh term pada ketiga dokumen tertera pada Tabel 4.29.
Tabel 4.29 Perhitungan manual TF-IDF korpus resume
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
demonstrated 1,693147181 0 0
ability 1,693147181 0 0
design 1,287682072 1,287682072 0
developmentally 1,693147181 0 0
appropriate 1,693147181 0 0
lesson 1,693147181 0 0
68
Tabel 4.29 Perhitungan manual TF-IDF korpus resume (lanjutan)
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
activity 1,693147181 0 0
allow 1,693147181 0 0
integration 1,693147181 0 0
learning 1,693147181 0 0
style 1,693147181 0 0
highly 1,693147181 0 0
educate 1,693147181 0 0
differentiated 1,693147181 0 0
classroom 1,693147181 0 0
determined 1,693147181 0 0
maximize 1,693147181 0 0
educational 1,693147181 0 0
achievement 1,693147181 0 0
student 1,693147181 0 0
trained 1,693147181 0 0
developmental 1,693147181 0 0
reading 1,693147181 0 0
assessments 1,693147181 0 0
digital 0 3,386294361 0
production 0 5,079441542 0
manager 0 1,287682072 1,287682072
responsible 0 1,693147181 0
aspect 0 1,693147181 0
premium 0 1,693147181 0
printing 0 1,693147181 0
graphic 0 1,693147181 0
company 0 1,693147181 0
delivering 0 1,693147181 0
high 0 1,693147181 0
quality 0 1,693147181 0
meet 0 1,693147181 0
69
Tabel 4.29 Perhitungan manual TF-IDF korpus resume (lanjutan)
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
client 0 1,693147181 0
direct 0 1,693147181 0
deadline 0 1,693147181 0
acted 0 0 1,693147181
liaison 0 0 1,693147181
senior 0 0 1,693147181
business 0 0 1,693147181
various 0 0 1,693147181
global 0 0 1,693147181
stake 0 0 1,693147181
holder 0 0 1,693147181
recruited 0 0 1,693147181
analysts 0 0 1,693147181
process 0 0 1,693147181
suggest 0 0 1,693147181
best 0 0 1,693147181
practice 0 0 1,693147181
effective 0 0 1,693147181
method 0 0 1,693147181
70
Secara bawaan, TfidfTransformer dari library Scikit-learn
2
mengimplementasikan L (Euclidean distance) norm pada hasil perhitungan TF- IDF. Perhitungan normalisasi tertera pada Persamaan 4.12 dan contoh perhitungannya untuk term “demonstrated” tertera mulai dari Persamaan 4.13
𝑣𝑣 𝑣==       (4.12)
𝑛𝑜𝑟𝑚
222‖‖𝑣√𝑣+𝑣+⋯+𝑣
212𝑛
1,693147181 𝑣=   (4.13)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1)
222√(1,693147181)+(1,693147181)+⋯+(0)
1,693147181 𝑣==0,2059410105    (4.14)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1) 8,221515356
0 𝑣=      (4.15)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2)
222√(0)+(0)+⋯+(0)
0 𝑣==0     (4.16)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2) 8,823360017
0 𝑣=    (4.17)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3)
222√(0)+(0)+⋯+(1,693147181)
0 𝑣==0      (4.18)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3) 6,893916385
Hasil akhir TF-IDF setelah normalisasi tertera pada tabel 4.30.
Tabel 4.30 Perhitungan manual TF-IDF korpus resume setelah normalisasi
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
demonstrated 0,2059410105 0 0
ability 0,2059410105 0 0
design 0,1566234467 0,1459401033 0
developmentally 0,2059410105 0 0
appropriate 0,2059410105 0 0
lesson 0,2059410105 0 0
activity 0,2059410105 0 0
allow 0,2059410105 0 0
integration 0,2059410105 0 0
learning 0,2059410105 0 0
style 0,2059410105 0 0
highly 0,2059410105 0 0
educate 0,2059410105 0 0
differentiated 0,2059410105 0 0
classroom 0,2059410105 0 0
determined 0,2059410105 0 0
maximize 0,2059410105 0 0
71
Tabel 4.30 Perhitungan manual TF-IDF korpus resume setelah normalisasi (lanjutan)
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
educational 0,2059410105 0 0
achievement 0,2059410105 0 0
student 0,2059410105 0 0
trained 0,2059410105 0 0
developmental 0,2059410105 0 0
reading 0,2059410105 0 0
assessments 0,2059410105 0 0
digital 0 0,3837873956 0
production 0 0,5756810934 0
manager 0 0,1459401033 0,1867852757
responsible 0 0,1918936978 0
aspect 0 0,1918936978 0
premium 0 0,1918936978 0
printing 0 0,1918936978 0
graphic 0 0,1918936978 0
company 0 0,1918936978 0
delivering 0 0,1918936978 0
high 0 0,1918936978 0
quality 0 0,1918936978 0
meet 0 0,1918936978 0
client 0 0,1918936978 0
direct 0 0,1918936978 0
deadline 0 0,1918936978 0
acted 0 0 0,245600191
liaison 0 0 0,245600191
senior 0 0 0,245600191
business 0 0 0,245600191
various 0 0 0,245600191
global 0 0 0,245600191
stake 0 0 0,245600191
72
Tabel 4.30 Perhitungan manual TF-IDF korpus resume setelah normalisasi (lanjutan)
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
holder 0 0 0,245600191
recruited 0 0 0,245600191
analysts 0 0 0,245600191
process 0 0 0,245600191
suggest 0 0 0,245600191
best 0 0 0,245600191
practice 0 0 0,245600191
effective 0 0 0,245600191
method 0 0 0,245600191
Perhitungan manual pada kualifikasi lowongan kerja menggunakan beberapa Descriptionsample data dari kolom  dengan rincian yang bisa dilihat pada Tabel 4.31.
Tabel 4.31 Korpus kualifikasi lowongan kerja untuk perhitungan manual

## Dokumen 4 Dokumen 5 Dokumen 6
strong background event execute daytoday design play vital role support lead design branding request internal external teacher create nurturing storytelling ability lead communication material stimulate learning inspire team creatives develop creative visual environment young event professional content include motion student assist lead teacher effectively present idea graphic static design planning implement client collaborate engage educational stakeholder activity
Nilai Term Frequency (TF) untuk deskripsi kualifikasi lowongan kerja dapat dihitung berdasarkan term yang telah ditokenisasi sebelumnya dari korpus resume, sehingga hasil perhitungan TF kualifikasi lowongan kerja tertera pada Tabel 4.32
Tabel 4.32 Perhitungan manual TF korpus kualifikasi lowongan kerja
Term TF di Dokumen 4 TF di Dokumen 5 TF di Dokumen 6
demonstrated 0 0 0
ability 1 0 0
design 1 2 0
73
Tabel 4.32 Perhitungan manual TF korpus kualifikasi lowongan kerja (lanjutan)
Term TF di Dokumen 4 TF di Dokumen 5 TF di Dokumen 6
developmentally 0 0 0
appropriate 0 0 0
lesson 0 0 0
activity 0 0 1
allow 0 0 0
integration 0 0 0
learning 0 0 1
style 0 0 0
highly 0 0 0
educate 0 0 0
differentiated 0 0 0
classroom 0 0 0
determined 0 0 0
maximize 0 0 0
educational 0 0 1
achievement 0 0 0
student 0 0 1
trained 0 0 0
developmental 0 0 0
reading 0 0 0
assessments 0 0 0
digital 0 0 0
production 0 0 0
manager 0 0 0
responsible 0 0 0
aspect 0 0 0
premium 0 0 0
printing 0 0 0
74
Tabel 4.32 Perhitungan manual TF korpus kualifikasi lowongan kerja (lanjutan)
Term TF di Dokumen 4 TF di Dokumen 5 TF di Dokumen 6
graphic 0 1 0
company 0 0 0
delivering 0 0 0
high 0 0 0
quality 0 0 0
meet 0 0 0
client 1 0 0
direct 0 0 0
deadline 0 0 0
acted 0 0 0
liaison 0 0 0
senior 0 0 0
business 0 0 0
various 0 0 0
global 0 0 0
stake 0 0 0
holder 0 0 0
recruited 0 0 0
analysts 0 0 0
process 0 0 0
suggest 0 0 0
best 0 0 0
practice 0 0 0
effective 0 0 0
method 0 0 0
75
Nilai Inverse Document Frequency (IDF) bisa didapatkan dengan menghitung document frequency (DF) terlebih dahulu. Kemudian, dihitung dengan formula seperti pada Persamaan 4.19. Mulai dari Persamaan 4.20 mendemonstrasikan perhitungan IDF untuk term “design”.
1+𝑁 𝐼𝐷𝐹=log()+1        (4.19)
(𝑡) 1+𝑑𝑓
1+34 𝐼𝐷𝐹=log()+1=log()+1      (4.20)
(𝑑𝑒𝑠𝑖𝑔𝑛) 1+23

# 𝐼𝐷𝐹=0,2876820725+1=1,287682072    (4.21)
(𝑑𝑒𝑠𝑖𝑔𝑛)
Hasil perhitungan IDF korpus kualifikasi lowongan kerja tertera pada Tabel 4.33.
Tabel 4.33 Perhitungan manual IDF korpus kualifikasi lowongan kerja

## Term DF IDF
demonstrated 0 2,386294361
ability 1 1,693147181
design 2 1,287682072
developmentally 0 2,386294361
appropriate 0 2,386294361
lesson 0 2,386294361
activity 1 1,693147181
allow 0 2,386294361
integration 0 2,386294361
learning 1 1,693147181
style 0 2,386294361
highly 0 2,386294361
educate 0 2,386294361
differentiated 0 2,386294361
classroom 0 2,386294361
determined 0 2,386294361
maximize 0 2,386294361
educational 1 1,693147181
achievement 0 2,386294361
student 1 1,693147181
trained 0 2,386294361
developmental 0 2,386294361
76
Tabel 4.33 Perhitungan manual IDF korpus kualifikasi lowongan kerja (lanjutan)

## Term DF IDF
reading 0 2,386294361
assessments 0 2,386294361
digital 0 2,386294361
production 0 2,386294361
manager 0 2,386294361
responsible 0 2,386294361
aspect 0 2,386294361
premium 0 2,386294361
printing 0 2,386294361
graphic 1 1,693147181
company 0 2,386294361
delivering 0 2,386294361
high 0 2,386294361
quality 0 2,386294361
meet 0 2,386294361
client 1 1,693147181
direct 0 2,386294361
deadline 0 2,386294361
acted 0 2,386294361
liaison 0 2,386294361
senior 0 2,386294361
business 0 2,386294361
various 0 2,386294361
global 0 2,386294361
stake 0 2,386294361
holder 0 2,386294361
recruited 0 2,386294361
analysts 0 2,386294361
process 0 2,386294361
suggest 0 2,386294361
best 0 2,386294361
77
Tabel 4.33 Perhitungan manual IDF korpus kualifikasi lowongan kerja (lanjutan)

## Term DF IDF
practice 0 2,386294361
effective 0 2,386294361
method 0 2,386294361
Setelah mendapatkan nilai term frequency (TF) dan inverse document frequency (IDF), TF-IDF untuk kualifikasi lowongan kerja dihitung menggunakan formula pada Persamaan 4.22. Mulai dari Persamaan 4.23 merupakan demonstrasi perhitungan TF-IDF untuk term “design”.

# 𝑇𝐹−𝐼𝐷𝐹=𝑇𝐹×𝐼𝐷𝐹       (4.22)
()𝑡,𝑑(𝑡,𝑑)(𝑡)

# 𝑇𝐹−𝐼𝐷𝐹=1×1,287682072=1,287682072   (4.23)
()𝑑𝑒𝑠𝑖𝑔𝑛,𝑑4

# 𝑇𝐹−𝐼𝐷𝐹=2×1,287682072=2,575364145   (4.24)
()𝑑𝑒𝑠𝑖𝑔𝑛,𝑑5

# 𝑇𝐹−𝐼𝐷𝐹=0×1,287682072=0     (4.25)
()𝑑𝑒𝑠𝑖𝑔𝑛,𝑑6
Hasil perhitungan manual TF-IDF korpus kualifikasi lowongan kerja tertera pada Tabel 4.34.
Tabel 4.34 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6
demonstrated 0 0 0
ability 1,693147181 0 0
design 1,287682072 2,575364145 0
developmentally 0 0 0
appropriate 0 0 0
lesson 0 0 0
activity 0 0 1,693147181
allow 0 0 0
integration 0 0 0
learning 0 0 1,693147181
style 0 0 0
highly 0 0 0
educate 0 0 0
differentiated 0 0 0
classroom 0 0 0
determined 0 0 0
78
Tabel 4.34 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja (lanjutan)
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6
maximize 0 0 0
educational 0 0 1,693147181
achievement 0 0 0
student 0 0 1,693147181
trained 0 0 0
developmental 0 0 0
reading 0 0 0
assessments 0 0 0
digital 0 0 0
production 0 0 0
manager 0 0 0
responsible 0 0 0
aspect 0 0 0
premium 0 0 0
printing 0 0 0
graphic 0 1,693147181 0
company 0 0 0
delivering 0 0 0
high 0 0 0
quality 0 0 0
meet 0 0 0
client 1,693147181 0 0
direct 0 0 0
deadline 0 0 0
acted 0 0 0
liaison 0 0 0
senior 0 0 0
business 0 0 0
various 0 0 0
global 0 0 0
79
Tabel 4.34 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja (lanjutan)
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6
stake 0 0 0
holder 0 0 0
recruited 0 0 0
analysts 0 0 0
process 0 0 0
suggest 0 0 0
best 0 0 0
practice 0 0 0
effective 0 0 0
method 0 0 0
Hasil TF-IDF korpus kualifikasi lowongan kerja juga dilakukan normalisasi menggunakan formula pada Persamaan 4.26. Mulai dari Persamaan 4.27 merupakan demonstrasi perhitungan normalisasi TF-IDF untuk term “design”
𝑣𝑣 𝑣==       (4.26)
𝑛𝑜𝑟𝑚
222‖‖𝑣√𝑣+𝑣+⋯+𝑣
212𝑛
1,287682072 𝑣=     (4.27)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑4)
222√(0)+(1,693147181)+⋯+(0)
1,287682072 𝑣==0,473629601     (4.28)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑4) 2,718753367
2,575364145 𝑣=       (4.29)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑5)
222√(0)+(0)+⋯+(0)
2,575364145 𝑣==0,8355915419    (4.30)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑5) 3,082084985
0 𝑣=       (4.31)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑6)
222√(0)+(0)+⋯+(0)
0 𝑣==0       (4.32)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑6) 3,386294361
Hasil perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah normalisasi tertera pada Tabel 4.35.
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah normalisasi
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6 demonstrated 0 0 0 ability 0,6227660078 0 0 design 0,473629601 0,8355915419 0
80
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah normalisasi (lanjutan)
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6
developmentally 0 0 0
appropriate 0 0 0
lesson 0 0 0
activity 0 0 0,5
allow 0 0 0
integration 0 0 0
learning 0 0 0,5
style 0 0 0
highly 0 0 0
educate 0 0 0
differentiated 0 0 0
classroom 0 0 0
determined 0 0 0
maximize 0 0 0
educational 0 0 0,5
achievement 0 0 0
student 0 0 0,5
trained 0 0 0
developmental 0 0 0
reading 0 0 0
assessments 0 0 0
digital 0 0 0
production 0 0 0
manager 0 0 0
responsible 0 0 0
aspect 0 0 0
premium 0 0 0
printing 0 0 0
graphic 0 0,549351231 0
company 0 0 0
81
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah normalisasi (lanjutan)
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6
delivering 0 0 0
high 0 0 0
quality 0 0 0
meet 0 0 0
client 0,6227660078 0 0
direct 0 0 0
deadline 0 0 0
acted 0 0 0
liaison 0 0 0
senior 0 0 0
business 0 0 0
various 0 0 0
global 0 0 0
stake 0 0 0
holder 0 0 0
recruited 0 0 0
analysts 0 0 0
process 0 0 0
suggest 0 0 0
best 0 0 0
practice 0 0 0
effective 0 0 0
method 0 0 0
82
4.7.5.2Perhitungan Manual Word2Vec
Tujuan dari Skip-gram adalah memprediksi konteks (output) disekitar kata target (input). Untuk demonstrasi perhitungan manual Word2Vec menggunakan salah satu kalimat dari resume, yakni “demonstrated ability design developmentally appropriate lesson activity allow integration learning style highly educate differentiated classroom determined maximize educational achievement student trained developmental reading assessments” dengan parameter dengan vocab = 24, window size = 3, dan learning rate = 0,1.
Gambar 4.23 Pasangan target-konteks Word2Vec Skip-gram
Gambar 4.23 merupakan rincian pasangan target-konteks, kotak berwarna biru merupakan kata target dan kotak berwarna merah merupakan konteks dari kata target yang sesuai dengan nilai window size.
Tabel 4.36 merupakan one-hot encoding untuk setiap token dalam vocabulary ["Demonstrated", "ability", "design", "developmentally”, “appropriate”, “lesson", "activity", "integration", "learning”, “style", "differentiated”, “classroom", “determined”, “maximize”, "educational”, “achievement", "student", “trained” "developmental”, “reading”, “assessments"].
Tabel 4.36 Perhitungan manual one-hot encoding
Term One-Hot Encoding
demonstrated [1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
ability [0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
[0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  0  design 0  0  0  0  0  0  0]
[0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  0  developmentally 0  0  0  0  0  0  0]
[0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0  0  appropriate 0  0  0  0  0  0  0]
lesson [0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
83
Tabel 4.36 Perhitungan manual one-hot encoding (lanjutan)
Term One-Hot Encoding
activity [0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
allow [0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
integration [0  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
learning [0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0  0 0  0  0  0  0  0  0]
style [0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0  0 0  0  0  0  0  0  0]
highly [0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0  0 0  0  0  0  0  0  0]
educate [0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0  0 0  0  0  0  0  0  0]
differentiated [0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0  0 0  0  0  0  0  0  0]
classroom [0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0  0 0  0  0  0  0  0  0]
determined [0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1  0 0  0  0  0  0  0  0]
maximize [0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  1 0  0  0  0  0  0  0]
educational [0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 1  0  0  0  0  0  0]
[0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  achievement 0  1  0  0  0  0  0]
[0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  student 0  0  1  0  0  0  0]
[0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  trained 0  0  0  1  0  0  0]
developmental [0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  1  0  0]
reading [0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  1  0]
assessments [0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  1]
84
Pada perhitungan manual ini, dilakukan penargetan pada kata “design” dan menggunakan hidden layer = 3. Selanjutnya adalah melakukan inisialisasi acak bobot input layer ke tiga hidden layer yang tertera pada Tabel 4.37.
Tabel 4.37 Bobot input layer-hidden layer

## Term H1 H2 H3
demonstrated -0,3 -0,8 -0,3
ability 0,2 -0,5 -0,6
design 0,8 -0,6 -0,2
developmentally -0,8 0 0,9
appropriate -0,3 0,2 -0,8
lesson -0,8 -0,3 0,2
activity -0,6 0,2 -0,3
allow 0,2 -0,3 -0,8
integration -0,3 0,2 -0,6
learning -0,8 -0,3 0,2
style -0,6 0,2 -0,3
highly 0,2 -0,3 -0,8
educate -0,3 0,2 -0,6
differentiated -0,8 -0,3 0,2
classroom -0,6 0,2 -0,3
determined 0,2 -0,3 -0,8
maximize -0,3 -0,5 0,2
educational 0,2 -0,3 -0,5
achievement -0,8 0,2 -0,3
student -0,5 -0,3 0,2
trained -0,3 0,2 -0,8
developmental 0,2 -0,3 -0,5
reading -0,8 0,2 -0,3
assessments -0,5 -0,3 0,2
85
Setelah menginisialisasi acak bobot input ke hidden layer, dapat menginisialisasi acak bobot juga untuk hidden layer ke output layer yang tertera pada Tabel 4.38 sampai dengan Tabel 4.41.
Tabel 4.38 Bobot hidden layer-output layer
Neuron demonstrability design developmapproprialesson ated entally te

# H1 0,3 -0,2 -0,2 0 -0,2 -0,1
# H2 -0,4 -0,3 -0,6 0,3 -0,1 -0,2
# H3 -0,1 -0,8 0,5 0,2 -0,4 0,3
Tabel 4.39 Bobot hidden layer-output layer
Neuron activity allow integratiolearning style highly n

# H1 -0,1 0,3 -0,2 -0,1 -0,1 0,3
# H2 0,3 -0,2 0,3 -0,2 0,3 -0,2
# H3 -0,2 -0,1 -0,1 0,3 -0,2 -0,1
Tabel 4.40 Bobot hidden layer-output layer
Neuron educate differenticlassroodeterminmaximize education ated m ed al

# H1 -0,2 -0,1 -0,1 0,3 -0,2 -0,1
# H2 0,3 -0,2 0,3 -0,2 0,3 -0,2
# H3 -0,1 0,3 -0,2 -0,1 -0,1 0,3
Tabel 4.41 Bobot hidden layer-output layer
achievemdevelopmassessmeNeuron student trained reading ent ental nts

# H1 -0,10,3-0,2-0,4-0,10,3
# H2 0,3-0,20,3-0,10,30
# H3 -0,2-0,1-0,10,30-0,6
86
Telah didapatkan bobot untuk hidden layer ke output layer pada Tabel 4.38 sampai dengan Tabel 4.41. Perhitungan dilanjutkan ke feedforward dengan mengalikan one-hot vector dari kata target “design” dengan matriks bobot input- hidden seperti pada Persamaan 4.33 sampai dengan Persamaan 4.39.
−0,3 0,2 0,8

# []𝐻1=×       (4.33) 001…00
⋮ −0,8 []−0,5

# ()()()()()𝐻1=0 −0,3+0 0,2+10,8+⋯+0−0,8+0−0,5= 0,8  (4.34)
−0,8 −0,5 −0,6

# []𝐻2=×       (4.35) 001…00
⋮ 0,2 []−0,3

# ()()()()()𝐻2=0 −0,8+0 −0,5+1−0,6+⋯+00,2+0−0,3=−0,6  (4.36)
−0,3 −0,6 −0,2

# []𝐻3=×       (4.37) 001…00
⋮ −0,3 []0,2

# ()()()()()𝐻3=0 −0,3+0 −0,6+1−0,2+⋯+0−0,3+00,2=−0,2  (4.38)
[]0,8−0,6−0,2ℎ=       (4.39)
𝑑𝑒𝑠𝑖𝑔𝑛
ℎKalikan  dengan bobot hidden-output untuk menghitung skor prediksi
𝑑𝑒𝑠𝑖𝑔𝑛 kata target dengan konteksnya tertera pada Persamaan 4.40 sampai dengan Persamaan 4.41.
0,3−0,2−0,2⋯0,3 []0,8−0,6−0,2−0,4−0,30,3⋯0𝑢= × []   (4.40)
1,1 −0,1−0,80,2⋯−0,6
()()()𝑢=0,8 0,3+(−0,6) −0,4+(−0,2)−0,1=0,5    (4.41)
1,1
1×24Matriks hasil berbentuk  yang tertera pada Persamaan 4.42.
[]𝑧=0,50,180,1−0,22…−0,32−0,260,36  (4.42)
𝑑𝑒𝑠𝑖𝑔𝑛
87
Setelah didapatkan skor prediksi, lakukan normalisasi dengan Softmax dengan rumus seperti Persamaan 4.43.
𝑒𝑥𝑝(𝑘) 𝑦̂=𝑃(𝑘𝑎𝑡𝑎|𝑘𝑎𝑡𝑎)=      (4.43)
𝑘𝑟𝑘𝑘𝑜𝑛𝑡𝑒𝑘𝑠
∑𝑒𝑥𝑝(𝑛)
𝑛
Jumlahkan semua nilai eksponensial untuk denominator seperti Persamaan 4.44 sampai dengan 4.45.
()()()𝑒𝑥𝑝0,5+𝑒𝑥𝑝0,18+⋯+𝑒𝑥𝑝−0,26+𝑒𝑥𝑝(0,36)=24.5489614  (4.44)
1,648721271 𝑢==0,06716053035      (4.45)
1,1 24,54896145
1×24Matriks Softmax untuk kata target “design” berbentuk  tertera pada Persamaan 4.46.
[]𝑦̂=0,06716050,04876856…0,03140870,0583866  (4.46)
𝑑𝑒𝑠𝑖𝑔𝑛
Selanjutnya dilakukan backpropagation untuk memperbaharui nilai bobot matriks dengan rumus seperti Persamaan 4.47.
𝑑𝐿𝑜𝑠𝑠 =𝑑𝑧=𝑦̂−𝑦(1×𝑉)        (4.47) 𝑑𝑧
𝑦Diketahui nilai  untuk konteks “ability” pada Persamaan 4.48 dan “development” pada Persamaan 4.49.
[]𝑦=      (4.48) 0100…000
𝑎𝑏𝑖𝑙𝑖𝑡𝑦
[]𝑦=     (4.49) 0001…000
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡
Maka, perhitungan error konteks “ability” pada kata target “design” tertera pada Persamaan 4.50 sampai dengan Persamaan 4.51.
[][]𝑒=0,06720,0488…0,03140,0584− (4.50) 01…0
𝑎𝑏𝑖𝑙𝑖𝑙𝑡𝑦
[]𝑒=0,0672−0,9512…0,03140,0584    (4.51)
𝑎𝑏𝑖𝑙𝑖𝑙𝑡𝑦
Perhitungan error konteks “development” pada kata target “design” tertera pada Persamaan 4.52 sampai dengan Persamaan 4.53.
[][]𝑒=0,06720,0488…0,03140,0584−  (4.52) 0…0
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡
[]𝑒=0,06720,0488…0,03140,0584    (4.53)
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡
88
Perhitungan error rata-rata dari kedua konteks tertera pada Persamaan 4.54 sampai dengan Persamaan 4.56.
𝑒+𝑒
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡𝑎𝑏𝑖𝑙𝑖𝑡𝑦 𝑒=       (4.54)
𝑐𝑜𝑛𝑡𝑒𝑥𝑡 2 0,06716053035+0,06716053035 𝑒==0,06716053035   (4.55)
𝑐𝑜𝑛𝑡𝑒𝑥𝑡
1,12 −0,9512314456+0,04876855444 𝑒==−0,4512314456   (4.56)
𝑐𝑜𝑛𝑡𝑒𝑥𝑡
1,22
Matriks error konteks tertera pada Persamaan 4.57.
[]𝑑𝑧=0,06716053−0,4512314…0,031408730,05838656  (4.57)
Setelah mendapatkan hasil perhitungan error, dilanjutkan dengan perhitungan gradien dari output layer ke hidden layer dengan rumus seperti pada Persamaan 4.58.
𝑑𝐿𝑜𝑠𝑠
𝑇=𝑑𝑈=ℎ.𝑑𝑧(𝑁×𝑉)       (4.58) 𝑑𝑈
ℎDiketahui matriks  dan dilakukan transpose pada Persamaan 4.59
𝑑𝑒𝑠𝑖𝑔𝑛 sampai dengan 4.60.
[]0,8−0,6−0,2ℎ=       (4.59)
𝑑𝑒𝑠𝑖𝑔𝑛
0,8 𝑇−0,6ℎ=[]         (4.60)
𝑑𝑒𝑠𝑖𝑔𝑛 −0,2
𝑑𝑈Maka, perhitungan  tertera pada Persamaan 4.61.
0,8 []−0,6𝑑𝑈=[]×0,0672−0,4512…0,03140,0584   (4.61) −0,2
𝑑𝑈=0,8×0,067160530= 0,05372842428     (4.62)
1,1
𝑑𝑈=0,6×0,067160530= −0,04029631821    (4.63)
2,1
𝑑𝑈=0,8×−0,45123144= −0,3609851564     (4.64)
1,2
𝑑𝑈=0,6×−0,45123144= 0,2707388673     (4.65)
2,2
𝑑𝑈3×24Matriks  berbentuk  tertera pada Persamaan 4.66.
0,05372842428−0,3609851564…0,04670924812 𝑑𝑈=[−0,040296318210,2707388673…−0,03503193609]  (4.66) −0,013432106070,09024628911…−0,01167731203
89
Setelah mendapatkan hasil perhitungan gradien dari output layer ke hidden layer, dilanjutkan menghitung gradien dari hidden layer ke input layer dengan rumus seperti pada Persamaan 4.67.ex
𝑑𝐿𝑜𝑠𝑠𝑑𝐿𝑜𝑠𝑠𝑑𝑧
𝑇=.=𝑑𝑧.𝑈(1×𝑁)       (4.67) 𝑑ℎ𝑑𝑧𝑑ℎ
Diketahui matriks hidden layer 1, 2, dan 3 dilakukan transpose pada Persamaan 4.68 sampai dengan 4.73.
[]0,3−0,2−0,2…0,3ℎ=       (4.68)
1
0,2 −0,2 𝑇−0,2ℎ=          (4.69)
1 ⋮ []0,3
[]−0,4−0,3−0,6…0ℎ=       (4.70)
2
−0,4 −0,3 𝑇ℎ=          (4.71) −0,6
2 ⋮ []
0
[]ℎ=−0,1−0,8−0,5…−0,6      (4.72)
3
−0,1 −0,8 𝑇−0,5ℎ=          (4.73)
3 ⋮ []−0,6
𝑑𝐿𝑜𝑠𝑠 Maka, perhitungan  tertera pada Persamaan 4.74 sampai dengan 𝑑ℎ Persamaan 4.76.
0,2 −0,2 𝑑𝐿𝑜𝑠𝑠 []−0,2=0,0672−0,4512…0,03140,0584×   (4.74) 𝑑ℎ
1 ⋮ []0,3
𝑑𝐿𝑜𝑠𝑠 ()()()=0,0672×0,2+(−0,4512 ×−0,2)+ … +0,0584 ×0,3  (4.75) 𝑑ℎ
1
𝑑𝐿𝑜𝑠𝑠 =0,1147162368        (4.76) 𝑑ℎ
1
90
𝑑𝐿𝑜𝑠𝑠𝑑𝐿𝑜𝑠𝑠 Hitung dengan persamaan yang sama untuk  dan . Maka hasil 𝑑ℎ𝑑ℎ

# 23 perhitungan gradien dari hidden layer ke input layer tertera pada Persamaan 4.77 sampai dengan 4.79.
𝑑𝐿𝑜𝑠𝑠 =0,1147162368        (4.77) 𝑑ℎ
1
𝑑𝐿𝑜𝑠𝑠 =−0,06109851674        (4.78) 𝑑ℎ
2
𝑑𝐿𝑜𝑠𝑠 =0,2272906395        (4.79) 𝑑ℎ
3
Pembaharuan bobot dihitung menggunakan learning rate dan gradien dari hidden layer ke input layer dilakukan seperti pada Persamaan 4.80 sampai dengan Persamaan 4.82.

# ()𝑊=0,8−0,1×0,1147162368=0,7885283763    (4.80)
1,1

# ()()𝑊=−0,6−0,1×−0,06109851674=−0,5938901483   (4.81)
1,2

# ()𝑊=(−0,2)−0,1×0,2272906395=−0,222729064   (4.82)
1,3
Hasil pembaharuan bobot pada kata “design” tertera pada Tabel 4.42.
Tabel 4.42 Pembaharuan bobot input layer-hidden layer

## Term H1 H2 H3
demonstrated -0,3 -0,8 -0,3
ability 0,2 -0,5 -0,6
design 0,7885283763 -0,5938901483 -0,222729064
developmentally -0,8 0 0,9
appropriate -0,3 0,2 -0,8
lesson -0,8 -0,3 0,2
activity -0,6 0,2 -0,3
allow 0,2 -0,3 -0,8
integration -0,3 0,2 -0,6
learning -0,8 -0,3 0,2
style -0,6 0,2 -0,3
highly 0,2 -0,3 -0,8
educate -0,3 0,2 -0,6
differentiated -0,8 -0,3 0,2
classroom -0,6 0,2 -0,3
91
Tabel 4.42 Pembaharuan bobot input layer-hidden layer (lanjutan)

## Term H1 H2 H3
determined 0,2 -0,3 -0,8
maximize -0,3 -0,5 0,2
educational 0,2 -0,3 -0,5
achievement -0,8 0,2 -0,3
student -0,5 -0,3 0,2
trained -0,3 0,2 -0,8
developmental 0,2 -0,3 -0,5
reading -0,8 0,2 -0,3
assessments -0,5 -0,3 0,2
Pembaharuan bobot dihitung menggunakan learning rate dan gradien dari hidden layer ke input layer dilakukan seperti pada Persamaan Persamaan 4.83 sampai dengan Persamaan 4.90.
𝑊=𝑊−(0,1×𝑑𝑈)        (4.83)
𝑡+1𝑡

# 0,3…0,30,0537…0,0467 −0,4…0()𝑊=[]−0,1×[−0,0403…−0,0350]  (4.84)
𝑡+1 −0,1…−0,6−0,0134…−0,0117

# ()𝑊=0,3−0,1×0,05372842428=0,2946271576   (4.85)
𝑡+1
1,1

# ()𝑊=0,3−0,1×0,04670924812=0,2953290752   (4.86)
𝑡+1
1,24

# ()𝑊=−0,4−0,1(−0,04029631821)=−0,3959703682   (4.87)
𝑡+1
2,1

# ()𝑊=0−0,1(−0,03503193609)=0,003503193609   (4.88)
𝑡+1
2,24

# ()𝑊=−0,1−0,1(−0,01343210607=−0,09865678939   (4.89)
𝑡+1
3,1

# ()𝑊=−0,6−0,1(−0,01167731203)=−0,5988322688  (4.90)
𝑡+1
3,24
Hasil pembaharuan bobot hidden layer ke output layer tertera pada Tabel 4.43 hingga Tabel 4.46.
Tabel 4.43 Pembaharuan bobot input layer-output layer
demonstrdevelopmappropriaNeuron ability design lesson ated entally te

# H1 0,294627 -0,16390 -0,20360 0,037385 -0,20319 -0,10319
# H2 -0,39597 -0,32707 -0,5973 0,271961 -0,09760 -0,19760
# H3 -0,09866 -0,80902 0,500900 0,190654 -0,39920 0,300799
92
Tabel 4.44 Pembaharuan bobot input layer-output layer
Neuron activity allow integratiolearning style highly n

# H1 -0,10262 0,295235 -0,20237 -0,10319 -0,10262 0,295235
# H2 0,301961 -0,19643 0,301775 -0,19760 0,301961 -0,19643
# H3 -0,19935 -0,09881 -0,09941 0,3008 -0,19935 -0,09881
Tabel 4.45 Pembaharuan bobot input layer-output layer
differenticlassroodetermineducationNeuron educate maximize ated m ed al

# H1 -0,20237 -0,10319 -0,10262 0,295235 -0,20237 -0,10319
# H2 0,301775 -0,19760 0,301961 -0,19643 0,301775 -0,19760
# H3 -0,09941 0,300799 -0,19935 -0,09881 -0,09941 0,300799
Tabel 4.46 Pembaharuan bobot input layer-output layer
Neuron achievemstudent trained developmreading assessme ent ental nts

# H1 -0,10262 0,295235 -0,20237 -0,40237 -0,10251 0,295329
# H2 0,301961 -0,19643 0,301775 -0,09823 0,301885 0,003503
# H3 -0,19935 -0,09881 -0,09941 0,300592 0,000628 -0,59883
93
4.7.6Perhitungan Manual Similaritas
Perhitungan manual similaritas dilakukan menggunakan vektor TF-IDF dan Word2Vec dari resume dengan ID 15265464 dan section Experience. Sedangkan untuk kualifikasi lowongan kerja menggunakan posisi Teacher dari PT Abadi Cahaya Edukasi. Isian data sampel yang dimaksud tertera pada Tabel 4.47.
Tabel 4.47 Data sampel perhitungan manual similaritas

## Resume Kualifikasi Lowongan Kerja
intervention specialist teacher math play vital role support lead teacher create language arts identified student nurturing stimulate learning environment substantial academic difficulty evaluation young student assist lead teacher use developmental reading assessments planning implement engage educational consultation staff member referred activity child age 36 year help maintain student developed differentiate lesson safe organised classroom environment plan select appropriate instructional provide individual attention support material reach individualized student goal student needed collaborate teach team developed implement creative lesson monitor record childrens progress clear objective link common core participate staff meeting professional incorporate differentiated instruction development opportunity maintain open attended gain knowledge numerous communication parent caregiver ensure service improved overall lexiles test score compliance relevant childcare regulation facilitated group lesson dependent policy diploma degree early childhood student reading level determine run education related field least 1 year record assessment evaluated student experience work childcare educational growth progress monitoring formal setting strong interpersonal informal assessment instructed student communication skill patience creativity accordance schedule previously devise genuine passion work young child ability enhanced lesson use smart board work collaboratively part team technology computer assessed regular knowledge child development basis objective student set led basic skill ageappropriate teaching method class student time conducted small group proficiency bahasa indonesia english individual classroom activity student base differentiated learning need nd grade replacement teacher implement positive behavior management use color system developed clear objective student parent lesson activity designed differentiated common core lesson plan activity meet need learner enhanced lesson use smartboard technology pads computer lab assessed student growth informal formal assessment developed lesson accordance student reading level determine quarterly running record testing maintained positive collaboration communication parent weekly newsletter weekly student progress update email conference attended service staff...
94
4.7.6.1Perhitungan Manual TF-IDF Dengan Improved Sqrt-Cosine Similarity
Untuk metode representasi teks menggunakan TF-IDF, langkah pertama 𝑥𝑦adalah mengambil nilai vektor  (resume) dan vektor  (kualifikasi lowongan kerja) dari hasil TF-IDF. Vektor resume dan kualifikasi lowongan kerja tertera pada Tabel 4.48.
Tabel 4.48 Vektor TF-IDF perhitungan manual Improved Sqrt-Cosine Similarity

## Resume Kualifikasi Lowongan Kerja
[0 ... 0 ... 0,03772064 ... 0 ... 0 ... [0 ... 0 ... 0,06593613 ... 0 ... 0 ... 0,07763420 ... 0 ... 0 ... 0,11012862 ...  0] 0,06276407 ... 0 ... 0 ... 0,09679995 ... 0]
Hitung penjumlahan dari akar perkalian elemen-elemen yang sesuai antara 𝑥𝑦vektor  dan  sebagai numerator menggunakan formula seperti pada Persamaan 4.91.
𝑚∑𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=𝑥𝑦        (4.91) √
𝑖𝑖𝑖=1
Demonstrasi perhitungan tertera mulai dari Persamaan 4.92 sampai dengan Persamaan 4.94.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=𝑥𝑦+𝑥𝑦+⋯+𝑥𝑦+⋯+𝑥𝑦  (4.92) √√√√
11225265264333143331
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=0×0+0×0+⋯+0,110×0,063+⋯+0×0  (4.93)  √√√√
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=1,4044        (4.94)
𝑥Hitung hasil kali dari akar penjumlahan semua elemen masing-masing vektor 𝑦(resume) dan vektor  (kualifikasi) sebagai denominator dengan formula seperti pada Persamaan 4.95.
𝑚𝑚(∑)(∑)𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=𝑥𝑦      (4.95) √√
𝑖𝑖𝑖=1𝑖=1
Demonstrasi perhitungan tertera mulai dari Persamaan 4.96 sampai dengan Persamaan 4.98.
()𝒅𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=√𝑥+𝑥+⋯+𝑥+⋯+𝑥×
1252643331 ()√𝑦+𝑦+⋯+𝑦+⋯+𝑦       (4.96)
1252643331
()√𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=0+0+⋯+0,1101+⋯+0×
()√0+0+⋯+0,0628+⋯+0        (4.97)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=8,4315         (4.98)
95
Skor similaritas Improved Sqrt-Cosine didapatkan dengan membagi numerator dengan denominator seperti formula pada Persamaan 4.99.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 𝐼𝑆𝐶=         (4.99) 𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟
Hasil pembagian antara numerator dengan denominator yang sudah didapatkan tertera pada Persamaan 4.100.

# 1,4044 𝐼𝑆𝐶==0,1666        (4.100) 8,4315
Hasil similaritas antara keseluruhan section resume ID 15265464 dengan kualifikasi lowongan kerja posisi Teachers tertera pada Tabel 4.49.
Tabel 4.49 Hasil skor similaritas resume ID 15265464 perhitungan manual Improved Sqrt-Cosine Similarity

## Section Skor Similaritas
Education 0,1365
Experience 0,1666
Summary 0,1460
Pengujian pada penelitian ini menggunakan dua skenario, yakni “Tanpa Bobot” dan “Dengan Bobot”. Pada skenario “Tanpa Bobot”, skor similaritas untuk masing- masing section di resume ID 15265464 langsung dijumlah dan dirata-ratakan seperti pada Persamaan 4.101.
0,1365+0,1666+0,1460 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦==0,1497     (4.101) 3
Pada skenario “Dengan Bobot”, skor similaritas untuk masing-masing section di resume ID 15265464 dikalikan dengan persentase bobot yang diberikan oleh ahli, lalu ditotal dan dibagi dengan jumlah persentase section yang digunakan pada resume. Pada kategori industri “TEACHER”, diketahui rincian bobot untuk setiap section tertera pada Tabel 4.50.
Tabel 4.50 Bobot section kategori industri "TEACHER"
Industry Section Bobot (%)

## TEACHER Summary 5
TEACHER Accomplishments/Awards 15
TEACHER Skills/Qualifications 20

## TEACHER Education 20
## TEACHER Experience 20
96
Tabel 4.50 Bobot section kategori industri "TEACHER" (lanjutan)
Industry Section Bobot (%)

## TEACHER Organization 5
## TEACHER Projects 5
## TEACHER Certifications 10
## TEACHER Portfolio 10
Maka total skor similaritas untuk resume ID 15265464 dapat dihitung seperti pada Persamaan 4.102 sampai dengan Persamaan 4.103.
()()()0,1365×0,2+0,1666×0,2+0,1460×0,05 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦=    (4.102) (0,2+0,2+0,05)
0,0273+0,03332+0,0073 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦==0,1509     (4.103) 0,45
4.7.6.2Perhitungan Manual Word2Vec Dengan Cosine Similarity
Untuk metode representasi teks menggunakan Word2Vec, langkah pertama 𝑥adalah mengambil nilai rata-rata dokumen untuk keseluruhan vektor  (resume) 𝑦dan keseluruhan vektor  (kualifikasi lowongan kerja) dari hasil Word2Vec. Vektor resume dan kualifikasi lowongan kerja tertera pada Tabel 4.51.
Tabel 4.51 Vektor Word2Vec perhitungan manual Cosine Similarity

## Resume Kualifikasi
[0,071130395  0,12649915   [-0,04582439  0,0966028
-0,1145207  -0,08985851 ...  0,19086754] -0,18032219 -0,11506447 ... 0,11572151]
Hitung penjumlahan dari perkalian elemen-elemen yang bersesuaian antara 𝑥𝑦vektor  dan  sebagai numerator menggunakan formula seperti pada Persamaan 4.104.
𝑚∑𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=𝑥𝑦        (4.104)
𝑖𝑖𝑖=1
Demonstrasi perhitungan tertera mulai dari Persamaan 4.105 sampai dengan Persamaan 4.107.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=𝑥𝑦+𝑥𝑦+⋯+𝑥𝑦     (4.105)
1122100100
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=(0,0711×(−0,0458))+(0,1265×0,0966)+⋯+(0,1909× 0,1157)          (4.106)
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=(−0,00323)+0,01221+⋯+0,02208=1,9022  (4.107)
97
𝑥Hitung hasil kali dari akar semua elemen masing-masing vektor  (resume) dan 𝑦vektor  (kualifikasi) yang dikuadratkan sebagai denominator dengan formula seperti pada Persamaan 4.108.
𝑚𝑚22(∑)(∑)𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=𝑥𝑦      (4.108) √√
𝑖𝑖𝑖=1𝑖=1
Demonstrasi perhitungan tertera mulai dari Persamaan 4.109 sampai dengan Persamaan 4.111.
222222()()𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=√𝑥+𝑥+⋯+𝑥×√𝑦+𝑦+⋯+𝑦
1210012100
(4.109)
222()√𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=0,0711+0,1265+⋯+0,1909× 222()(−0,0458)+0,0966+⋯+0,1157√      (4.110)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=2,1667         (4.111)
Skor Cosine Similarity didapatkan dengan membagi numerator dengan denominator seperti formula pada Persamaan 4.112.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 𝐶𝑜𝑠𝑆𝑖𝑚=        (4.112) 𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟
Hasil pembagian antara numerator dengan denominator yang sudah didapatkan tertera pada Persamaan 4.113.
1,9022 𝐶𝑜𝑠𝑆𝑖𝑚==0,8779        (4.113) 2,1667
Hasil similaritas antara keseluruhan section resume ID 15265464 dengan kualifikasi lowongan kerja posisi Teachers tertera pada Tabel 4.52.
Tabel 4.52 Hasil skor similaritas resume ID 15265464 perhitungan manual Cosine Similarity

## Section Skor Similaritas
Education 0,7303
Experience 0,8779
Summary 0,9277
98
Pengujian pada penelitian ini menggunakan dua skenario, yakni “Tanpa Bobot” dan “Dengan Bobot”. Pada skenario “Tanpa Bobot”, skor similaritas untuk resume ID 15265464 bisa langsung dijumlah dan dirata-ratakan seperti pada Persamaan 4.114.
0,7303+0,8779+0,9277 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦==0,8453     (4.114) 3
Pada skenario “Dengan Bobot”, skor similaritas untuk masing-masing section di resume ID 15265464 dikalikan dengan persentase bobot yang diberikan oleh ahli. Pada kategori industri “TEACHER”, diketahui rincian bobot untuk setiap section tertera pada Tabel 4.50 sebelumnya.
Maka total skor similaritas untuk resume ID 15265464 dapat dihitung seperti pada Persamaan 4.115 sampai dengan Persamaan 4.116.
()()()0,7303×0,2+0,8779×0,2+0,9277×0,05 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦=    (4.115) (0,2+0,2+0,05)
0,14606+0,17558+0,046385 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦==0,8178     (4.116) 0,45
4.7.6.3Perhitungan Manual Word2Vec Dengan Improved Sqrt- Cosine Similarity
Pada perhitungan manual sebelumnya sudah dirincikan nilai rata-rata 𝑥𝑦dokumen untuk keseluruhan vektor  (resume) dan keseluruhan vektor (kualifikasi lowongan kerja) dari hasil Word2Vec yang tertera pada Tabel 4.51. Namun, untuk menghitung similaritasnya dengan Improved Sqrt-Cosine, perlu mengonversi nilai vektor-vektornya menjadi absolut karena akan menjadi bilangan imajiner jika nilai negatif diakarkan. Vektor resume dan kualifikasi lowongan kerja tertera pada Tabel 4.53.
Tabel 4.53 Vektor Word2Vec perhitungan manual Improved Sqrt-Cosine Similarity

## Resume Kualifikasi
[0,071130395  0,12649915  0,1145207  [0,04582439  0,0966028  0,18032219 0,08985851  ... 0,19086754] 0,11506447 ... 0,11572151]
Hitung penjumlahan dari akar perkalian elemen-elemen yang sesuai antara 𝑥𝑦vektor  dan  sebagai numerator menggunakan formula seperti pada Persamaan 4.117.
𝑚∑𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=𝑥𝑦        (4.117) √
𝑖𝑖𝑖=1
99
Demonstrasi perhitungan tertera mulai dari Persamaan 4.118 sampai dengan Persamaan 4.120.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=𝑥𝑦+𝑥𝑦+⋯+𝑥𝑦     (4.118) √√√
1122100100
√√𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=0,0711×−0,0458+0,1265×0,0966+⋯+
√0,1909×0,1157         (4.119)
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟=11,2936        (4.120)
𝑥Hitung hasil kali dari akar penjumlahan semua elemen masing-masing vektor 𝑦(resume) dan vektor  (kualifikasi) sebagai denominator dengan formula seperti pada Persamaan 4.121.
𝑚𝑚(∑)(∑)𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=𝑥𝑦      (4.121) √√
𝑖𝑖𝑖=1𝑖=1
Demonstrasi perhitungan tertera mulai dari Persamaan 4.122 sampai dengan Persamaan 4.124.
()()𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=√𝑥+𝑥+⋯+𝑥×√𝑦+𝑦+⋯+𝑦  (4.122)
1210012100
()√𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=0,0711+0,1265+⋯+0,1909× ()√0,0458+0,0966+⋯+0,1157       (4.123)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟=11,861         (4.124)
Skor similaritas Improved Sqrt-Cosine didapatkan dengan membagi numerator dengan denominator seperti formula pada Persamaan 4.125.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 𝐼𝑆𝐶=         (4.125) 𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟
Hasil pembagian antara numerator dengan denominator yang sudah didapatkan tertera pada Persamaan 4.126.

# 11,2936 𝐼𝑆𝐶==0,9521        (4.126) 11,861
Hasil similaritas antara keseluruhan section resume ID 15265464 dengan kualifikasi lowongan kerja posisi Teachers tertera pada Tabel 4.54.
Tabel 4.54 Hasil skor similaritas resume ID 15265464 perhitungan manual Improved Sqrt-Cosine Similarity

## Section Skor Similaritas
Education 0,9065
100
Tabel 4.54 Hasil skor similaritas resume ID 15265464 perhitungan manual Improved Sqrt-Cosine Similarity

## Section Skor Similaritas
Experience 0,9521
Summary 0,9657
Pengujian pada penelitian ini menggunakan dua skenario, yakni “Tanpa Bobot” dan “Dengan Bobot”. Pada skenario “Tanpa Bobot”, skor similaritas untuk resume ID 15265464 bisa langsung dijumlah dan dirata-ratakan seperti pada Persamaan 4.127.
0,9065+0,9521+0,9657 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦==0,9414     (4.127) 3
Pada skenario “Dengan Bobot”, skor similaritas untuk masing-masing section di resume ID 15265464 dikalikan dengan persentase bobot yang diberikan oleh ahli. Pada kategori industri “TEACHER”, diketahui rincian bobot untuk setiap section tertera pada Tabel 4.50 sebelumnya.
Maka total skor similaritas untuk resume ID 15265464 dapat dihitung seperti pada Persamaan 4.128 sampai dengan Persamaan 4.129.
()()()0,9065×0,2+0,9521×0,2+0,9657×0,05 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦=    (4.128) (0,2+0,2+0,05)
0,1813+0,19042+0,048285 𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦==0,93334     (4.129) 0,45
4.7.7Skenario Pengujian
Pengujian akan dilakukan dengan human-level performance, dihitung parameter setiap parameter penilaiannya, mulai dari korelasi peringkat dengan Spearman Rank Correlation Coefficient (SRCC), persentase relevansi, dan persentase senioritas.
Setelah implementasi metode menghasilkan skor similaritas resume terhadap setiap kualifikasi lowongan kerja, diberikan pemeringkatan berdasarkan skor similaritas tertinggi, lalu diambil lima resume teratas. Kemudian, lima resume tersebut diberikan kepada seorang ahli di bidang rekrutmen untuk dinilai relevansinya secara manual. Ahli akan memberikan peringkat secara ulang sebagai ground truth dari peringkat satu sampai lima yang telah dihasilkan implementasi metode terhadap kualifikasi lowongan kerja tersebut. Selain itu, ahli akan mengevaluasi lima resume tersebut untuk memastikan relevansi dengan kualifikasi lowongan kerja yang tertera pada deskripsi lowongan kerja serta kesesuaian tingkat senioritas atau level posisi dengan deskripsi kualifikasi lowongan kerja.
101
Korelasi antara peringkat yang dihasilkan oleh implementasi metode dan peringkat dari ahli menunjukkan sejauh mana implementasi metode dapat meniru penilaian manusia. Semakin tinggi nilai korelasi (mendekati 1), semakin baik kinerja implementasi metode dalam menyelaraskan hasilnya dengan penilaian ahli. Untuk setiap implementasi metode, dilakukan perhitungan SRCC yang sama, maka untuk demonstrasi perhitungan SRCC akan menggunakan hasil pemeringkatan dari implementasi TF-IDF dengan Improved Sqrt-Cosine Similarity (ISC) pada kualifikasi lowongan kerja posisi “Teachers” skenario “Tanpa Bobot” yang tertera pada Tabel 4.55.
Tabel 4.55 Peringkat 1-5 resume dengan skor similaritas terbesar untuk perhitungan manual SRCC

## Resume_ID Peringkat Peringkat Ahli
15850434 1 3
96547039 2 1
28772892 3 4
22056333 4 2
37220856 5 5
Setelah diketahui peringkat lima resume dengan skor similaritas terbesar hasil implementasi metode dan peringkat dari ahli, selanjutnya adalah menghitung selisih peringkat dan dikuadratkan yang didemonstrasikan pada Tabel 4.56.
Tabel 4.56 Selisih peringkat 1-5 resume perhitungan manual SRCC
𝟐𝒅Resume_ID Peringkat Peringkat Ahli Selisih ()
𝒊
𝒅
𝒊
1−3=−215850434 1 3  4
2−1=196547039 2 1  1
3−4=−128772892 3 4  1
4−2=222056333 4 2  4
5−5=037220856 5 5  0
Pada Tabel 4.56, diketahui hasil kuadrat dari selisih perangkat. Jumlahkah hasil kuadrat tersebut untuk perhitungan SRCC sebagai numerator seperti pada Persamaan 4.130.
2
∑𝑑=4+1+1+4+0=10       (4.130)
𝑖
102
Gunakan rumus SRCC seperti Persamaan 4.131 untuk menghitung korelasi antara peringkat hasil implementasi dengan peringkat ahli.
∑6𝑑
𝑖𝑆𝑅𝐶𝐶 = 1−         (4.131) 2𝑛(𝑛−1)
Demonstrasi perhitungan untuk peringkat lima resume dijabarkan mulai dari Persamaan 4.132 sampai dengan Persamaan 4.135.

# 6×10 𝑆𝑅𝐶𝐶 = 1−         (4.132) 25(5−1)
# 60 𝑆𝑅𝐶𝐶 = 1−         (4.133) 5(24)
12060 𝑆𝑅𝐶𝐶 = −         (4.134) 120120 60 𝑆𝑅𝐶𝐶 = =0,5         (4.135) 120
Hasil evaluasi relevansi dari ahli dihitung dalam bentuk persentase. Semakin besar persentase maka semakin baik suatu metode menghasilkan lima resume yang relevan dengan deskripsi lowongan kerja. Sama halnya dengan hasil evaluasi senioritas dari ahli, semakin besar persentase maka semakin baik suatu metode mengenali lima resume dengan level posisi yang sesuai. Untuk setiap implementasi metode, dilakukan perhitungan relevansi dan senirotas yang sama, maka untuk demonstrasi perhitungan relevansi dan senioritas akan menggunakan hasil pemeringkatan dari implementasi TF-IDF dengan Improved Sqrt-Cosine Similarity (ISC) pada kualifikasi lowongan kerja posisi “Teachers” skenario “Tanpa Bobot” yang tertera pada Tabel 4.57
Tabel 4.57 Peringkat 1-5 resume dengan hasil evaluasi relevansi dan senioritas ahli terbesar untuk perhitungan manual

## Resume_ID Relevance Seniority
# 15850434 TRUE TRUE
# 96547039 TRUE TRUE
# 28772892 TRUE TRUE
# 22056333 TRUE TRUE
# 37220856 FALSE TRUE
103
Untuk masing-masing parameter (relevansi dan senioritas), hitung pembagian antara jumlah nilai “TRUE” dengan jumlah total resume, lalu kalikan 100% seperti pada Persamaan 4.136 untuk relevansi dan 4.137 untuk senioritas.

# 𝑁
𝑟𝑃= ()×100%       (4.136)
𝑅𝑒𝑙𝑒𝑣𝑎𝑛𝑐𝑒 𝑁

# 𝑁
𝑠𝑃= ()×100%       (4.137)
𝑆𝑒𝑛𝑖𝑜𝑟𝑖𝑡𝑦 𝑁

## Keterangan
𝑃 = Persentase relevansi
𝑅𝑒𝑙𝑒𝑣𝑎𝑛𝑐𝑒
𝑃  = Persentase senioritas
𝑆𝑒𝑛𝑖𝑜𝑟𝑖𝑡𝑦
𝑁   = Jumlah resume dengan relevansi bernilai TRUE
𝑟
𝑁   = Jumlah resume dengan senioritas bernilai TRUE
𝑠
𝑁   = Total jumlah resume
Demonstrasi perhitungan untuk relevansi lima resume tertera pada Persamaan 4.138.

# 4 𝑃= ()×100%=0,8×100%=80%      (4.138)
𝑅𝑒𝑙𝑒𝑣𝑎𝑛𝑐𝑒 5
Demonstrasi perhitungan untuk senioritas lima resume tertera pada Persamaan 4.139.

# 5 𝑃= ()×100%=1×100%=100%      (4.139)
𝑆𝑒𝑛𝑖𝑜𝑟𝑖𝑡𝑦 5
104

# BAB 5IMPLEMENTASI
Bab implementasi berisi implementasi dari metode kalkulasi similaritas teks pada resume pelamar dengan kualifikasi instansi yang digunakan pada penelitian ini, seperti metode perhitungan similaritas Improved Sqrt-Cosine (ISC) dan Cosine Similarity (CosSim), serta metode representasi teks TF-IDF dan Word2Vec.
5.1Implementasi Kode Program Import Libraries dan Load Dataset
Dalam kode program ini, dilakukan pemuatan dataset resume yang akan dikelola dan dataset kualifikasi lowongan kerja yang dikumpulkan dari https://id.jobstreet.com/ dengan 24 posisi kualifikasi lowongan kerja. Implementasi kode program tertera pada Kode Program 5.1.
Kode Program 5.1 Implementasi kode program import libraries dan load dataset

# 1 import pandas as pd 2 from bs4 import BeautifulSoup 3 import re 4 from gensim.models import Word2Vec 5 import numpy as np 6 from sklearn.metrics.pairwise import cosine_similarity 7 from sklearn.feature_extraction.text import TfidfVectorizer 8 import string 9 from tqdm import tqdm 10 import time 11 12 import nltk 13 nltk.download('wordnet') 14 nltk.download('omw-1.4') 15 nltk.download('punkt') 16 nltk.download('averaged_perceptron_tagger') 17 nltk.download('averaged_perceptron_tagger_eng') 18 19 from nltk.corpus import wordnet 20 from nltk.stem import WordNetLemmatizer 21 from nltk.tokenize import word_tokenize 22 from nltk.corpus import stopwords 23 from nltk import pos_tag 24 25 # Load dataset resume 26 resume_df = pd.read_csv(r'C:\...\archive2024\Resume\Resume.csv') 27 resume_df 28 29 # Load dataset kualifikasi lowongan kerja 30 vacancy_df = pd.read_csv(r'C:\...\archive2024\kualifikasi_loker.csv') 31 vacancy_df 32
105
Kode Program 5.1 Implementasi kode program import libraries dan load dataset (lanjutan)
33 # Load dataset bobot section 34 section_df = pd.read_csv(r'C:\...\archive2024\bobot_section.csv') 35 section_df
Penjelasan dari Kode Program 5.1 mengenai implementasi import libraries dan load dataset, yaitu:
1.Baris 1-10 merupakan proses import library yang diperlukan untuk: pandaspd a. alias  untuk manipulasi data dan analisis data, BeautifulSoupbs4 b. dari library  untuk ekstraksi teks dari HTML, re c. untuk ekspresi reguler atau regular expression (REGEX), gensim.models import Word2Vec  d.untuk menggunakan library Gensim dalam implementasi representasi teks menggunakan pendekatan Word2Vec, numpynp  e. alias untuk operasi numerik seperti perhitungan matematis, sklearn.metrics.pairwise import  f. cosine_similarity untuk menghitung kesamaan antar vektor teks menggunakan Cosine Similarity dari library Scikit-learn, g.sklearn.feature_extraction.text import TfidfVectorizer untuk menggunakan library Scikit-learn dalam implementasi representasi teks menggunakan pendekatan TF-IDF, h.import string  untuk menyediakan daftar karakter tanda baca untuk preprocessing teks, i.from tqdm import tqdm  untuk menampilkan progress bar guna memantau progress dari suatu proses, j.import time   untuk mengukur waktu eksekusi. nltk 2.Baris 12-17 merupakan proses import library dari  (Natural Language Toolkit) yang digunakan untuk pemrosesan teks, termasuk unduhan resource yang diperlukan untuk tokenisasi, lematisasi, dan Part of Speech (POS) tagging, seperti: wordnet a. merupakan basis data leksikal Bahasa Inggris, omw-1.4 b. merupakan Open Multilingual Wordnet versi 1.4 untuk mendukung lematisasi dalam berbagai bahasa, Punkt c. untuk memecah teks atau tokenisasi teks averaged_perceptron_tagger d. dan averaged_perceptron_tagger_eng untuk POS tagging yang memberi label jenis kata seperti kata benda (noun), kata kerja (verb), kata sifat (adjective), dan kata keterangan (adverb).
106
nltk 3.Baris 19-23 merupakan import tambahan dari library , yaitu: wordnetnltk.corpus a. dari  untuk mengakses basis data leksikal WordNet, WordNetLemmatizernltk.stem b. dari  untuk melakukan mengubah kata ke bentuk dasar atau lematisasi, word_tokenizenltk.tokenize c. dari  untuk memecah teks menjadi token, stopwordsnltk.corpus  d. dari menyediakan  daftar kata-kata umum yang tidak bermakna dalam analisis teks untuk dihapus, pos_tag e. untuk memberikan label POS tagging pada setiap kata dalam teks. 4.Baris 25-26 merupakan proses memuat dataset dari file dengan format .csv Resume.csvpandas.read_csv()bernama  menggunakan  yang berisi informasi resume kandidat dan mengubahnya menjadi DataFrame. 5.Baris 27 merupakan sintaksis untuk menampilkan DataFrame resume_df. 6.Baris 29-30 merupakan proses memuat dataset dari file dengan format .csv kualifikasi_loker.csvbernama  menggunakan pandas.read_csv() dan mengubahnya menjadi DataFrame yang berisi informasi lowongan pekerjaan, termasuk nama posisi, nama perusahaan, dan deskripsi kualifikasinya. 7.Baris 31 merupakan sintaksis untuk menampilkan DataFrame vacancy_df. 8.Baris 33-34 merupakan proses memuat dataset dari file dengan format .csv bobot_section.csvbernama  menggunakan pandas.read_csv() dan mengubahnya menjadi DataFrame yang berisi bobot pemberian ahli untuk setiap section yang ada di resume.
107
5.2Implementasi Kode Program Preprocessing Resume
Dalam kode program ini, dilakukan untuk melakukan pra-pemrosesan dataset Resume. Diawali dengan mengekstrak setiap section dari resume yang berformat HTML dan disimpan dalam bentuk DataFrame dengan tambahan informasi mengenai bagian (section) dan isi teks dari masing-masing section. Implementasi kode program ekstraksi section tertera pada Kode Program 5.2.
Kode Program 5.2 Implementasi kode program preprocessing resume bagian ekstraksi section
1 # Melihat informasi kolom dan tipe data 2 resume_df.info() 3 4 # Cek missing values 5 resume_df.isnull().sum() 6 7 # Menghapus kolom yang tidak digunakan 8 resume_df_1 = resume_df.drop(columns=["Category"]) 9 10 # List untuk menyimpan hasil sementara per section dengan semua data dari df 11 data = [] 12 13 # Loop untuk memproses setiap resume 14 for index, row in resume_df.iterrows(): 15     # Ambil ID dan data lainnya dari DataFrame yang ada 16     resume_data = row.to_dict()  # Mengambil semua data di baris ini 17 18     # Ambil resume_str langsung dari kolom 'Resume_str' 19     resume_str = row['Resume_str'] 20 21     # Menemukan semua <div> dengan class "sectiontitle" di 'Resume_html' 22     soup = BeautifulSoup(row['Resume_html'], "html.parser") 23     section_divs = soup.find_all("div", class_="sectiontitle") 24 25     # Menyimpan teks dari setiap section 26     sections = [div.get_text(strip=True) for div in section_divs] 27 28     # Menemukan posisi setiap section dalam resume_str 29     for i, section in enumerate(sections): 30         # Copy data resume agar setiap section mendapatkan data asli resume 31         section_data = resume_data.copy() 32 33         # Cari posisi awal section 34         start_index = resume_str.find(section) 35 36         # Tentukan posisi akhir section 37         if i + 1 < len(sections): 38             end_index = resume_str.find(sections[i + 1], start_index)
108
Kode Program 5.2 Implementasi kode program preprocessing resume bagian ekstraksi section (lanjutan)

# 39 else: 40             end_index = len(resume_str)  # Jika ini adalah section terakhir 41 42         # Ambil teks dari section tersebut dan hapus nama section jika ada di awal teks 43         section_text = resume_str[start_index:end_index].strip() 44         if section_text.startswith(section): 45             section_text = section_text[len(section):].strip() 46 47         # Tambahkan kolom Section dan Text 48         section_data["Section"] = section 49         section_data["Text"] = section_text 50 51         # Tambahkan hasil ke expanded_data 52         data.append(section_data) 53 54 # Mengonversi list menjadi DataFrame 55 resume_df_1 = pd.DataFrame(data)
Penjelasan dari Kode Program 5.2 mengenai implementasi kode program ekstraksi section, yaitu:
1.Baris 1-2 merupakan proses untuk menampilkan informasi mengenai dataset resume, termasuk jumlah kolom, nama kolom, tipe data, dan df.info()jumlah non-null menggunakan . 2.Baris 4-5 merupakan proses untuk memeriksa nilai yang hilang (missing df.isnull().sum()values) dalam dataset resume menggunakan . Category 3.Baris 7-8 merupakan proses untuk menghapus kolom  dari df.drop(columns=["Category"])dataset resume menggunakan resume_df_1dan menyimpan hasilnya ke DataFrame baru sebagai . data 4.Baris 10-11 merupakan proses untuk membuat list kosong bernama untuk menyimpan hasil pemrosesan ekstraksi section resume. 5.Baris 13-14 merupakan proses untuk memulai iterasi melalui setiap baris df.iterrows()dataset resume menggunakan . 6.Baris 15-16 merupakan proses untuk mengubah data baris menjadi row.to_dict()dictionary menggunakan  dan menyimpannya ke resume_datavariabel . 7.Baris 18-19 merupakan proses untuk mengambil teks resume dari kolom Resume_strrow['Resume_str'] menggunakan  dan resume_strmenyimpannya ke variabel . Resume_html 8.Baris 21-23 merupakan proses untuk mem-parsing kolom BeautifulSoup(row['Resume_html'], menggunakan "html.parser")<div> dan menemukan semua elemen  dengan kelas sectiontitlesoup.find_all() menggunakan .
109
9.Baris 25-26 merupakan proses untuk mengekstrak teks dari setiap elemen <div>div.get_text(strip=True) menggunakan  dan sectionsmenyimpannya dalam list . 10.Baris 28-29 merupakan proses untuk memulai iterasi melalui setiap section sectionsenumerate(sections)dalam list  menggunakan . 11.Baris 30-31 merupakan proses untuk membuat salinan dictionary resume_dataresume_data.copy() menggunakan  dan section_datamenyimpannya ke variabel . 12.Baris 33-34 merupakan proses untuk mencari posisi awal nama section resume_strdalam teks  menggunakan resume_str.find(section). 13.Baris 36-40 merupakan proses untuk menentukan posisi akhir section dengan memeriksa apakah ada section berikutnya menggunakan resume_str.find(sections[i + 1], start_index) atau resume_strmenggunakan panjang  jika section terakhir. 14.Baris 42-45 merupakan proses untuk mengambil teks section dari resume_str[start_index:end_index] menggunakan slicing , strip()menghapus spasi berlebih dengan , dan menghapus nama section jika ada yang terdeteksi di awal kalimat pada teks menggunakan section_text[len(section):].strip(). Section 15.Baris 47-49 merupakan proses untuk menambahkan key  dan Textsection_data ke dictionary  dengan value nama section dan teks section yang telah diekstrak. 16.Baris 51-52 merupakan proses untuk menambahkan dictionary section_datadatadata.append() ke list  menggunakan . data 17.Baris 54-55 merupakan proses untuk mengonversi list  menjadi pd.DataFrame(data)DataFrame baru menggunakan  dan resume_df_1menyimpannya sebagai .
110
Selanjutnya, isian resume dilakukan langkah-langkah pra-pemrosesan teks seperti yang sudah dijelaskan pada diagram alur di bab Perancangan. Implementasi kode program preprocessing isian resume tertera pada Kode Program 5.3.
Kode Program 5.3 Implementasi kode program preprocessing resume bagian preprocessing isian resume
1 # Inisialisasi lemmatizer 2 lemmatizer = WordNetLemmatizer() 3 4 # Daftar stop words 5 stop_words = set(stopwords.words('english')) 6 7 # Fungsi untuk mendapatkan tipe kata untuk lemmatization 8 def get_wordnet_pos(tag): 9     if tag.startswith('J'): 10         return wordnet.ADJ 11     elif tag.startswith('V'): 12         return wordnet.VERB 13     elif tag.startswith('N'): 14         return wordnet.NOUN 15     elif tag.startswith('R'): 16         return wordnet.ADV 17     else: 18         return wordnet.NOUN 19 20 def preprocess(text): 21     # Hapus email dan nomor telepon 22     email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A- Za-z]{2,}\b' 23     phone_pattern = r'\b(?:\+?\d{1,3}[- .\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{2,4}[-.\s]?\d{2,4}[- .\s]?\d{2,4}\b' 24 25     text = re.sub(email_pattern, '', text) 26     text = re.sub(phone_pattern, '', text) 27 28     # Hapus berbagai tipe tanda minus 29     text = re.sub(r'[\u2010- \u2015\u2212\uFF0D\uFF0E\uFE63\u002D]', ' ', text) 30 31     # Regex untuk menghapus bulan (termasuk singkatan) & present/current 32     bulan_pattern = r"\b(?:january|jan|february|feb|march|mar|april|apr|may|june|ju n|july|jul|august|aug|september|sep|october|oct|november|nov|de cember|dec)\b" 33     present_pattern = r"\b(?:present|current)\b" 34 35     text = re.sub(bulan_pattern, '', text, flags=re.IGNORECASE) # Hapus bulan dan singkatan 36     text = re.sub(present_pattern, '', text, flags=re.IGNORECASE)  # Hapus "present/current" 37 38     # Regex untuk menangani berbagai format tanggal & rentang
111
Kode Program 5.3 Implementasi kode program preprocessing resume bagian preprocessing isian resume (lanjutan)

# 39 date_pattern = r""" 40         \b( 41         (?:\d{1,2}/(?:\d{4}|Current))  # Format "01/2024" atau "01/ Current" 42         |(?:\d{4})                     # Tahun "2023" 43 －        (?:\s?(?:-|to||–|—)\s?(?:\d{4}|Current|Present))?  # －Rentang waktu "2022 - 2023" atau "2022  Present" 44
)\b 45
""" 46
text = re.sub(date_pattern, '', text, flags=re.IGNORECASE | re.VERBOSE) 47 48
# Hapus placeholder seperti "Company Name" dan "State" 49
text = re.sub(r'\b(?:Company Name|State|City)\b', '', text, flags=re.IGNORECASE) 50 51
# Hapus tanda baca 52
text = re.sub(r'[^a-zA-Z\s]', '', text) 53 54
# Hapus angka 55
text = re.sub(r'\d+', '', text) 56 57
# Hapus spasi berlebihan setelah penghapusan 58
text = re.sub(r'\s+', ' ', text).strip() 59 60
tokens = word_tokenize(text) 61
tokens_pos = pos_tag(tokens) 62 63
# Lemmatization dan hapus stop words 64
lemmatized_text = [] 65
for token, pos in tokens_pos: 66
if token.lower() not in stop_words:  # Menghapus stop words 67
wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN 68
lemmatized_text.append(lemmatizer.lemmatize(token, pos=wordnet_pos)) 69 70
return ' '.join(lemmatized_text) 71 72
# Implementasikan preprocessing ke dataset 73
resume_df_1['Text'] = resume_df_1['Text'].apply(preprocess) 74
resume_df_1['Text'] = resume_df_1['Text'].apply(preprocess)
Penjelasan dari Kode Program 5.3 mengenai implementasi kode program ekstraksi section, yaitu:
1.Baris 1-2 merupakan proses untuk menginisialisasi object WordNetLemmatizer dari NLTK menggunakan WordNetLemmatizer() dan menyimpannya ke variabel lemmatizer untuk melakukan lemmatisasi kata. 2.Baris 4-5 merupakan proses untuk membuat set stop words dalam Bahasa stopwords.words('english')Inggris menggunakan  dan stop_wordsmenyimpannya ke variabel .
112
3.Baris 7-18 merupakan proses untuk mendefinisikan fungsi get_wordnet_pos yang mengonversi tag part-of-speech (POS) ke tipe wordnet.ADJwordnet.VERBkata WordNet seperti , , wordnet.NOUNwordnet.ADV,  berdasarkan awalan tag, dengan wordnet.NOUNdefault  jika tidak sesuai. preprocess 4.Baris 20 merupakan pendefinisian fungsi  yang menerima textparameter  untuk mengeksekusi proses preprocessing teks. 5.Baris 21-23 merupakan proses untuk mendefinisikan pola regex untuk email_patternemail menggunakan  dan nomor telepon menggunakan phone_pattern untuk dihapus dari teks. 6.Baris 25-26 merupakan proses untuk menghapus email dan nomor telepon re.sub()dari teks menggunakan  dengan pola regex yang telah didefinisikan sebelumnya. 7.Baris 28-29 merupakan proses untuk menghapus berbagai jenis tanda re.sub()minus dari teks menggunakan  dan menggantinya dengan spasi. 8.Baris 31-33 merupakan proses untuk mendefinisikan pola regex untuk bulan_patternmenghapus nama bulan menggunakan  dan kata present_pattern"present" atau "current" menggunakan . 9.Baris 35-36 merupakan proses untuk menghapus nama bulan dan kata re.sub()"present" atau "current" dari teks menggunakan  dengan pola regex, mengabaikan huruf besar maupun kecil dengan flags=re.IGNORECASE. 10.Baris 38-46 merupakan proses untuk mendefinisikan pola regex untuk date_patternberbagai format tanggal menggunakan  dan re.sub()menghapusnya dari teks menggunakan  dengan flag re.IGNORECASEre.VERBOSE dan . 11.Baris 48-49 merupakan proses untuk menghapus kata-kata placeholder seperti "Company Name", "State", dan "City" dari teks menggunakan re.sub()flags=re.IGNORECASE dengan . 12.Baris 51-52 merupakan proses untuk menghapus semua tanda baca dan karakter non-huruf. 13.Baris 54-55 merupakan proses untuk menghapus semua angka dari teks. 14.Baris 57-58 merupakan proses untuk mengganti spasi yang berlebihan strip()menjadi hanya satu spasi dan menggunakan  untuk menghapus spasi di awal dan akhir string. 15.Baris 60 merupakan proses untuk memecah teks menjadi daftar kata word_tokenize()(token) menggunakan  dari NLTK. 16.Baris 61 merupakan proses untuk memberikan part-of-speech (POS) tag pos_tag()pada setiap token menggunakan  dari NLTK. 17.Baris 63-68 merupakan proses untuk membuat list kosong lemmatized_text, mengiterasi token dan tag POS-nya, menghapus stop_wordsstop words jika token tidak ada di , mengonversi tag POS ke get_wordnet_pos()format WordNet menggunakan , dan melakukan lemmatizer.lemmatize()lematisasi menggunakan .
113
18.Baris 70 merupakan proses untuk menggabungkan token yang telah di- lematisasi menjadi satu string dengan spasi sebagai pemisah ' '.join()menggunakan . preprocess 19.Baris 72-74 merupakan proses untuk menerapkan fungsi  ke Textresume_df_1kolom  pada DataFrame  menggunakan df['Text'].apply(preprocess). Proses ini dilakukan dua kali karena pada iterasi pertama ada beberapa nama bulan yang belum sepenuhnya terhapus, lalu pada iterasi kedua menghasilkan teks bersih yang sudah sesuai.
SectionSelanjutnya adalah menstandarisasi kolom  ke huruf kecil, keyword_mappingmenyeragamkan nama section menggunakan , menggabungkan teks yang diketahui section-nya lebih dari satu berdasarkan per ID resume-nya, melakukan pemetaan untuk section yang tidak valid berdasarkan pola teks, dan menghapus baris dengan teks kosong. Implementasi kode program preprocessing isian resume per section tertera pada Kode Program 5.4.
Kode Program 5.4 Implementasi kode program preprocessing resume bagian preprocessing isian resume per section

# 1 resume_df_1["Section"] = resume_df_1["Section"].str.lower() 2 3 # Menampilkan nilai unik dari kolom 'Section' 4 unique_sections = resume_df_1['Section'].unique() 5 6 # Menampilkan hasil 7 print("Unique Sections in the Resume:") 8 for section in unique_sections: 9     print(section) 10 11 # Mapping kata kunci ke kategori yang diinginkan 12 keyword_mapping = { 13     "experience": "Experience", 14     "skill": "Skills/Qualifications", 15     "award": "Accomplishments/Awards", 16     "project": "Projects", 17     "education": "Education", 18     "certification": "Certifications", 19     "portfolio": "Portfolio", 20     "organization": "Organization", 21     "volunteer": "Organization", 22     "accomplishment": "Accomplishments/Awards", 23     "achievement": "Accomplishments/Awards", 24     "summary": "Summary", 25     "overview": "Summary", 26     "course": "Education", 27     "academ": "Education", 28     "work": "Experience", 29     "profile": "Summary", 30     "strength": "Skills/Qualifications",
114
Kode Program 5.4 Implementasi kode program preprocessing resume bagian preprocessing isian resume per section (lanjutan)
31     "competencies": "Skills/Qualifications", 32     "compentencies": "Skills/Qualifications", 33     "quali": "Skills/Qualifications", 34     "honor": "Certifications", 35     "honour": "Certifications", 36     "affiliation": "Certifications", 37     "affliation": "Certifications", 38     "language": "Skills/Qualifications", 39     "community": "Organization", 40     "about": "Summary", 41     "training": "Certifications", 42     "scholarship": "Education", 43     "license": "Certifications", 44     "highlight": "Skills/Qualifications", 45     "expertise": "Skills/Qualifications", 46     "focus": "Summary", 47     "background": "Summary", 48     "interest": "Skills/Qualifications", 49     "military": "Experience", 50     "presentation": "Skills/Qualifications", 51     "objective": "Summary", 52     "reference": "Skills/Qualifications", 53     "referance": "Skills/Qualifications", 54     "proficien": "Skills/Qualifications", 55     "dissertation": "Projects", 56     "publications": "Skills/Qualifications", 57     "associat": "Skills/Qualifications", 58     "professional": "Experience", 59     "leadership": "Organization", 60     "curricular": "Organization", 61     "credential": "Skills/Qualifications", 62     "information": "Others", 63     "societ": "Organization", 64     "research": "Skills/Qualifications", 65     "employment": "Experience", 66     "adjunct": "Skills/Qualifications", 67     "personal": "Others", 68     "characteristic": "Others", 69     "goal": "Summary", 70     "apply": "Summary", 71     "role": "Experience", 72     "general": "Others", 73     "link": "Portfolio", 74     "snap shot": "Experience", 75     "tool": "Skills/Qualifications", 76     "hobb": "Others", 77     "activit": "Organization", 78     "client": "Experience", 79     "success": "Accomplishments/Awards", 80     "computer": "Skills/Qualifications", 81     "technical": "Skills/Qualifications", 82     "acumen": "Skills/Qualifications", 83     "development": "Skills/Qualifications", 84     "knowledge": "Skills/Qualifications", 85     "membership": "Skills/Qualifications", 86     "speak": "Accomplishments/Awards",
115
Kode Program 5.4 Implementasi kode program preprocessing resume bagian preprocessing isian resume per section (lanjutan)
87     "participat": "Projects", 88     "vocation": "Experience", 89     "clearance": "Skills/Qualifications", 90     "attribute": "Skills/Qualifications", 91     "exhibit": "Projects", 92 } 93 94 # Ubah nilai 'Section' berdasarkan kata kunci 95 for keyword, category in keyword_mapping.items(): 96    resume_df_1.loc[resume_df_1['Section'].str.contains(keyword, case=False, na=False), 'Section'] = category 97 98 # Gabungkan teks dari section terkait jika ada duplikasi dalam satu resume 99 resume_df_1 = resume_df_1.groupby(['ID', 'Section'], as_index=False).agg({ 100     'Text': ' '.join, 101     'Resume_str': 'first', 102     'Resume_html': 'first', 103 }) 104 105 # Daftar section yang tidak boleh diubah 106 allowed_sections = [ 107     "Summary", "Accomplishments/Awards", "Skills/Qualifications", 108     "Education", "Experience", "Organization", "Projects", 109     "Certifications", "Portfolio", "Others" 110 ] 111 112 # Pola regex untuk kata-kata yang harus masuk ke Summary 113 summary_pattern = r'\b(?:Summary|I am|I\'m|years|experience|professional)\b' 114 115 # Ubah ke "Summary" jika ada salah satu kata dalam summary_pattern 116 resume_df_1.loc[ 117     (~resume_df_1["Section"].isin(allowed_sections)) & 118     (resume_df_1["Text"].str.contains(summary_pattern, case=False, na=False, regex=True)), 119     "Section" 120 ] = "Summary" 121 122 # Ubah ke "Portfolio" jika ada kata "LinkedIn" dalam "Text" 123 resume_df_1.loc[ 124     (~resume_df_1["Section"].isin(allowed_sections)) & 125     (resume_df_1["Text"].str.contains(r'\bLinkedIn\b', case=False, na=False, regex=True)), 126     "Section" 127 ] = "Portfolio" 128
116
Kode Program 5.4 Implementasi kode program preprocessing resume bagian preprocessing isian resume per section (lanjutan)
129 # Jika section tidak termasuk valid_sections dan kolom "Text" kosong, hapus baris tersebut 130 resume_df_1 = resume_df_1[~((~resume_df_1['Section'].isin(allowed_sections)) & (resume_df_1['Text'].isna()))] 131 132 # Jika section tidak termasuk valid_sections tetapi ada isian di "Text", ubah menjadi "Others" 133 resume_df_1.loc[~resume_df_1['Section'].isin(allowed_sections), 'Section'] = 'Others' 134 135 # Hapus baris dengan Text yang NaN, kosong, atau hanya spasi untuk semua Section 136 resume_df_1 = resume_df_1[~(resume_df_1['Text'].isna() | (resume_df_1['Text'].str.strip() == ''))] 137 138 resume_df_1["Text"] = resume_df_1["Text"].str.lower() 139 resume_df_1 = resume_df_1.drop(columns=["Resume_str"]) 140 resume_df_1 = resume_df_1.drop(columns=["Resume_html"])
Penjelasan dari Kode Program 5.4 mengenai implementasi kode program ekstraksi section, yaitu:
1.Baris 1 merupakan proses untuk mengubah semua nilai di kolom Sectionresume_df_1 pada DataFrame  menjadi huruf kecil str.lower()menggunakan  guna lebih mudah dalam menyeragamkan nama-nama section. 2.Baris 3-9 merupakan proses untuk mengambil nilai unik dari kolom Sectionresume_df_1unique() pada DataFrame  menggunakan unique_sectionsdan menyimpannya ke variabel  guna memahami ada apa saja nama-nama section yang digunakan seluruh resume di dataset. 3.Baris 11-92 merupakan proses untuk mendefinisikan dictionary keyword_mapping yang berisi pasangan key dan value, di mana key adalah nama section yang telah diketahui dari pemeriksaan nilai unik Sectionkolom  sebelumnya, lalu value adalah nama section yang diinginkan untuk mengelompokkan nama-nama section resume. 4.Baris 94-96 merupakan proses untuk mengiterasi setiap pasangan key dan keyword_mappingitems()value di  menggunakan , lalu mengubah Sectionnilai kolom  yang mengandung kata kunci seperti di key menjadi keyword_mappingvalue seperti  dan mengabaikan huruf besar maupun kecil. 5.Baris 98-103 merupakan proses untuk mengelompokkan isi DataFrame resume_df_1IDSection berdasarkan kolom  dan  menggunakan groupby()Text, lalu menggabungkan teks untuk kolom  menggunakan ' '.joinSection jika ada nilai di kolom  yang sama.
117
6.Baris 105-110 merupakan proses untuk mendefinisikan list allowed_sections yang berisi daftar nama-nama section yang diizinkan untuk tetap ada dalam DataFrame. 7.Baris 112-113 merupakan proses untuk mendefinisikan pola regex summary_pattern yang mencakup kata-kata seperti "Summary", "I am", "I'm", "years", "experience", atau "professional" untuk mengidentifikasi teks yang relevan dengan nama section "Summary". Section 8.Baris 115-120 merupakan proses untuk mengubah nilai kolom allowed_sectionsmenjadi "Summary" jika section tidak ada di  dan Textsummary_patternkolom  mengandung kata-kata dari . Section 9.Baris 122-127 merupakan proses untuk mengubah nilai kolom allowed_sectionsmenjadi "Portfolio" jika section tidak ada di  dan Textkolom  mengandung kata "LinkedIn". 10.Baris 129-130 merupakan proses untuk menghapus baris dari resume_df_1Sectionallowed_sections jika kolom  tidak ada di Textdan kolom  kosong. Section 11.Baris 132-133 merupakan proses untuk mengubah nilai kolom allowed_sectionsmenjadi "Others" jika section tidak ada di  tetapi Textkolom  tidak kosong. 12.Baris 135-136 merupakan proses untuk menghapus baris dari resume_df_1Text jika kolom  kosong atau jika hanya berisi spasi. Text 13.Baris 138 merupakan proses untuk mengubah semua nilai di kolom resume_df_1pada DataFrame  menjadi huruf kecil atau lower casing. Resume_str 14.Baris 139 merupakan proses untuk menghapus kolom  dari resume_df_1DataFrame  karena sudah tidak digunakan. Resume_html 15.Baris 140 merupakan proses untuk menghapus kolom  dari resume_df_1DataFrame  karena sudah tidak digunakan.
5.3Implementasi Kode Program Preprocessing Kualifikasi Lowongan Kerja
Dalam kode program ini, dilakukan untuk membersihkan teks pada kolom Description yang merupakan deskripsi lowongan kerja dengan mengubah ke huruf kecil, menghapus tanda baca dan spasi berlebih, melakukan tokenisasi, POS tagging, menghapus stop words, dan lematisasi. Implementasi kode program tertera pada Kode Program 5.5.
Kode Program 5.5 Implementasi kode program preprocessing kualifikasi lowongan kerja

# 1 def preprocess_vacancy(text): 2     text = text.lower()  # Ubah ke huruf kecil 3     text = re.sub(r'\d+', '', text)  # Hapus angka 4     text = text.translate(str.maketrans('', '', string.punctuation))  # Hapus tanda baca 5     text = ' '.join(text.split())  # Hapus spasi berlebih 6
118
Kode Program 5.5 Implementasi kode program preprocessing kualifikasi lowongan kerja (lanjutan)
7     # Tokenisasi 8     tokens = word_tokenize(text) 9 10     # POS tagging 11     tagged_tokens = pos_tag(tokens) 12 13     # Hapus stop words & Lemmatization 14     processed_tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) 15                         for word, tag in tagged_tokens if word not in stop_words] 16 17     return ' '.join(processed_tokens) 18 19 # Terapkan preprocessing pada kolom "Description" di vacancy_df vacancy_df_1 = vacancy_df.copy() 20 vacancy_df_1["Description"] = 21 vacancy_df["Description"].apply(preprocess_vacancy)
Penjelasan dari Kode Program 5.5 mengenai implementasi preprocessing isian teks deskripsi kualifikasi lowongan kerja, yaitu:
1.Baris 1 merupakan proses untuk mendefinisikan fungsi preprocess_vacancytext yang menerima parameter  untuk memproses teks deskripsi lowongan kerja. 2.Baris 2 merupakan proses untuk mengubah teks input menjadi huruf kecil text.lower()menggunakan  untuk standarisasi. 3.Baris 3 merupakan proses untuk menghapus angka-angka dari teks. 4.Baris 4 merupakan proses untuk menghapus semua tanda baca dari teks string.punctuationberdasarkan daftar punctuation dari . 5.Baris 5 merupakan proses untuk menghapus spasi berlebih dengan split()memecah teks menjadi kata-kata menggunakan , lalu ' '.join()menggabungkannya kembali menggunakan  dengan spasi tunggal 6.Baris 7-8 merupakan proses untuk memecah teks menjadi daftar kata word_tokenize()(token) menggunakan  dari NLTK dan tokensmenyimpannya ke variabel . 7.Baris 10-11 merupakan proses untuk memberikan part-of-speech (POS) tag pos_tag()pada setiap token menggunakan  dari NLTK dan tagged_tokensmenyimpannya ke variabel . processed_tokens 8.Baris 13-15 merupakan proses untuk membuat list tagged_tokensdengan mengiterasi , menghapus kata-kata yang ada di stop_words, dan melakukan lematisasi pada setiap kata menggunakan lemmatizer.lemmatize() dengan tipe kata dari get_wordnet_pos(tag).
119
9.Baris 17 merupakan proses untuk menggabungkan token yang telah diproses menjadi satu string dengan spasi sebagai pemisah menggunakan ' '.join() dan mengembalikannya sebagai hasil dari fungsi preprocess_vacancy. 10.Baris 19-20 merupakan proses untuk membuat salinan DataFrame vacancy_dfcopy() menggunakan  dan menyimpannya ke variabel vacancy_df_1 guna menghindari modifikasi data asli. 11.Baris 21 merupakan proses untuk menerapkan fungsi preprocess_vacancyDescription ke kolom  pada DataFrame vacancy_dfDescription dan menyimpan hasilnya ke kolom  pada vacancy_df_1DataFrame .
5.4Implementasi Kode Program Representasi Teks TF-IDF
Dalam kode program ini, dilakukan implementasi representasi teks menggunakan TF-IDF dengan TfidfVectorizer dari library Scikit-learn untuk Textresume_df_1mengubah teks pada kolom  dari  dan kolom Descriptionvacancy_df_1 dari  menjadi vektor TF-IDF. Vektor-vektor ini TFIDF_Vectordisimpan sebagai list dalam kolom baru  pada kedua DataFrame. Implementasi kode program tertera pada Kode Program 5.6.
Kode Program 5.6 Implementasi kode program representasi teks TF-IDF
1 # Inisialisasi TF-IDF Vectorizer 2 vectorizer = TfidfVectorizer() 3 4 # Fit dan transform data 5 tfidf_resume = vectorizer.fit_transform(resume_df_1["Text"]) 6 tfidf_vacancy = vectorizer.transform(vacancy_df_1["Description"]) 7 8 # Simpan vektor dalam kolom baru 9 resume_df_1["TFIDF_Vector"] = list(tfidf_resume.toarray()) 10 vacancy_df_1["TFIDF_Vector"] = list(tfidf_vacancy.toarray())
Penjelasan dari Kode Program 5.6 mengenai implementasi representasi teks dengan pendekatan TF-IDF, yaitu:
1.Baris 1-2 merupakan proses untuk menginisialisasi objek TfidfVectorizer TfidfVectorizer()dari library Scikit-learn menggunakan  dan vectorizermenyimpannya ke variabel  untuk mengubah teks menjadi vektor TF-IDF. Text 2.Baris 4-5 merupakan proses untuk mempelajari kosa kata dari kolom resume_df_1pada DataFrame  dan mengubahnya menjadi matriks TF- fit_transform()IDF menggunakan , lalu menyimpan hasilnya ke tfidf_resumevariabel .
120
Description 3.Baris 6 merupakan proses untuk mengubah kolom  pada vacancy_df_1DataFrame  menjadi matriks TF-IDF menggunakan transform() berdasarkan kosa kata yang telah dipelajari dari resume_df_1["Text"], lalu menyimpan hasilnya ke variabel tfidf_vacancy. 4.Baris 8-9 merupakan proses untuk mengonversi matriks TF-IDF tfidf_resumetoarray() menjadi array menggunakan  dan TFIDF_Vectormenyimpan setiap vektor sebagai list dalam kolom baru resume_df_1pada DataFrame . 5.Baris 10 merupakan proses untuk mengonversi matriks TF-IDF tfidf_vacancytoarray() menjadi array menggunakan  dan TFIDF_Vectormenyimpan setiap vektor sebagai list dalam kolom baru vacancy_df_1pada DataFrame .
5.5Implementasi Kode Program Representasi Teks Word2Vec
Dalam kode program ini, dilakukan implementasi representasi teks Textmenggunakan Word2Vec dari library Gensim. Kode ini memproses kolom resume_df_1Descriptionvacancy_df_1pada  dan kolom  pada  untuk pelatihan model Word2Vec dengan menggabungkan teks resume dan deskripsi lowongan kerja. Model Word2Vec dilatih dengan parameter ukuran vektor kata bernilai 100, jarak antar kata dalam konteks (window) bernilai 5, menggunakan skip-gram, dan learning rate bernilai 0,1. Hasil vektor disimpan ke kolom baru W2V_Vector pada kedua DataFrame. Implementasi kode program tertera pada Kode Program 5.7.
Kode Program 5.7 Implementasi kode program representasi teks Word2Vec

# 1 def tokenize_text(text): 2     return word_tokenize(text.lower())  # Tokenisasi dan ubah ke huruf kecil 3 4 # Tokenisasi teks dari resume_df_1 dan vacancy_df_1 5 resume_texts = resume_df_1['Text'].dropna().apply(tokenize_text).tolist() 6 vacancy_texts = vacancy_df_1['Description'].dropna().apply(tokenize_text).tolis t() 7 8 # Gabungkan semua teks untuk pelatihan Word2Vec 9 all_texts = resume_texts + vacancy_texts 10 11 # Latih model Word2Vec 12 word2vec_model = Word2Vec( 13     sentences=all_texts, 14     vector_size=100  #ukuran vektor kata 15     window=5, #jarak maksimum antar kata dalam konteks 16     workers=4, #jumlah thread untuk pelatihan 17     sg=1, 18     alpha=0,1 19 ) 20 21 # Menghitung vektor rata-rata dokumen 22 def get_document_vector(text, model):
121
Kode Program 5.7 Implementasi kode program representasi teks Word2Vec (lanjutan)

# 23 words = tokenize_text(text) 24     word_vectors = [model.wv[word] for word in words if word in model.wv] 25     if not word_vectors:  # Jika tidak ada kata yang dikenali 26         return np.zeros(model.vector_size) 27     return np.mean(word_vectors, axis=0) 28 29 # Penerapan ke dataset 30 resume_df_1['W2V_Vector'] = resume_df_1['Text'].apply(lambda x: get_document_vector(x, word2vec_model)) 31 vacancy_df_1['W2V_Vector'] = vacancy_df_1['Description'].apply(lambda x: get_document_vector(x, word2vec_model))
Penjelasan dari Kode Program 5.7 mengenai implementasi representasi teks dengan pendekatan Word2Vec, yaitu:
1.Baris 1-2 merupakan proses untuk mendefinisikan fungsi tokenize_texttext yang mengambil  sebagai input, mengonversi ke text.lower()huruf kecil (lower casing) dengan , dan melakukan word_tokenizetokenisasi menggunakan  dari library NLTK. 2.Baris 3-4 merupakan proses untuk menghapus nilai kosong dari kolom Textresume_df_1dropna() pada DataFrame  menggunakan , word_tokenize()melakukan tokenisasi kata dengan , dan tolist()mengonversi hasilnya menjadi list menggunakan , lalu resume_textsmenyimpannya ke variabel . 3.Baris 5-6 merupakan proses untuk menghapus nilai kosong dari kolom Descriptionvacancy_df_1 pada DataFrame  menggunakan dropna()word_tokenize(), melakukan tokenisasi kata dengan , tolist()dan mengonversi hasilnya menjadi list menggunakan , lalu vacancy_textsmenyimpannya ke variabel . resume_texts 4.Baris 8-9 merupakan proses untuk menggabungkan list vacancy_textsall_textsdan  menjadi satu list  untuk digunakan dalam pelatihan model Word2Vec. 5.Baris 11-19 merupakan proses untuk melatih model Word2Vec Word2Vec()menggunakan  dari library Gensim dengan parameter: sentences=all_textsvector_size=100 (data teks),  (ukuran window=5workers=4vektor kata),  (jarak konteks kata),  (jumlah sg=1alpha=0,1thread),  (menggunakan algoritma skip-gram), dan word2vec_model(learning rate), lalu menyimpan model ke variabel .
122
6.Baris 21-27 merupakan proses untuk mendefinisikan fungsi get_document_vector yang menghitung vektor rata-rata dokumen tokenize_text()dengan melakukan tokenisasi teks menggunakan , model.wvmodelmengambil vektor kata dari  untuk kata yang ada di . vector_sizeFungsi ini mengembalikan vektor nol dengan panjang  jika tidak ada kata yang dikenali atau mengembalikan hasil rata-rata vektor np.mean()kata menggunakan . 7.Baris 30 merupakan proses untuk menerapkan fungsi get_document_vectorText ke kolom  pada DataFrame resume_df_1apply() menggunakan  dengan model word2vec_model, lalu menyimpan vektor rata-rata dokumen ke kolom W2V_Vectorbaru . 8.Baris 231 merupakan proses untuk menerapkan fungsi get_document_vectorDescription ke kolom  pada DataFrame vacancy_df_1apply() menggunakan  dengan model word2vec_model, lalu menyimpan vektor rata-rata dokumen ke kolom W2V_Vectorbaru .

## 5.6Implementasi Kode Program Perhitungan Similaritas
5.6.1Implementasi Kode Program Improved Sqrt-Cosine Similarity
Dalam kode program ini, dilakukan penghitungan kemiripan antara dua vektor menggunakan pendekatan Improved Sqrt-Cosine (ISC) Similarity. Prosesnya mencakup memeriksa validitas input, mengubah elemen vektor menjadi positif, menghitung pembilang (jumlah akar kuadrat perkalian elemen) dan penyebut (perkalian akar kuadrat jumlah elemen), lalu mengembalikan nilai kemiripan atau 0 jika perhitungan tidak valid. Implementasi kode program tertera pada Kode Program 5.8.
Kode Program 5.8 Implementasi kode program Improved Sqrt-Cosine Similarity
1 # Fungsi Improved Sqrt-Cosine Similarity (ISC) 2 def improved_sqrt_cosine_similarity(x, y): 3     if x is None or y is None or len(x) != len(y): 4         return 0 5 6     # Mengambil nilai absolut untuk penggunaan dengan Word2Vec 7     x = np.abs(x) 8     y = np.abs(y) 9 10     # Menghitung pembilang dan penyebut sesuai dengan rumus ISC 11     numerator = np.sum(np.sqrt(x * y)) 12     denominator = np.sqrt(np.sum(x)) * np.sqrt(np.sum(y)) 13 14     # Menghitung ISC 15     isc = numerator / denominator if denominator != 0 else 0 16     return isc
123
Penjelasan dari Kode Program 5.8 mengenai implementasi perhitungan Improved Sqrt-Cosine Similarity, yaitu:
1.Baris 1-2 merupakan proses untuk mendefinisikan fungsi improved_sqrt_cosine_similarity yang menerima dua xyparameter, yakni  dan  (vektor) untuk menghitung kemiripan menggunakan metrik Improved Sqrt-Cosine Similarity (ISC). x 2.Baris 3-4 merupakan proses untuk memeriksa apakah salah satu vektor yNoneatau  adalah  atau memiliki panjang yang berbeda menggunakan if0kondisi . Kemudian, mengembalikan nilai  jika kondisi tersebut true. x 3.Baris 6-8 merupakan proses untuk mengubah semua elemen vektor  atau ynp.abs() menjadi nilai absolut menggunakan . Absolut ini digunakan ketika mengimplementasi pendekatan Word2Vec dengan ISC. 4.Baris 10-11 merupakan proses untuk menghitung numerator (pembilang) xyrumus ISC dengan mengalikan elemen-elemen vektor  dan , mengambil np.sqrt()akar kuadrat dari hasil perkalian dengan , dan menjumlahkan np.sum()semua hasilnya menggunakan . 5.Baris 12 merupakan proses untuk menghitung denominator (penyebut) xyrumus ISC dengan menjumlahkan elemen vektor  atau  menggunakan np.sum(), mengambil akar kuadrat dari masing-masing jumlah dengan np.sqrt(), lalu mengalikan kedua akar tersebut. 6.Baris 14-16 merupakan proses untuk menghitung nilai ISC yang disimpan iscpada variabel  dengan membagi numerator dengan denominator jika denominator tidak nol atau mengembalikan 0 jika denominator nol untuk menghindari pembagian dengan nol. Kemudian, mengembalikan nilai iscvariabel  yang telah dihitung sebagai hasil dari fungsi improved_sqrt_cosine_similarity.
5.6.2Implementasi Kode Program TF-IDF dan Improved Sqrt-Cosine Similarity
Dalam kode program ini, dilakukan perhitungan kemiripan antara resume dan kualifikasi lowongan kerja menggunakan Improved Sqrt-Cosine (ISC) Similarity untuk vektor TF-IDF, dengan dua skenario, yakni “Tanpa Bobot” (hasil kemiripan semua section dirata-ratakan) dan “Dengan Bobot” (hasil kemiripan semua section section_dfdiberikan bobot persentase berdasarkan ). Hasil disimpan dalam result_df_tfidfDataFrame , dan lima resume teratas untuk setiap posisi ditampilkan berdasarkan kemiripan “Tanpa Bobot” dan “Dengan Bobot”. Implementasi kode program tertera pada Kode Program 5.9.
Kode Program 5.9 Implementasi kode program TF-IDF dan Improved Sqrt- Cosine Similarity

# 1 start_time = time.time() # Catat waktu mulai 2 3 # List untuk menyimpan hasil similarity setiap resume 4 final_results_tfidf = [] 5
124
Kode Program 5.9 Implementasi kode program TF-IDF dan Improved Sqrt- Cosine Similarity (lanjutan)
6 # Looping untuk setiap job vacancy 7 for _, vacancy_row_tfidf in tqdm(vacancy_df_1.iterrows(), total=len(vacancy_df_1), desc="Processing Vacancies"): 8     vacancy_category_tfidf = vacancy_row_tfidf["Category"] 9     job_vec_tfidf = vacancy_row_tfidf["TFIDF_Vector"] 10     position_name = vacancy_row_tfidf["Position"] 11 12     # Ambil bobot section sesuai kategori dan ubah ke skala desimal 13     category_weights = (section_df[section_df["Category"] == vacancy_category_tfidf] 14                         .set_index("Section")["Bobot"] 15                         .div(100) 16                         .to_dict()) 17 18     # Looping untuk setiap resume 19     for resume_id in resume_df_1["ID"].unique(): 20         resume_sections = resume_df_1[resume_df_1["ID"] == resume_id] 21         similarity_scores_tfidf = {} 22 23         # Hitung similarity untuk setiap section 24         for _, section_row_tfidf in resume_sections.iterrows(): 25             section_name_tfidf = section_row_tfidf["Section"] 26             section_vec_tfidf = section_row_tfidf["TFIDF_Vector"] 27 28             sim_tfidf = improved_sqrt_cosine_similarity(section_vec_tfidf, job_vec_tfidf) 29             similarity_scores_tfidf[section_name_tfidf] = sim_tfidf 30 31         # Versi 1: Tanpa bobot (rata-rata similarity semua section) 32         sim_no_weight = sum(similarity_scores_tfidf.values()) / len(similarity_scores_tfidf) if similarity_scores_tfidf else 0 33 34         # Versi 2: Dengan bobot (weighted sum tanpa normalisasi total weight) 35         weighted_sum_v2 = 0 36         total_weight_v2 = 0 37         for sec in similarity_scores_tfidf: 38             sim = similarity_scores_tfidf[sec] 39             weight = category_weights.get(sec, 0) 40             weighted_sum_v2 += sim * weight 41             total_weight_v2 += weight 42         sim_with_weight = weighted_sum_v2 / total_weight_v2 if total_weight_v2 > 0 else 0 43 44         # Simpan hasil 45         final_results_tfidf.append((resume_id, position_name, sim_no_weight, sim_with_weight)) 46 47 # Catat waktu selesai dan hitung durasi 48 end_time = time.time() 49 total_time = end_time - start_time 50 51 # Konversi waktu ke format yang lebih mudah dibaca 52 minutes = int(total_time // 60) 53 seconds = int(total_time % 60)
125
Kode Program 5.9 Implementasi kode program TF-IDF dan Improved Sqrt- Cosine Similarity (lanjutan)
54 55 # Buat DataFrame hasil similarity 56 result_df_tfidf = pd.DataFrame( 57     final_results_tfidf, 58     columns=["Resume_ID", "Position", "Similarity_No_Weight", "Similarity_With_Weight"] 59 ) 60 61 # Tampilkan waktu total 62 print(f"Total waktu pemrosesan: {minutes} menit {seconds} detik") 63 64 print("Similaritas Tanpa Bobot Section") 65 66 top5_per_position_no_weight = result_df_tfidf.groupby('Position', group_keys=False).apply( 67     lambda x: x.nlargest(5, 'Similarity_No_Weight') 68 ) 69 70 grouped_no_weight = top5_per_position_no_weight.groupby('Position') 71 for position, group in grouped_no_weight: 72     print(f"\nPosition: {position}") 73     print(group[['Resume_ID', 'Similarity_No_Weight']]) 74 75 print("Similaritas Dengan Bobot Section") 76 77 top5_per_position_with_weight = result_df_tfidf.groupby('Position', group_keys=False).apply( 78     lambda x: x.nlargest(5, 'Similarity_With_Weight') 79 ) 80 81 grouped_with_weight = top5_per_position_with_weight.groupby('Position') 82 for position, group in grouped_with_weight: 83     print(f"\nPosition: {position}") 84     print(group[['Resume_ID', 'Similarity_With_Weight']])
Penjelasan dari Kode Program 5.9 mengenai implementasi perhitungan similaritas antara resume dan kualifikasi lowongan kerja dengan Improved Sqrt- Cosine (ISC) Similarity jika menggunakan vektor TF-IDF, yaitu:
1.Baris 1 merupakan proses untuk mencatat waktu mulai eksekusi time.time()menggunakan  dan menyimpannya ke variabel start_time. 2.Baris 3-4 merupakan proses untuk membuat list kosong final_results_tfidf untuk menyimpan hasil perhitungan kemiripan (similarity) antara resume dan kualifikasi lowongan kerja. 3.Baris 6-7 merupakan proses untuk memulai iterasi melalui setiap baris di vacancy_df_1iterrows()DataFrame  menggunakan  dengan tqdmprogress bar dari  untuk menampilkan kemajuan pemrosesan. Category 4.Baris 8 merupakan pengambilan nilai kolom  dari baris lowongan kerja pada iterasi terkini dan menyimpannya ke variabel vacancy_category_tfidf.
126
5.Baris 9 merupakan pengambilan vektor TF-IDF dari kolom TFIDF_Vector pada baris lowongan kerja di iterasi terkini dan job_vec_tfidfmenyimpannya ke variabel . Position 6.Baris 10 merupakan pengambilan nilai kolom  dari baris lowongan kerja pada iterasi terkini dan menyimpannya ke variabel position_name. section_df 7.Baris 12-16 merupakan proses untuk memfilter DataFrame vacancy_category_tfidfberdasarkan , menetapkan kolom SectionBobot sebagai indeks, mengambil kolom , membaginya dengan div(100)100 menggunakan  untuk mengubah ke skala desimal (karena bobot dalam persentase), dan mengonversinya menjadi dictionary to_dict()menggunakan , lalu menyimpannya ke variabel category_weights sebagai persentase bobot per section untuk kualifikasi lowongan kerja pada iterasi terkini sesuai industrinya. 8.Baris 18-19 merupakan proses untuk memulai iterasi melalui setiap nilai IDresume_df_1unik di kolom  pada DataFrame  menggunakan unique(). resume_df_1 9.Baris 20 merupakan proses untuk memfilter DataFrame IDuntuk mendapatkan semua baris dengan kolom  yang sesuai dengan resume_iditerasi  terkini dan menyimpannya ke variabel resume_sections. 10.Baris 21 merupakan pembuatan dictionary kosong similarity_scores_tfidf untuk menyimpan skor kemiripan setiap section dalam resume. 11.Baris 23-24 merupakan proses untuk memulai iterasi melalui setiap baris resume_sectionsiterrows()di  menggunakan  untuk memproses setiap section dalam resume. Section 12.Baris 25 merupakan proses untuk mengambil nilai kolom  dari baris section terkini dan menyimpannya ke variabel section_name_tfidf. 13.Baris 26 merupakan proses untuk mengambil vektor TF-IDF dari kolom TFIDF_Vector pada baris section saat ini dan menyimpannya ke section_vec_tfidfvariabel . 14.Baris 28 merupakan proses untuk menghitung kemiripan antara vektor section_vec_tfidfsection pada resume () dan vektor kualifikasi job_vec_tfidflowongan kerja () menggunakan fungsi improved_sqrt_cosine_similarity, lalu menyimpan hasilnya sim_tfidfke variabel . 15.Baris 29 merupakan proses untuk menyimpan skor kemiripan sim_tfidfsimilarity_scores_tfidf ke dictionary .
127
16.Baris 31-32 merupakan proses untuk menguji skenario “Tanpa Bobot” dengan menghitung rata-rata kemiripan dengan menjumlahkan semua similarity_scores_tfidfsum()skor kemiripan di  menggunakan len()dan membaginya dengan jumlah section menggunakan , atau mengembalikan 0 jika dictionary kosong, lalu menyimpan hasilnya ke sim_no_weightvariabel . 17.Baris 34-42 merupakan proses untuk menguji skenario “Dengan Bobot”, weighted_sum_v2dimana baris 35-36 menginisialisasi variabel  dan total_weight_v2 dengan nilai 0 untuk menghitung jumlah kemiripan terbobot dan total bobot. 18.Baris 37-41 merupakan proses untuk mengiterasi setiap section di similarity_scores_tfidf, mengambil skor kemiripan yang simdisimpan pada variabel , mendapatkan bobot section dari variabel category_weightsget() dengan default 0 menggunakan , mengalikan skor “Dengan Bobot” untuk menambah ke weighted_sum_v2total_weight_v2, dan menambah bobot ke . 19.Baris 42 merupakan proses untuk menghitung total similarity pada weighted_sum_v2skenario “Dengan Bobot” dengan membagi  dengan total_weight_v2total_weight_v2 jika  lebih dari 0 atau mengembalikan nilai 0 jika tidak. Kemudian, menyimpan hasilnya ke sim_with_weightvariabel . resume_id 20.Baris 44-45 merupakan proses untuk menambahkan data , position_namesim_no_weightsim_with_weight, , dan  ke list final_results_tfidfappend() menggunakan . 21.Baris 47-49 merupakan proses untuk mencatat waktu selesai time.time()menggunakan , menghitung durasi dengan mengurangkan start_timeend_time dari , dan menyimpan hasilnya ke variabel total_time. total_time 22.Baris 51-53 merupakan proses untuk mengonversi  ke menit minutessecondsdan detik, lalu menyimpannya ke variabel  dan . 23.Baris 55-59 merupakan proses untuk membuat DataFrame result_df_tfidffinal_results_tfidf dari list  menggunakan pd.DataFrame()Resume_IDPosition, dengan kolom , , Similarity_No_WeightSimilarity_With_Weight, dan . 24.Baris 61-62 merupakan proses untuk mencetak total waktu pemrosesan print()dalam format menit dan detik menggunakan . 25.Baris 64 merupakan proses untuk mencetak judul "Similaritas Tanpa Bobot print()Section" menggunakan . 26.Baris 66-68 merupakan proses untuk mengelompokkan DataFrame result_df_tfidfPosition berdasarkan kolom  menggunakan groupby(), lalu memilih 5 baris dengan nilai Similarity_No_Weight tertinggi untuk setiap posisi menggunakan nlargest(), dan menyimpan hasilnya ke variabel top5_per_position_no_weight.
128
27.Baris 70-73 merupakan proses untuk mengelompokkan top5_per_position_no_weightPosition berdasarkan kolom , Positionmengiterasi setiap kualifikasi lowongan kerja (), mencetak Resume_IDnama posisi, mencetak nilai kolom , serta mencetak nilai Similarity_No_Weight untuk setiap kualifikasi lowongan kerja. 28.Baris 75 merupakan proses untuk mencetak judul "Similaritas Dengan print()Bobot Section" menggunakan . 29.Baris 77-79 merupakan proses untuk mengelompokkan DataFrame result_df_tfidfPosition berdasarkan kolom  menggunakan groupby(), lalu memilih 5 baris dengan nilai Similarity_With_Weight tertinggi untuk setiap posisi nlargest()menggunakan , dan menyimpan hasilnya ke variabel top5_per_position_with_weight. 30.Baris 81-84 merupakan proses untuk mengelompokkan top5_per_position_with_weightPosition berdasarkan , Positionmengiterasi setiap kualifikasi lowongan kerja (), mencetak Resume_IDnama posisi, mencetak kolom , serta Similarity_With_Weight untuk setiap kualifikasi lowongan kerja.
5.6.3Implementasi Kode Program Word2Vec dan Cosine Similarity
Dalam kode program ini, dilakukan menghitung kemiripan antara resume dan kualifikasi lowongan kerja menggunakan metrik Cosine Similarity (CosSim) untuk vektor Word2Vec, dengan dua skenario, yakni “Tanpa Bobot” (hasil kemiripan semua section dirata-ratakan) dan “Dengan Bobot” (hasil kemiripan semua section section_dfdiberikan bobot persentase berdasarkan ). Hasil disimpan dalam result_df_w2vDataFrame , dan lima resume teratas untuk setiap posisi ditampilkan berdasarkan kemiripan “Tanpa Bobot” dan “Dengan Bobot”. Implementasi kode program tertera pada Kode Program 5.10.
Kode Program 5.10 Implementasi kode program Word2Vec dan Cosine Similarity

# 1 start_time = time.time() # Catat waktu mulai 2 3 # List untuk menyimpan hasil 4 final_results_w2v = [] 5 6 # Iterasi untuk setiap vacancy 7 for vac_idx, vac_row in tqdm(vacancy_df_1.iterrows(), total=len(vacancy_df_1), desc="Processing Vacancies"): 8     position = vac_row['Position'] 9     vacancy_category = vac_row['Category'] 10     job_vec_w2v = np.array([vac_row['W2V_Vector']])  # Vektor vacancy dalam bentuk 2D untuk cosine_similarity 11 12     # Ambil bobot section sesuai kategori dan ubah ke skala desimal 13     category_weights = (section_df[section_df["Category"] == vacancy_category] 14                        .set_index("Section")["Bobot"] 15                        .div(100)
129
Kode Program 5.10 Implementasi kode program Word2Vec dan Cosine Similarity (lanjutan)
16                        .to_dict()) 17 18     # Iterasi untuk setiap resume 19     for resume_id in resume_df_1['ID'].unique(): 20         resume_sections = resume_df_1[resume_df_1['ID'] == resume_id] 21         similarity_scores = {} 22 23         # Hitung similarity untuk setiap section 24         for _, section_row in resume_sections.iterrows(): 25             section_name = section_row['Section'] 26             section_vector = np.array([section_row['W2V_Vector']])  # Vektor section dalam bentuk 2D 27 28             # Hitung cosine similarity antara section dan vacancy 29             sim_score = cosine_similarity(section_vector, job_vec_w2v)[0][0] 30             similarity_scores[section_name] = sim_score 31 32         # Versi 1: Tanpa bobot (rata-rata similarity semua section) 33         sim_no_weight = sum(similarity_scores.values()) / len(similarity_scores) if similarity_scores else 0 34 35         # Versi 2: Dengan bobot (weighted sum tanpa normalisasi ketat) 36         weighted_sum_v2 = 0 37         total_weight_v2 = 0 38         for section in similarity_scores: 39             sim = similarity_scores.get(section, 0) 40             weight = category_weights.get(section, 0) 41             weighted_sum_v2 += sim * weight 42             total_weight_v2 += weight 43         sim_with_weight = weighted_sum_v2 / total_weight_v2 if total_weight_v2 > 0 else 0 44 45         # Simpan hasil 46         final_results_w2v.append({ 47             'Resume_ID': resume_id, 48             'Position': position, 49             'Similarity_No_Weight': sim_no_weight, 50             'Similarity_With_Weight': sim_with_weight, 51         }) 52 53 # Catat waktu selesai dan hitung durasi 54 end_time = time.time() 55 total_time = end_time - start_time 56 57 # Konversi waktu ke format yang lebih mudah dibaca 58 minutes = int(total_time // 60) 59 seconds = int(total_time % 60) 60 61 # Konversi hasil ke DataFrame 62 result_df_w2v = pd.DataFrame(final_results_w2v) 63 64 # Tampilkan waktu total 65 print(f"Total waktu pemrosesan: {minutes} menit {seconds} detik") 66
130
Kode Program 5.10 Implementasi kode program Word2Vec dan Cosine Similarity (lanjutan)

# 67 print("Similaritas Tanpa Bobot Section") 68 69 top5_per_position_no_weight = result_df_w2v.groupby('Position', group_keys=False).apply( 70     lambda x: x.nlargest(5, 'Similarity_No_Weight') 71 ) 72 73 grouped_no_weight = top5_per_position_no_weight.groupby('Position') 74 for position, group in grouped_no_weight: 75     print(f"\nPosition: {position}") 76     print(group[['Resume_ID', 'Similarity_No_Weight']]) 77 78 print("Similaritas Dengan Bobot Section") 79 80 top5_per_position_with_weight = result_df_w2v.groupby('Position', group_keys=False).apply( 81     lambda x: x.nlargest(5, 'Similarity_With_Weight') 82 ) 83 84 grouped_with_weight = top5_per_position_with_weight.groupby('Position') 85 for position, group in grouped_with_weight: 86     print(f"\nPosition: {position}") 87     print(group[['Resume_ID', 'Similarity_With_Weight']])
Penjelasan dari Kode Program 5.10 mengenai implementasi perhitungan similaritas antara resume dan kualifikasi lowongan kerja dengan Cosine Similarity (CosSim) jika menggunakan vektor Word2Vec, yaitu:
1.Baris 1 merupakan proses untuk mencatat waktu mulai eksekusi time.time()menggunakan  dan menyimpannya ke variabel start_time. 2.Baris 3-4 merupakan proses untuk membuat list kosong final_results_w2v untuk menyimpan hasil perhitungan kemiripan (similarity) antara resume dan kualifikasi lowongan kerja. 3.Baris 6-7 merupakan proses untuk memulai iterasi melalui setiap baris di vacancy_df_1iterrows()DataFrame  menggunakan  dengan tqdmprogress bar dari  untuk menampilkan kemajuan pemrosesan. Position 4.Baris 8 merupakan proses untuk mengambil nilai kolom  dari baris kualifikasi lowongan kerja terkini dan menyimpannya ke variabel position. Category 5.Baris 9 merupakan pengambilan nilai kolom  dari baris lowongan kerja pada iterasi terkini dan menyimpannya ke variabel vacancy_category. 6.Baris 10 merupakan pengambilan vektor Word2Vec dari kolom W2V_Vector pada baris kualifikasi lowongan kerja di iterasi terkini dan job_vec_w2vmenyimpannya ke variabel .
131
section_df 7.Baris 12-16 merupakan proses untuk memfilter DataFrame vacancy_categorySectionberdasarkan , menetapkan kolom Bobotsebagai indeks, mengambil kolom , membaginya dengan 100 div(100)menggunakan  untuk mengubah ke skala desimal (karena bobot dalam persentase), dan mengonversinya menjadi dictionary to_dict()menggunakan , lalu menyimpannya ke variabel category_weights sebagai persentase bobot per section untuk kualifikasi lowongan kerja pada iterasi terkini sesuai industrinya. 8.Baris 18-19 merupakan proses untuk memulai iterasi melalui setiap nilai IDresume_df_1unik di kolom  pada DataFrame  menggunakan unique(). resume_df_1 9.Baris 20 merupakan proses untuk memfilter DataFrame IDuntuk mendapatkan semua baris dengan kolom  yang sesuai dengan resume_iditerasi  terkini dan menyimpannya ke variabel resume_sections. 10.Baris 21 merupakan pembuatan dictionary kosong similarity_scores untuk menyimpan skor kemiripan setiap section dalam resume. 11.Baris 23-24 merupakan proses untuk memulai iterasi melalui setiap baris resume_sectionsiterrows()di  menggunakan  untuk memproses setiap section dalam resume. Section 12.Baris 25 merupakan proses untuk mengambil nilai kolom  dari section_namebaris section terkini dan menyimpannya ke variabel . 13.Baris 26 merupakan proses untuk mengambil vektor Word2Vec dari kolom W2V_Vector pada baris section saat ini dan menyimpannya ke variabel section_vector. 14.Baris 28-29 merupakan proses untuk menghitung kemiripan antara vektor section_vectorsection pada resume () dan vektor kualifikasi vac_vectorlowongan kerja () menggunakan fungsi cosine_similarity dari library Scikit-learn, lalu menyimpan hasilnya sim_scoreke variabel . 15.Baris 30 merupakan proses untuk menyimpan skor kemiripan sim_scoresimilarity_scores ke dictionary . 16.Baris 32-33 merupakan proses untuk menguji skenario “Tanpa Bobot” dengan menghitung rata-rata kemiripan dengan menjumlahkan semua similarity_scoressum()skor kemiripan di  menggunakan  dan len()membaginya dengan jumlah section menggunakan , atau mengembalikan 0 jika dictionary kosong, lalu menyimpan hasilnya ke sim_no_weightvariabel . 17.Baris 35-43 merupakan proses untuk menguji skenario “Dengan Bobot”, weighted_sum_v2dimana baris 36-37 menginisialisasi variabel  dan total_weight_v2 dengan nilai 0 untuk menghitung jumlah kemiripan terbobot dan total bobot.
132
18.Baris 38-42 merupakan proses untuk mengiterasi setiap section di similarity_scores, mengambil skor kemiripan yang disimpan pada simvariabel , mendapatkan bobot section dari variabel category_weightsget() dengan default 0 menggunakan , mengalikan skor “Dengan Bobot” untuk menambah ke weighted_sum_v2total_weight_v2, dan menambah bobot ke . 19.Baris 43 merupakan proses untuk menghitung total similarity pada weighted_sum_v2skenario “Dengan Bobot” dengan membagi  dengan total_weight_v2total_weight_v2 jika  lebih dari 0 atau mengembalikan nilai 0 jika tidak. Kemudian, menyimpan hasilnya ke sim_with_weightvariabel . resume_id 20.Baris 45-46 merupakan proses untuk menambahkan data , positionsim_no_weightsim_with_weight, , dan  ke list final_results_w2vappend() menggunakan . 21.Baris 53-55 merupakan proses untuk mencatat waktu selesai time.time()menggunakan , menghitung durasi dengan mengurangkan start_timeend_time dari , dan menyimpan hasilnya ke variabel total_time. total_time 22.Baris 57-59 merupakan proses untuk mengonversi  ke menit minutessecondsdan detik, lalu menyimpannya ke variabel  dan . 23.Baris 61-62 merupakan proses untuk membuat DataFrame result_df_w2vfinal_results_w2v dari list  menggunakan pd.DataFrame()Resume_IDPosition, dengan kolom , , Similarity_No_WeightSimilarity_With_Weight, dan . 24.Baris 64-65 merupakan proses untuk mencetak total waktu pemrosesan print()dalam format menit dan detik menggunakan . 25.Baris 67 merupakan proses untuk mencetak judul "Similaritas Tanpa Bobot print()Section" menggunakan . 26.Baris 69-71 merupakan proses untuk mengelompokkan DataFrame result_df_w2vPosition berdasarkan kolom  menggunakan groupby(), lalu memilih 5 baris dengan nilai Similarity_No_Weight tertinggi untuk setiap posisi menggunakan nlargest(), dan menyimpan hasilnya ke variabel top5_per_position_no_weight. 27.Baris 73-76 merupakan proses untuk mengelompokkan top5_per_position_no_weightPosition berdasarkan kolom , Positionmengiterasi setiap kualifikasi lowongan kerja (), mencetak Resume_IDnama posisi, mencetak nilai kolom , serta mencetak nilai Similarity_No_Weight untuk setiap kualifikasi lowongan kerja. 28.Baris 78 merupakan proses untuk mencetak judul "Similaritas Dengan print()Bobot Section" menggunakan .
133
29.Baris 80-82 merupakan proses untuk mengelompokkan DataFrame result_df_w2vPosition berdasarkan kolom  menggunakan groupby(), lalu memilih 5 baris dengan nilai Similarity_With_Weight tertinggi untuk setiap posisi nlargest()menggunakan , dan menyimpan hasilnya ke variabel top5_per_position_with_weight. 30.Baris 84-87 merupakan proses untuk mengelompokkan top5_per_position_with_weightPosition berdasarkan , Positionmengiterasi setiap kualifikasi lowongan kerja (), mencetak Resume_IDnama posisi, mencetak kolom , serta Similarity_With_Weight untuk setiap kualifikasi lowongan kerja.
5.6.4Implementasi Kode Program Word2Vec dan Improved Sqrt- Cosine Similarity
Dalam kode program ini, dilakukan kemiripan antara resume dan kualifikasi lowongan kerja menggunakan metrik Improved Sqrt-Cosine (ISC) Similarity untuk vektor Word2Vec, dengan dua skenario, yakni “Tanpa Bobot” (hasil kemiripan semua section dirata-ratakan) dan “Dengan Bobot” (hasil kemiripan semua section section_dfdiberikan bobot persentase berdasarkan ). Hasil disimpan dalam result_df_w2v_iscDataFrame , dan lima resume teratas untuk setiap posisi ditampilkan berdasarkan kemiripan “Tanpa Bobot” dan ‘Dengan Bobot”. Implementasi kode program tertera pada Kode Program 5.11.
Kode Program 5.11 Implementasi kode program Word2Vec dan Improved Sqrt- Cosine Similarity

# 1 start_time = time.time()  # Catat waktu mulai 2 3 # List untuk menyimpan hasil 4 final_results_w2v_isc = [] 5 6 # Iterasi untuk setiap vacancy 7 for vac_idx, vac_row in tqdm(vacancy_df_1.iterrows(), total=len(vacancy_df_1), desc="Processing Vacancies"): 8     position = vac_row['Position'] 9     vacancy_category = vac_row['Category'] 10     job_vec_w2v = vac_row['W2V_Vector']  # Vektor vacancy dalam bentuk 1D 11 12     # Ambil bobot section sesuai kategori dan ubah ke skala desimal 13     category_weights = (section_df[section_df["Category"] == vacancy_category] 14                        .set_index("Section")["Bobot"] 15                        .div(100) 16                        .to_dict()) 17 18     # Iterasi untuk setiap resume 19     for resume_id in resume_df_1['ID'].unique(): 20         resume_sections = resume_df_1[resume_df_1['ID'] == resume_id] 21         similarity_scores = {} 22 23         # Hitung similarity untuk setiap section
134
Kode Program 5.11 Implementasi kode program Word2Vec dan Improved Sqrt- Cosine Similarity (lanjutan)

# 24 for _, section_row in resume_sections.iterrows(): 25             section_name = section_row['Section'] 26             section_vector = section_row['W2V_Vector']  # Vektor section dalam bentuk 1D 27 28             # Hitung improved sqrt-cosine similarity antara section dan vacancy 29             sim_score = improved_sqrt_cosine_similarity(section_vector, job_vec_w2v) 30             similarity_scores[section_name] = sim_score 31 32         # Versi 1: Tanpa bobot (rata-rata similarity semua section) 33         sim_no_weight = sum(similarity_scores.values()) / len(similarity_scores) if similarity_scores else 0 34 35         # Versi 2: Dengan bobot (weighted sum tanpa normalisasi ketat) 36         weighted_sum_v2 = 0 37         total_weight_v2 = 0 38         for section in similarity_scores: 39             sim = similarity_scores.get(section, 0) 40             weight = category_weights.get(section, 0) 41             weighted_sum_v2 += sim * weight 42             total_weight_v2 += weight 43         sim_with_weight = weighted_sum_v2 / total_weight_v2 if total_weight_v2 > 0 else 0 44 45         # Simpan hasil 46         final_results_w2v_isc.append({ 47             'Resume_ID': resume_id, 48             'Position': position, 49             'Similarity_No_Weight': sim_no_weight, 50             'Similarity_With_Weight': sim_with_weight, 51         }) 52 53 # Catat waktu selesai dan hitung durasi 54 end_time = time.time() 55 total_time = end_time - start_time 56 57 # Konversi waktu ke format yang lebih mudah dibaca 58 minutes = int(total_time // 60) 59 seconds = int(total_time % 60) 60 61 # Konversi hasil ke DataFrame 62 result_df_w2v_isc = pd.DataFrame(final_results_w2v_isc) 63 64 # Tampilkan waktu total 65 print(f"Total waktu pemrosesan: {minutes} menit {seconds} detik") 66 67 print("Similaritas Tanpa Bobot Section") 68 69 top5_per_position_no_weight = result_df_w2v_isc.groupby('Position', group_keys=False).apply( 70     lambda x: x.nlargest(5, 'Similarity_No_Weight') 71 ) 72 73 grouped_no_weight = top5_per_position_no_weight.groupby('Position') 74 for position, group in grouped_no_weight:
135
Kode Program 5.11 Implementasi kode program Word2Vec dan Improved Sqrt- Cosine Similarity (lanjutan)

# 75 print(f"\nPosition: {position}") 76     print(group[['Resume_ID', 'Similarity_No_Weight']]) 77 78 print("Similaritas Dengan Bobot Section") 79 80 top5_per_position_with_weight = result_df_w2v_isc.groupby('Position', group_keys=False).apply( 81     lambda x: x.nlargest(5, 'Similarity_With_Weight') 82 ) 83 84 grouped_with_weight = top5_per_position_with_weight.groupby('Position') 85 for position, group in grouped_with_weight: 86     print(f"\nPosition: {position}") 87     print(group[['Resume_ID', 'Similarity_With_Weight']])
Penjelasan dari Kode Program 5.11 mengenai implementasi perhitungan similaritas antara resume dan kualifikasi lowongan kerja dengan Improved Sqrt- Cosine (ISC) Similarity jika menggunakan vektor Word2Vec, yaitu:
1.Baris 1 merupakan proses untuk mencatat waktu mulai eksekusi time.time()menggunakan  dan menyimpannya ke variabel start_time. 2.Baris 3-4 merupakan proses untuk membuat list kosong final_results_w2v_isc untuk menyimpan hasil perhitungan kemiripan (similarity) antara resume dan kualifikasi lowongan kerja. 3.Baris 6-7 merupakan proses untuk memulai iterasi melalui setiap baris di vacancy_df_1iterrows()DataFrame  menggunakan  dengan tqdmprogress bar dari  untuk menampilkan kemajuan pemrosesan. Position 4.Baris 8 merupakan proses untuk mengambil nilai kolom  dari baris kualifikasi lowongan kerja terkini dan menyimpannya ke variabel position. Category 5.Baris 9 merupakan pengambilan nilai kolom  dari baris lowongan kerja pada iterasi terkini dan menyimpannya ke variabel vacancy_category. 6.Baris 10 merupakan pengambilan vektor Word2Vec dari kolom W2V_Vector pada baris kualifikasi lowongan kerja di iterasi terkini dan job_vec_w2vmenyimpannya ke variabel . section_df 7.Baris 12-16 merupakan proses untuk memfilter DataFrame vacancy_categorySectionberdasarkan , menetapkan kolom Bobotsebagai indeks, mengambil kolom , membaginya dengan 100 div(100)menggunakan  untuk mengubah ke skala desimal (karena bobot dalam persentase), dan mengonversinya menjadi dictionary to_dict()menggunakan , lalu menyimpannya ke variabel category_weights sebagai persentase bobot per section untuk kualifikasi lowongan kerja pada iterasi terkini sesuai industrinya.
136
8.Baris 18-19 merupakan proses untuk memulai iterasi melalui setiap nilai IDresume_df_1unik di kolom  pada DataFrame  menggunakan unique(). resume_df_1 9.Baris 20 merupakan proses untuk memfilter DataFrame IDuntuk mendapatkan semua baris dengan kolom  yang sesuai dengan resume_iditerasi  terkini dan menyimpannya ke variabel resume_sections. 10.Baris 21 merupakan pembuatan dictionary kosong similarity_scores untuk menyimpan skor kemiripan setiap section dalam resume. 11.Baris 23-24 merupakan proses untuk memulai iterasi melalui setiap baris resume_sectionsiterrows()di  menggunakan  untuk memproses setiap section dalam resume. Section 12.Baris 25 merupakan proses untuk mengambil nilai kolom  dari section_namebaris section terkini dan menyimpannya ke variabel . 13.Baris 26 merupakan proses untuk mengambil vektor Word2Vec dari kolom W2V_Vector pada baris section saat ini dan menyimpannya ke variabel section_vector. 14.Baris 28-29 merupakan proses untuk menghitung kemiripan antara vektor section_vectorsection pada resume () dan vektor kualifikasi vac_vectorlowongan kerja () menggunakan fungsi cosine_similarity dari library Scikit-learn, lalu menyimpan hasilnya sim_scoreke variabel . 15.Baris 30 merupakan proses untuk menyimpan skor kemiripan sim_scoresimilarity_scores ke dictionary . 16.Baris 32-33 merupakan proses untuk menguji skenario “Tanpa Bobot” dengan menghitung rata-rata kemiripan dengan menjumlahkan semua similarity_scoressum()skor kemiripan di  menggunakan  dan len()membaginya dengan jumlah section menggunakan , atau mengembalikan 0 jika dictionary kosong, lalu menyimpan hasilnya ke sim_no_weightvariabel . 17.Baris 35-43 merupakan proses untuk menguji skenario “Dengan Bobot”, weighted_sum_v2dimana baris 36-37 menginisialisasi variabel  dan total_weight_v2 dengan nilai 0 untuk menghitung jumlah kemiripan terbobot dan total bobot. 18.Baris 38-42 merupakan proses untuk mengiterasi setiap section di similarity_scores, mengambil skor kemiripan yang disimpan pada simvariabel , mendapatkan bobot section dari variabel category_weightsget() dengan default 0 menggunakan , mengalikan skor “Dengan Bobot” untuk menambah ke weighted_sum_v2total_weight_v2, dan menambah bobot ke .
137
19.Baris 43 merupakan proses untuk menghitung total similarity pada weighted_sum_v2skenario “Dengan Bobot” dengan membagi  dengan total_weight_v2total_weight_v2 jika  lebih dari 0 atau mengembalikan nilai 0 jika tidak. Kemudian, menyimpan hasilnya ke sim_with_weightvariabel . resume_id 20.Baris 45-46 merupakan proses untuk menambahkan data , positionsim_no_weightsim_with_weight, , dan  ke list final_results_w2v_iscappend() menggunakan . 21.Baris 53-55 merupakan proses untuk mencatat waktu selesai time.time()menggunakan , menghitung durasi dengan mengurangkan start_timeend_time dari , dan menyimpan hasilnya ke variabel total_time. total_time 22.Baris 57-59 merupakan proses untuk mengonversi  ke menit minutessecondsdan detik, lalu menyimpannya ke variabel  dan . 23.Baris 61-62 merupakan proses untuk membuat DataFrame result_df_w2v_iscfinal_results_w2v_isc dari list pd.DataFrame()Resume_IDmenggunakan , dengan kolom , PositionSimilarity_No_Weight, , dan Similarity_With_Weight. 24.Baris 64-65 merupakan proses untuk mencetak total waktu pemrosesan print()dalam format menit dan detik menggunakan . 25.Baris 67 merupakan proses untuk mencetak judul "Similaritas Tanpa Bobot print()Section" menggunakan . 26.Baris 69-71 merupakan proses untuk mengelompokkan DataFrame result_df_w2v_iscPosition berdasarkan kolom  menggunakan groupby(), lalu memilih 5 baris dengan nilai Similarity_No_Weight tertinggi untuk setiap posisi menggunakan nlargest(), dan menyimpan hasilnya ke variabel top5_per_position_no_weight. 27.Baris 73-76 merupakan proses untuk mengelompokkan top5_per_position_no_weightPosition berdasarkan kolom , Positionmengiterasi setiap kualifikasi lowongan kerja (), mencetak Resume_IDnama posisi, mencetak nilai kolom , serta mencetak nilai Similarity_No_Weight untuk setiap kualifikasi lowongan kerja. 28.Baris 78 merupakan proses untuk mencetak judul "Similaritas Dengan print()Bobot Section" menggunakan . 29.Baris 80-82 merupakan proses untuk mengelompokkan DataFrame result_df_w2v_iscPosition berdasarkan kolom  menggunakan groupby(), lalu memilih 5 baris dengan nilai Similarity_With_Weight tertinggi untuk setiap posisi nlargest()menggunakan , dan menyimpan hasilnya ke variabel top5_per_position_with_weight.
138
30.Baris 84-87 merupakan proses untuk mengelompokkan top5_per_position_with_weightPosition berdasarkan , Positionmengiterasi setiap kualifikasi lowongan kerja (), mencetak Resume_IDnama posisi, mencetak kolom , serta Similarity_With_Weight untuk setiap kualifikasi lowongan kerja.
5.7Implementasi Kode Program Pengujian
5.7.1Implementasi Kode Program Perhitungan SRCC
Dalam kode program ini, dilakukan pemuatan enam DataFrame dengan format CSV yang berisi peringkat resume dengan dan “Tanpa Bobot” untuk metode TF- IDF dengan Improved Sqrt-Cosine (ISC) Similarity, Word2Vec dengan Cosine calculate_srccSimilarity (CosSim), dan Word2Vec dengan ISC. Fungsi menghitung Spearman Rank Correlation Coefficient (SRCC) untuk membandingkan peringkat hasil implementasi metode dengan peringkat pakar per posisi. Hasil merged_dfPositionSRCC digabungkan ke dalam DataFrame  dengan kolom styled_dfsebagai indeks dan divisualisasikan melalui DataFrame  dengan pewarnaan berdasarkan nilai SRCC, ditandai dengan warna hijau jika nilai SRCC Positionpada suatu kualifikasi lowongan kerja () bernilai di atas ambang batas dan ditandai dengan warna merah jika nilai SRCC di bawah ambang batas. Implementasi kode program tertera pada Kode Program 5.12.
Kode Program 5.12 Implementasi kode program perhitungan Spearman Rank Correlation Coefficient
1 # Input DataFrame 2 result_df_bobot_tfidf = pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu me2-23\rank_df_bobot_tfidf.csv') 3 result_df_bobot_w2v = pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu me2-23\rank_df_bobot_w2v.csv') 4 result_df_bobot_w2v_isc = pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu me2-23\rank_df_bobot_w2v_isc.csv') 5 6 result_df_tanpa_bobot_tfidf = pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu me2-23\rank_df_tanpa_bobot_tfidf.csv') 7 result_df_tanpa_bobot_w2v = pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu me2-23\rank_df_tanpa_bobot_w2v.csv') 8 result_df_tanpa_bobot_w2v_isc = pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu me2-23\rank_df_tanpa_bobot_w2v_isc.csv') 9 10 result_df_bobot_tfidf = result_df_bobot_tfidf.drop(columns=["Link_Gdrive"]) 11 result_df_bobot_w2v = result_df_bobot_w2v.drop(columns=["Link_Gdrive"]) 12 result_df_bobot_w2v_isc = result_df_bobot_w2v_isc.drop(columns=["Link_Gdrive"]) 13 14 result_df_tanpa_bobot_tfidf = result_df_tanpa_bobot_tfidf.drop(columns=["Link_Gdrive"])
139
Kode Program 5.12 Implementasi kode program perhitungan Spearman Rank Correlation Coefficient (lanjutan)

# 15 result_df_tanpa_bobot_w2v = result_df_tanpa_bobot_w2v.drop(columns=["Link_Gdrive"]) 16 result_df_tanpa_bobot_w2v_isc = result_df_tanpa_bobot_w2v_isc.drop(columns=["Link_Gdrive"]) 17 18 # Korelasi Ranking SRCC 19 def calculate_srcc(df): 20     df['d_i'] = df['Rank'] - df['Rank_Expert'] # Selisih peringkat (d_i) 21 22     df['d_i_squared'] = df['d_i'] ** 2 # Kuadrat selisih peringkat (d_i^2) 23 24     sum_d_i_squared = df['d_i_squared'].sum() # Total kuadrat selisih peringkat (∑ d_i^2) 25 26     n = len(df) 27 28     # Hitung SRCC 29     if n < 2 or n * (n**2 - 1) == 0: # Mengatasi pembagian dengan 0 30         return None 31     srcc = 1 - ((6 * sum_d_i_squared) / (n * (n**2 - 1))) 32 33     return srcc 34 35 def calculate_srcc_per_position(df): 36     results = {} 37     for position, group in df.groupby('Position'): # Hitung SRCC berdasarkan 'Position' 38         srcc = calculate_srcc(group) 39         if srcc is not None: 40             results[position] = srcc 41     return results 42 43 # Implementasi Fungsi SRCC 44 srcc_bobot_tfidf = calculate_srcc_per_position(result_df_bobot_tfidf) 45 srcc_bobot_w2v = calculate_srcc_per_position(result_df_bobot_w2v) 46 srcc_bobot_w2v_isc = calculate_srcc_per_position(result_df_bobot_w2v_isc) 47 48 srcc_tanpa_bobot_tfidf = calculate_srcc_per_position(result_df_tanpa_bobot_tfidf) 49 srcc_tanpa_bobot_w2v = calculate_srcc_per_position(result_df_tanpa_bobot_w2v) 50 srcc_tanpa_bobot_w2v_isc = calculate_srcc_per_position(result_df_tanpa_bobot_w2v_isc) 51 52 # Merge semua df ke satu df 53 df_bobot_tfidf = pd.DataFrame(list(srcc_bobot_tfidf.items()), columns=['Position', 'TFIDF_Bobot']) 54 df_bobot_w2v = pd.DataFrame(list(srcc_bobot_w2v.items()), columns=['Position', 'W2V_Bobot']) 55 df_bobot_w2v_isc = pd.DataFrame(list(srcc_bobot_w2v_isc.items()), columns=['Position', 'W2V_ISC_Bobot']) 56 df_tanpa_bobot_tfidf = pd.DataFrame(list(srcc_tanpa_bobot_tfidf.items()), columns=['Position', 'TFIDF_Tanpa_Bobot'])
140
Kode Program 5.12 Implementasi kode program perhitungan Spearman Rank Correlation Coefficient (lanjutan)

# 57 df_tanpa_bobot_w2v = pd.DataFrame(list(srcc_tanpa_bobot_w2v.items()), columns=['Position', 'W2V_Tanpa_Bobot']) 58 df_tanpa_bobot_w2v_isc = pd.DataFrame(list(srcc_tanpa_bobot_w2v_isc.items()), columns=['Position', 'W2V_ISC_Tanpa_Bobot']) 59 60 # Jadikan 'Position' sebagai index 61 merged_df = df_bobot_tfidf.set_index('Position') 62 merged_df = merged_df.join(df_bobot_w2v.set_index('Position'), how='outer') 63 merged_df = merged_df.join(df_bobot_w2v_isc.set_index('Position'), how='outer') 64 merged_df = merged_df.join(df_tanpa_bobot_tfidf.set_index('Position'), how='outer') 65 merged_df = merged_df.join(df_tanpa_bobot_w2v.set_index('Position'), how='outer') 66 merged_df = merged_df.join(df_tanpa_bobot_w2v_isc.set_index('Position'), how='outer') 67 68 # Pemberian warna untuk visualisasi 69 def color_srcc(val): 70     if pd.isna(val):  # Jika ada NaN 71         return '' 72     if val >= 0,6:  # Kuat (hijau) 73         return 'background-color: lightgreen' 74     else:  # Lemah (merah) 75         return 'background-color: lightcoral' 76 77 styled_df = merged_df.style.format("{:.16f}").applymap(color_srcc) 78 styled_df
Penjelasan dari Kode Program 5.12 mengenai implementasi kode program pengujian bagian perhitungan Spearman Rank Correlation Coefficient (SRCC), yaitu:
1.Baris 2 merupakan proses untuk menginput file dengan format CSV result_df_bobot_tfidfrank_df_bobot_tfidf ke dalam DataFrame pd.read_csv()menggunakan . 2.Baris 3 merupakan proses untuk menginput file dengan format CSV result_df_bobot_w2vrank_df_bobot_w2v ke dalam DataFrame pd.read_csv()menggunakan . 3.Baris 4 merupakan proses untuk menginput file dengan format CSV rank_df_bobot_w2v_isc ke dalam DataFrame result_df_bobot_w2v_iscpd.read_csv() menggunakan .
141
4.Baris 6 merupakan proses untuk menginput file dengan format CSV rank_df_tanpa_bobot_tfidf ke dalam DataFrame result_df_tanpa_bobot_tfidf menggunakan pd.read_csv(). 5.Baris 7 merupakan proses untuk menginput file dengan format CSV rank_df_tanpa_bobot_w2v ke dalam DataFrame result_df_tanpa_bobot_w2vpd.read_csv() menggunakan . 6.Baris 8 merupakan proses untuk menginput file dengan format CSV rank_df_tanpa_bobot_w2v_isc ke dalam DataFrame result_df_tanpa_bobot_w2v_isc menggunakan pd.read_csv(). Link_Gdrive 7.Baris 10-16 merupakan proses untuk menghapus kolom dari enam DataFrame yang sudah diinput. 8.Baris 18-19 merupakan proses untuk mendefinisikan fungsi calculate_srccdf yang menerima DataFrame . Rank 9.Baris 20 merupakan proses untuk menghitung selisih antara kolom Rank_Expertd_idan  yang disimpan pada kolom baru . d_i 10.Baris 22 merupakan proses untuk menghitung kuadrat dari kolom d_i_squaredyang disimpan ke kolom baru . 11.Baris 24 merupakan proses untuk menjumlahkan semua nilai di kolom d_i_squaredsum() menggunakan  dan disimpan ke variabel sum_d_i_squared. 12.Baris 26 merupakan proses untuk menghitung jumlah baris di DataFrame dflen()n menggunakan  dan menyimpannya ke variabel . n 13.Baris 28-30 merupakan proses untuk memeriksa apakah  kurang dari 2 n * (n**2 - 1)atau penyebut yang merupakan rumus SRCC () sama Nonedengan 0  lalu mengembalikan  jika kondisi terpenuhi (true) untuk menghindari pembagian dengan nol. 14.Baris 31 merupakan proses untuk menghitung Spearman Rank Correlation 1 - (6 * Coefficient (SRCC) menggunakan persamaan sum_d_i_squared) / (n * (n**2 - 1)) dan disimpan ke srccvariabel . srcc 15.Baris 33 merupakan proses untuk mengembalikan nilai  sebagai hasil calculate_srccdari fungsi . 16.Baris 35-36 merupakan proses untuk mendefinisikan fungsi calculate_srcc_per_position dan pembuatan dictionary kosong results untuk menyimpan nilai hasil perhitungan SRCC setiap kualifikasi lowongan kerja. df 17.Baris 37-40 mengelompokkan DataFrame  berdasarkan kolom Position, lalu menghitung SRCC untuk setiap kualifikasi lowongan kerja Positioncalculate_srcc() dengan memanggil fungsi  dan disimpan resultshasil-hasilnya ke dictionary  jika fungsi tersebut tidak Nonemengembalikan .
142
18.Baris 41 merupakan proses untuk mengembalikan isian dictionary results yang merupakan nilai-nilai SRCC per kualifikasi lowongan kerja calculate_srcc_per_positionsebagai hasil dari fungsi . 19.Baris 43-50 merupakan proses untuk menghitung SRCC per kualifikasi lowongan kerja pada enam DataFrame, yaitu: result_df_bobot_tfidf a.Hasil SRCC  disimpan ke variabel srcc_bobot_tfidf, result_df_bobot_w2v b.Hasil SRCC  disimpan ke variabel srcc_bobot_w2v, result_df_bobot_w2v_isc c.Hasil SRCC  disimpan ke variabel srcc_bobot_w2v_isc, result_df_tanpa_bobot_tfidf d.Hasil SRCC  disimpan ke srcc_tanpa_bobot_tfidfvariabel , result_df_tanpa_bobot_w2v e.Hasil SRCC  disimpan ke srcc_tanpa_bobot_w2vvariabel , result_df_tanpa_bobot_w2v_isc f.Hasil SRCC  disimpan ke srcc_tanpa_bobot_w2v_iscvariabel . 20.Baris 52-58 merupakan proses untuk membuat DataFrame menggunakan pd.DataFrame() dari masing-masing hasil enam perhitungan SRCC per posisi yang disimpan menjadi: df_bobot_tfidfsrcc_bobot_tfidf a. dari dictionary PositionTFIDF_Bobotdengan kolom  dan , df_bobot_w2vsrcc_bobot_w2v b. dari dictionary  dengan PositionW2V_Bobotkolom  dan , df_bobot_w2v_iscsrcc_bobot_w2v_isc c. dari dictionary PositionW2V_ISC_Bobotdengan kolom  dan , df_tanpa_bobot_tfidf d. dari dictionary srcc_tanpa_bobot_tfidfPosition dengan kolom  dan TFIDF_Tanpa_Bobot, df_tanpa_bobot_w2v e. dari dictionary srcc_tanpa_bobot_w2vPosition dengan kolom  dan W2V_Tanpa_Bobot, df_tanpa_bobot_w2v_isc f. dari dictionary srcc_tanpa_bobot_w2v_iscPosition dengan kolom  dan W2V_ISC_Tanpa_Bobot. Position 21.Baris 60-66 merupakan proses mengatur kolom  sebagai indeks dan menggabungkan enam DataFrame untuk dijadikan satu menggunakan df.join()merged_df dan disimpan ke DataFrame . color_srcc 22.Baris 68-75 merupakan proses untuk mendefinisikan fungsi yang memberikan warna pada isian nilai di DataFrame berdasarkan nilai SRCC, di mana jika kosong atau NaN, maka tidak diberi warna; jika lebih dari sama dengan 0,6, maka diberi warna hijau; dan jika kurang dari 0,6, maka diberi warna merah.
143
merged_df 23.Baris 77 merupakan proses untuk memformat DataFrame style.format("{:.16f}")menggunakan  dan menerapkan fungsi color_srccapplymap() untuk pemberian warna menggunakan . styled_dfKemudian, disimpan pada DataFrame baru dengan variabel . styled_df 24.Baris 78 merupakan proses untuk menampilkan DataFrame .
5.7.2Implementasi Kode Program Perhitungan Relevansi dan Senioritas
Dalam kode program ini, dilakukan perhitungan persentase relevansi dan Positionsenioritas per kualifikasi lowongan kerja () untuk enam DataFrame dengan dan “Tanpa Bobot” untuk metode TF-IDF dengan Improved Sqrt-Cosine (ISC) Similarity, Word2Vec dengan Cosine Similarity (CosSim), dan Word2Vec dengan ISC menggunakan fungsi calculate_relevance_seniority_per_position. Tampilan hasilnya dibuat menjadi dua DataFrame agar lebih mudah dalam segi pembacaan, yakni df_relevancedf_seniority untuk relevansi dan  untuk senioritas. Kedua DataFrame tersebut divisualisasikan dengan pewarnaan berdasarkan nilai persentase, ditandai dengan warna hijau jika persentase pada suatu kualifikasi Positionlowongan kerja () bernilai di atas ambang batas dan ditandai dengan warna merah jika persentase di bawah ambang batas. Implementasi kode program tertera pada Kode Program 5.13.
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan senioritas
1 # Menghitung persentase Relevansi dan Senioritas per posisi 2 def calculate_relevance_seniority_per_position(df): 3     results = {} 4         for position, group in df.groupby('Position'): 5         total_resumes = len(group) 6 7         # Hitung jumlah TRUE untuk Relevansi dan Senioritas 8         relevance_count = (group['Relevance'] == True).sum() 9         seniority_count = (group['Seniority'] == True).sum() 10 11         # Hitung persentase 12         relevance_percent = (relevance_count / total_resumes) * 13 100 seniority_percent = (seniority_count / total_resumes) * 14 100
15         # Simpan hasil 16         results[position] = {'Relevance': relevance_percent, 'Seniority': seniority_percent} 17 18     return results 19 20 # Implementasi Fungsi Relevansi dan Senioritas 21 relevance_seniority_bobot_tfidf = calculate_relevance_seniority_per_position(result_df_bobot_tfid f) 22 relevance_seniority_bobot_w2v = calculate_relevance_seniority_per_position(result_df_bobot_w2v)
144
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan senioritas (lanjutan)

# 23 relevance_seniority_bobot_w2v_isc = calculate_relevance_seniority_per_position(result_df_bobot_w2v_ isc) 24 relevance_seniority_tanpa_bobot_tfidf = calculate_relevance_seniority_per_position(result_df_tanpa_bobo t_tfidf) 25 relevance_seniority_tanpa_bobot_w2v = calculate_relevance_seniority_per_position(result_df_tanpa_bobo t_w2v) 26 relevance_seniority_tanpa_bobot_w2v_isc = calculate_relevance_seniority_per_position(result_df_tanpa_bobo t_w2v_isc) 27 28 # Membedakan DataFrames untuk Relevansi dan Senioritas 29 df_relevance_bobot_tfidf = pd.DataFrame( 30     [(pos, val['Relevance']) for pos, val in relevance_seniority_bobot_tfidf.items()], 31     columns=['Position', 'TFIDF_Bobot'] 32 ) 33 df_relevance_bobot_w2v = pd.DataFrame( 34     [(pos, val['Relevance']) for pos, val in relevance_seniority_bobot_w2v.items()], 35     columns=['Position', 'W2V_Bobot'] 36 ) 37 df_relevance_bobot_w2v_isc = pd.DataFrame( 38     [(pos, val['Relevance']) for pos, val in relevance_seniority_bobot_w2v_isc.items()], 39     columns=['Position', 'W2V_ISC_Bobot'] 40 ) 41 df_relevance_tanpa_bobot_tfidf = pd.DataFrame( 42     [(pos, val['Relevance']) for pos, val in relevance_seniority_tanpa_bobot_tfidf.items()], 43     columns=['Position', 'TFIDF_Tanpa_Bobot'] 44 ) 45 df_relevance_tanpa_bobot_w2v = pd.DataFrame( 46     [(pos, val['Relevance']) for pos, val in relevance_seniority_tanpa_bobot_w2v.items()], 47     columns=['Position', 'W2V_Tanpa_Bobot'] 48 ) 49 df_relevance_tanpa_bobot_w2v_isc = pd.DataFrame( 50     [(pos, val['Relevance']) for pos, val in relevance_seniority_tanpa_bobot_w2v_isc.items()], 51     columns=['Position', 'W2V_ISC_Tanpa_Bobot'] 52 ) 53 54 df_seniority_bobot_tfidf = pd.DataFrame( 55     [(pos, val['Seniority']) for pos, val in relevance_seniority_bobot_tfidf.items()], 56     columns=['Position', 'TFIDF_Bobot'] 57 ) 58 df_seniority_bobot_w2v = pd.DataFrame( 59     [(pos, val['Seniority']) for pos, val in relevance_seniority_bobot_w2v.items()], 60     columns=['Position', 'W2V_Bobot'] 61 ) 62 df_seniority_bobot_w2v_isc = pd.DataFrame( 63     [(pos, val['Seniority']) for pos, val in relevance_seniority_bobot_w2v_isc.items()], 64     columns=['Position', 'W2V_ISC_Bobot'] 65 )
145
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan senioritas (lanjutan)

# 66 df_seniority_tanpa_bobot_tfidf = pd.DataFrame( 67     [(pos, val['Seniority']) for pos, val in relevance_seniority_tanpa_bobot_tfidf.items()], 68     columns=['Position', 'TFIDF_Tanpa_Bobot'] 69 ) 70 df_seniority_tanpa_bobot_w2v = pd.DataFrame( 71     [(pos, val['Seniority']) for pos, val in relevance_seniority_tanpa_bobot_w2v.items()], 72     columns=['Position', 'W2V_Tanpa_Bobot'] 73 ) 74 df_seniority_tanpa_bobot_w2v_isc = pd.DataFrame( 75     [(pos, val['Seniority']) for pos, val in relevance_seniority_tanpa_bobot_w2v_isc.items()], 76     columns=['Position', 'W2V_ISC_Tanpa_Bobot'] 77 ) 78 79 merged_relevance_df = df_relevance_bobot_tfidf.set_index('Position') 80 merged_relevance_df = merged_relevance_df.join(df_relevance_bobot_w2v.set_index('Posi tion'), how='outer') 81 merged_relevance_df = merged_relevance_df.join(df_relevance_bobot_w2v_isc.set_index(' Position'), how='outer') 82 merged_relevance_df = merged_relevance_df.join(df_relevance_tanpa_bobot_tfidf.set_ind ex('Position'), how='outer') 83 merged_relevance_df = merged_relevance_df.join(df_relevance_tanpa_bobot_w2v.set_index ('Position'), how='outer') 84 merged_relevance_df = merged_relevance_df.join(df_relevance_tanpa_bobot_w2v_isc.set_i ndex('Position'), how='outer') 85 86 merged_seniority_df = df_seniority_bobot_tfidf.set_index('Position') 87 merged_seniority_df = merged_seniority_df.join(df_seniority_bobot_w2v.set_index('Posi tion'), how='outer') 88 merged_seniority_df = merged_seniority_df.join(df_seniority_bobot_w2v_isc.set_index(' Position'), how='outer') 89 merged_seniority_df = merged_seniority_df.join(df_seniority_tanpa_bobot_tfidf.set_ind ex('Position'), how='outer') 90 merged_seniority_df = merged_seniority_df.join(df_seniority_tanpa_bobot_w2v.set_index ('Position'), how='outer') 91 merged_seniority_df = merged_seniority_df.join(df_seniority_tanpa_bobot_w2v_isc.set_i ndex('Position'), how='outer') 92 93 # Pemberian warna untuk visualisasi 94 def color_percentage(val): 95     if pd.isna(val): # Jika ada NaN 96         return '' 97     if val >= 60: # Kuat (hijau) 98         return 'background-color: lightgreen' 99     else: # Lemah (merah) 100         return 'background-color: lightcoral' 101
146
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan senioritas (lanjutan)

# 102 styled_relevance_df = merged_relevance_df.style.format("{:.2f}%").applymap(color_perc entage) 103 styled_seniority_df = merged_seniority_df.style.format("{:.2f}%").applymap(color_perc entage) 104 105 styled_relevance_df 106 107 styled_seniority_df
Penjelasan dari Kode Program 5.13 mengenai implementasi kode program pengujian bagian perhitungan relevansi dan senioritas, yaitu:
1.Baris 1-3 merupakan proses untuk mendefinisikan fungsi calculate_relevance_seniority_per_position yang dfresultsmenerima DataFrame  dan membuat dictionary kosong untuk menyimpan hasil perhitungan persentase relevansi dan senioritas. df 2.Baris 5 merupakan proses untuk mengelompokkan DataFrame Positionberdasarkan kolom  dan memulai iterasi untuk setiap Positionkualifikasi lowongan kerja (). 3.Baris 6 merupakan proses untuk menghitung jumlah resume yang ada di kualifikasi lowongan kerjalen()dalam  menggunakan  dan total_resumesmenyimpannya ke variabel . True 4.Baris 8-9 merupakan proses untuk menghitung jumlah nilai  di kolom Relevance(group['Relevance'] ==  menggunakan True).sum()Seniority dan di kolom  menggunakan (group['Seniority'] == True).sum(). Kemudian, disimpan ke relevance_countseniority_countvariabel  dan . 5.Baris 12-14 merupakan proses untuk menghitung persentase relevansi relevance_counttotal_resumesdengan membagi  dengan  dan mengalikan dengan 100 agar hasilnya dalam bentuk persen, lalu disimpan relevance_percentke variabel . Hal yang sama dilakukan pada perhitungan persentase senioritas dengan membagi seniority_counttotal_resumes dengan  dan mengalikan dengan seniority_percent100  lalu disimpan ke variabel . position 6.Baris 15-18 merupakan proses untuk menambahkan nilai , relevance_percentseniority_percent, dan  ke dictionary results. Kemudian, dikonversi menjadi DataFrame menggunakan pd.DataFrame().
147
7.Baris 20-26 merupakan proses untuk menghitung persentase relevansi dan senioritas per kualifikasi lowongan kerja pada enam DataFrame, yaitu: a.Hasil perhitungan relevansi dan senioritas result_df_bobot_tfidf disimpan ke variabel relevance_seniority_bobot_tfidf, b.Hasil perhitungan relevansi dan senioritas result_df_bobot_w2v disimpan ke variabel relevance_seniority_bobot_w2v, c.Hasil perhitungan relevansi dan senioritas result_df_bobot_w2v_isc disimpan ke variabel relevance_seniority_bobot_w2v_isc, d.Hasil perhitungan relevansi dan senioritas result_df_tanpa_bobot_tfidf disimpan ke variabel relevance_seniority_tanpa_bobot_tfidf, e.Hasil perhitungan relevansi dan senioritas result_df_tanpa_bobot_w2v disimpan ke variabel relevance_seniority_tanpa_bobot_w2v, f.Hasil perhitungan relevansi dan senioritas result_df_tanpa_bobot_w2v_isc disimpan ke variabel relevance_seniority_tanpa_bobot_w2v_isc. 8.Baris 28-52 merupakan proses untuk membuat enam DataFrame terpisah, yakni menyimpan masing-masing data relevansi dari setiap hasil result_dfPositionperhitungan  dengan kolom , serta kolom nama pendekatan dan skenario yang digunakan. 9.Baris 54-77 merupakan proses untuk membuat enam DataFrame terpisah, yakni menyimpan masing-masing data senioritas dari setiap hasil result_dfPositionperhitungan  dengan kolom , serta kolom nama pendekatan dan skenario yang digunakan. Position 10.Baris 79-84 merupakan proses mengatur kolom  sebagai indeks dan mengabungkan enam DataFrame hasil data relevansi menggunakan df.join()merged_relevance_df dan disimpan ke DataFrame . Position 11.Baris 86-91 merupakan proses mengatur kolom  sebagai indeks dan mengabungkan enam DataFrame hasil data senioritas menggunakan df.join()merged_relevance_df dan disimpan ke DataFrame . 12.Baris 93-100 merupakan proses untuk mendefinisikan fungsi color_percentage yang memberikan warna pada isian nilai di DataFrame berdasarkan persentanse relevansi atau senioritas, di mana jika kosong atau NaN, maka tidak diberi warna; jika lebih dari sama dengan 60 maka diberi warna hijau; dan jika kurang dari 60  maka diberi warna merah. 13.Baris 102 merupakan proses untuk memformat DataFrame relevance_dfstyle.format("{:.2f}%") menggunakan  dan color_percentagemenerapkan fungsi  untuk pemberian warna applymap()menggunakan . Kemudian, disimpan pada DataFrame baru styled_relevance_dfdengan variabel .
148
14.Baris 103 merupakan proses untuk memformat DataFrame seniority_dfstyle.format("{:.2f}%") menggunakan  dan color_percentagemenerapkan fungsi  untuk pemberian warna applymap()menggunakan . Kemudian, disimpan hasilnya ke variabel styled_seniority_df. 15.Baris 105 merupakan proses untuk menampilkan DataFrame styled_relevance_df. 16.Baris 107 merupakan proses untuk menampilkan DataFrame styled_seniority_df.
149

# BAB 6PENGUJIAN DAN ANALISIS HASIL
Pemaparan hasil dari pengujian akan dijelaskan di bab pengujian, serta pembahasan dan analisa dari hasil pengujian tersebut sebagai bahan evaluasi.
6.1Pengujian
Penelitian ini menggunakan dua pendekatan perhitungan representasi teks, yakni TF-IDF dan Word2Vec. Untuk pendekatan perhitungan similaritasnya dibuat menjadi tiga kombinasi pendekatan, yakni TF-IDF dengan Improved Sqrt-Cosine (ISC) Similarity, Word2Vec dengan Cosine Similarity (CosSim), dan Word2Vec dengan ISC. Masing-masing pendekatan diuji dengan dua skenario. Skenario pertama adalah lima resume dengan skor similaritas terbesar jika tanpa menggunakan pembobotan per section dari ahli dan skenario kedua adalah lima resume dengan skor similaritas terbesar jika menggunakan pembobotan per section dari ahli. Dalam masing-masing kombinasi pendekatan dan skenario terdapat tiga parameter penilaian untuk ahli memberikan ground truth berdasarkan hasil keluaran implementasi dan skenario, yakni peringkat (rank), relevansi, dan senioritas, dengan fokus utama pada parameter peringkat. Parameter relevansi dan senioritas berperan sebagai pendukung untuk memperkaya evaluasi. Implementasi metode atau pendekatan menghasilkan skor similaritas antara setiap resume dengan masing-masing kualifikasi lowongan kerja. Untuk setiap kualifikasi lowongan kerja, dipilih lima resume dengan skor similaritas tertinggi. Kelima resume tersebut selanjutnya dievaluasi oleh ahli berdasarkan tiga parameter, yakni: (1) urutan peringkat yang dianggap paling sesuai (ground truth), (2) relevansi isi resume terhadap kualifikasi lowongan kerja, dan (3) kesesuaian level posisi resume dengan level posisi yang diminta dalam kualifikasi.
Lima peringkat teratas hasil keluaran dari implementasi metode dipindahkan ke dalam spreadsheet saat disajikan kepada ahli untuk memudahkan proses evaluasi. Cuplikan template penyajian tersebut tertera pada Gambar 6.1 dan Gambar 6.2
Gambar 6.1 Cuplikan template spreadsheet evaluasi ahli
150
Gambar 6.2 Cuplikan template spreadsheet evaluasi ahli
Hasil evaluasi dari ahli dihimpun dan dirapikan agar bisa dijadikan DataFrame untuk perhitungan ketiga parameter penilaian seperti pada Gambar 6.3
Gambar 6.3 Cuplikan spreadsheet hasil evaluasi ahli
151
Parameter peringkat (rank) dievaluasi hasil pengujiannya dengan menghitung Spearman Rank Correlation Coefficient (SRCC) untuk menunjukkan korelasi antara peringkat yang dihasilkan implementasi metode dengan peringkat yang dibenarkan (ground truth) oleh ahli. Semakin tinggi nilai korelasi, maka semakin baik metode tersebut mengurutkan similaritas yang sesuai dengan pandangan ahli (manusia). Pada penelitian ini, dilakukan deskripsi statistik melalui SPSS untuk mengetahui persentil dari keseluruhan nilai korelasi seperti tertera pada Gambar 6.4 dan diketahui persentil ke-75 adalah korelasi positif 0,6. Nilai 0,6 ini menunjukkan bahwa 75% dari data lainnya memiliki nilai yang lebih rendah. Oleh karena itu, nilai ≥ 0,6 ditentukan sebagai ambang batas parameter korelasi.
Gambar 6.4 Hasil descriptive statistics SPSS
Sebagai parameter pendukung, relevansi dan senioritas pada penelitian ini dianggap baik jika setidaknya tiga dari lima resume memenuhi deskripsi kualifikasi lowongan kerja berdasarkan evaluasi ahli. Sehingga, nilai persentase ≥ 60% ditentukan sebagai ambang batas parameter relevansi dan senioritas.
152
Dari 24 kualifikasi lowongan kerja pada penelitian ini, SRCC dengan nilai ≥ 0,6 dianggap kuat (strong) yang ditandai dengan warna hijau. Sedangkan SRCC dengan nilai < 0,6 dianggap lemah (weak) yang ditandai dengan warna merah. Gambar 6.5 merupakan visualisasi dari nilai korelasi setiap kombinasi pendekatan berdasarkan posisi kualifikasi lowongan kerja.
Gambar 6.5 Visualisasi nilai korelasi
153
Parameter relevansi (relevance) dievaluasi hasil pengujiannya dengan menghitung persentasenya untuk menunjukkan seberapa relevan resume-resume yang menjadi keluaran implementasi metode dengan kualifikasi lowongan kerja. Semakin tinggi persentasenya menunjukkan performa yang lebih baik dalam konteks relevansi. Dari 24 kualifikasi lowongan kerja pada penelitian ini, persentase dengan nilai ≥ 60% dianggap memiliki kesesuaian yang tinggi (high) dan ditandai dengan warna hijau. Sedangkan persentase dengan nilai < 60% dianggap memiliki kesesuaian yang kurang (low) dan ditandai dengan warna merah. Gambar 6.6 merupakan visualisasi dari nilai persentase relevansi setiap kombinasi pendekatan berdasarkan posisi kualifikasi lowongan kerja.
Gambar 6.6 Visualisasi persentase relevansi
154
Parameter senioritas (seniority) dievaluasi hasil pengujiannya dengan menghitung persentasenya untuk menunjukkan seberapa sesuai level posisi yang tercantum di resume-resume yang menjadi keluaran implementasi metode dengan level posisi yang dibutuhkan pada kualifikasi lowongan kerja. Semakin tinggi persentasenya menunjukkan tingkat kesesuaian yang lebih baik. Dari 24 kualifikasi lowongan kerja pada penelitian ini, persentase dengan nilai ≥ 60% dianggap memiliki kesesuaian level posisi yang tinggi (high) dan ditandai dengan warna hijau. Sedangkan persentase dengan nilai < 60% dianggap memiliki kesesuaian level posisi yang rendah (low) dan ditandai dengan warna merah. Gambar 6.7 merupakan visualisasi dari nilai persentase senioritas setiap kombinasi pendekatan berdasarkan posisi kualifikasi lowongan kerja.
Gambar 6.7 Visualisasi persentase senioritas
155
6.2Analisis Hasil
Metode Improved Sqrt-Cosine (ISC) Similarity pada penelitian ini digunakan untuk memeringkat lima resume berdasarkan skor similaritas tertinggi untuk masing-masing 24 kualifikasi lowongan kerja. Perhitungan similaritas ISC memungkinkan implementasi pada representasi teks TF-IDF yang berbasis frekuensi. Namun, untuk yang berbasis semantik menggunakan Word2Vec, vektor harus diambil nilai absolutnya karena vektor hasil Word2Vec dapat mengandung bilangan negatif. Sedangkan, rumus ISC melibatkan operasi akar kuadrat yang tidak dapat diterapkan langsung pada bilangan negatif. Oleh karena itu, Kombinasi pendekatan Word2Vec dengan Cosine Similarity juga digunakan untuk mempertahankan makna semantik asli dari vektor Word2Vec tanpa modifikasi nilai absolut.
Performa masing-masing pendekatan dievaluasi melalui tiga parameter, yakni Spearman Rank Correlation Coefficient (SRCC) untuk mengukur korelasi dengan pemeringkatan dari hasil evaluasi ahli, relevansi untuk menilai kesesuaian resume dengan kualifikasi lowongan kerja, dan senioritas untuk mengevaluasi kesesuaian level posisi berdasarkan kata-kata kunci. Pengujian dilakukan dalam dua skenario, yakni “Tanpa Bobot” dan “Dengan Bobot”, di mana bobot per section (misalnya, Summary 5%, Experience 20%, Certification 15%) mencerminkan prioritas penilaian seorang rekruter.
Berdasarkan hasil pengujian dengan skenario “Tanpa Bobot”, jumlah kualifikasi lowongan kerja yang memenuhi ambang batas (SRCC ≥ 0,6; relevansi ≥ 60%; senioritas ≥ 60%; ditandai hijau pada visualisasi) dan yang tidak memenuhi ambang batas (ditandai merah) pada Tabel 6.1 dan Tabel 6.2.
Tabel 6.1 Hasil pengujian berwarna hijau skenario tanpa bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC CosSim
Jumlah yang nilai 5 7 8 SRCC ≥ 0,6
Jumlah yang 15 9 11 persentase Relevansi ≥ 60%
Jumlah yang 14 10 16 persentase Senioritas ≥ 60%
156
Tabel 6.2 Hasil pengujian berwarna merah skenario tanpa bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC CosSim
Jumlah yang nilai 19 17 16 SRCC < 0,6
Jumlah yang 9 15 13 persentase Relevansi < 60%
Jumlah yang 10 14 8 persentase SenioritasS < 60%
Pada parameter korelasi, pendekatan Word2Vec dengan ISC unggul menempati urutan tertinggi berjumlah 8 kualifikasi lowongan kerja yang memenuhi ambang batas, diikuti oleh Word2Vec dengan CosSim berjumlah 7, dan TF-IDF dengan ISC di urutan terakhir berjumlah 5. Ini menunjukkan hasil pemeringkatan yang dihasilkan implementasi metode Word2Vec dengan ISC lebih dekat dengan penilaian ahli.
Pada parameter relevansi, pendekatan TF-IDF dengan ISC unggul dengan 15 kualifikasi lowongan kerja, disusul pendekatan Word2Vec dengan ISC berjumlah 11, dan Word2Vec dengan CosSim yang berada di urutan terakhir berjumlah 9. Ini menunjukkan isi dari lima resume keluaran implementasi metode TF-IDF dengan ISC lebih banyak yang sesuai dengan deskripsi kualifikasi lowongan kerja.
Sementara itu, dalam hal senioritas, pendekatan Word2Vec dengan ISC kembali unggul di urutan pertama dengan 16 kualifikasi lowongan kerja, diikuti oleh pendekatan TF-IDF dengan ISC berjumlah 14, dan Word2Vec dengan CosSim berjumlah 10. Ini menunjukkan isi dari lima resume keluaran implementasi Word2Vec dengan ISC lebih banyak yang level senioritasnya atau level posisinya yang sesuai dengan deskripsi kualifikasi lowongan kerja.
157
Berdasarkan hasil pengujian dengan skenario “Dengan Bobot”, jumlah kualifikasi lowongan kerja yang memenuhi ambang batas (SRCC ≥ 0,6; relevansi ≥ 60%; senioritas ≥ 60%; ditandai hijau pada visualisasi) dan yang tidak memenuhi ambang batas (ditandai merah).
Tabel 6.3 Hasil pengujian berwarna hijau skenario dengan bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC CosSim
Jumlah yang nilai 6 9 4 SRCC ≥ 0,6
Jumlah yang 13 10 11 persentase Relevansi ≥ 60%
Jumlah yang 10 14 16 persentase Senioritas ≥ 60%
Tabel 6.4 Hasil pengujian berwarna merah skenario dengan bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC CosSim
Jumlah yang nilai 18 15 20 SRCC < 0,6
Jumlah yang 11 14 13 persentase Relevansi < 60%
Jumlah yang 14 10 8 persentase Senioritas < 60%
Pada parameter korelasi, pendekatan Word2Vec dengan CosSim unggul menempati urutan tertinggi dengan jumlah 9 kualifikasi, diikuti oleh TF-IDF dengan ISC berjumlah 6, dan Word2Vec dengan ISC di urutan terakhir berjumlah 4. Ini menunjukkan hasil pemeringkatan yang dihasilkan implementasi metode Word2Vec dengan CosSim lebih dekat dengan penilaian ahli.
Pada parameter relevansi, pendekatan TF-IDF dengan ISC unggul dengan jumlah 13 kualifikasi, disusul pendekatan Word2Vec dengan ISC berjumlah 11, dan Word2Vec dengan CosSim yang berada di urutan terakhir berjumlah 10. Ini menunjukkan isi dari lima resume keluaran implementasi metode TF-IDF dengan ISC lebih banyak yang sesuai dengan deskripsi kualifikasi lowongan kerja.
158
Sementara itu, dalam hal senioritas, pendekatan Word2Vec dengan ISC unggul di urutan pertama dengan jumlah 16 kualifikasi, diikuti oleh pendekatan Word2Vec dengan CosSim berjumlah 14, dan TF-IDF dengan ISC berjumlah 10. Ini menunjukkan isi dari lima resume keluaran implementasi metode Word2Vec dengan ISC lebih banyak yang sesuai dengan deskripsi kualifikasi lowongan kerja.
Secara jumlah kualifikasi lowongan kerja yang memenuhi dan yang tidak memenuhi ambang batas pada Tabel 6.1 hingga Tabel 6.4, dihitung menggunakan weighted scoring, di mana jumlah yang di atas ambang batas diberikan poin +2. Sedangkan, jumlah yang di bawah ambang batas diberikan poin -1. Hasil perhitungan weighted score untuk setiap pendekatan dan skenario tertera pada Tabel 6.5.
Tabel 6.5 Weighted score keseluruhan pendekatan dan skenario

## Pendekatan Korelasi Relevansi Senioritas Weighted Score
()()()4×214×213×2TF-IDF + ISC 30 ()()()+20×−1+10×−1+11×−1Tanpa Bobot =(−12)=18=15
()()()7×29×210×2Word2Vec + 6 ()()()+17×−1+15×−1+14×−1CosSim Tanpa =(−3)=3=6   Bobot
()()()8×211×216×2Word2Vec + 33 ()()()+16×−1+13×−1+8×−1ISC Tanpa =0=9=24   Bobot
()()()5×212×210×2TF-IDF + ISC 15 ()()()+19×−1+12×−1+14×−1Dengan Bobot =−9=12=6
()()()9×210×214×2Word2Vec + 27 ()()()+15×−1+14×−1+10×−1CosSim =3=6=18   Dengan Bobot
()()()4×211×216×2Word2Vec + 21 ()()()+20×−1+13×−1+8×−1ISC Dengan =(−12)=9=24   Bobot
Dari Tabel 6.5, diurutkan berdasarkan weighted score tertinggi untuk masing- masing skenario seperti pada Tabel 6.6.
Tabel 6.6 Urutan pendekatan berdasarkan weighted score tertinggi

## Tanpa Bobot Dengan Bobot
Word2Vec + ISC (33) Word2Vec + CosSim (27)
TF-IDF + ISC (30) Word2Vec + ISC (21)
Word2Vec + CosSim (6) TF-IDF + ISC (15)
159
Secara rata-rata, dihitung untuk setiap parameter pada masing-masing kombinasi pendekatan dan skenario yang tertera hasilnya pada Tabel 6.7.
Tabel 6.7 Perhitungan rata-rata parameter setiap pendekatan dan skenario

## Pendekatan Korelasi Relevansi Senioritas
TF-IDF + ISC Tanpa 0,004348 58,33% 55,83% Bobot
Word2Vec + 0,079167 39,17% 49,17% CosSim Tanpa Bobot
Word2Vec + ISC 0,269565 45,83% 56,67% Tanpa Bobot
TF-IDF + ISC 0,113636 55,83% 50,0% Dengan Bobot
Word2Vec + 0,183333 42,5% 50,0% CosSim Dengan Bobot Word2Vec + ISC 0,077083 40,83% 56,67% Dengan Bobot
Terlihat bahwa Word2Vec dengan ISC unggul pada skenario “Tanpa Bobot” dengan nilai korelasi rata-rata 0,269565. Namun, nilai tersebut tergolong sebagai korelasi yang lemah. Di skenario “Dengan Bobot”, Word2Vec dengan CosSim unggul dengan nilai korelasi rata-rata 0,183333 yang tergolong sebagai korelasi sangat lemah.
Dalam skenario “Tanpa Bobot” maupun “Dengan Bobot”, pendekatan ISC dengan representasi teks TF-IDF menunjukkan performa terbaik pada parameter relevansi, mengungguli Word2Vec dengan ISC dan Word2Vec dengan CosSim. Hal ini menunjukkan bahwa ISC dengan TF-IDF lebih baik dalam mengidentifikasi isi resume yang relevan dengan kualifikasi lowongan kerja berdasarkan kesesuaian kualifikasi lowongan kerja. Keunggulan TF-IDF dengan ISC pada relevansi disebabkan oleh kemampuan TF-IDF dalam memberi bobot lebih tinggi pada kata- kata penting yang jarang muncul, tetapi relevan dengan kualifikasi lowongan kerja, seperti istilah-istilah teknis.
160
Pendekatan Word2Vec dengan ISC menunjukkan keterbatasan akibat distorsi semantik dari penyesuaian nilai absolut, seperti terlihat dari visualisasi yang menunjukkan pergeseran posisi kata pada Gambar 6.8.
Gambar 6.8 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli dengan vektor nilai absolut
Lebih rincinya, dilakukan perhitungan similaritas antar term menggunakan CosSim dengan hasil tertera pada Tabel 6.8.
Tabel 6.8 Perhitungan similaritas antar term Word2Vec vektor nilai asli dengan vektor nilai absolut
Term 1 versus Similaritas (Nilai Similaritas (Nilai Perubahan Term 2 Asli) Absolut)
technology versus 0,5711 0,7413 0,1701 engineering
technology versus 0,2471 0,7262 0,4791 fashion
design versus 0,6348 0,8274 0,1927 designer
software versus 0,4153 0,6950 0,2797 java
marketing versus 0,4816 0,6899  0,2083 sales
university versus 0,0751 0,6303 0,5552 cook
pastry versus cook 0,6423 0,7609 0,1185
pastry versus 0,2151 0,7557 0,5406 economy
bake versus 0,2106 0,6603 0,4497 diploma
law versus style 0,0141 0,7308 0,7167
161
Tabel 6.8 menunjukkan peningkatan atau penurunan nilai similaritas antar term, misalnya antara “technology” dengan “fashion” seharusnya kedua term ini secara semantik berjauhan dan dibuktikan dengan similaritasnya yang bernilai 0,2471. Namun, setelah nilai vektor dibuat absolut, nilai similaritasnya menjadi 0,7262 yang menyatakan kedua term ini berdekatan secara semantik, perubahannya cukup drastis sebanyak 0,4791. Kemudian, ada juga term yang sudah berdekatan secara semantik menjadi semakin dekat setelah nilainya dibuat absolut, seperti “design” dan “designer” dari similaritasnya bernilai 0,6348 menjadi 0,8274 yang menyatakan posisi kedua term ini menjadi semakin dekat. Visualisasi dari beberapa pasangan term yang dibandingkan pada Tabel 6.5 diilustrasikan pada Gambar 6.9.
Gambar 6.9 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli dengan vektor nilai absolut
Oleh karena itu, Word2Vec dengan ISC unggul dalam skenario “Tanpa Bobot” disebabkan oleh kemampuan representasi semantik Word2Vec yang masih cukup mampu menangkap hubungan antar kata kunci yang relevan, meskipun distorsi terjadi.
Keunggulan Word2Vec dengan CosSim dalam skenario “Dengan Bobot” menunjukkan bahwa pendekatan ini paling selaras dengan pandangan manusia karena CosSim menjaga hubungan semantik asli vektor Word2Vec tanpa distorsi akibat penyesuaian nilai absolut, dan bobot per section memungkinkan penyesuaian skor sesuai prioritas rekruter, seperti penekanan pada pengalaman kerja. Namun, perlu dicatat bahwa bobot per section di penelitian ini hanya didasarkan pada satu ahli yang mungkin tidak mencerminkan variasi preferensi rekruter dari berbagai industri atau budaya instansi terkait. Pemberian bobot dengan melibatkan lebih banyak ahli akan meningkatkan hasil secara general.
Melihat lebih dekat setiap kualifikasi lowongan kerja, ketiga parameter dibuat grafik garis, dengan parameter korelasi diwarnai biru, parameter relevansi diwarnai hijau, dan paremeter senioritas diwarnai merah. Sumbu Y menunjukkan nilai, sehingga nilai persentase relevansi dan senioritas dijadikan bilangan desimal. Sumbu X menunjukkan pendekatan dan skenario yang digunakan. Grafik untuk beberapa kualifikasi lowongan kerja tertera pada Gambar 6.10.
162
Gambar 6.10 Grafik garis tiga parameter setiap kualifikasi lowongan kerja
Nilai korelasi pada lowongan kerja posisi “Executive Chef” memiliki nilai tertinggi 0,5 dan terlihat jauh di bawah nilai relevansi dan senioritasnya. Nilai korelasi tertinggi tersebut tergolong sedang. Sementara itu, nilai korelasi lainnya bernilai negatif dan tergolong sebagai korelasi sangat lemah. Hal ini menunjukkan walaupun korelasi antara hasil implementasi dengan hasil evaluasi ahli tergolong lemah, keluaran resume yang dihasilkan untuk posisi ini tetap sesuai dengan deskripsi kualifikasi lowongan kerja berdasarkan kesesuaian kata kunci atau istilah-istilah tertentu yang dimiliki resume maupun pada kebutuhan posisi.
Nilai korelasi pada posisi “Medical Doctor” cukup stabil dengan rata-rata 0,2833 di antara berbagai implementasi pendekatan dan skenario, meskipun tergolong sebagai korelasi lemah. Namun, nilai relevansi menunjukkan 0 yang menandakan tidak ada resume yang isiannya sesuai dengan kebutuhan posisi tersebut. Hal ini menunjukkan perlu adanya penyesuaian dataset resume dengan menambahkan resume yang mencakup beragam spesialisasi dalam industri healthcare atau sebaliknya dengan memperkaya dataset kualifikasi lowongan kerja di industri healthcare yang lebih variatif spesialisasinya.
Nilai korelasi pada posisi “Unmanaged Merchant Engagement Senior Associate, BPO Field Sales” tergolong korelasi sedang ke korelasi kuat berdasarkan nilai rata-rata 0,5667 dan nilai tertinggi 0,7. Namun, untuk nilai senioritasnya memiliki rata-rata 0,3667 atau sekitar 36%. Hal ini menunjukkan kurang mampunya hasil implementasi dalam mengenali kesuaian level senioritas dengan yang dibutuhkan pada posisi tersebut. Sehingga, perlu adanya penyesuaian dataset resume maupun kualifikasi lowongan kerja yang lebih beragam level senioritasnya atau pengelompokkan terpisah berdasarkan level senioritas berdasarkan years of experience di dalam resume.
163
Nilai korelasi pada posisi “HR Specialist” tergolong korelasi sedang ke korelasi kuat berdasarkan nilai rata-rata 0,5333 dan nilai tertinggi 0,8. Namun, untuk nilai relevansinya memiliki rata-rata 0,3667 atau sekitar 36%. Hal ini menunjukkan kurang mampunya hasil implementasi dalam mengenali kesesuaian kata kunci atau istilah dengan yang dibutuhkan pada posisi tersebut. Sehingga, perlu adanya penyesuaian dataset resume maupun kualifikasi lowongan kerja yang memperbanyak kata-kata penting seperti kata kunci atau istilah teknis sesuai industri atau bidang minat.
164

# BAB 7PENUTUP
Pada bab penutup, bagian kesimpulan merangkum hasil penelitian untuk menjawab rumusan masalah. Sedangkan, bagian saran memberikan masukan untuk perbaikan dan pengembangan penelitian selanjutnya.
7.1Kesimpulan
Berikut merupakan kesimpulan dari penelitian ini untuk menjawab rumusan masalah.
1.Hasil pemeringkatan lima resume menggunakan Improved Sqrt-Cosine (ISC) Similarity dalam mengkalkulasikan similaritas teks resume dengan kualifikasi lowongan kerja menunjukkan bahwa pendekatan representasi teks menggunakan Word2Vec lebih unggul dibandingkan dengan TF-IDF untuk skenario “Tanpa Bobot”. Meskipun terdapat distorsi akibat penyesuaian nilai absolut, mengingat adanya term yang jarak posisinya sudah dekat dan menjadi semakin dekat, Word2Vec cukup mampu menangkap hubungan semantik kata kunci. Pada skenario “Dengan Bobot”, pendekatan perhitungan similaritas menggunakan Cosine Similarity (CosSim) dengan representasi teks Word2Vec lebih unggul. Namun, dalam penggunaan ISC, representasi teks Word2Vec tetap unggul dibandingkan TF-IDF. Keunggulan Word2Vec dengan CosSim menunjukkan bahwa pendekatan ini paling selaras dengan pandangan manusia karena CosSim menjaga hubungan semantik asli vektor Word2Vec tanpa distorsi akibat penyesuaian nilai absolut dan memungkinan penyesuaian bobot per section sesuai prioritas seorang ahli dalam penelitian ini. 2.Korelasi peringkat antara hasil pemeringkatan dari ISC dengan penilaian ahli terhadap kesesuaian kualifikasi lowongan kerja menunjukkan keunggulan yang bervariasi berdasarkan representasi teks dan skenario, di mana pada skenario “Tanpa Bobot”, Word2Vec dengan ISC lebih unggul menghasilkan pemeringkatan lima resume yang sesuai dengan hasil evaluasi pemeringkatan ahli terhadap deskripsi lowongan kerja (SRCC > 0,6). Kemudian, pada skenario “Dengan Bobot”, Word2Vec dengan CosSim lebih unggul dalam menghasilkan pemeringkatan yang sesuai dengan evaluasi ahli. Walaupun begitu, Word2Vec dengan ISC pada skenario tanpa bobot section, memiliki nilai korelasi rata-rata 0,269565 yang dikategorikan sebagai korelasi lemah.  Pada skenario dengan bobot section, Word2Vec dengan CosSim memiliki nilai korelasi rata-rata 0,183333 yang dikategorikan sebagai korelasi sangat lemah.
165
7.2Saran
Berikut merupakan saran dari penelitian ini untuk penelitian berikutnya.
1.Pemberian bobot per section berdasarkan penilaian seorang ahli dapat menimbulkan bias, sehingga kurang mencerminkan variasi preferensi rekruter pada umumnya. Pada penelitian selanjutnya, disarankan untuk melibatkan lebih banyak ahli. 2.Meskipun implementasi Improved Sqrt-Cosine (ISC) Similarity dengan representasi teks Word2Vec unggul karena masih cukup mampu menangkap hubungan semantik kata kunci, tetap kurang disarankan karena mengaburkan hubungan semantik asli. Jika berpacu pada seberapa relevan isian resume dengan kualifikasi lowongan kerja, maka implementasi ISC dengan TF-IDF lebih disarankan untuk digunakan. 3.Jumlah kualifikasi lowongan kerja dengan parameter-parameter yang di atas ambang batas rata-rata lebih sedikit dibandingkan yang di bawah ambang batas. Oleh karena itu, penelitian selanjutnya disarankan mencantumkan kata-kata teknis spesifik terkait suatu posisi pada deskripsi kualifikasi lowongan kerja agar deskripsi yang digunakan tidak terlalu umum. 4.Penelitian ini berfokus pada peringkat sebagai parameter utama, parameter relevansi dan senioritas ditambahkan sebagai parameter pendukung. Untuk penelitian selanjutnya, disarankan menganalisa hubungan parameter peringkat dengan parameter relevansi dan senioritas. 5.Pemrosesan kata untuk mengelompokkan tingkat senioritas pada setiap resume menjadi entry level, junior level, dan management level dapat meningkatkan kesesuaian resume-resume dari keluaran implementasi metode dengan tingkat senioritas yang dibutuhkan sesuai deskripsi kualifikasi lowongan kerja. 6.Pemrosesan ekstraksi section pada penelitian ini memanfaatkan kolom Resume_html yang merupakan fitur asli dari dataset resume. Untuk penelitian selanjutnya, disarankan mengembangkan proses ekstraksi section tanpa memanfaatkan class dari struktur HTML. 7.Penyeragaman nama-nama section pada penelitian ini dilakukan secara manual. Untuk penelitian selanjutnya, disarankan mengembangkan proses penyeragaman nama-nama section secara semantik. 8.Penelitian ini hanya menggunakan dataset resume dan kualifikasi lowongan kerja dengan Bahasa Inggris. Untuk penelitian selanjutnya, disarankan mengembangkan dataset resume dan kualifikasi lowongan kerja dengan Bahasa Indonesia.
166

# DAFTAR REFERENSI
Abdusyukur, F., 2023. PENERAPAN ALGORITMA SUPPORT VECTOR MACHINE (SVM) UNTUK KLASIFIKASI PENCEMARAN NAMA BAIK DI MEDIA SOSIAL TWITTER. KOMPUTA : Jurnal Ilmiah Komputer dan Informatika, 12(1), pp. 73- 82.
Alsharef, A., Sonia, Nassour, H. & Sharma, J., 2023. Exploring the Efficiency of Text- Similarity Measures in Automated Resume Screening for Recruitment. New Delhi, India, IEEE, pp. 36-42.
Amin, M. D. et al., 2023. Real Time Data based Automated Resume Classification and Job Matching using SVC, Jaccard Index and Cosine Similarity. Roorkee, India, IEEE, pp. 1-6.
Ayuningtyas, P. & Tantyoko, H., 2024. Perbandingan Metode Word2vec Model Skipgram pada Ulasan Aplikasi Linkaja menggunakan Algoritma Bidirectional LSTM dan Support Vector Machine. JUSTIN (Jurnal Sistem dan Teknologi Informasi), 12(1), pp. 189-196.
Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi Republik Indonesia, 2016. KBBI VI Daring. [Online] Tersedia di: <https://kbbi.kemdikbud.go.id/entri/resume>
Bhawal, S., 2021. Kaggle. [Online] Tersedia di: <https://www.kaggle.com/datasets/snehaanbhawal/resume- dataset>
Cambridge University Press & Assessment, 2024. Meaning of curriculum vitae in English. [Online] Tersedia di: <https://dictionary.cambridge.org/dictionary/essential-british- english/curriculum-vitae>
Cholissodin, I. & Riyandani, E., 2018. Big Data vs Big Information vs Big Knowledge. Malang: Fakultas Ilmu Komputer Universitas Brawijaya.
Cowley, H. P. et al., 2022. A framework for rigorous evaluation of human performance in human and machine learning comparison studies. Scientific Reports, 12(5444).
Daryani, C. et al., 2020. AN AUTOMATED RESUME SCREENING SYSTEM USING NATURAL LANGUAGE PROCESSING AND SIMILARITY. Ethics and Information Technology (ETIT), 2(2), pp. 99-103.
Dewan Perwakilan Rakyat Republik Indonesia - Komisi IX, 2023. Tingkat Pengangguran Terbuka Masih Jauh di Atas Target RPJMN. [Online] Tersedia di: <https://www.dpr.go.id/berita/detail/id/47507/t/Tingkat%20Pengangguran %20Terbuka%20Masih%20Jauh%20di%20Atas%20Target%20RPJMN>
167
Dwivedi, A. & Anand, S. K., 2023. Word Embedding using Skip Gram Approach. Interdisciplinary Journal of Contemporary Research, 10(3), pp. 1-5.
Effendi, M. S., 2013. Desain Eksperimental dalam Penelitian Pendidikan. Jurnal Perspektif Pendidikan, 6(1), pp. 87-102.
Guritno, S., S. & Rahardja, U., 2011. Theory and Application of IT RESEARCH. Penerbit Andi.
He, Z., Dumdumaya, C. E. & Quimno, V. A., 2024. MEASUREMENT OF SEMANTIC TEXT SIMILARITY. Journal of Theoretical and Applied Information Technology, 102(5), pp. 1673-1685.
H. & H., 2024. SPEARMAN'S RANK CORRELATION ANALYSIS METHOD TO IDENTIFY CHANGES IN THE GPA OF GRADUATES FROM THE 5TH BATCH OF THE TEACHING CAMPUS PROGRAM AT UNIVERSITAS BAKTI INDONESIA. TRANSPUBLIKA INTERNATIONAL RESEARCH IN EXACT SCIENCES (TIRES), 30 8, 3(3), pp. 18-27.
International Monetary Fund, 2024. World Economic Outlook (April 2024) - Unemployment Rate. [Online] Tersedia di: <https://www.imf.org/external/datamapper/LUR@WEO/OEMDC/ADVEC/ WEOWORLD/DA>
Iskandar, D. & Kurniawan, A., 2025. ANALISIS PERBANDINGAN TEKNIK WORD2VEC DAN DOC2VECDALAM MENGUKUR KEMIRIPAN DOKUMEN MENGGUNAKAN COSINE SIMILARITY. Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK), 12(1), pp. 133-144.
Jawale, D. S. et al., 2024. COSINE SIMILARITY: A KEY DRIVER FOR ENHANCED RECOMMENDATION SYSTEMS. International Research Journal of Modernization in Engineering Technology and Science, 06(04), pp. 1466- 1470.
Kementerian Ketenagakerjaan RI - Badan Perencanaan dan Pengembangan Ketenagakerjaan, 2021. REVIEW RENCANA TENAGA KERJA NASIONAL 2020- 2024. [Online] Tersedia di: <https://satudata.kemnaker.go.id/satudata- public/2022/04/files/publikasi/1649938621648_Buku%2520Review%2520R TKN_2020_2024.pdf>
Kulshretha, S. & Lodha, L., 2023. Performance Evaluation of Word Embedding Algorithms. International Journal of Innovative Science and Research Technology, 8(12), pp. 1555-1561.
Kumaladewi, A. K., 2018. EFEKTIVITAS REKRUTMEN DAN SELEKSI DALAM MEMENUHI KEBUTUHAN TENAGA PERAWAT DI RSIA MUSLIMAT JOMBA. PARSIMONIA Jurnal Akuntansi, Manajemen, dan Bisnis, 11 4, 5(1), pp. 29-40.
Lailasari, N. A. et al., 2024. Pengaruh Pengangguran Terhadap Pertumbuhan Ekonomi. IJM: Indonesian Journal of Multidisciplinary, 2(5), pp. 275-286.
168
Musfiqon, 2016. Panduan Lengkap Metodologi Penelitian Pendidikan. PT. Prestasi Pustakaraya.
Meyer, D., 2016. How exactly does word2vec work?
P, A., K, A. K., Bharadwaj, S. K. & Venugopalan, M., 2024. Semantic Similarity Analysis for Resume Filtering using PySpark. Pune, India, IEEE, pp. 1-5
Prasetya, D. D., Wibawa, A. P. & Hirashima, T., 2018. The performance of text similarity algorithms. International Journal of Advances in Intelligent Informatics, 4(1), pp. 63-69.
Prasetya, M. A., Wulandari, M. & Nikmah, S. A., 2024. Implementasi NLP(Natural Language Processing) Dasar pada Analisis Sentiment Review Spotify. PROSIDING SEMINAR NASIONAL TEKNOLOGI DAN SAINS TAHUN 2024, pp. 145-153.
Pundir, R. S. et al., 2024. Enhancing Resume Recommendation System through Skill-based Similarity using Deep Learning Models.
Ramadhan, R. F., Wijoyo, S. H. & Saputra, M. C., 2023. Penerapan Metode K-Means Clustering pada Ulasan Perumahan PT XYZ di Google Maps untuk Formulasi Strategi Bisnis dengan Analisis SWOT. Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer, 7(6), pp. 2879-2888.
Řehůřek, R., 2024. Word2vec embeddings. [Online] Tersedia di: <https://radimrehurek.com/gensim/models/word2vec.html>
scikit-learn developers, 2025. User Guide. [Online] Tersedia di: <https://scikit- learn.org/stable/modules/feature_extraction.html#text-feature-extraction>
Septiani, D. & Isabela, I., 2022. ANALISIS TERM FREQUENCY INVERSE DOCUMENT FREQUENCY (TF-IDF). SINTESIA: Jurnal Sistem dan Teknologi Informasi Indonesia, 01(2), pp. 81-88.
Sihombing, D. O., 2022. Implementasi Natural Language Processing (NLP) dan Algoritma Cosine Similarity dalam Penilaian Ujian Esai Otomatis. Jurnal Sistem Komputer dan Informatika (JSON), 4(2), pp. 396-406.
Sohangir, S. & Wang, D., 2017. Improved sqrt-cosine similarity measurement. Journal of Big Data, 4(25), pp. 1-13.
Stanford Career Education, 2018. Pursuing Meaningful Work: A Strategies Guide for PhDs and Postdocs. [Online] Tersedia di: <https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/st anfordphd_pmw_18-19.pdf>
Stanford Career Education, 2024. Steps to Writing Your Resume. [Online] Tersedia di: <https://careered.stanford.edu/resources/resources- links#resume>
169
Suningsih, S. et al., 2024. Pelatihan Pembuatan Curriculum Vitae dalam Bahasa Inggris yang Berbasis Application Tracking System. Jurnal Nusantara Mengabdi, 3(2), pp. 85-93.
Temizhan, E., Mirtagioglu, H. & Mendes, M., 2022. Which Correlation Coefficient Should Be Used for Investigating Relations between Quantitative Variables?. American Academic Scientific Research Journal for Engineering, Technology, and Sciences, 85(1), pp. 265-277.
Titisari, M. & Ikhwan, K., 2021. Proses Rekrutmen dan Seleksi: Potensi Ketidakefektifan dan Faktornya. JMK (Jurnal Manajemen dan Kewirausahaan), 6(3), pp. 11-27.
Wujarso, R., 2022. PERAN HUMAN CAPITAL DALAM PERTUMBUHAN EKONOMI. Journal of Information System, Applied, Management, Accounting and Research, 6(2), pp. 430-438.
170

# LAMPIRAN ASURAT PERNYATAAN VALIDITAS
171

# LAMPIRAN BBOBOT PER SECTION BERDASARKAN INDUSTRI
172
173
174
175
176
177
178
179

## LAMPIRAN CHASIL PEMERINGKATAN LIMA RESUME PER KUALIFIKASI LOWONGAN KERJA
C.1Tanpa Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority Score Expert
1 38688388 Business 0,19196053 TRUE FALSE Developm416 ent Executive
Business 0,18632532 31638814 2 TRUE FALSE Developm744 ent Executive
3 18311419 Business 0,17838445 TRUE FALSE Developm987 ent Executive
4 15535920 Business 0,17084201 TRUE FALSE Developm879 ent Executive
5 17132168 Business 0,16827734 TRUE FALSE Developm892 ent Executive

# 1 26932091 CLUB 0,18715875 TRUE TRUE GENERAL 776 MANAGE R
# 2 17818707 CLUB 0,17941732 TRUE TRUE GENERAL 858 MANAGE R
# 3 15535920 CLUB 0,17141704 TRUE TRUE GENERAL 333 MANAGE R
# 4 38688388 CLUB 0,16051493 TRUE TRUE GENERAL 45 MANAGE R
180

# 5 25162378 CLUB 0,15616631 TRUE TRUE GENERAL 095 MANAGE R
1 27246366 Construct0,23094322 TRUE TRUE ion 449 Superviso r
2 39027764 Construct0,22583101 TRUE TRUE ion 516 Superviso r
3 12839152 Construct0,21587093 TRUE TRUE ion 047 Superviso r
4 22718826 Construct0,20897574 TRUE FALSE ion 732 Superviso r
5 26994282 Construct0,19910655 FALSE TRUE ion 198 Superviso r
1 68781345 Creative 0,14491833 TRUE TRUE Director / 029 Manager
2 13964744 Creative 0,13657465 FALSE FALSE Director / 594 Manager
3 308648Creative 0,13036571 TRUE TRUE 28 Director / 835 Manager
4 17781039 Creative 0,12824614 FALSE FALSE Director / 853 Manager
5 22706174 Creative 0,12641992 TRUE TRUE Director / 202 Manager
1 22754014 Digital 0,13517444 FALSE TRUE and Social 084 Media Executive
181
2 16620172 Digital 0,13033001 TRUE TRUE and Social 184 Media Executive
3 18905648 Digital 0,1297599 5 FALSE TRUE and Social Media Executive
4 18927233 Digital 0,12900323 TRUE FALSE and Social 048 Media Executive
5 16536141 Digital 0,11788542 TRUE FALSE and Social 437 Media Executive
1 14937492 Digital 0,16921864 FALSE FALSE Banking 127 Officer
2 27080812 Digital 0,16534743 FALSE FALSE Banking 431 Officer
3 26932091 Digital 0,16280285 FALSE FALSE Banking 08 Officer
Digital 0,15952694 22423839 1 FALSE FALSE Banking 82 Officer
5 25038571 Digital 0,15426142 FALSE FALSE Banking 74 Officer
1 34252537 Executive 0,23937431 TRUE TRUE Chef 131
2 29775391 Executive 0,23621694 TRUE TRUE Chef 724
3 10653119 Executive 0,23241952 TRUE TRUE Chef 106
4 25924968 Executive 0,23100075 TRUE TRUE Chef 976
5 16924102 Executive 0,22292713 TRUE TRUE Chef 471
182
1 21338490 Finance 0,23656625 TRUE FALSE Executive 907 / Accounta nt
Finance 0,23396422 25846894 4 TRUE FALSE Executive 328 / Accounta nt
3 25862026 Finance 0,19169053 TRUE TRUE Executive 061 / Accounta nt
4 29999135 Finance 0,18870911 TRUE TRUE Executive 447 / Accounta nt
Finance 0,18830695 28969385 2 TRUE TRUE Executive 276 / Accounta nt
1 23734441 Finance 0,24715923 TRUE TRUE Officer ( 921 Jr/Sr.)
2 28298773 Finance 0,22556751 TRUE TRUE Officer ( 767 Jr/Sr.)
3 29999135 Finance 0,21127042 TRUE TRUE Officer ( 543 Jr/Sr.)
4 53640713 Finance 0,19993004 TRUE FALSE Officer ( 064 Jr/Sr.)
5 21338490 Finance 0,19844635 TRUE FALSE Officer ( 036 Jr/Sr.)
1 38946032 Financial 0,18177934 TRUE TRUE Consolida037 tion
183

## Consultan t
2 70541112 Financial 0,18111551 TRUE TRUE Consolida551 tion Consultan t
213384Financial 0,17458773 5 TRUE TRUE 90 Consolida097 tion Consultan t
4 29821051 Financial 0,17309652 TRUE TRUE Consolida599 tion Consultan t
5 25862026 Financial 0,17256393 TRUE TRUE Consolida591 tion Consultan t
Graphics 0,21023281 18354623 4 TRUE FALSE Designer 956
2 18460045 Graphics 0,19939082 TRUE TRUE Designer 853
3 20210676 Graphics 0,17931445 FALSE FALSE Designer 558
4 22560013 Graphics 0,17491081 TRUE TRUE Designer 248
5 26046064 Graphics 0,17478243 TRUE TRUE Designer 455
1 30862904 HR 0,24283951 TRUE TRUE Specialist 272
2 24508725 HR 0,23966082 TRUE TRUE Specialist 996
3 16877897 HR 0,23014325 FALSE TRUE Specialist 719
4 11480899 HR 0,22160533 FALSE TRUE Specialist 793
5 53701275 HR 0,21899964 FALSE TRUE Specialist 296
184
1 39413067 INFORMA0,23568601 TRUE TRUE TION & 514 TECHNOL OGY STAFF
INFORMA0,22732222 17983957 4 FALSE FALSE TION & 616 TECHNOL OGY STAFF
3 91635250 INFORMA0,21844613 TRUE FALSE TION & 588 TECHNOL OGY STAFF
4 15535920 INFORMA0,20943395 FALSE FALSE TION & 334 TECHNOL OGY STAFF
INFORMA0,19712535 36434348 2 TRUE FALSE TION & 698 TECHNOL OGY STAFF
1 36671891 Junior 0,12064673 FALSE FALSE Associate 025 Lawyer
2 19557384 Junior 0,12036864 FALSE FALSE Associate 863 Lawyer
3 10332998 Junior 0,11955921 TRUE TRUE Associate 716 Lawyer
4 15100547 Junior 0,11802292 TRUE TRUE Associate 251 Lawyer
5 11065180 Junior 0,11707645 FALSE FALSE Associate 78 Lawyer
1 23719943 Junior 0,17716792 TRUE FALSE Designer 315 for Apparel
185
2 15746146 Junior 0,16274931 TRUE TRUE Designer 142 for Apparel
3 26503829 Junior 0,14793953 TRUE FALSE Designer 386 for Apparel
4 12122372 Junior 0,14108294 FALSE FALSE Designer 334 for Apparel
5 26932091 Junior 0,13670255 FALSE FALSE Designer 452 for Apparel
1 26932091 Manager 0,20158795 FALSE FALSE Aviation 825 Safety, Quality and Security
Manager 0,20137632 11169163 2 TRUE TRUE Aviation 559 Safety, Quality and Security
3 19796840 Manager 0,20109874 FALSE FALSE Aviation 541 Safety, Quality and Security
4 28186635 Manager 0,18773343 TRUE FALSE Aviation 005 Safety, Quality and Security
5 28383893 Manager 0,18627041 TRUE TRUE Aviation 602 Safety, Quality
186
and Security
1 16356151 Medical 0,21573861 FALSE TRUE Doctor 58
2 13565152 Medical 0,18753155 FALSE FALSE Doctor 396
3 17818707 Medical 0,16285954 FALSE FALSE Doctor 03
4 12544735 Medical 0,15957742 FALSE FALSE Doctor 142
5 43994605 Medical 0,15952043 FALSE FALSE Doctor 988
1 77828437 Productio0,12646971 TRUE TRUE n 128 Engineeri ng
2 55595908 Productio0,12013215 FALSE FALSE n 813 Engineeri ng
3 28803888 Productio0,11541673 TRUE FALSE n 25 Engineeri ng
4 30288581 Productio0,11183934 FALSE FALSE n 979 Engineeri ng
5 86828820 Productio0,11018052 FALSE FALSE n 298 Engineeri ng
1 21297828 Public 0,19076083 TRUE TRUE Relations 096 Officer
2 13129275 Public 0,18022535 FALSE TRUE Relations 973 Officer
3 28290448 Public 0,17361072 TRUE TRUE Relations 376 Officer
187
4 31220062 Public 0,17329004 FALSE TRUE Relations 471 Officer
5 20210676 Public 0,17255351 TRUE TRUE Relations 861 Officer
1 26888302 Quality 0,12528112 FALSE TRUE Control 704 Superviso r - Corn Commodi ty
2 26932091 Quality 0,12393984 FALSE TRUE Control 512 Superviso r - Corn Commodi ty
3 20905088 Quality 0,11060553 FALSE FALSE Control 359 Superviso r - Corn Commodi ty
4 28020046 Quality 0,10813901 FALSE TRUE Control 286 Superviso r - Corn Commodi ty
5 22861181 Quality 0,10697575 FALSE FALSE Control 33 Superviso r - Corn Commodi ty
1 26932091 Regional 0,21341355 FALSE TRUE Sales 079 Manager
2 25038571 Regional 0,20320242 TRUE TRUE Sales 859 Manager
3 27080812 Regional 0,20299293 FALSE TRUE Sales 331 Manager
188
4 38688388 Regional 0,19641194 FALSE FALSE Sales 402 Manager
5 17818707 Regional 0,19492211 TRUE TRUE Sales 894 Manager
1 35474904 Spare part 0,14203295 FALSE FALSE Admin 913
Spare part 0,13795832 22861181 4 FALSE FALSE Admin 676
Spare part 0,13713743 19473948 1 FALSE TRUE Admin 364
Spare part 0,13712274 71772815 2 FALSE TRUE Admin 976
5 24670867 Spare part 0,13693403 FALSE FALSE Admin 491
1 15850434 Teachers 0,22010572 TRUE TRUE 854
2 96547039 Teachers 0,19787951 TRUE TRUE 776
3 28772892 Teachers 0,18898723 TRUE TRUE 465
4 58105060 Teachers 0,18691355 TRUE TRUE 69
5 37220856 Teachers 0,18048594 FALSE TRUE 322
1 26932091 Unmanag0,22803081 TRUE TRUE ed 996 Merchant Engagem ent Senior Associate, BPO Field Sales
2 68781345 Unmanag0,20435285 FALSE FALSE ed 088 Merchant Engagem ent Senior Associate, BPO Field Sales
189
3 17818707 Unmanag0,17838464 FALSE FALSE ed 929 Merchant Engagem ent Senior Associate, BPO Field Sales
4 27884470 Unmanag0,17264013 FALSE FALSE ed 754 Merchant Engagem ent Senior Associate, BPO Field Sales
5 38688388 Unmanag0,16700922 TRUE FALSE ed 401 Merchant Engagem ent Senior Associate, BPO Field Sales

### C.2Tanpa Bobot - Word2Vec dan Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority Score Expert
Business 0,89108361 26932091 4 TRUE FALSE Developm577 ent Executive
2 10464113 Business 0,86972643 TRUE FALSE Developm314 ent Executive
3 13352113 Business 0,83978275 TRUE TRUE Developm595 ent Executive
4 17132168 Business 0,83541001 TRUE TRUE Developm585 ent Executive
190
5 27715131 Business 0,83428302 TRUE FALSE Developm539 ent Executive

# 1 26932091 CLUB 0,87955875 FALSE FALSE GENERAL 818 MANAGE R
# 2 10464113 CLUB 0,85764204 FALSE FALSE GENERAL 188 MANAGE R
# 3 13411858 CLUB 0,85696793 FALSE FALSE GENERAL 499 MANAGE R
# 4 27715131 CLUB 0,85424782 FALSE TRUE GENERAL 204 MANAGE R
# 5 12938389 CLUB 0,84919471 TRUE TRUE GENERAL 293 MANAGE R
1 27246366 Construct0,85582411 TRUE TRUE ion 725 Superviso r
2 39027764 Construct0,85225674 TRUE FALSE ion 153 Superviso r
3 26932091 Construct0,84790265 FALSE FALSE ion 556 Superviso r
4 16203589 Construct0,84252653 FALSE TRUE ion 431 Superviso r
5 12839152 Construct0,84122882 TRUE TRUE ion 904 Superviso r
191
1 13115648 Creative 0,84815303 FALSE FALSE Director / 845 Manager
2 81508860 Creative 0,84278841 TRUE TRUE Director / 43 Manager
3 129383Creative 0,83892294 FALSE FALSE Director / 89 774 Manager
4 23917826 Creative 0,83723982 FALSE FALSE Director / 466 Manager
5 24588864 Creative 0,83194165 FALSE FALSE Director / 642 Manager
1 18905648 Digital 0,88331784 FALSE TRUE and Social 282 Media Executive
2 18354623 Digital 0,84706182 TRUE FALSE and Social 427 Media Executive
3 70750649 Digital 0,84037111 TRUE FALSE and Social 468 Media Executive
4 26932091 Digital 0,83308775 FALSE FALSE and Social 423 Media Executive
5 22754014 Digital 0,82417943 FALSE TRUE and Social 109 Media Executive
1 26932091 Digital 0,88297664 FALSE TRUE Banking 711 Officer
2 98379112 Digital 0,84191381 FALSE FALSE Banking 193 Officer
192
3 26167298 Digital 0,84033313 FALSE FALSE Banking 637 Officer
4 18824120 Digital 0,84023942 FALSE TRUE Banking 056 Officer
5 10464113 Digital 0,83821705 FALSE TRUE Banking 916 Officer
1 35579812 Executive 0,88259655 TRUE TRUE Chef 822
2 29775391 Executive 0,88101873 TRUE TRUE Chef 817
3 34252537 Executive 0,86828334 TRUE TRUE Chef 076
4 21060367 Executive 0,86427901 TRUE TRUE Chef 198
5 25924968 Executive 0,86074102 TRUE TRUE Chef 938
1 20393721 Finance 0,87862403 TRUE TRUE Executive 816 / Accounta nt
2 23636277 Finance 0,85329852 TRUE TRUE Executive 747 / Accounta nt
3 70541112 Finance 0,85243241 TRUE TRUE Executive 417 / Accounta nt
4 22861181 Finance 0,84753735 FALSE FALSE Executive 387 / Accounta nt
5 26695839 Finance 0,84488394 FALSE TRUE Executive 585 /
193

## Accounta nt
1 20393721 Finance 0,87473403 TRUE FALSE Officer ( 639 Jr/Sr.)
2 23734441 Finance 0,84861611 TRUE TRUE Officer ( 629 Jr/Sr.)
Finance 0,83909573 27558837 2 TRUE TRUE Officer ( 117 Jr/Sr.)
4 25497147 Finance 0,83817444 FALSE TRUE Officer ( 027 Jr/Sr.)
5 53640713 Finance 0,82855365 FALSE TRUE Officer ( 528 Jr/Sr.)
1 70541112 Financial 0,86013191 TRUE TRUE Consolida313 tion Consultan t
2 18365443 Financial 0,84977762 FALSE TRUE Consolida538 tion Consultan t
3 269320Financial 0,84671984 FALSE TRUE 91 Consolida412 tion Consultan t
4 26695839 Financial 0,83887305 FALSE FALSE Consolida884 tion Consultan t
5 19446337 Financial 0,82725043 FALSE TRUE Consolida449 tion Consultan t
1 18354623 Graphics 0,88906293 TRUE FALSE Designer 709
194
2 22754014 Graphics 0,82654732 TRUE TRUE Designer 545
3 70750649 Graphics 0,82131654 FALSE FALSE Designer 402
4 37664296 Graphics 0,82052031 TRUE TRUE Designer 891
5 22848179 Graphics 0,80966405 FALSE FALSE Designer 706
1 16877897 HR 0,90911452 FALSE TRUE Specialist 694
2 26932091 HR 0,89796275 FALSE FALSE Specialist 291
3 30862904 HR 0,89755471 TRUE TRUE Specialist 701
4 29134372 HR 0,86765083 FALSE FALSE Specialist 904
5 11289482 HR 0,86294134 FALSE FALSE Specialist 128
INFORMA0,86926471 26932091 5 FALSE TRUE TION & 02 TECHNOL OGY STAFF
2 28672970 INFORMA0,86445423 TRUE FALSE TION & 694 TECHNOL OGY STAFF
3 10840430 INFORMA0,85213122 TRUE FALSE TION & 773 TECHNOL OGY STAFF
INFORMA0,84959824 11957080 1 TRUE TRUE TION & 438 TECHNOL OGY STAFF
5 15535920 INFORMA0,84774724 FALSE FALSE TION & 961 TECHNOL OGY STAFF
195
1 81508860 Junior 0,84114795 FALSE FALSE Associate 443 Lawyer
2 98379112 Junior 0,83500524 FALSE FALSE Associate 088 Lawyer
3 18297650 Junior 0,82874511 FALSE FALSE Associate 416 Lawyer
4 22485475 Junior 0,82820452 FALSE FALSE Associate 275 Lawyer
5 16877897 Junior 0,82766583 FALSE FALSE Associate 654 Lawyer
1 26932091 Junior 0,86299545 FALSE FALSE Designer 656 for Apparel
2 15154822 Junior 0,82167611 TRUE FALSE Designer 589 for Apparel
3 19195747 Junior 0,81222683 FALSE FALSE Designer 17 for Apparel
4 23719943 Junior 0,81015012 FALSE FALSE Designer 614 for Apparel
5 18354623 Junior 0,80570584 FALSE FALSE Designer 156 for Apparel
1 13195436 Manager 0,87601081 TRUE TRUE Aviation 203 Safety, Quality and Security
Manager 0,86366702 11169163 2 TRUE TRUE Aviation 262 Safety,
196

## Quality and Security
3 12654876 Manager 0,83544264 FALSE TRUE Aviation 771 Safety, Quality and Security
4 35651876 Manager 0,83261463 FALSE FALSE Aviation 305 Safety, Quality and Security
5 26932091 Manager 0,83217235 FALSE FALSE Aviation 739 Safety, Quality and Security
1 25328428 Medical 0,85498532 FALSE FALSE Doctor 325
2 96260484 Medical 0,85115281 FALSE TRUE Doctor 522
3 37402097 Medical 0,84489845 FALSE FALSE Doctor 325
4 15958967 Medical 0,83840913 FALSE FALSE Doctor 616
5 12544735 Medical 0,83575004 FALSE FALSE Doctor 881
1 54100393 Productio0,79405235 FALSE FALSE n 922 Engineeri ng
2 30288581 Productio0,79270102 FALSE FALSE n 179 Engineeri ng
3 12011623 Productio0,79009941 TRUE TRUE n 569 Engineeri ng
197
4 37751611 Productio0,78885284 FALSE FALSE n 109 Engineeri ng
5 10751444 Productio0,78845843 FALSE FALSE n 188 Engineeri ng
1 28290448 Public 0,85578761 TRUE TRUE Relations 945 Officer
2 70750649 Public 0,83941372 TRUE FALSE Relations 621 Officer
3 22861181 Public 0,83219765 FALSE FALSE Relations 066 Officer
4 22754014 Public 0,83131173 TRUE TRUE Relations 474 Officer
5 18354623 Public 0,82151534 TRUE FALSE Relations 068 Officer
1 26932091 Quality 0,85152015 FALSE TRUE Control 807 Superviso r - Corn Commodi ty
2 35651876 Quality 0,82612242 FALSE FALSE Control 329 Superviso r - Corn Commodi ty
3 12011623 Quality 0,81616043 FALSE FALSE Control 106 Superviso r - Corn Commodi ty
4 26070334 Quality 0,81409731 FALSE TRUE Control 449 Superviso r - Corn
198

## Commodi ty
5 26888302 Quality 0,81078274 FALSE FALSE Control 604 Superviso r - Corn Commodi ty
1 26932091 Regional 0,91355853 FALSE TRUE Sales 03 Manager
2 28867567 Regional 0,86280781 TRUE TRUE Sales 401 Manager
3 12059198 Regional 0,84365462 FALSE TRUE Sales 087 Manager
4 18368613 Regional 0,83556454 TRUE FALSE Sales 984 Manager
5 23917826 Regional 0,83405005 FALSE TRUE Sales 742 Manager
1 26932091 Spare part 0,86061925 FALSE TRUE Admin 668
2 22861181 Spare part 0,85548303 FALSE FALSE Admin 7
3 16378091 Spare part 0,84867161 FALSE TRUE Admin 747
4 23917826 Spare part 0,83744424 FALSE TRUE Admin 756
Spare part 0,83642155 37764298 2 FALSE TRUE Admin 493
0,92862521 28772892 Teachers 4 TRUE TRUE 558
0,90541982 15850434 Teachers 2 TRUE TRUE 861
3 54100393 Teachers 0,90024765 TRUE TRUE 335
4 37220856 Teachers 0,89556503 FALSE TRUE 21
199
5 96547039 Teachers 0,88290451 TRUE TRUE 147
1 26932091 Unmanag0,92653011 TRUE TRUE ed 426 Merchant Engagem ent Senior Associate, BPO Field Sales
2 11289482 Unmanag0,85958162 TRUE FALSE ed 135 Merchant Engagem ent Senior Associate, BPO Field Sales
Unmanag0,83743213 16877897 5 FALSE FALSE ed 014 Merchant Engagem ent Senior Associate, BPO Field Sales
4 30862904 Unmanag0,82527244 FALSE FALSE ed 558 Merchant Engagem ent Senior Associate, BPO Field Sales
5 12938389 Unmanag0,82378823 FALSE FALSE ed 972 Merchant Engagem ent Senior Associate, BPO Field Sales
200
C.3Tanpa Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority Score Expert
1 26932091 Business 0,95268632 TRUE FALSE Developm545 ent Executive
2 10464113 Business 0,94692955 FALSE TRUE Developm215 ent Executive
3 27715131 Business 0,94316824 TRUE FALSE Developm632 ent Executive
Business 0,94312534 91467795 1 TRUE TRUE Developm452 ent Executive
5 17132168 Business 0,94150563 TRUE TRUE Developm337 ent Executive

# 1 26932091 CLUB 0,94997131 TRUE TRUE GENERAL 215 MANAGE R
# 2 10464113 CLUB 0,94701965 FALSE FALSE GENERAL 187 MANAGE R
# CLUB 0,94652613 13411858 4 FALSE TRUE GENERAL 069 MANAGE R
# 4 27715131 CLUB 0,94637473 FALSE TRUE GENERAL 964 MANAGE R
# 5 12938389 CLUB 0,94495842 FALSE TRUE GENERAL 126 MANAGE R
201
1 39027764 Construct0,94641034 TRUE FALSE ion 571 Superviso r
2 27246366 Construct0,94184112 TRUE TRUE ion 329 Superviso r
3 12839152 Construct0,94057051 TRUE TRUE ion 386 Superviso r
4 26932091 Construct0,93882705 FALSE TRUE ion 484 Superviso r
5 10176013 Construct0,93553133 TRUE TRUE ion 332 Superviso r
1 22861181 Creative 0,94882842 FALSE TRUE Director / 06 Manager
Creative 0,94764422 13115648 5 FALSE FALSE Director / 985 Manager
3 815088Creative 0,94652951 TRUE TRUE 60 Director / 591 Manager
4 16899268 Creative 0,94643483 FALSE TRUE Director / 445 Manager
5 26932091 Creative 0,94578784 FALSE TRUE Director / 553 Manager
1 18905648 Digital 0,95417871 TRUE TRUE and Social 533 Media Executive
2 70750649 Digital 0,94764433 TRUE FALSE and Social 214 Media Executive
202
3 18354623 Digital 0,94671362 TRUE FALSE and Social 247 Media Executive
4 34712719 Digital 0,94365585 FALSE TRUE and Social 5 Media Executive
5 14304010 Digital 0,94127604 TRUE TRUE and Social 663 Media Executive
1 26932091 Digital 0,95485944 FALSE FALSE Banking 827 Officer
2 18905648 Digital 0,94893722 FALSE FALSE Banking 807 Officer
3 13352113 Digital 0,94624833 FALSE TRUE Banking 878 Officer
4 10464113 Digital 0,94603025 FALSE TRUE Banking 848 Officer
5 15423153 Digital 0,94429211 FALSE TRUE Banking 952 Officer
1 35579812 Executive 0,95708385 FALSE TRUE Chef 092
2 29775391 Executive 0,95245802 TRUE TRUE Chef 434
3 10276858 Executive 0,94798834 TRUE FALSE Chef 343
4 16924102 Executive 0,94797013 TRUE TRUE Chef 332
5 65373280 Executive 0,94621831 TRUE TRUE Chef 423
1 20393721 Finance 0,95119453 FALSE TRUE Executive 992 / Accounta nt
203
2 70541112 Finance 0,94564731 TRUE TRUE Executive 07 / Accounta nt
Finance 0,94469613 25846894 2 TRUE TRUE Executive 732 / Accounta nt
4 19446337 Finance 0,94431894 FALSE TRUE Executive 041 / Accounta nt
5 25497147 Finance 0,94387165 FALSE TRUE Executive 017 / Accounta nt
Finance 0,96003861 20393721 3 FALSE TRUE Officer ( 8 Jr/Sr.)
2 23734441 Finance 0,95223992 TRUE TRUE Officer ( 562 Jr/Sr.)
3 25497147 Finance 0,95178914 FALSE TRUE Officer ( 475 Jr/Sr.)
4 53640713 Finance 0,95080165 FALSE TRUE Officer ( 156 Jr/Sr.)
5 34816637 Finance 0,94636081 TRUE TRUE Officer ( 681 Jr/Sr.)
1 70541112 Financial 0,94179912 TRUE TRUE Consolida803 tion Consultan t
2 27330027 Financial 0,93865464 FALSE FALSE Consolida765 tion
204

## Consultan t
3 153632Financial 0,93593283 TRUE TRUE 77 Consolida764 tion Consultan t
Financial 0,93424424 19446337 1 TRUE TRUE Consolida62 tion Consultan t
5 18365443 Financial 0,93311005 FALSE TRUE Consolida827 tion Consultan t
1 18354623 Graphics 0,95682011 TRUE FALSE Designer 853
2 70750649 Graphics 0,95315534 TRUE FALSE Designer 81
3 22754014 Graphics 0,94450302 TRUE FALSE Designer 836
4 28679359 Graphics 0,94354365 TRUE FALSE Designer 506
5 14304010 Graphics 0,94260003 TRUE FALSE Designer 143
1 16877897 HR 0,95793031 TRUE FALSE Specialist 028
2 30862904 HR 0,95611922 TRUE FALSE Specialist 703
HR 0,95152693 26932091 5 FALSE FALSE Specialist 99
HR 0,94536644 22861181 3 FALSE FALSE Specialist 87
HR 0,94444345 11289482 4 FALSE FALSE Specialist 517
1 10840430 INFORMA0,94848592 TRUE FALSE TION & 45 TECHNOL OGY STAFF
205
2 11676151 INFORMA0,94749581 TRUE TRUE TION & 077 TECHNOL OGY STAFF
INFORMA0,94608833 26932091 5 FALSE FALSE TION & 964 TECHNOL OGY STAFF
4 28672970 INFORMA0,94579373 TRUE FALSE TION & 874 TECHNOL OGY STAFF
5 17963031 INFORMA0,94575884 FALSE FALSE TION & 681 TECHNOL OGY STAFF
Junior 0,94024691 64589506 1 FALSE FALSE Associate 427 Lawyer
2 26932091 Junior 0,94002532 FALSE FALSE Associate 197 Lawyer
3 22861181 Junior 0,93934403 FALSE FALSE Associate 608 Lawyer
4 16877897 Junior 0,93828834 FALSE FALSE Associate 659 Lawyer
5 19557384 Junior 0,93806325 FALSE FALSE Associate 209 Lawyer
1 23719943 Junior 0,94048682 FALSE FALSE Designer 792 for Apparel
Junior 0,93945432 26932091 5 FALSE FALSE Designer 595 for Apparel
206
3 23917826 Junior 0,93283624 FALSE FALSE Designer 478 for Apparel
4 15154822 Junior 0,93107741 TRUE FALSE Designer 192 for Apparel
5 70750649 Junior 0,92983303 FALSE FALSE Designer 345 for Apparel
1 13195436 Manager 0,94867181 TRUE TRUE Aviation 093 Safety, Quality and Security
2 11169163 Manager 0,94791573 TRUE TRUE Aviation 24 Safety, Quality and Security
3 12654876 Manager 0,94381784 FALSE FALSE Aviation 526 Safety, Quality and Security
4 35651876 Manager 0,94381605 FALSE FALSE Aviation 536 Safety, Quality and Security
5 17483843 Manager 0,94116062 TRUE TRUE Aviation 041 Safety, Quality and Security
1 96260484 Medical 0,93659361 FALSE TRUE Doctor 609
207
2 37402097 Medical 0,93594833 FALSE TRUE Doctor 901
3 25328428 Medical 0,93579255 FALSE TRUE Doctor 524
4 15499825 Medical 0,93432984 FALSE TRUE Doctor 543
5 14667957 Medical 0,93224472 FALSE TRUE Doctor 061
1 13087952 Productio0,93914302 FALSE TRUE n 121 Engineeri ng
Productio0,93585662 10504237 4 FALSE TRUE n 737 Engineeri ng
3 11890896 Productio0,93553671 TRUE FALSE n 658 Engineeri ng
4 22861181 Productio0,93522053 FALSE TRUE n 072 Engineeri ng
5 11522068 Productio0,93402925 FALSE TRUE n 108 Engineeri ng
Public 0,94763161 28290448 1 TRUE TRUE Relations 491 Officer
2 70750649 Public 0,94678672 TRUE FALSE Relations 469 Officer
3 22861181 Public 0,94044394 FALSE FALSE Relations 705 Officer
4 13115648 Public 0,93936155 FALSE FALSE Relations 415 Officer
5 22732234 Public 0,93866593 TRUE TRUE Relations 303 Officer
208
1 26888302 Quality 0,93800532 FALSE FALSE Control 431 Superviso r - Corn Commodi ty
2 22861181 Quality 0,93581594 FALSE TRUE Control 329 Superviso r - Corn Commodi ty
3 20905088 Quality 0,93238241 FALSE TRUE Control 831 Superviso r - Corn Commodi ty
Quality 0,93208974 21629057 3 FALSE FALSE Control 127 Superviso r - Corn Commodi ty
5 26932091 Quality 0,92928745 FALSE TRUE Control 126 Superviso r - Corn Commodi ty
1 26932091 Regional 0,95265803 TRUE TRUE Sales 458 Manager
Regional 0,93800752 28867567 4 TRUE TRUE Sales 485 Manager
3 29306433 Regional 0,93753665 TRUE FALSE Sales 445 Manager
4 27715131 Regional 0,93701841 TRUE TRUE Sales 881 Manager
5 28051330 Regional 0,93633372 TRUE TRUE Sales 906 Manager
209
1 22861181 Spare part 0,94827371 FALSE FALSE Admin 396
2 23917826 Spare part 0,94712263 FALSE TRUE Admin 141
3 26932091 Spare part 0,94671462 FALSE FALSE Admin 582
4 16378091 Spare part 0,94669344 FALSE TRUE Admin 216
5 10464113 Spare part 0,94492955 FALSE TRUE Admin 182
1 28772892 Teachers 0,96426665 TRUE TRUE 724
2 15850434 Teachers 0,95758432 TRUE TRUE 692
3 58105060 Teachers 0,95216004 TRUE FALSE 9
4 37220856 Teachers 0,94961243 TRUE FALSE 554
0,94716075 48547319 Teachers 1 TRUE FALSE 207
Unmanag0,96215741 26932091 1 TRUE TRUE ed 749 Merchant Engagem ent Senior Associate, BPO Field Sales
2 11289482 Unmanag0,94395413 TRUE TRUE ed 207 Merchant Engagem ent Senior Associate, BPO Field Sales
3 30862904 Unmanag0,93801254 FALSE FALSE ed 051 Merchant Engagem ent Senior Associate,
210

## BPO Field Sales
4 13964744 Unmanag0,93323952 FALSE FALSE ed 557 Merchant Engagem ent Senior Associate, BPO Field Sales
5 24727739 Unmanag0,93310515 FALSE FALSE ed 675 Merchant Engagem ent Senior Associate, BPO Field Sales
C.4Dengan Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority Score Expert

# 1 Business 0,2059132 TRUE FALSE 38688388 Developme2303 nt Executive
# 2 Business 0,2029121 TRUE FALSE 31638814 Developme8525 nt Executive
# 3 Business 0,1925983 TRUE FALSE 47067533 Developme8694 nt Executive
# 4 Business 0,1878345 FALSE TRUE 26932091 Developme9723 nt Executive
# 5 Business 0,1837794 TRUE FALSE 17132168 Developme5536 nt Executive
211

# 1 CLUB 0,2045175 FALSE FALSE 26932091 GENERAL 8615 MANAGER
# 2 CLUB 0,1912281 TRUE TRUE 17818707 GENERAL 4503 MANAGER
# 3 CLUB 0,1854663 TRUE TRUE 18171955 GENERAL 2893 MANAGER
# 4 CLUB 0,1814164 FALSE FALSE 15535920 GENERAL 6723 MANAGER
# 5 CLUB 0,1806792 TRUE TRUE 31761591 GENERAL 3312 MANAGER
# 1 Constructio0,2224581 TRUE FALSE 39027764 n 9589 Supervisor
# 2 Constructio0,2195714 TRUE TRUE 12839152 n 2303 Supervisor
# 3 Constructio0,2057733 TRUE FALSE 27246366 n 4896 Supervisor
# 4 Constructio0,2007952 TRUE TRUE 56525735 n 8072 Supervisor
# 5 Constructio0,1966745 FALSE FALSE 26932091 n 0695 Supervisor
Creative 0,1770421 2 FALSE TRUE 68781345 Director / 6406 Manager

# 2 Creative 0,1524073 TRUE FALSE 18460045 Director / 9329 Manager
# 3 Creativ0,1490014 FALSE FALSE 13964744 e Director / 695 Manager
# 4 Creative 0,1389845 FALSE FALSE 17781039 Director / 5056 Manager
212

# 5 Creative 0,1340541 TRUE TRUE 30864828 Director / 7236 Manager
# 1 Digital and 0,1700295 FALSE TRUE 22754014 Social 822 Media Executive
Digital and 0,1613782 3 TRUE FALSE 15479281 Social 88 Media Executive

# 3 Digital and 0,1474631 TRUE TRUE 16620172 Social 8205 Media Executive
# 4 Digital and 0,1446424 TRUE FALSE 16536141 Social 1125 Media Executive
# 5 Digital and 0,1444502 TRUE TRUE 75329822 Social 2095 Media Executive
Digital 0,2007691 5 FALSE TRUE 26932091 Banking 5753 Officer

# 2 Digital 0,1817781 TRUE FALSE 98965485 Banking 1123 Officer
# 3 Digital 0,1599484 FALSE FALSE 14937492 Banking 4431 Officer
# 4 Digital 0,1576373 TRUE FALSE 27080812 Banking 613 Officer
# 5 Digital 0,1546712 TRUE FALSE 29406313 Banking 2682 Officer
# 1 Executive 0,2608344 TRUE TRUE 29775391 Chef 3156
# 2 Executive 0,2600573 TRUE TRUE 20321582 Chef 9128
213

# 3 Executive 0,2493231 TRUE TRUE 34252537 Chef 4669
# 4 Executive 0,2463985 TRUE TRUE 25924968 Chef 796
# 5 Executive 0,2463162 TRUE TRUE 25128608 Chef 0122
# 1 Finance 0,2448525 TRUE FALSE 37370455 Executive / 904 Accountant
# 2 Finance 0,2389354 TRUE FALSE 25846894 Executive / 8751 Accountant
Finance 0,2290033 3 TRUE FALSE 21338490 Executive / 7916 Accountant

# 4 Finance 0,2189882 TRUE FALSE 24670867 Executive / 459 Accountant
# 5 Finance 0,2123731 TRUE TRUE 23387174 Executive / 8693 Accountant
# 1 Finance 0,2239542 TRUE TRUE 23734441 Officer ( 8861 Jr/Sr.)
# 2 Finance 0,2169143 TRUE TRUE 29999135 Officer ( 026 Jr/Sr.)
# 3 Finance 0,2167655 TRUE FALSE 24670867 Officer ( 7361 Jr/Sr.)
# 4 Finance 0,2158491 TRUE TRUE 28298773 Officer ( 502 Jr/Sr.)
Finance 0,2041565 4 TRUE TRUE 53640713 Officer ( 394 Jr/Sr.)

# 1 Financial 0,2101915 FALSE FALSE 68781345 Consolidati4441 on Consultant
# 2 Financial 0,1949781 TRUE TRUE 95792386 Consolidati4098
214
on Consultant

# 3 Financi0,1901583 TRUE TRUE 70541112 al 5017 Consolidati on Consultant
Financial 0,1895114 2 TRUE TRUE 38946032 Consolidati6438 on Consultant

# 5 Financial 0,1839034 TRUE FALSE 19234823 Consolidati2081 on Consultant
# 1 Graphics 0,2795612 TRUE TRUE 18460045 Designer 5313
# 2 Graphics 0,2220083 TRUE FALSE 18354623 Designer 2185
# 3 Graphics 0,1989271 TRUE TRUE 26676567 Designer 8803
# 4 Graphics 0,1951684 TRUE FALSE 16893572 Designer 6831
# 5 Graphics 0,1919995 FALSE TRUE 22754014 Designer 01
# 1 HR 0,2664032 TRUE TRUE 24508725 Specialist 927
# 2 HR 0,2639681 TRUE TRUE 30862904 Specialist 2699
# 3 HR 0,2340104 FALSE TRUE 16877897 Specialist 6126
# 4 HR 0,2279963 FALSE TRUE 24184357 Specialist 3281
# 5 HR 0,2270325 FALSE TRUE 26932091 Specialist 5052
# 1 INFORMATI0,2211704 FALSE FALSE 17983957 ON & 9312 TECHNOLO GY STAFF
# 2 INFORMATI0,2205451 TRUE TRUE 39413067 ON & 8455
215

# TECHNOLO GY STAFF
# 3 INFORMATI0,2152233 FALSE FALSE 17570634 ON & 6294 TECHNOLO GY STAFF
# 4 INFORMATI0,2071112 TRUE FALSE 21283365 ON & 8727 TECHNOLO GY STAFF
# 5 INFORMATI0,2022525 FALSE FALSE 38897568 ON & 2526 TECHNOLO GY STAFF
# 1 Junior 0,1243074 FALSE TRUE 29406313 Associate 7984 Lawyer
# 2 Junior 0,1215681 TRUE TRUE 10332998 Associate 8418 Lawyer
# 3 Junior 0,1204043 FALSE TRUE 69181350 Associate 3196 Lawyer
# 4 Junior 0,1175635 FALSE TRUE 23636277 Associate 5815 Lawyer
Junior 0,1175485 2 TRUE TRUE 15100547 Associate 7301 Lawyer

# 1 Junior 0,1669882 TRUE FALSE 23719943 Designer 3684 for Apparel
# 2 Junior 0,1646021 TRUE TRUE 15746146 Designer 35 for Apparel
# 3 Junior 0,1502075 FALSE FALSE 12122372 Designer 8775 for Apparel
# 4 Junior 0,1447224 FALSE FALSE 26932091 Designer 2826 for Apparel
216

# 5 Junior 0,1425713 FALSE FALSE 11722421 Designer 9056 for Apparel
# 1 Manager 0,2348122 FALSE FALSE 26932091 Aviation 8415 Safety, Quality and Security
# 2 Manager 0,2101541 TRUE FALSE 28186635 Aviation 9087 Safety, Quality and Security
# 3 Manager 0,2074043 FALSE FALSE 24589765 Aviation 6317 Safety, Quality and Security
# 4 Manager 0,2014924 FALSE FALSE 29406313 Aviation 0559 Safety, Quality and Security
# 5 Manager 0,1949655 FALSE FALSE 11289482 Aviation 5358 Safety, Quality and Security
# 1 Medical 0,2257121 FALSE TRUE 16356151 Doctor 691
# 2 Medical 0,1743465 FALSE FALSE 13565152 Doctor 7306
# 3 Medical 0,1727042 FALSE TRUE 43994605 Doctor 0952
# 4 Medical 0,1610993 FALSE FALSE 24588864 Doctor 4638
# 5 Medical 0,1521774 FALSE FALSE 49325370 Doctor 5854
# 1 Production 0,1444482 TRUE FALSE 28803888 Engineering 7571
# 2 Production 0,1307514 FALSE FALSE 30288581 Engineering 2078
217

# 3 Production 0,1285431 TRUE TRUE 77828437 Engineering 7933
# 4 Production 0,1238893 TRUE FALSE 17103000 Engineering 6191
# 5 Production 0,1218915 FALSE FALSE 54100393 Engineering 3506
# 1 Public 0,2007191 TRUE TRUE 21297828 Relations 3257 Officer
# 2 Public 0,1965975 FALSE TRUE 13129275 Relations 6361 Officer
Public 0,1950113 2 TRUE FALSE 27257013 Relations 6308 Officer

# 4 Public 0,1858104 FALSE FALSE 31220062 Relations 0177 Officer
# 5 Public 0,1836933 TRUE FALSE 27000192 Relations 9263 Officer
# 1 Quality 0,1403704 FALSE TRUE 26932091 Control 3197 Supervisor - Corn Commodity
# 2 Quality 0,1272195 FALSE FALSE 28186635 Control 2623 Supervisor - Corn Commodity
# 3 Quality 0,1266081 FALSE TRUE 16723524 Control 0495 Supervisor - Corn Commodity
# 4 Quality 0,1231592 FALSE FALSE 28628090 Control 2765 Supervisor - Corn Commodity
# 5 Quality 0,1219373 FALSE FALSE 20905088 Control 0839 Supervisor -
218

## Corn Commodity
# 1 Regional 0,2430534 FALSE TRUE 26932091 Sales 1858 Manager
# 2 Regional 0,2247093 FALSE TRUE 27080812 Sales 9765 Manager
Regional 0,2178413 1 FALSE TRUE 25038571 Sales 7617 Manager

# 4 Regional 0,2128312 FALSE FALSE 38688388 Sales 0977 Manager
# 5 Regional 0,2103245 FALSE TRUE 26919036 Sales 2631 Manager
# 1 Spare part 0,1552135 FALSE FALSE 16911115 Admin 3324
# 2 Spare part 0,1499734 FALSE FALSE 38897568 Admin 7297
# 3 Spare part 0,1480601 TRUE TRUE 10189110 Admin 5907
# 4 Spare part 0,1470322 TRUE TRUE 20504094 Admin 3157
# 5 Spare part 0,1461123 FALSE FALSE 24670867 Admin 3257
# 1 Teachers 0,2507454 TRUE TRUE 15850434 2502
# 2 Teachers 0,2138403 TRUE TRUE 20399718 2469
# 3 Teachers 0,2003425 TRUE TRUE 28772892 6776
# 4 Teachers 0,1966352 TRUE TRUE 22056333 771
# 5 Teachers 0,1961001 TRUE TRUE 96547039 2177
# 1 Unmanage0,2221771 TRUE TRUE 26932091 d Merchant 0964 Engagemen t Senior Associate,
219

## BPO Field Sales
# 2 Unmanage0,1921963 FALSE FALSE 24589765 d Merchant 5525 Engagemen t Senior Associate, BPO Field Sales
# 3 Unmanage0,1865804 FALSE FALSE 68781345 d Merchant 6571 Engagemen t Senior Associate, BPO Field Sales
# 4 Unmanage0,1634892 TRUE FALSE 11289482 d Merchant 1955 Engagemen t Senior Associate, BPO Field Sales
# 5 Unmanage0,1617525 FALSE TRUE 26919036 d Merchant 4074 Engagemen t Senior Associate, BPO Field Sales
C.5Dengan Bobot - Word2Vec dan Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority Score Expert
1 26932091 Business 0,90162953 TRUE FALSE Developm473 ent Executive
2 10464113 Business 0,86647822 TRUE TRUE Developm882 ent Executive
220
3 14790629 Business 0,86520204 TRUE TRUE Developm196 ent Executive
4 27715131 Business 0,84788531 TRUE FALSE Developm941 ent Executive
5 16276121 Business 0,84141565 FALSE TRUE Developm304 ent Executive

# 1 13411858 CLUB 0,87814171 TRUE TRUE GENERAL 949 MANAGE R
# 2 26932091 CLUB 0,87737205 FALSE FALSE GENERAL 443 MANAGE R
# 3 10464113 CLUB 0,85926734 FALSE TRUE GENERAL 114 MANAGE R
# 4 27715131 CLUB 0,85455792 TRUE TRUE GENERAL 91 MANAGE R
# 5 34033933 CLUB 0,85229223 FALSE FALSE GENERAL 794 MANAGE R
1 26932091 Construct0,86214285 FALSE FALSE ion 311 Superviso r
2 12839152 Construct0,82651702 TRUE TRUE ion 306 Superviso r
3 24589765 Construct0,82427143 FALSE FALSE ion 703 Superviso r
221
4 27246366 Construct0,82201161 TRUE TRUE ion 446 Superviso r
5 39027764 Construct0,82056594 TRUE FALSE ion 688 Superviso r
1 34033933 Creative 0,85447492 FALSE FALSE Director / 737 Manager
2 23917826 Creative 0,85386413 FALSE FALSE Director / 334 Manager
3 295257Creative 0,85052935 FALSE FALSE 15 Director / 826 Manager
4 28471099 Creative 0,84542531 FALSE TRUE Director / 674 Manager
5 13115648 Creative 0,84179964 FALSE TRUE Director / 705 Manager
1 18905648 Digital 0,88443265 FALSE TRUE and Social 053 Media Executive
2 16276121 Digital 0,87920894 FALSE TRUE and Social 298 Media Executive
3 18354623 Digital 0,86782902 TRUE FALSE and Social 546 Media Executive
4 22754014 Digital 0,85912753 FALSE TRUE and Social 096 Media Executive
5 70750649 Digital 0,85613201 TRUE FALSE and Social 066 Media Executive
222
1 26932091 Digital 0,89927284 FALSE TRUE Banking 761 Officer
2 29406313 Digital 0,88626562 FALSE FALSE Banking 554 Officer
3 11289482 Digital 0,86449343 TRUE FALSE Banking 257 Officer
4 16276121 Digital 0,86108061 TRUE TRUE Banking 125 Officer
5 10464113 Digital 0,85056925 FALSE TRUE Banking 522 Officer
1 35579812 Executive 0,88596715 TRUE TRUE Chef 312
2 21060367 Executive 0,88542684 TRUE TRUE Chef 859
3 20321582 Executive 0,87891942 TRUE TRUE Chef 787
4 29775391 Executive 0,87567741 TRUE TRUE Chef 834
5 34252537 Executive 0,87040003 TRUE TRUE Chef 922
1 20393721 Finance 0,88252293 TRUE TRUE Executive 636 / Accounta nt
2 23636277 Finance 0,87818472 TRUE TRUE Executive 954 / Accounta nt
3 70541112 Finance 0,87730931 TRUE TRUE Executive 777 / Accounta nt
4 28522529 Finance 0,87086894 TRUE FALSE Executive 809 /
223

## Accounta nt
5 11289482 Finance 0,86494385 FALSE FALSE Executive 109 / Accounta nt
Finance 0,89983441 34198885 1 TRUE TRUE Officer ( 839 Jr/Sr.)
2 70541112 Finance 0,87261093 TRUE TRUE Officer ( 783 Jr/Sr.)
3 28522529 Finance 0,86447924 TRUE FALSE Officer ( 199 Jr/Sr.)
4 20393721 Finance 0,85890662 TRUE TRUE Officer ( 515 Jr/Sr.)
5 25497147 Finance 0,85025375 FALSE TRUE Officer ( 529 Jr/Sr.)
1 70541112 Financial 0,86435371 TRUE TRUE Consolida442 tion Consultan t
2 18365443 Financial 0,85424222 FALSE TRUE Consolida007 tion Consultan t
3 269320Financial 0,85187663 FALSE TRUE 91 Consolida099 tion Consultan t
4 26695839 Financial 0,83981454 FALSE FALSE Consolida871 tion Consultan t
5 16877897 Financial 0,82222005 FALSE TRUE Consolida423
224
tion Consultan t
1 18460045 Graphics 0,89835311 TRUE TRUE Designer 892
2 18354623 Graphics 0,89723592 TRUE TRUE Designer 945
3 33893326 Graphics 0,85831443 TRUE TRUE Designer 695
4 22754014 Graphics 0,85264345 FALSE FALSE Designer 749
5 16276121 Graphics 0,84446234 TRUE FALSE Designer 484
HR 0,90842931 30862904 1 TRUE TRUE Specialist 384
HR 0,90576232 16877897 2 FALSE TRUE Specialist 595
HR 0,90272553 26932091 5 FALSE FALSE Specialist 476
4 29134372 HR 0,87105553 FALSE TRUE Specialist 988
5 11289482 HR 0,87057814 FALSE FALSE Specialist 315
1 26932091 INFORMA0,88069725 FALSE FALSE TION & 802 TECHNOL OGY STAFF
2 28471099 INFORMA0,87906583 TRUE FALSE TION & 832 TECHNOL OGY STAFF
3 10839851 INFORMA0,85557761 TRUE TRUE TION & 477 TECHNOL OGY STAFF

# 4 28672970 INFORMA0,85081724 TRUE FALSE TION & 572 TECHNOL
225

# OGY STAFF
5 26341987 INFORMA0,84652972 TRUE FALSE TION & 371 TECHNOL OGY STAFF
Junior 0,84346961 26330995 3 FALSE FALSE Associate 848 Lawyer
2 24589765 Junior 0,84091522 FALSE FALSE Associate 248 Lawyer
3 11289482 Junior 0,83808424 FALSE FALSE Associate 897 Lawyer
4 28871170 Junior 0,83401031 TRUE FALSE Associate 447 Lawyer
5 81508860 Junior 0,83206895 FALSE FALSE Associate 852 Lawyer
1 26932091 Junior 0,86701083 FALSE FALSE Designer 12 for Apparel
Junior 0,82210672 28471099 2 FALSE FALSE Designer 895 for Apparel
3 19195747 Junior 0,80966441 FALSE FALSE Designer 228 for Apparel
4 27715131 Junior 0,80872514 FALSE FALSE Designer 828 for Apparel
5 76196367 Junior 0,80849145 FALSE FALSE Designer 625 for Apparel
226
1 13195436 Manager 0,86085901 TRUE TRUE Aviation 662 Safety, Quality and Security
2 24589765 Manager 0,86045152 FALSE TRUE Aviation 94 Safety, Quality and Security
3 28186635 Manager 0,84465573 FALSE FALSE Aviation 224 Safety, Quality and Security
Manager 0,84284574 26932091 5 FALSE FALSE Aviation 081 Safety, Quality and Security
5 16877897 Manager 0,84101344 FALSE FALSE Aviation 763 Safety, Quality and Security
1 15958967 Medical 0,85060423 FALSE FALSE Doctor 004
2 14667957 Medical 0,84702901 FALSE FALSE Doctor 78
3 28745844 Medical 0,84648384 FALSE FALSE Doctor 862
Medical 0,84381344 24588864 5 FALSE FALSE Doctor 193
Medical 0,83811385 96260484 2 FALSE TRUE Doctor 295
1 54100393 Productio0,83485785 FALSE FALSE n 215 Engineeri ng
227
2 24544244 Productio0,80706563 FALSE FALSE n 359 Engineeri ng
3 30288581 Productio0,80649192 FALSE FALSE n 114 Engineeri ng
4 37751611 Productio0,80052534 FALSE FALSE n 474 Engineeri ng
5 17312146 Productio0,79768751 TRUE FALSE n 544 Engineeri ng
1 28290448 Public 0,85461041 TRUE TRUE Relations 868 Officer
2 22754014 Public 0,83732243 TRUE TRUE Relations 586 Officer
3 16276121 Public 0,83065624 FALSE TRUE Relations 04 Officer
Public 0,83034844 70750649 2 TRUE FALSE Relations 569 Officer
5 22861181 Public 0,82975835 FALSE FALSE Relations 163 Officer
1 26932091 Quality 0,87054244 FALSE TRUE Control 666 Superviso r - Corn Commodi ty
2 35651876 Quality 0,83610862 FALSE FALSE Control 76 Superviso r - Corn Commodi ty
228
3 26070334 Quality 0,82792471 FALSE TRUE Control 06 Superviso r - Corn Commodi ty
4 21060367 Quality 0,82561605 FALSE FALSE Control 915 Superviso r - Corn Commodi ty
5 12011623 Quality 0,81789113 FALSE FALSE Control 124 Superviso r - Corn Commodi ty
Regional 0,92046371 26932091 3 FALSE TRUE Sales 706 Manager
2 28867567 Regional 0,8558917 2 TRUE TRUE Sales Manager
3 18368613 Regional 0,84883364 TRUE FALSE Sales 618 Manager
4 27715131 Regional 0,84651751 FALSE TRUE Sales 219 Manager
5 14790629 Regional 0,84215035 FALSE FALSE Sales 535 Manager
1 26932091 Spare part 0,89872495 FALSE TRUE Admin 136
2 16378091 Spare part 0,85448021 FALSE TRUE Admin 836
3 14790629 Spare part 0,84722874 FALSE FALSE Admin 589
4 23917826 Spare part 0,84469653 FALSE TRUE Admin 705
5 37764298 Spare part 0,84420252 FALSE TRUE Admin 726
229
1 28772892 Teachers 0,92975274 TRUE TRUE 121
2 15850434 Teachers 0,91528212 TRUE TRUE 211
3 54100393 Teachers 0,90129505 TRUE TRUE 182
4 37220856 Teachers 0,88759923 FALSE TRUE 112
5 20399718 Teachers 0,88417721 TRUE TRUE 63
1 26932091 Unmanag0,92527121 TRUE TRUE ed 045 Merchant Engagem ent Senior Associate, BPO Field Sales
2 11289482 Unmanag0,86673853 TRUE FALSE ed 379 Merchant Engagem ent Senior Associate, BPO Field Sales
3 24589765 Unmanag0,85077614 FALSE FALSE ed 608 Merchant Engagem ent Senior Associate, BPO Field Sales
4 29406313 Unmanag0,83419172 TRUE FALSE ed 147 Merchant Engagem ent Senior Associate, BPO Field Sales
5 16877897 Unmanag0,83203815 FALSE FALSE ed 194 Merchant
230
Engagem ent Senior Associate, BPO Field Sales
C.6Dengan Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority Score Expert
1 26932091 Business 0,95396682 TRUE FALSE Developm445 ent Executive
2 14790629 Business 0,95067804 TRUE FALSE Developm856 ent Executive
3 91467795 Business 0,94752521 TRUE TRUE Developm332 ent Executive
4 10464113 Business 0,94666345 FALSE TRUE Developm695 ent Executive

# 5 27715131   0,94368233 TRUE TRUE 33
# 1 13411858 CLUB 0,95272684 FALSE TRUE GENERAL 773 MANAGE R
# 2 28471099 CLUB 0,94908122 TRUE TRUE GENERAL 742 MANAGE R
# 3 26932091 CLUB 0,94881341 TRUE TRUE GENERAL 43 MANAGE R
# 4 10464113 CLUB 0,94770725 FALSE FALSE GENERAL 07
231

# MANAGE R
# 5 24727739 CLUB 0,94746573 FALSE FALSE GENERAL 096 MANAGE R
1 26932091 Construct0,94129275 FALSE TRUE ion 301 Superviso r
2 39027764 Construct0,93906673 TRUE FALSE ion 24 Superviso r
3 12839152 Construct0,93719281 TRUE TRUE ion 374 Superviso r
4 21060367 Construct0,93525134 FALSE FALSE ion 378 Superviso r
5 27246366 Construct0,93265402 TRUE TRUE ion 113 Superviso r
1 28471099 Creative 0,95301154 FALSE TRUE Director / 037 Manager
2 17781039 Creative 0,94832125 FALSE FALSE Director / 768 Manager
3 139647Creative 0,94778642 FALSE TRUE 44 Director / 338 Manager
4 24589765 Creative 0,94770073 FALSE TRUE Director / 135 Manager
5 81508860 Creative 0,94718951 TRUE TRUE Director / 609 Manager
1 18905648 Digital 0,95532232 TRUE TRUE and Social 582
232

## Media Executive
2 18354623 Digital 0,95427733 TRUE TRUE and Social 245 Media Executive
3 16276121 Digital 0,95413601 FALSE FALSE and Social 868 Media Executive
4 34712719 Digital 0,95254425 FALSE TRUE and Social 674 Media Executive
5 70750649 Digital 0,95190864 TRUE FALSE and Social 079 Media Executive
1 26932091 Digital 0,96116105 FALSE FALSE Banking 445 Officer
2 16276121 Digital 0,95361831 FALSE TRUE Banking 744 Officer
3 29406313 Digital 0,95281143 FALSE TRUE Banking 795 Officer
4 14790629 Digital 0,95148194 FALSE TRUE Banking 96 Officer
5 28471099 Digital 0,94962122 FALSE FALSE Banking 248 Officer
1 35579812 Executive 0,95910795 FALSE TRUE Chef 737
2 29775391 Executive 0,95197461 TRUE TRUE Chef 137
3 21060367 Executive 0,95179754 FALSE TRUE Chef 364
4 16924102 Executive 0,94975172 TRUE TRUE Chef 649
233
5 10276858 Executive 0,94917443 TRUE FALSE Chef 926
1 23636277 Finance 0,95314943 TRUE TRUE Executive 892 / Accounta nt
Finance 0,95193142 20393721 4 FALSE TRUE Executive 231 / Accounta nt
3 70541112 Finance 0,95145781 TRUE TRUE Executive 621 / Accounta nt
4 24670867 Finance 0,95057662 TRUE TRUE Executive 607 / Accounta nt
Finance 0,94841625 24953921 5 FALSE FALSE Executive 525 / Accounta nt
1 34198885 Finance 0,96180731 TRUE TRUE Officer ( 275 Jr/Sr.)
2 25497147 Finance 0,96013593 FALSE TRUE Officer ( 54 Jr/Sr.)
3 20393721 Finance 0,95873292 FALSE TRUE Officer ( 409 Jr/Sr.)
4 53640713 Finance 0,95364184 FALSE TRUE Officer ( 681 Jr/Sr.)
Finance 0,95358845 28522529 5 FALSE FALSE Officer ( 272 Jr/Sr.)
1 70541112 Financial 0,94199541 TRUE TRUE Consolida621
234
tion Consultan t
2 27330027 Financial 0,93921073 FALSE FALSE Consolida855 tion Consultan t
3 139647Financial 0,93592154 FALSE TRUE 44 Consolida062 tion Consultan t
4 18365443 Financial 0,93426275 FALSE TRUE Consolida198 tion Consultan t
5 15363277 Financial 0,93415592 FALSE TRUE Consolida481 tion Consultan t
1 18354623 Graphics 0,96004322 TRUE FALSE Designer 242
2 18460045 Graphics 0,95344821 TRUE TRUE Designer 538
3 16276121 Graphics 0,95313185 TRUE FALSE Designer 897
4 70750649 Graphics 0,95283034 TRUE FALSE Designer 428
5 22754014 Graphics 0,95188643 TRUE FALSE Designer 807
1 30862904 HR 0,96005553 TRUE FALSE Specialist 505
2 16877897 HR 0,95697242 TRUE FALSE Specialist 647
3 26932091 HR 0,95026145 FALSE FALSE Specialist 406
4 24508725 HR 0,94613601 TRUE TRUE Specialist 144
235
5 11289482 HR 0,94532404 FALSE FALSE Specialist 462
1 28471099 INFORMA0,95299813 FALSE FALSE TION & 197 TECHNOL OGY STAFF
INFORMA0,94698002 16911115 2 FALSE TRUE TION & 961 TECHNOL OGY STAFF
3 26932091 INFORMA0,94668215 FALSE FALSE TION & 773 TECHNOL OGY STAFF
4 10839851 INFORMA0,94613301 TRUE TRUE TION & 73 TECHNOL OGY STAFF
INFORMA0,94429405 10549585 4 FALSE FALSE TION & 569 TECHNOL OGY STAFF
1 24589765 Junior 0,94896885 FALSE FALSE Associate 544 Lawyer
2 26330995 Junior 0,94563412 FALSE FALSE Associate 09 Lawyer
3 27375577 Junior 0,94149184 FALSE FALSE Associate 355 Lawyer
4 28471099 Junior 0,93983513 FALSE FALSE Associate 781 Lawyer
Junior 0,93922795 11289482 1 FALSE FALSE Associate 01 Lawyer
1 26932091 Junior 0,94111212 FALSE FALSE Designer 762
236
for Apparel
2 23917826 Junior 0,93517944 FALSE FALSE Designer 4 for Apparel
3 28745844 Junior 0,93441925 FALSE FALSE Designer 132 for Apparel
4 20553895 Junior 0,93177233 FALSE FALSE Designer 528 for Apparel
5 70750649 Junior 0,93139741 FALSE FALSE Designer 978 for Apparel
1 21060367 Manager 0,94595665 FALSE FALSE Aviation 999 Safety, Quality and Security
2 13195436 Manager 0,94253601 TRUE TRUE Aviation 008 Safety, Quality and Security
3 12333703 Manager 0,94204963 FALSE FALSE Aviation 615 Safety, Quality and Security
Manager 0,94005264 29167286 2 TRUE TRUE Aviation 723 Safety, Quality and Security
5 35651876 Manager 0,93942154 FALSE FALSE Aviation 969 Safety,
237

## Quality and Security
1 14667957 Medical 0,93799452 FALSE TRUE Doctor 709
2 28745844 Medical 0,93711135 FALSE TRUE Doctor 42
3 15958967 Medical 0,93456411 FALSE TRUE Doctor 05
4 24588864 Medical 0,93191054 FALSE TRUE Doctor 3
5 96260484 Medical 0,93102413 FALSE TRUE Doctor 31
Productio0,94403331 54100393 4 FALSE TRUE n 022 Engineeri ng
2 22861181 Productio0,93937313 FALSE TRUE n 832 Engineeri ng
3 11890896 Productio0,93868301 TRUE FALSE n 222 Engineeri ng
4 15850434 Productio0,93808163 FALSE TRUE n 317 Engineeri ng
5 11522068 Productio0,93673805 FALSE TRUE n 258 Engineeri ng
1 28290448 Public 0,94752461 TRUE TRUE Relations 991 Officer
2 70750649 Public 0,94427862 TRUE FALSE Relations 542 Officer
3 13115648 Public 0,94239685 FALSE FALSE Relations 156 Officer
238
4 27000192 Public 0,94184733 TRUE FALSE Relations 849 Officer
5 22732234 Public 0,94130684 TRUE TRUE Relations 995 Officer
1 26888302 Quality 0,93971453 FALSE FALSE Control 7 Superviso r - Corn Commodi ty
2 28628090 Quality 0,93745731 FALSE FALSE Control 193 Superviso r - Corn Commodi ty
3 22861181 Quality 0,93529064 FALSE TRUE Control 635 Superviso r - Corn Commodi ty
4 20905088 Quality 0,93360732 FALSE TRUE Control 888 Superviso r - Corn Commodi ty
5 21060367 Quality 0,93345635 FALSE FALSE Control 762 Superviso r - Corn Commodi ty
1 26932091 Regional 0,95379643 TRUE TRUE Sales 128 Manager
2 27715131 Regional 0,93888971 TRUE TRUE Sales 552 Manager
3 14790629 Regional 0,93827424 FALSE FALSE Sales 131 Manager
239
4 23917826 Regional 0,93816685 FALSE TRUE Sales 276 Manager
5 14070138 Regional 0,93812972 TRUE TRUE Sales 179 Manager
1 14790629 Spare part 0,95410405 FALSE FALSE Admin 064
Spare part 0,95299972 26932091 2 FALSE FALSE Admin 728
Spare part 0,94873593 16378091 3 FALSE TRUE Admin 951
Spare part 0,94769894 28745844 1 TRUE TRUE Admin 518
5 23917826 Spare part 0,94741614 FALSE TRUE Admin 594
1 28772892 Teachers 0,96508215 TRUE TRUE 12
2 15850434 Teachers 0,96144042 TRUE TRUE 383
3 58105060 Teachers 0,95251034 TRUE FALSE 733
4 20399718 Teachers 0,94827501 TRUE TRUE 764
5 46055835 Teachers 0,94762723 FALSE FALSE 471
1 26932091 Unmanag0,95952021 TRUE TRUE ed 941 Merchant Engagem ent Senior Associate, BPO Field Sales
2 29406313 Unmanag0,94284942 TRUE TRUE ed 614 Merchant Engagem ent Senior Associate, BPO Field Sales
240
3 11289482 Unmanag0,94004994 TRUE TRUE ed 924 Merchant Engagem ent Senior Associate, BPO Field Sales
4 30862904 Unmanag0,93887575 FALSE FALSE ed 821 Merchant Engagem ent Senior Associate, BPO Field Sales
5 24589765 Unmanag0,93886793 TRUE TRUE ed 936 Merchant Engagem ent Senior Associate, BPO Field Sales
241

## LAMPIRAN DGRAFIK GARIS TIGA PARAMETER SETIAP KUALIFIKASI LOWONGAN KERJA
242
243
244
245
246
247
248
249
250
251
252
253