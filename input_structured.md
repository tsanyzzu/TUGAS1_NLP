# IMPLEMENTASI IMPROVED SQRT-COSINE SIMILARITY
# UNTUK PEMERINGKATAN RESUME BERDASARKAN
# KUALIFIKASI LOWONGAN KERJA
# SKRIPSI
## Untuk memenuhi sebagian persyaratan
memperoleh gelar Sarjana Komputer

## Disusun oleh
## Khansa Salsabila Sangdiva Laksono
# NIM: 215150201111068
# TEKNIK INFORMATIKA
# DEPARTEMEN TEKNIK INFORMATIKA
# FAKULTAS ILMU KOMPUTER
# UNIVERSITAS BRAWIJAYA
# MALANG
# 2025
# PERNYATAAN ORISINALITAS
Saya menyatakan dengan sebenar-benarnya bahwa sepanjang pengetahuan
saya, di dalam naskah skripsi ini tidak terdapat karya ilmiah yang pernah diajukan
oleh orang lain untuk memperoleh gelar akademik di suatu perguruan tinggi, dan
tidak terdapat karya atau pendapat yang pernah ditulis atau diterbitkan oleh orang
lain, kecuali yang secara tertulis disitasi dalam naskah ini dan disebutkan dalam
daftar referensi.
Apabila ternyata didalam naskah skripsi ini dapat dibuktikan terdapat unsur-
unsur plagiasi, saya bersedia skripsi ini digugurkan dan gelar akademik yang telah
saya peroleh (sarjana) dibatalkan, serta diproses sesuai dengan peraturan
perundang-undangan yang berlaku (UU No. 20 Tahun 2003, Pasal 25 ayat 2 dan
Pasal 70).
Malang, 3 Juli 2025

## Khansa Salsabila Sangdiva Laksono
# NIM: 215150201111068
iii

# PRAKATA
Puji syukur penulis panjatkan ke hadirat Allah SWT yang telah melimpahkan
rahmat dan hidayah-Nya sehingga penulis dapat menyelesaikan skripsi yang
berjudul “Implementasi Improved Sqrt-Cosine Similarity Untuk Pemeringkatan
Resume Berdasarkan Kualifikasi Lowongan Kerja”. Penulis menyadari bahwa
dalam penyusunan skripsi tidak terwujud tanpa adanya dukungan, bimbingan,
arahan, serta doa yang tiada hentinya dari berbagai pihak. Pada kesempatan kali
ini penulis mengucapkan terima kasih sebesar-besarnya kepada:

# Bapak Rizal Setya Perdana, S.Kom., M.Kom., Ph.D. selaku dosen pembimbing
satu yang telah menyetujui dan mengarahkan penulis sehingga dapat
menyelesaikan skripsi ini.

# Ibu Ir. Indriati, S.T., M.Kom. selaku dosen pembimbing dua yang telah
menyetujui dan membimbing dalam penulisan untuk pengerjaan skripsi ini.

# Bapak Bayu Priyambadha, S.Kom., M.Kom., Ph.D. selaku Ketua Program Studi
Teknik Informatika Fakultas Ilmu Komputer Universitas Brawijaya.

# Bapak Sabriansyah Rizqika Akbar, S.T., M.Eng., Ph.D. selaku Ketua Departemen
Teknik Informatika Fakultas Ilmu Komputer Universitas Brawijaya.

# Rajiv Maulana selaku validator dalam skripsi ini, serta seluruh rekan kerja
penulis yang telah berkontribusi dalam memperluas wawasan dan
pengetahuan penulis selama proses penelitian.

# Ayah Tripinto Laksono, S.Kom. dan Bunda Dian Laksono selaku kedua orang tua
penulis, Sangkaisar Laksono selaku adik penulis, dan seluruh keluarga penulis
yang senantiasa memberikan dukungan, doa, dan motivasi sehingga dapat
menyelesaikan skripsi ini.

# P4OP Dinas Pendidikan Jakarta selaku penyelenggara beasiswa KJMU yang
membantu penulis dalam menyelesaikan studi sarjana.

# Seluruh teman tercinta penulis hingga saat ini yang telah menjadi teman diskusi
selama proses penelitian, teman seperjuangan, serta sumber motivasi,
terutama Salsabila Rachmayani, Kirana Alivia, Nathania Putri, Aidah Az Zahra,
Raditya Atmaja, Roiyan Zain, Ade Arya, Nadhira Nurannisa, Saqina Salsabila,
Ghania Tanziela, Gustav Ali, Emilia Putri, Farel Rakha, Aldiansyah, Dzaki Rafif,
Bagas Antarino, Safia Putri, Rayshanda Yuwandina, Arkan, Alka, Faqih, Audrey,
Aelissa, Dina, Kurnia, dan Zahra.
Malang, 25 Juni 2025

## Penulis
khansalaksono@gmail.com
iv

# ABSTRAK
Khansa Salsabila Sangdiva Laksono, Implementasi Improved Sqrt-Cosine
Similarity Untuk Pemeringkatan Resume Berdasarkan Kualifikasi Lowongan

## Kerja
Pembimbing: Rizal Setya Perdana, S.Kom., M.Kom., Ph.D. dan Indriati, Ir., S.T.,
M.Kom.
Ketidaksesuaian antara kualifikasi pelamar dengan kebutuhan penyedia
lowongan kerja dapat menjadi salah satu penyebab fenomena pengangguran.
Penelitian ini menggunakan pendekatan representasi teks TF-IDF dan Word2Vec
untuk implementasi perhitungan similaritas Improved Sqrt-Cosine (ISC) antara
resume dengan kualifikasi lowongan kerja, memeringkat lima resume per
kualifikasi lowongan kerja, dan dievaluasi hasilnya oleh seorang ahli dengan dua
skenario yang melibatkan pemberian bobot pada setiap section dalam resume.
Hasil penelitian ini menunjukkan keunggulan pada Word2Vec dengan ISC pada
skenario tanpa bobot section dan Word2Vec dengan Cosine Similarity pada
skenario dengan bobot section. TF-IDF dengan ISC menunjukkan performa terbaik
dalam menghasilkan lima resume yang isiannya relevan dengan deskripsi
lowongan kerja. Meskipun implementasi ISC dengan representasi teks Word2Vec
unggul karena masih cukup mampu menangkap hubungan semantik kata kunci,
tetap kurang disarankan karena mengaburkan hubungan semantik asli akibat nilai
absolut. Jika preferensi bobot section dapat menimbulkan bias karena kurang
mencerminkan variasi preferensi rekruter pada umumnya, maka implementasi ISC
dengan TF-IDF lebih disarankan untuk digunakan.
Kata kunci: similaritas resume, pemeringkatan, improved sqrt-cosine, spearman
v

# ABSTRACT
Khansa Salsabila Sangdiva Laksono, The Implementation of Improved Sqrt-
Cosine Similarity for Resume Ranking Based on Job Vacancy Qualifications
Supervisors: Rizal Setya Perdana, S.Kom., M.Kom., Ph.D. and Indriati, Ir., S.T.,
M.Kom.
The mismatch between a job applicant's qualifications and the requirements of
job providers can contribute to the phenomenon of unemployment. This research
employs TF-IDF and Word2Vec text representation approaches to implement the
Improved Sqrt-Cosine (ISC) similarity calculation between resumes and job
vacancy qualifications, ranking the top five resumes per job qualification, and
evaluating the results by an expert using two scenarios involving the weighting of
resume sections. The results indicate that Word2Vec with ISC performs best in the
scenario without section weighting, while Word2Vec with Cosine Similarity excels
in the scenario with section weighting. TF-IDF with ISC demonstrates the best
performance in generating the top five resumes with content relevant to the job
description. Although the implementation of ISC with Word2Vec performs best
because it is still quite capable of capturing the semantic relationships of
keywords, it is less recommended due to the distortion of original semantic
relationships caused by absolute value transformations. If section weighting
preferences introduce bias by not reflecting the general preferences of recruiters,
the implementation of ISC with TF-IDF is more recommended for use.
Keywords: resume similarity, ranking, improved sqrt-cosine, spearman
vi

# DAFTAR ISI
PENGESAHAN ........................................................................................................... ii
PERNYATAAN ORISINALITAS ................................................................................... iii
PRAKATA.................................................................................................................. iv
ABSTRAK ................................................................................................................... v
ABSTRACT ................................................................................................................ vi
DAFTAR ISI .............................................................................................................. vii
DAFTAR TABEL .......................................................................................................... x
DAFTAR GAMBAR .................................................................................................. xiii
DAFTAR LAMPIRAN ................................................................................................ xv

# BAB 1 PENDAHULUAN ...................................................................................... 1
## Latar Belakang ................................................................................. 1
## Rumusan Masalah ........................................................................... 2
## Tujuan .............................................................................................. 2
## Manfaat ........................................................................................... 3
## Batasan Masalah ............................................................................. 3
## Sistematika Pembahasan ................................................................ 3
# BAB 2 LANDASAN KEPUSTAKAAN ..................................................................... 5
## Kajian Pustaka ................................................................................. 5
## Dasar Teori ...................................................................................... 7
### Resume .................................................................................... 7
### Similaritas Teks ........................................................................ 8
### Pra-pemrosesan Teks .............................................................. 9
### TF-IDF .................................................................................... 10
### Word2Vec .............................................................................. 12
### Improved Sqrt-Cosine Similarity ............................................ 13
### Cosine Similarity .................................................................... 14
### Human-Level Performance .................................................... 14
### Spearman Rank Correlation Coefficient (SRCC) .................... 15
# BAB 3 METODOLOGI ....................................................................................... 16
vii

## Tipe Penelitian ............................................................................... 16
## Strategi Penelitian ......................................................................... 16
## Lokasi Penelitian ............................................................................ 16
## Metode Pengumpulan Data .......................................................... 16
## Metode Analisis Data .................................................................... 17
## Metode Evaluasi ............................................................................ 17
## Peralatan Pendukung .................................................................... 18
### Perangkat Lunak (Software) .................................................. 18
### Perangkat Keras (Hardware) ................................................. 18
## Perancangan Algoritma ................................................................. 18
# BAB 4 PERANCANGAN .................................................................................... 20
## Deskripsi Umum ............................................................................ 20
## Preprocessing ................................................................................ 20
### Ekstraksi Section .................................................................... 20
### Preprocessing Isian Resume .................................................. 25
### Preprocessing Penamaan Section ......................................... 27
### Preprocessing Kualifikasi Lowongan Kerja ............................ 29
## Perhitungan Representasi Teks ..................................................... 30
### TF-IDF .................................................................................... 30
### Word2Vec .............................................................................. 33
## Perhitungan Similaritas ................................................................. 36
### Improved Sqrt-Cosine Similarity ............................................ 36
### Cosine Similarity .................................................................... 38
## Perhitungan Korelasi ..................................................................... 40
## Perhitungan Relevansi dan Senioritas........................................... 42
## Perhitungan Manual...................................................................... 44
### Data Uji .................................................................................. 44
### Perhitungan Manual Ekstraksi Section .................................. 45
### Perhitungan Manual Preprocessing Resume ........................ 46
### Perhitungan Manual Preprocessing Kualifikasi
Lowongan Kerja .................................................................................... 59

### Perhitungan Manual Representasi Teks ............................... 61
viii

### Perhitungan Manual Similaritas ............................................ 94
### Skenario Pengujian .............................................................. 101
# BAB 5 IMPLEMENTASI................................................................................... 105
## Implementasi Kode Program Import Libraries dan Load
Dataset ..................................................................................................... 105

## Implementasi Kode Program Preprocessing Resume ................. 108
## Implementasi Kode Program Preprocessing Kualifikasi
Lowongan Kerja ....................................................................................... 118

## Implementasi Kode Program Representasi Teks TF-IDF ............. 120
## Implementasi Kode Program Representasi Teks Word2Vec
# 121
## Implementasi Kode Program Perhitungan Similaritas ................ 123
### Implementasi Kode Program Improved Sqrt-Cosine
Similarity............................................................................................. 123

### Implementasi Kode Program TF-IDF dan Improved
Sqrt-Cosine Similarity ......................................................................... 124

### Implementasi Kode Program Word2Vec dan Cosine
Similarity............................................................................................. 129

### Implementasi Kode Program Word2Vec dan
Improved Sqrt-Cosine Similarity ......................................................... 134

## Implementasi Kode Program Pengujian ..................................... 139
### Implementasi Kode Program Perhitungan SRCC ................ 139
### Implementasi Kode Program Perhitungan Relevansi
dan Senioritas ..................................................................................... 144

# BAB 6 PENGUJIAN DAN ANALISIS HASIL ....................................................... 150
## Pengujian ..................................................................................... 150
## Analisis Hasil ................................................................................ 156
# BAB 7 PENUTUP ............................................................................................ 165
## Kesimpulan .................................................................................. 165
## Saran ............................................................................................ 166
ix

# DAFTAR TABEL
Tabel 1.1 Tingkat pengangguran 7 negara ASEAN World Economic Outlook ........ 1
Tabel 2.1 Hasil eksperimen pertama penelitian oleh Ahmad Alsharef dkk. ........... 5
Tabel 2.2 Hasil eksperimen kedua penelitian oleh Ahmad Alsharef dkk. ............... 6
Tabel 4.1 Data uji resume untuk perhitungan manual ......................................... 44
Tabel 4.2 Data uji kualifikasi lowongan kerja untuk perhitungan manual ........... 45
Tabel 4.3 Hasil perhitungan manual ekstraksi section .......................................... 45
Tabel 4.4 Hasil perhitungan manual preprocessing resume bagian menghapus
email ...................................................................................................................... 46
Tabel 4.5 Hasil perhitungan manual preprocessing resume bagian menghapus
nomor telepon ...................................................................................................... 47
Tabel 4.6 Hasil perhitungan manual preprocessing resume bagian menghapus
berbagai tipe tanda minus (－, –, —) ................................................................... 48
Tabel 4.7 Hasil perhitungan manual preprocessing resume bagian menghapus
nama bulan ............................................................................................................ 48
Tabel 4.8 Hasil perhitungan manual preprocessing resume bagian menghapus kata
“Present” dan “Current” ........................................................................................ 49
Tabel 4.9 Hasil perhitungan manual preprocessing resume bagian menghapus
tanggal ................................................................................................................... 50
Tabel 4.10 Hasil perhitungan manual preprocessing resume bagian menghapus
placeholder ............................................................................................................ 51
Tabel 4.11 Hasil perhitungan manual preprocessing resume bagian menghapus
tanda baca ............................................................................................................. 52
Tabel 4.12 Hasil Perhitungan manual preprocessing resume bagian menghapus
angka ..................................................................................................................... 53
Tabel 4.13 Hasil perhitungan manual preprocessing resume bagian menghapus
spasi kosong berlebih ............................................................................................ 54
Tabel 4.14 Hasil perhitungan manual preprocessing resume bagian lematisasi dan
menghapus stop words ......................................................................................... 54
Tabel 4.15 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi nama section menjadi huruf kecil (lower casing) ........................... 55
Tabel 4.16 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi nama section menjadi huruf kecil (lower casing) ........................... 56
Tabel 4.17 hasil perhitungan manual penyetaraan nama section bagian
menyeragamkan pengelompokan section berdasarkan pemetaan ..................... 57
x
Tabel 4.18 Hasil perhitungan manual penyetaraan nama section bagian klasifikasi,
penghapusan, dan pengelompokan section tidak valid ........................................ 58
Tabel 4.19 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi isi resume menjadi huruf kecil (lower casing) ................................ 58
Tabel 4.20 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian mengonversi isi kualifikasi lowongan kerja menjadi huruf kecil (lower
casing) ................................................................................................................... 59
Tabel 4.21 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian menghapus angka ..................................................................................... 59
Tabel 4.22 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian menghapus tanda baca ............................................................................. 60
Tabel 4.23 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian menghapus spasi kosong berlebih ............................................................ 60
Tabel 4.24 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian lematisasi dan menghapus stop words ..................................................... 61
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
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah
normalisasi ............................................................................................................ 80
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
Tabel 4.49 Hasil skor similaritas resume ID 15265464 perhitungan manual
Improved Sqrt-Cosine Similarity ............................................................................ 96
Tabel 4.50 Bobot section kategori industri "TEACHER" ........................................ 96
Tabel 4.51 Vektor Word2Vec perhitungan manual Cosine Similarity .................. 97
Tabel 4.52 Hasil skor similaritas resume ID 15265464 perhitungan manual Cosine
Similarity................................................................................................................ 98
Tabel 4.53 Vektor Word2Vec perhitungan manual Improved Sqrt-Cosine Similarity
............................................................................................................................... 99
Tabel 4.54 Hasil skor similaritas resume ID 15265464 perhitungan manual
Improved Sqrt-Cosine Similarity .......................................................................... 100
Tabel 4.55 Peringkat 1-5 resume dengan skor similaritas terbesar untuk
perhitungan manual SRCC ................................................................................... 102
Tabel 4.56 Selisih peringkat 1-5 resume perhitungan manual SRCC .................. 102
Tabel 4.57 Peringkat 1-5 resume dengan hasil evaluasi relevansi dan senioritas ahli
terbesar untuk perhitungan manual ................................................................... 103
Tabel 6.1 Hasil pengujian berwarna hijau skenario tanpa bobot section ........... 156
Tabel 6.2 Hasil pengujian berwarna merah skenario tanpa bobot section ........ 157
Tabel 6.3 Hasil pengujian berwarna hijau skenario dengan bobot section ........ 158
Tabel 6.4 Hasil pengujian berwarna merah skenario dengan bobot section ..... 158
Tabel 6.5 Weighted score keseluruhan pendekatan dan skenario ..................... 159
Tabel 6.6 Urutan pendekatan berdasarkan weighted score tertinggi ................ 159
Tabel 6.7 Perhitungan rata-rata parameter setiap pendekatan dan skenario ... 160
Tabel 6.8 Perhitungan similaritas antar term Word2Vec vektor nilai asli dengan
vektor nilai absolut .............................................................................................. 161
xii

# DAFTAR GAMBAR
Gambar 2.1 Pengelompokan text similarity measure ............................................ 8
Gambar 2.2 Arsitektur pendekatan Skip-gram ..................................................... 12
Gambar 3.1 Struktur proses implementasi pemeringkatan similaritas resume dan
kualifikasi lowongan kerja ..................................................................................... 19
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
Gambar 6.8 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli dengan
vektor nilai absolut .............................................................................................. 161
Gambar 6.9 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli dengan
vektor nilai absolut .............................................................................................. 162
Gambar 6.10 Grafik garis tiga parameter setiap kualifikasi lowongan kerja ...... 163
xiv

# DAFTAR LAMPIRAN
# LAMPIRAN A SURAT PERNYATAAN VALIDITAS ................................................... 171
LAMPIRAN B BOBOT PER SECTION BERDASARKAN INDUSTRI ............................ 172

# LAMPIRAN C HASIL PEMERINGKATAN LIMA RESUME PER KUALIFIKASI
# LOWONGAN KERJA ............................................................................................. 180
# 1 Tanpa Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity............... 180
# 2 Tanpa Bobot - Word2Vec dan Cosine Similarity ................................ 190
# 3 Tanpa Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity ........ 201
# 4 Dengan Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity ............ 211
# 5 Dengan Bobot - Word2Vec dan Cosine Similarity ............................. 220
# 6 Dengan Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity
................................................................................................................. 231

# LAMPIRAN D GRAFIK GARIS TIGA PARAMETER SETIAP KUALIFIKASI
# LOWONGAN KERJA ............................................................................................. 242
xv

# BAB 1 PENDAHULUAN
Bab pendahuluan membahas mengenai latar belakang penelitian, rumusan
masalah, tujuan, manfaat, batasan masalah, serta sistematika pembahasan dari
penelitian ini.

## Latar Belakang
Tingkat pengangguran yang tinggi merupakan salah satu tantangan utama
yang dihadapi Indonesia. Masalah ini tidak hanya mempengaruhi kondisi
perekonomian, tetapi juga kesejahteraan sosial masyarakat. Perkembangan
ketenagakerjaan sangat penting bagi stabilitas ekonomi, dan setiap hambatan
dalam aspek ini dapat berdampak negatif pada upaya meningkatkan taraf hidup
masyarakat.
Tabel 1.1 Tingkat pengangguran 7 negara ASEAN World Economic Outlook

## No Negara Tingkat Pengangguran
# Indonesia 5,2
# Filipina 5,1
# Brunei Darussalam 4,9
# Malaysia 3,5
# Viet Nam 2,1
# Singapore 1,9
# Thailand 1,1
Tabel 1.1 menunjukkan data yang diambil dari World Economic Outlook pada
April 2024 oleh International Monetary Fund, di antara 7 negara ASEAN yang
datanya tercantum, Indonesia memiliki tingkat pengangguran tertinggi di angka

# ,2. Pengangguran bisa disebabkan oleh beberapa fenomena dan salah satunya
adalah ketidaksesuaian antara karakteristik pencari kerja dengan tawaran kerja
atau bisa disebut dengan pengangguran struktural (Kementerian Ketenagakerjaan
RI - Badan Perencanaan dan Pengembangan Ketenagakerjaan, 2021). Sumber
daya, kualifikasi, keterampilan, dan pengetahuan yang tersedia dan diperoleh oleh
individu untuk memaksimalkan kemampuan kerja mereka sendiri disebut dengan
human capital. Nilai-nilai ini berkontribusi pada pendapatan yang lebih tinggi,
kepuasan hidup, dan kohesi sosial, sehingga juga menjadi salah satu penentu
pertumbuhan ekonomi negara (Wujarso, 2022).

# 1
Proses mencari dan melamar pekerjaan identik dengan penggunaan
curriculum vitae (CV) atau beberapa orang menyebutnya resume. Tahapan awal
perekrutan adalah proses screening CV yang selanjutnya diikuti dengan proses
wawancara. Rekrutmen dianggap efektif ketika mendapatkan banyak pelamar
yang sesuai dengan kualifikasi untuk mendapatkan calon karyawan terbaik dari
yang terbaik (Budiantoro dalam Kumaladewi, 2018).
Terdapat beberapa penelitian sebelumnya yang berkaitan dengan perhitungan
similaritas teks untuk otomatisasi penyaringan resume. Pertama, penelitian oleh
Ahmad Alsharef dkk. (2023) membandingkan pendekatan Cosine Similarity, Sqrt-
Cosine Similarity, dan Improved Sqrt-Cosine (ISC) Similarity, menggunakan TF-IDF
sebagai metode vektorisasi teks, dan menunjukkan bahwa pendekatan ISC
dianggap lebih baik dibandingkan dua pendekatan lainnya. Kedua, penelitian oleh
Rahul Singh Pundir dkk. (2024) mengembangkan sistem rekomendasi resume
berbasis keterampilan, menggunakan Word2Vec untuk menangkap kesamaan
semantik keterampilan dan Cosine Similarity untuk mengukur kesesuaian antara
vektor keterampilan dengan kebutuhan pekerjaan. Merujuk pada penelitian
sebelumnya, penelitian ini bertujuan untuk mengimplementasikan Improved Sqrt-
Cosine (ISC) Similarity dalam memeringkat resume berdasarkan kualifikasi
lowongan kerja, dengan mengeksplorasi metode representasi teks TF-IDF dan
Word2Vec.

## Rumusan Masalah
Berikut ini merupakan rumusan masalah penelitian.

# Bagaimana hasil pemeringkatan lima resume untuk setiap kualifikasi
lowongan kerja menggunakan Improved Sqrt-Cosine Similarity dalam
mengkalkulasikan similaritas teks?

# Bagaimana korelasi antara peringkat hasil implementasi Improved Sqrt-
Cosine Similarity dengan peringkat hasil evaluasi ahli untuk setiap
kualifikasi lowongan kerja menggunakan Spearman Rank Correlation
Coefficient?

## Tujuan
Berikut ini merupakan tujuan penelitian ini.

# Menganalisis hasil pemeringkatan lima resume untuk setiap kualifikasi
lowongan kerja menggunakan Improved Sqrt-Cosine Similarity dalam
mengkalkulasikan similaritas teks.

# Menganalisis korelasi antara peringkat hasil implementasi Improved Sqrt-
Cosine Similarity dengan peringkat hasil evaluasi ahli untuk setiap
kualifikasi lowongan kerja menggunakan Spearman Rank Correlation
Coefficient.

# 2
## Manfaat
Berikut merupakan manfaat yang dapat diperoleh dari penelitian ini.

# Memberikan interpretasi hasil Improved Sqrt-Cosine Similarity dalam
menghasilkan perhitungan similaritas teks pada pemeringkatan lima
resume untuk setiap kualifikasi lowongan kerja.

# Memberikan pemaparan mengenai korelasi antara peringkat hasil
Improved Sqrt-Cosine Similarity dengan peringkat hasil evaluasi ahli
menggunakan Spearman Rank Correlation Coefficient.

## Batasan Masalah
Batasan masalah yang ditetapkan dalam penelitian ini sebagai berikut.

# Penelitian ini terbatas pada dataset Kaggle dengan 2.484 resume.
# Penelitian ini berfokus pada pemeringkatan lima resume berdasarkan nilai
similaritas tertinggi untuk setiap kualifikasi lowongan kerja.

# Penelitian ini melibatkan seorang ahli di bidang rekrutmen dalam
mengevaluasi hasil pemeringkatan.

# Kualifikasi lowongan kerja yang digunakan diambil dari 24 posisi di portal
lowongan pekerjaan https://id.jobstreet.com/.

## Sistematika Pembahasan
Susunan sistematika pembahasan ditulis di bawah ini dan terdiri dari beberapa
bab yang menjelaskan mengenai penelitian mengenai kalkulasi similaritas teks
pada resume pelamar dengan kualifikasi lowongan kerja.

# BAB 1 PENDAHULUAN
Bab pendahuluan membahas mengenai latar belakang penelitian, rumusan
masalah, tujuan, manfaat, batasan masalah, serta sistematika pembahasan dari
penelitian ini.

# BAB 2 LANDASAN KEPUSTAKAAN
# andasan kepustakaan berisi kajian pustaka dan dasar teori. Penelitian-
penelitian sebelumnya yang berhubungan dengan kalkulasi similaritas teks pada
resume dijelaskan pada kajian pustaka. Sedangkan, penjelasan teori, konsep, dan
metode yang digunakan dijelaskan pada dasar teori.

# BAB 3 METODOLOGI PENELITIAN
Terdapat beberapa bagian di bab metodologi penelitian, seperti tipe
penelitian, strategi penelitian, lokasi penelitian, metode pengumpulan data,
metode analisis data, peralatan pendukung, dan perancangan algoritma.

# BAB 4 PERANCANGAN
Bab perancangan menjelaskan tentang perancangan algoritma dari metode-
metode serta flow diagram dari setiap algoritma yang digunakan pada penelitian
ini. Selain itu, bab ini juga merincikan perhitungan manual.

# 3
# BAB 5 IMPLEMENTASI
# mplementasi berisi implementasi dari metode kalkulasi similaritas teks
pada resume pelamar dengan kualifikasi instansi yang digunakan pada penelitian
ini, seperti metode perhitungan similaritas Improved Sqrt-Cosine (ISC) dan Cosine
Similarity (CosSim), serta metode representasi teks TF-IDF dan Word2Vec.

# BAB 6 PENGUJIAN DAN ANALISIS HASIL
Pemaparan hasil dari pengujian akan dijelaskan di bab pengujian, serta
pembahasan dan analisa dari hasil pengujian tersebut sebagai bahan evaluasi.

# BAB 7 PENUTUP
Terakhir, kesimpulan dan saran ditulis pada bab penutup. Bagian kesimpulan
memaparkan rangkuman dari hasil penelitian untuk menjawab semua rumusan
masalah yang dijabarkan pada latar belakang. Sedangkan, bagian saran
memaparkan masukan-masukan untuk penelitian selanjutnya agar penelitian ini
dapat diperbaiki dan dikembangkan.

# 4
# BAB 2 LANDASAN KEPUSTAKAAN
# andasan kepustakaan berisi kajian pustaka dan dasar teori. Penelitian-
penelitian sebelumnya yang berhubungan dengan kalkulasi similaritas teks pada
resume dijelaskan pada kajian pustaka. Sedangkan, penjelasan teori, konsep, dan
metode yang digunakan dijelaskan pada dasar teori.

## Kajian Pustaka
Terdapat beberapa penelitian yang dilakukan sebelumnya terkait perhitungan
similaritas teks untuk otomatisasi penyaringan resume. Penelitian pertama
dilakukan oleh Ahmad Alsharef dkk. (2023) berjudul "Exploring the Efficiency of
Text-Similarity Measures in Automated Resume Screening for Recruitment"
mengeksplorasi penggunaan text similarity sebagai alternatif dalam memproses
resume, dengan pendekatan Cosine Similarity, Sqrt-Cosine Similarity, dan
Improved Sqrt-Cosine (ISC) Similarity. Terdapat dua eksperimen dalam penelitian
ini. Eksperimen pertama melibatkan 40 resume yang disandingkan dengan
deskripsi pekerjaan untuk posisi manajer pengembangan bisnis di salah satu
platform terkemuka untuk manajemen kepatuhan UKM di Eropa. Pada lima urutan
teratas peringkat resume, dilakukan perbandingan antara peringkat yang
diberikan oleh manusia dan pengukuran otomatis, hasilnya tertera pada Tabel 2.1
Tabel 2.1 Hasil eksperimen pertama penelitian oleh Ahmad Alsharef dkk.
Human ISC Sqrt-Cosine Cosine

## Ranking of
## Resumes
# 2 (0,38) 11 (28,545) 7 (43,02)
# 3 (0,345) 2 (32,732) 1 (48,44)
# 1 (0,391) 9 (28,87) 4 (44,29)
# 4 (0,344) 17 (26,749) 14 (38,5)
# 8 (0,302) 1 (32,733) 15 (38,2)
Eksperimen kedua melibatkan 30 resume yang disandingkan dengan deskripsi
pekerjaan untuk posisi software engineer di salah satu perusahaan teknologi
multinasional Amerika. Pada lima urutan teratas peringkat resume, dilakukan
perbandingan antara peringkat yang diberikan oleh manusia dan pengukuran
otomatis, yang hasilnya tertera pada Tabel 2.2.

# 5
Tabel 2.2 Hasil eksperimen kedua penelitian oleh Ahmad Alsharef dkk.
Human ISC Sqrt-Cosine Cosine

## Ranking of
## Resumes
# 8 (0,181) 6 (21,205) 11 (18,47)
# 1 (0,246) 4 (22,136) 1 (26,99)
# 4 (0,199) 1 (22,744) 4 (22,25)
# 3 (0,206) 2 (22,65) 10 (18,52)
# 6 (0,181) 14 (18,708) 3 (24,36)
Berdasarkan hasil kedua eksperimen, hasil dari penelitian yang dilakukan oleh
Ahmad Alsharef dkk. (2023) menunjukkan bahwa peringkat Improved Sqrt-Cosine
(ISC) Similarity cenderung lebih mendekati peringkat yang diberikan oleh manusia.
Penelitian kedua dilakukan oleh Rahul Singh Pundir dkk. (2024) berjudul
"Enhancing Resume Recommendation System through Skill-based Similarity using
Deep Learning Models" membahas cara meningkatkan rekomendasi resume
dengan mempertimbangkan kesamaan keterampilan. Sistem ini menggunakan
metode Word2Vec untuk mengukur kecocokan kandidat dengan kebutuhan
pekerjaan berdasarkan skills dan LSTM-RNN untuk memprediksi profil pekerjaan.
Skor skill similarity dari penelitian ini berkisar dari 0,447 hingga 0,790, di mana nilai
yang lebih tinggi menunjukkan keterampilan kandidat lebih sesuai dengan
kebutuhan pekerjaan. Pendekatan ini juga membantu kandidat memahami
keterampilan tambahan yang perlu dikembangkan untuk memenuhi kualifikasi
posisi yang diinginkan.
Penelitian ketiga dilakukan oleh Chirag Daryani dkk. (2020) berjudul "An
Automated Resume Screening System Using Natural Language Processing and
Similarity" mengembangkan sistem rekomendasi yang mengekstraksi informasi
dari resume yang tidak terstruktur dan mengubahnya menjadi vektor yang
mewakili fitur-fitur penting seperti pendidikan, pengalaman, dan keterampilan.
Dengan menghitung kesamaan menggunakan Cosine Similarity antara resume dan
deskripsi pekerjaan, sistem ini mampu menyusun peringkat kandidat terbaik yang
sesuai dengan posisi pekerjaan yang ditawarkan. Hasil perhitungan Cosine
Similarity antara empat resume dan query pekerjaan menunjukkan bahwa resume
kandidat ke-2 menduduki peringkat pertama (0,680), diikuti resume kandidat ke-

# di peringkat kedua (0,651), resume kandidat ke-3 di peringkat ketiga (0,498), dan
resume kandidat ke-1 di peringkat terakhir (0,490).

# 6
Topik skripsi yang diambil memiliki beberapa kesamaan dengan penelitian
sebelumnya. Pertama, penelitian ini mengimplementasikan perhitungan
similaritas Improved Sqrt-Cosine (ISC), seperti pada penelitian pertama. Kedua,
cara menghitung similaritas dilakukan dengan membandingkan informasi yang
didapatkan dari resume dengan persyaratan atau kualifikasi posisi pekerjaan,
sebagaimana dilakukan pada penelitian pertama dan ketiga. Ketiga, penelitian ini
mengekstaksi informasi dari resume seperti pada penelitian ketiga, tetapi
berfokus pada pengambilan informasi per bagian (section) resume sesuai
standarisasi dari seorang ahli. Perbedaan dengan penelitian kedua adalah
penelitian tersebut menggunakan daftar skills yang diambil dari kumpulan resume
dan mengukur skill similarity-nya dengan resume yang digunakan. Sedangkan,
topik skripsi ini akan mengukur similarity dari suatu resume untuk melihat apakah
sesuai dengan yang dibutuhkan oleh suatu kualifikasi posisi pekerjaan. Meskipun
begitu, untuk tahap representasi teks juga akan menggunakan Word2Vec seperti
yang dilakukan pada penelitian kedua sebagai salah satu metode representasi teks
dari penelitian ini.

## Dasar Teori
### Resume
Resume menurut Kamus Besar Bahasa Indonesia (KBBI) merupakan kata
nominal yang berarti ikhtisar atau ringkasan. Stanford Career Education (2024)
menyatakan bahwa resume merupakan ringkasan pengalaman yang dipilih oleh
perekrut untuk menunjukkan kesesuaian pelamar dengan posisi yang dilamar.
Resume juga sering diartikan sama dengan Curriculum Vitae (CV), keduanya pun
memiliki definisi yang sama menurut Cambridge Dictionary (2024), yaitu sebuah
ringkasan tertulis yang menggambarkan latar belakang pendidikan, kualifikasi,
pengalaman kerja sebelumnya, serta minat pribadi seseorang dan dikirimkan
kepada instansi ketika melamar pekerjaan. Di Amerika Serikat, CV umumnya
digunakan saat melamar pekerjaan di bidang akademis, sedangkan resume
digunakan untuk pekerjaan lainnya (Cambridge University Press & Assessment,

# 2024
Perekrut hanya meluangkan kurang dari 30 detik untuk meninjau resume,
sehingga penting bagi pelamar untuk secara cepat dan jelas menunjukkan
bagaimana pelatihan dan pengalaman mereka dapat memberi nilai tambah bagi
perusahaan, serta memaparkan keterampilan secara tepat untuk memenuhi
kebutuhan perusahaan dengan format resume yang jelas, menarik, dan
disesuaikan dengan konvensi yang berlaku di setiap posisi atau sektor yang
dilamar (Stanford Career Education, 2018).

# 7
Stanford Career Education (2024) juga memberikan panduan dalam langkah-
langkah membuat resume, dikatakan bahwa resume yang efektif adalah ringkasan
singkat yang menyoroti pengalaman dan keterampilan yang langsung terkait
dengan pekerjaan. Informasi yang ingin disampaikan kepada perekrut mengenai
masing-masing pengalaman harus ditentukan dengan jelas, konten yang
difokuskan tergantung pada posisi yang dilamar karena setiap perekrut mencari
sekumpulan keterampilan tertentu dari pelamar yang sesuai dengan keterampilan
yang diperlukan untuk menjalankan pekerjaan tertentu (Stanford Career
Education, 2024). Saat mendeskripsikan keterampilan atau pencapaian yang
relevan, disarankan untuk menggunakan metode C-A-R: CONTEXT mencakup apa
yang dikerjakan, seperti tugas, proyek, atau tujuan keseluruhan yang tercapai,
serta pihak-pihak yang terlibat, seperti tim yang berkolaborasi dan/atau populasi
yang dilayani; ACTIONS menggambarkan bagaimana tugas tersebut dilaksanakan
dengan menekankan keterampilan yang digunakan untuk menyelesaikan tugas,
penggunaan action words sangat dianjurkan untuk mendeskripsikan tindakan
yang diambil; Terakhir, RESULTS menjelaskan apa hasilnya, kuantifikasi hasil harus
dilakukan jika memungkinkan, atau jika hasil tidak diketahui, penting untuk
menyertakan tujuan dari tugas, proyek, atau tujuan tersebut, yang menjelaskan
alasan pelaksanaan (Stanford Career Education, 2024).

## Similaritas Teks
Mengingat tujuan perekrut adalah mencari pelamar yang memiliki sekumpulan
keterampilan yang dibutuhkan oleh instansi untuk melaksanakan pekerjaan
tertentu, maka digunakan metode untuk menghitung similaritas antara kualifikasi
yang terdapat dalam resume pelamar dengan kualifikasi yang dibutuhkan oleh
instansi. Similaritas teks adalah membandingkan suatu teks dengan teks lainnya
dan menemukan persamaan di antara mereka. Pada dasarnya, ini tentang
menentukan tingkat kedekatan teks tersebut. Dalam pemrosesan bahasa alami,
menentukan apakah makna dari dua dokumen identik adalah tugas mendasar dan
luas yang memungkinkan komputer memahami bahasa manusia (He, et al., 2024).
Berbagai pendekatan telah dikembangkan untuk mengukur similaritas antara
satu teks dengan teks lainnya yang terbagi menjadi empat kelompok utama, yaitu
String-based, Corpus-based, Knowledge-based, dan Hybrid (Prasetya, et al., 2018).
Gambar 2.1 Pengelompokan text similarity measure
Sumber: Prasetya et al. (2018)

# 8
Seperti pada apa yang sudah diilustrasikan pada Gambar 2.1, String-based
adalah metode pengukuran tertua, paling sederhana, tetapi paling populer dan
beroperasi pada urutan string dan susunan karakter (Prasetya, et al., 2018).
Corpus-based menggunakan pendekatan semantik yang mana menentukan
kesamaan antara dua konsep berdasarkan informasi yang diekstraksi dari korpus
yang besar (Prasetya, et al., 2018). Knowledge-based menggunakan hubungan
semantik untuk mengidentifikasi tingkat kesamaan kata-kata (Prasetya, et al.,

# Selain tiga kelompok yang telah dijelaskan sebelumnya, terdapat
perhitungan similaritas secara Hybrid dengan tujuan untuk menggabungkan
metode yang telah disebutkan sebelumnya, termasuk String-based, Corpus-based,
dan Knowledge-based guna mencapai metrik yang lebih baik dengan mengadopsi
keunggulan masing-masing metode (Prasetya, et al., 2018).

## Pra-pemrosesan Teks
Sebelum menerapkan metode similaritas teks, diperlukan proses pra-
pemrosesan teks terlebih dahulu untuk menyiapkan dataset resume yang akan
diolah. Penting untuk melakukan pemrosesan data ini guna memastikan bahwa
data yang digunakan adalah data yang berkualitas sehingga dapat menghasilkan
akurasi yang akurat (Prasetya, et al., 2024). Adapun beberapa langkah selama
proses pra-pemrosesan teks, yaitu:

# Tokenization. Proses ini untuk memecahkan kalimat menjadi kata-kata
(Sohangir & Wang, 2017). Tools seperti NLTK dan spaCy biasa digunakan
untuk melakukan tokenisasi (Amin, et al., 2023).

# Lower Casing. Proses ini mengonversi semua teks menjadi huruf kecil
(Alsharef, et al., 2023).

# Stop Words. Proses ini untuk menghilangkan stop words, yaitu kata-kata
umum dalam dokumen yang tidak memiliki makna signifikan dan tidak
berkontribusi dalam membedakan dokumen, sehingga dapat diabaikan
(Sihombing, 2022). Bahasa pemrograman Python telah menyediakan
package Regular Expression (RegEx) untuk melaksanakan penghilangan
stop words (Amin, et al., 2023).

# Lemmatization. Tidak seperti stemming yang hanya mengubah kata
menjadi ke bentuk dasarnya, lemmatization memanfaatkan kosakata dan
morfologis yang sesuai dengan linguistik (Daryani, et al., 2020) sesuai
kamus bahasa yang digunakan. Untuk bahasa Inggris, dapat
memanfaatkan WordNet Lemmatizer yang tersedia melalui NLTK Python
(Daryani, et al., 2020).

# 9
## TF-IDF
Term Frequency-Inverse Document Frequency (TF-IDF) adalah salah satu teknik
yang digunakan untuk menghitung seberapa penting suatu kata (term) dalam
sebuah dokumen terhadap keseluruhan kumpulan dokumen (Septiani & Isabela,

# TF-IDF didapatkan dari hasil perkalian antara Term Frequency (TF) dan
Inverse Document Frequency (IDF) (Ramadhan, et al., 2023).

# 𝑇𝐹 −𝐼𝐷𝐹 = 𝑇𝐹 ×𝐼𝐷𝐹 (2.1)
(𝑡,𝑑) (𝑡,𝑑) (𝑡)
Adapun keterangan dari Persamaan 2.1:
𝑇𝐹 −𝐼𝐷𝐹 = Bobot TF-IDF pada term ke-𝑡 terhadap dokumen ke-𝑑
(𝑡,𝑑)
𝑇𝐹 = Frekuensi kemunculan term ke-𝑡 terhadap dokumen ke-𝑑
(𝑡,𝑑)
𝐼𝐷𝐹 = Nilai inverse dokumen yang memunculkan term ke-𝑡
(𝑡)
TF didapatkan dengan menghitung jumlah kemunculan kata dibagi dengan
total kata dalam dokumen (Septiani & Isabela, 2022). IDF menghitung seberapa
penting suatu kata dalam koleksi dokumen dengan membagi jumlah total
dokumen dengan jumlah dokumen yang mengandung suatu term (Septiani &
Isabela, 2022).
𝑓
𝑇𝐹 = 𝑡,𝑑 (2.2)
(𝑡,𝑑)
∑ 𝑓
𝑘 𝑘,𝑑
Adapun keterangan dari Persamaan 2.2:
𝑇𝐹 = Frekuensi kemunculan term ke-𝑡 terhadap dokumen ke-𝑑
(𝑡,𝑑)
𝑓 = Jumlah kemunculan term ke-𝑡 terhadap dokumen ke-𝑑
𝑡,𝑑
∑ 𝑓 = Total seluruh term terhadap dokumen ke-𝑑
𝑘 𝑘,𝑑

# 𝑁
𝐼𝐷𝐹 = log( ) (2.3)
(𝑡)
𝑑𝑓
Keterangan dari Persamaan 2.3:
𝐼𝐷𝐹 = Nilai inverse document frequency untuk term ke-𝑡
(𝑡)
𝑁 = Jumlah total dokumen
𝑑𝑓 = Banyaknya dokumen yang mengandung term

# 10
Dalam dokumentasi Scikit-learn, TF default tidak dinormalisasi dengan
membagi total term. Normalisasi baru dilakukan setelah mendapatkan hasil
perkalian TF dengan IDF menggunakan 𝐿 normalization, sehingga TF didapatkan

# 2
dari jumlah kemunculan (frekuensi) term terhadap suatu dokumen seperti pada
Persamaan 2.4
𝑇𝐹 = 𝑓 (2.4)
(𝑡,𝑑) 𝑡,𝑑

## Keterangan
𝑇𝐹 = Frekuensi kemunculan term ke-𝑡 terhadap dokumen ke-𝑑
(𝑡,𝑑)
𝑓 = Jumlah kemunculan term ke-𝑡 terhadap dokumen ke-𝑑
𝑡,𝑑
Pada dokumentasi Scikit-learn, IDF default menggunakan mekanisme
smoothing dengan menambahkan konstanta "1" pada pembilang dan penyebut,
seolah-olah ada dokumen tambahan yang mengandung setiap term dalam koleksi
tepat satu kali sehingga mencegah pembagian oleh nol. Rumusnya menjadi seperti
pada Persamaan 2.5

# +𝑁
𝐼𝐷𝐹 = log( )+1 (2.5)
(𝑡)

# +𝑑𝑓
## Keterangan
𝐼𝐷𝐹 = Nilai inverse document frequency untuk term ke-𝑡
(𝑡)
𝑁 = Jumlah total dokumen
𝑑𝑓 = Banyaknya dokumen yang mengandung term
Setelah mengalikan TF dan IDF, perhitungan TF-IDF dalam dokumentasi Scikit-
learn dinormalisasikan dengan 𝐿 normalization atau Euclidean norm, formula dari

# 2
normalisasi ini dapat tertera pada Persamaan 2.6
𝑣 𝑣
𝑣 = = (2.6)
𝑛𝑜𝑟𝑚 ‖𝑣‖ 2 √𝑣1 2+𝑣2 2+⋯+𝑣𝑛 2

## Keterangan
𝑣 = Vektor yang telah dinormalisasi
𝑛𝑜𝑟𝑚
𝑣 = Vektor asli sebelum dinormalisasikan
‖𝑣‖ = Akar kuadrat dari jumlah kuadrat semua elemen vektor 𝑣

# 2
# 11
## Word2Vec
Word2Vec adalah metode yang digunakan untuk menghasilkan word
embedding dengan memanfaatkan neural networks sederhana yang dilatih untuk
memahami konteks linguistik kata. Pendekatan ini menggunakan continuously
sliding Skip-gram atau continuously sliding Bag-of-Words (CBOW). Word2Vec
mengonversi kata-kata menjadi vektor, memungkinkan pengenalan hubungan
semantik dan telah menjadi kunci dalam perkembangan berbagai aplikasi Natural
Language Processing (NLP) (Kulshretha & Lodha, 2023). Pada pendekatan CBOW,
suatu kata diprediksi berdasarkan konteks yang mengelilinginya di dalam sebuah
kalimat. Sedangkan, pendekatan Skip-gram memprediksi konteks berdasarkan
kata yang diberikan (Meyer, 2016). Mengingat tujuan utama dari penelitian ini
adalah memperhitungkan similaritas teks, sehingga akan lebih fokus pada
penggunaan pendekatan Skip-gram yang arsitekturnya terlampir pada Gambar 2.2
Gambar 2.2 Arsitektur pendekatan Skip-gram
Sumber: Meyer (2016)
Skip-gram bekerja dengan menggunakan kata yang sedang diproses (current
word) sebagai input untuk mempelajari dan memprediksi kata-kata dalam konteks
sebagai target. Proses ini mempelajari distribusi probabilitas kata-kata dalam
sebuah kalimat berdasarkan jarak antara kata input dan kata-kata konteks
(windows) (Ayuningtyas & Tantyoko, 2024).

# 12
Dalam teknik Skip-gram, proses training dan inference dilakukan secara
terpisah. Selama proses training, skip-gram mempelajari konteks dari kata-kata
yang muncul di sekitar kata target dalam window tertentu. Sebagai contoh, jika
ukuran window adalah dua, maka kata-kata seperti 'Saya,' 'suka,' 'makan,' dan
'apel' menjadi konteks bagi kata 'apel' dalam kalimat 'Saya suka makan apel.'
Metode ini digunakan untuk menghasilkan distribusi probabilitas dari semua
kemungkinan konteks kata berdasarkan kata target (Dwivedi & Anand, 2023).
Pada dokumentasi Gensim, implementasinya menggunakan beberapa
parameter seperti sg yang ditetapkan dengan nilai 1 untuk memakai Skip-gram,
vector_size untuk menetapkan dimensi vektor-vektor kata, window untuk
menetapkan jarak maksimum antara kata saat ini dan kata yang diprediksi dalam
sebuah kalimat, alpha untuk menginisialisasi learning rate, dan epochs untuk
menetapkan iterasi yang secara default bernilai lima.

## Improved Sqrt-Cosine Similarity
Sohangir dan Wang (2017) memperkenalkan sebuah teknik pengukuran
similarity yang disebut Improved Sqrt-Cosine (ISC) similarity, yang didasarkan pada
normalisasi 𝐿 (Hellinger distance) dan telah terbukti bahwa pada data berdimensi

# 1
tinggi, normalisasi 𝐿 bekerja lebih baik daripada normalisasi 𝐿 (Euclidean

# 2
distance). Pada persamaan ISC, alih-alih menggunakan normalisasi 𝐿 , digunakan

# 1
akar kuadrat dari normalisasi 𝐿 (Sohangir & Wang, 2017). Sebagian besar

# 1
menganggap Cosine Similarity sebagai 'state of the art' dalam pengukuran
similarity (Sohangir & Wang, 2017). Melalui eksperimen yang mendalam, diamati
bahwa meskipun ISC mirip dengan Cosine Similarity dalam hal implementasi, ISC
menunjukkan kinerja yang lebih baik saat dibandingkan dengan metode
pengukuran kesamaan lainnya pada data berdimensi tinggi (Sohangir & Wang,

# 2017
𝐼𝑆𝐶(𝑥,𝑦) =
∑𝑚
𝑖=1
√𝑥
𝑖
𝑦
𝑖 (2.7)
√(∑𝑚 𝑥 )√(∑𝑚 𝑦 )
𝑖=1 𝑖 𝑖=1 𝑖
Adapun keterangan dari Persamaan 2.7:
𝑥 = Vektor yang mewakili dokumen pertama
𝑦 = Vektor yang mewakili dokumen kedua
𝑥 = Bobot pada term ke-𝑖 pada vektor 𝑥
𝑖
𝑦 = Bobot pada term ke-𝑖 pada vektor 𝑦
𝑖
𝑖 = Indeks term dalam suatu kalimat
𝑚 = Jumlah total term dalam vektor vektor 𝑥 dan 𝑦

# 13
## Cosine Similarity
Tujuan dari Cosine Similarity adalah mendapatkan nilai similaritas dari setiap
dokumen yang dibandingkan dengan mengukur kosinus sudut antara dua vektor,
dengan fokus pada arah vektor daripada besarnya (Jawale, et al., 2024). Dalam
kemiripan teks, setiap vektor mewakili sebuah dokumen, dan elemen-elemennya
adalah frekuensi kata. (Jawale, et al., 2024).
∑𝑚 𝑥 .𝑦
𝐶𝑜𝑠𝑆𝑖𝑚(𝑥,𝑦) = 𝑖=1 𝑖 𝑖 (2.8)
√∑𝑚 𝑥 2.√∑𝑚 𝑦 2
𝑖=1 𝑖 𝑖=1 𝑖
Keterangan dari Persamaan 2.8:
𝑥 = Vektor yang mewakili dokumen pertama
𝑦 = Vektor yang mewakili dokumen kedua
𝑥 = Bobot pada term ke-𝑖 pada vektor 𝑥
𝑖
𝑦 = Bobot pada term ke-𝑖 pada vektor 𝑦
𝑖
𝑖 = Indeks term dalam suatu kalimat
𝑚 = Jumlah total term dalam vektor vektor 𝑥 dan 𝑦

## Human-Level Performance
Meskipun algoritma dapat menunjukkan kinerja yang sangat baik, perlu
dipastikan bahwa perbandingan antara kinerja manusia dan algoritma dilakukan
secara adil dan tepat agar hasil yang diperoleh dapat dipercaya (Cowley, et al.,

# Memahami bagaimana manusia menyelesaikan tugas tertentu dapat
memberikan informasi yang berguna bagi penelitian di bidang machine learning
dan artificial intelligence (Cowley, et al., 2022). Penting untuk mempertimbangkan
apakah suatu sistem harus mencapai kinerja setara dengan manusia untuk
dianggap cerdas dan apakah mesin harus menyelesaikan masalah dengan cara
yang mirip dengan manusia, sehingga dapat menunjukkan pola keberhasilan dan
kesalahan yang serupa (Cowley, et al., 2022). Dengan demikian, mengetahui cara
manusia menyelesaikan tugas dapat membantu dalam pengembangan algoritma
yang lebih baik dan lebih efektif (Cowley, et al., 2022).

# 14
## Spearman Rank Correlation Coefficient (SRCC)
Spearman Rank Correlation Coefficient (SRCC) adalah versi nonparametrik dari
koefisien Pearson Correlation yang digunakan untuk menyelidiki hubungan linear
antara dua variabel, khususnya pada data ordinal (Temizhan, et al., 2022). SRCC
cocok digunakan ketika data tidak memenuhi asumsi parametrik, ukuran sampel
kecil, atau terdapat masalah outlier (Temizhan, et al., 2022). Koefisien ini dapat
diinterpretasikan dalam hal variabilitas peringkat dan dapat menilai hubungan
monoton, di mana satu variabel cenderung naik atau turun seiring perubahan
variabel lainnya (Temizhan, et al., 2022). Meskipun nonparametrik, asumsi penting
untuk menggunakan SRCC adalah data harus setidaknya bersifat ordinal dan harus
ada hubungan monoton antara skor pada satu variabel dengan variabel lainnya
(Temizhan, et al., 2022).

# ∑𝑑
𝑆𝑅𝐶𝐶 = 1− 𝑖 (2.9)
𝑛(𝑛2−1)
Adapun keterangan dari Persamaan 2.9:
𝑑 = Selisih antara peringkat variabel, dihitung sebagai 𝑋 −𝑌
𝑖 𝑖 𝑖
𝑛 = Jumlah total pasangan data yang digunakan dalam perhitungan
Rentang nilai koefisien korelasi berkisar dari -1 hingga 1 (Hermanto & Harliana,

# Nilai 1 menunjukkan korelasi positif sempurna, nilai -1 menunjukkan
korelasi negatif sempurna, dan nilai 0 menandakan tidak ada korelasi (Hermanto
& Harliana, 2024). Interpretasi koefisien korelasi pada buku oleh Robert
Kurniawan (2016), koefisien korelasi berkisar antara 0,00 hingga 1,00 (Hermanto
& Harliana, 2024). Nilai 0,00 hingga 0,19 menunjukkan korelasi sangat lemah; 0,20
hingga 0,39 menunjukkan korelasi lemah; 0,40 hingga 0,59 menunjukkan korelasi
sedang; 0,60 hingga 0,79 menunjukkan korelasi kuat; dan 0,80 hingga 1,00
menunjukkan korelasi sangat kuat (Hermanto & Harliana, 2024).

# 15
# BAB 3 METODOLOGI
Terdapat beberapa bagian di bab metodologi penelitian, seperti tipe
penelitian, strategi penelitian, lokasi penelitian, metode pengumpulan data,
metode analisis data, peralatan pendukung, dan perancangan algoritma.

## Tipe Penelitian
Penelitian ini merupakan penelitian non implementatif-analitik yang berarti
produk yang dihasilkan berupa hasil analisis yang relevan dengan topik yang
diteliti. Dalam penelitian ini, metode yang digunakan untuk menentukan resume
yang paling sesuai dengan kualifikasi perekrut adalah metode perhitungan nilai
similaritas tertinggi antara kualifikasi yang tercantum dalam resume dan kualifikasi
yang dibutuhkan oleh perekrut sehingga dapat membantu perekrut dalam
memilih 5 resume dengan tingkat kesesuaian tertinggi.

## Strategi Penelitian
Strategi penelitian yang dilakukan pada penelitian ini adalah penelitian
eksperimen. Penelitian eksperimen adalah salah satu metode penelitian yang
dapat menguji hipotesis mengenai hubungan sebab-akibat (Guritno, et al., 2011,
p. 29). Kemudian, didefinisikan juga bahwa pendekatan ini merupakan penelitian
untuk menguji sebab akibat antar variabel melalui langkah manipulasi,
pengendalian, dan pengamatan (Musfiqon, 2016, p. 60). Penelitian eksperimen
dilaksanakan dengan maksud mengetahui akibat dari suatu perlakuan melalui cara
sengaja menimbulkan kejadian (eksperimen) (Effendi, 2013, p. 88).

## Lokasi Penelitian
Penelitian ini akan dilaksanakan di Fakultas Ilmu Komputer, Universitas
Brawijaya, Kota Malang, Jawa Timur.

## Metode Pengumpulan Data
Data yang digunakan dalam penelitian ini didapatkan dari platform Kaggle,
berjudul “Resume Dataset” yang dibuat oleh Snehaan Bhawal. Dataset ini terdiri
dari 2.484 resume yang dikategorikan berdasarkan jenis pekerjaan yang dilamar,
seperti HR, Desainer, Teknologi Informasi, Guru, dan kategori lainnya. Dataset
tersebut mencakup format resume dalam bentuk string (teks) dan setiap resume
diidentifikasi dengan ID unik. Informasi yang terdapat dalam dataset meliputi teks
resume, data HTML hasil web scraping, dan kategori pekerjaan (Bhawal, 2021).

# 16
## Metode Analisis Data
Tujuan menganalisis data, antara lain mendapatkan perasaan terhadap data,
menguji kualitas data, dan menguji hipotesis penelitian (Guritno, et al., 2011, p.

# Menurut Cholissodin & Riyandani (2016), terdapat beberapa fase pada
gambaran umum siklus hidup analitik data, seperti:

# Discovery. Fase ini meliputi proses belajar, mencari dan menyelidiki fakta-
fakta, mengidentifikasi masalah, mengembangkan konteks dan
pemahaman, dan belajar tentang sumber data yang dibutuhkan, diikuti
dengan perumusan hipotesis awal yang nantinya dapat diuji dengan data
(Cholissodin & Riyandani, 2018, p. 22).

# Data Preparation. Fase ini meliputi persiapan data sebelum dipakai untuk
proses modelling dan evaluation yang dibagi menjadi dua bagian, yakni
cleaning untuk menyeleksi beberapa fitur dan transformation untuk
mengubah bentuk data ke dalam bentuk yang bisa diterima oleh algoritma
(Abdusyukur, 2023).

# Model Planning. Fase ini merupakan proses penentuan metode, teknik,
dan alur kerja dengan mengeksplorasi data untuk mempelajari hubungan
antara variabel yang selanjutnya memilih variabel kunci dan model yang
paling cocok untuk digunakan (Cholissodin & Riyandani, 2018, p. 23).

# Model Building. Pada fase ini, dataset dikembangkan untuk pengujian,
pelatihan, dan tujuan produksi, serta mempertimangkan apakah dengan
alat yanng ada akan cukup untuk menjalankan model (Cholissodin &
Riyandani, 2018, p. 23).

# Communicate Result. Pada fase ini, temuan-temuan yang didapatkan akan
didiskusikan dengan para pemangku kepentingan untuk menentukan
apakah hasil proyek tersebut sukses atau mengalami kegagalan
(Cholissodin & Riyandani, 2018, p. 24).

# Operationalize. Fase ini merupakan yang terakhir dengan menyerahkan
laporan akhir, pengarahan, kode, dan dokumen teknis (Cholissodin &
Riyandani, 2018, p. 24).

## Metode Evaluasi
Evaluasi metode similaritas teks dilakukan dengan menggunakan human-level
performance sebagai tolak ukur untuk membandingkan korelasi antara keluaran
lima resume dengan nilai similaritas tertinggi yang dihasilkan oleh implementasi
metode dengan peringkat ground truth keluaran lima resume tersebut oleh
seorang ahli yang memiliki pengalaman rekrutmen selama 2 tahun dan telah
meninjau lebih dari 5000 resume di bidang sales, marketing, teknologi, healthcare,
accounting, finance, human resources, dan legal. Evaluasi ini dilakukan untuk
setiap posisi lowongan kerja dari total 24 kualifikasi lowongan kerja dan hasilnya
dianalisis menggunakan tiga parameter penilaian, yakni korelasi sebagai
parameter utama, serta relevansi dan senioritas sebagai parameter tambahan.

# 17
## Peralatan Pendukung
Dalam melakukan penelitian ini dari awal hingga akhir, diperlukan beberapa
peralatan pendukung untuk membantu kelancaran jalannya penelitian. Peralatan
pendukung tersebut meliputi perangkat lunak (software) dan perangkat keras
(hardware)

### Perangkat Lunak (Software)
Perangkat lunak yang digunakan, antara lain:

# Sistem operasi Microsoft Windows 10 Home 64-bit
# Jupyter Notebook Versi 7.0.8
# Bahasa pemrograman Python 3.12.4
# Library Python Pandas Versi 2.2.3
# Library Python BeautifulSoup4 (bs4) Versi 4.12.3
# Library Python Gensim Versi 4.3.3
# Library Python Numpy Versi 1.26.4
# Library Python Scikit-learn Versi 1.6.1
# Library Python NLTK Versi 3.9.1
# Library Python TQDM Versi 4.67.1
# Microsoft® Word 2016 MSO (Version 2505 Build 16.0.18827.20102)
# bit
## Perangkat Keras (Hardware)
Perangkat keras yang digunakan, antara lain:

# Windows 10 Home (2009)
# Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz, 2401 Mhz, 2 Core(s), 4
Logical Processor(s)

# Memori RAM 8,00 GB
# SSD SanDisk Z400s 2.5 7MM 256GB
## Perancangan Algoritma
Pada perancangan algoritma dijabarkan proses pengimplementasian metode
similaritas teks untuk otomatisasi penyaringan resume berdasarkan kualifikasi
yang instansi butuhkan. Sebelumnya, dilakukan studi literatur, lalu proses
implementasi ini dimulai dengan melakukan pra-pemrosesan dataset resume dan
kualifikasi lowongan kerja. Kemudian, dilakukan perhitungan representasi teks
untuk keduanya yang menghasilkan vektor-vektor guna menghitung similaritas
antara vektor resume dengan vektor dari kualifikasi lowongan kerja. Setelah skor
similaritas didapatkan, resume pun diurutkan mulai dari yang paling besar
berdasarkan skor similaritasnya dan diberikan peringkat agar dapat dilakukan
pengujian.

# 18
Gambar 3.1 Struktur proses implementasi pemeringkatan similaritas resume
dan kualifikasi lowongan kerja

# 19
# BAB 4 PERANCANGAN
Bab perancangan menjelaskan tentang perancangan algoritma dari metode-
metode serta flow diagram dari setiap algoritma yang digunakan pada penelitian
ini. Selain itu, bab ini juga merincikan perhitungan manual.

## Deskripsi Umum
Penelitian ini dilakukan dengan memeringkat lima resume dari dataset
berdasarkan skor similaritas dengan kualifikasi suatu lowongan kerja dalam format
CSV. Langkah pertama yang dilakukan adalah ekstraksi bagian-bagian (section)
dari resume, diikuti dengan preprocessing pada dataset resume dan kualifikasi
lowongan kerja. Setelah data dibersihkan, dilakukan perhitungan representasi
teks untuk dataset resume dan kualifikasi lowongan kerja. Kemudian, vektor yang
diperoleh dari resume dan kualifikasi lowongan kerja dilakukan perhitungan
similaritas. Pemeringkatan lima resume ditentukan dengan skor similaritas
tertinggi untuk setiap kualifikasi lowongan kerja. Hasil pemeringkatan diberikan ke
seorang ahli untuk dievaluasi secara human-level performance.
Pada proses pemeringkatan lima resume, terdapat dua masukan, yakni dataset
resume (Resume.csv) dan kualifikasi lowongan kerja (kualifikasi_loker.csv) yang
merupakan kumpulan 24 kualifikasi lowongan kerja dari situs pencarian kerja
https://id.jobstreet.com/. Dalam dataset resume, terdapat kolom ID,
Resume_str, Resume_html, dan Category. Kolom ID merupakan nomor
identifier yang dimiliki setiap resume, kolom Resume_str merupakan isi dari
resume, kolom Resume_html merupakan isi dari resume dengan format HTML,
dan kolom Category merupakan pengelompokan industri atau bidang posisi
pekerjaan dari setiap resume. Diketahui terdapat 24 kategori industri, yaitu: “HR”,

# “DESIGNER”, “INFORMATION-TECHNOLOGY”, “TEACHER”, “ADVOCATE”,
# “BUSINESS-DEVELOPMENT”, “HEALTHCARE”, “FITNESS”, “AGRICULTURE”, “BPO”,
# “SALES”, “CONSULTANT”, “DIGITAL-MEDIA”, “AUTOMOBILE”, “CHEF”, “FINANCE”,
# “APPAREL”, “ENGINEERING”, “ACCOUNTANT”, “CONSTRUCTION”, “PUBLIC-
RELATIONS”, “BANKING, ARTS”, dan “AVIATION”. Kategori-kategori tersebut yang
dijadikan landasan untuk mencari 24 kualifikasi lowongan kerja.

## Preprocessing
### Ekstraksi Section
Langkah pertama adalah men-drop kolom yang tidak digunakan seperti kolom
Category dan dilanjut melakukan ekstraksi bagian-bagian (section) dengan
mengambil class sectiontitle dari kolom Resume_html. Setelah section
setiap resume diketahui, isian dari setiap bagian diambil dari kolom
Resume_str. Hasilnya adalah DataFrame resume_df_1 yang memiliki kolom
ID, Resume_str, Resume_hml, Section, dan Text. Diagram alur proses
ekstraksi section tertera pada Gambar 4.1 hingga Gambar 4.4.

# 20
Gambar 4.1 Diagram alur ekstraksi section

# 21
Gambar 4.2 Diagram alur ekstraksi section

# 22
Gambar 4.3 Diagram alur ekstraksi section

# 23
Gambar 4.4 Diagram alur ekstraksi section

# 24
## Preprocessing Isian Resume
Setelah langkah ekstraksi section dilakukan dan menghasilkan DataFrame
resume_df_1, selanjutnya adalah langkah preprocessing untuk kolom Text
yang merupakan isian dari setiap section pada setiap resume. Langkah-langkah
yang dilakukan mencakup penghapusan email, nomor telepon, tanggal, dan
tahun. Selain itu, juga dilakukan penghapusan kata “Current”, “Present”,
penghapusan istilah-istilah placeholder, penghapusan tanda baca, penghapusan
tanggal, penghapusan angka, dan penghapusan spasi berlebih. Selanjutnya,
dilakukan lematisasi dan penghapusan stopword agar kata-kata ditransformasikan
menjadi bentuk dasar sesuai dengan kamus. Diagram alur proses preprocessing
isian resume tertera pada Gambar 4.5 hingga Gambar 4.6.
Gambar 4.5 Diagram alur preprocessing isian resume

# 25
Gambar 4.6 Diagram alur preprocessing isian resume

# 26
## Preprocessing Penamaan Section
Setiap resume umumnya memiliki struktur informasi yang serupa, seperti
bagian Education, Work Experience, Skills, dan Summary. Namun, penamaan atau
label dari setiap bagian tersebut dapat sangat bervariasi antar resume, misalnya
Work Experience bisa juga ditulis sebagai Experience. Oleh karena itu, diperlukan
tahap preprocessing penamaan section untuk menyamakan atau menyeragamkan
nama-nama section tersebut ke dalam satu format baku. Berikut ini merupakan
daftar section standar yang digunakan.

# Summary. Bagian yang berisi ringkasan profil, tujuan karir, atau deskripsi
singkat.

# Accomplishments/Awards. Bagian yang berisi pencapaian, penghargaan,
atau prestasi yang pernah diraih.

# Skills/Qualifications. Bagian yang berisi daftar keterampilan teknis maupun
non-teknis, serta kualifikasi lainnya.

# Education. Bagian yang berisi latar belakang pendidikan formal.
# Experience. Bagian yang berisi pengalaman kerja atau pengalaman
profesional lainnya.

# Organization. Bagian yang berisi pengalaman dalam organisasi,
kepanitiaan, atau kegiatan sosial.

# Projects. Bagian yang berisi proyek-proyek yang pernah dikerjakan secara
individu maupun kelompok.

# Certifications. Bagian yang berisi rincian sertifikasi yang diperoleh.
# Portfolio. Bagian yang berisi riwayat karya atau tautan ke portofolio online.
# Others. Bagian-bagian lain yang tidak termasuk dalam section di atas,
seperti referensi, hobi, atau informasi tambahan lainnya.
Diagram alur proses preprocessing penamaan section resume tertera pada
Gambar 4.7.

# 27
Gambar 4.7 Diagram alur preprocessing penamaan section resume

# 28
## Preprocessing Kualifikasi Lowongan Kerja
Dilakukan preprocessing pada kolom Description yang berisi kebutuhan
terkait suatu posisi lowongan kerja. Langkah-langkah yang dilakukan mencakup
tokenisasi dan lematisasi agar kata-kata ditransformasikan menjadi bentuk dasar
sesuai dengan kamus. Diagram alur proses preprocessing isian kualifikasi
lowongan kerja tertera pada Gambar 4.8.
Gambar 4.8 Diagram alur preprocessing isian kualifikasi lowongan kerja

# 29
## Perhitungan Representasi Teks
### TF-IDF
Pengimplementasian TF-IDF menggunakan library Scikit-learn. Meskipun
proses implementasi menggunakan library, diagram alur yang menjelaskan detail
perhitungan TF-IDF tertera pada Gambar 4.9 hingga Gambar 4.11.
Gambar 4.9 Diagram alur TF-IDF

# 30
Gambar 4.10 Diagram alur TF-IDF

# 31
Gambar 4.11 Diagram alur TF-IDF

# 32
## Word2Vec
Pengimplementasian Word2Vec menggunakan library Gensim. Meskipun
proses implementasi menggunakan library, diagram alur yang menjelaskan detail
perhitungan Word2Vec tertera pada Gambar 4.12 hingga Gambar 4.14.
Gambar 4.12 Diagram alur Word2Vec

# 33
Gambar 4.13 Diagram alur Word2Vec

# 34
Gambar 4.14 Diagram alur Word2Vec

# 35
## Perhitungan Similaritas
### Improved Sqrt-Cosine Similarity
Proses perhitungan Improved Sqrt-Cosine (ISC) Similarity digunakan untuk
mengukur seberapa mirip antara resume dengan kualifikasi lowongan kerja.
Pertama, fungsi ini memeriksa apakah kedua vektor ada. Jika tidak, hasilnya adalah

# , Selanjutnya, dihitung skor similaritas dengan menjumlahkan akar dari hasil kali
elemen yang bersesuaian dalam kedua vektor sebagai pembilang. Hasil tersebut
dibagi dengan hasil kali akar dari total nilai di masing-masing vektor sebagai
penyebut. Terakhir, fungsi ini mengembalikan hasil pembagian yang merupakan
skor kemiripan kedua vektor tersebut. Diagram alur proses perhitungan similaritas
ISC tertera pada Gambar 4.15 hingga 4.16.
Gambar 4.15 Diagram alur Improved Sqrt-Cosine Similarity

# 36
Gambar 4.16 Diagram alur Improved Sqrt-Cosine Similarity

# 37
## Cosine Similarity
Meskipun dalam implementasi program digunakan library Scikit-learn untuk
menghitung nilai Cosine Similarity (CosSim) antara resume dan kualifikasi
lowongan kerja, proses perhitungan di balik fungsi tersebut tetap dijelaskan
melalui diagram alur pada Gambar 4.17 dan 4.18. Pertama, fungsi ini akan
memeriksa keberadaan kedua vektor. Jika salah satu tidak tersedia, maka akan
menghasilkan pesan error. Selanjutnya, nilai CosSim dihitung dengan membagi
jumlah hasil perkalian elemen-elemen bersesuaian dari kedua vektor (pembilang
atau numerator) dengan hasil perkalian akar kuadrat dari jumlah kuadrat elemen
pada masing-masing vektor (penyebut atau denominator). Skor akhir similaritas
diperoleh dari pembagian antara pembilang dan penyebut. Diagram alur proses
perhitungan CosSim tertera pada Gambar 4.17 hingga 4.18.
Gambar 4.17 Diagram alur Cosine Similarity

# 38
Gambar 4.18 Diagram alur Cosine Similarity

# 39
## Perhitungan Korelasi
Pada proses perhitungan korelasi, Spearman Rank Correlation Coefficient
(SRCC) digunakan untuk mengukur seberapa sesuai antara dua peringkat, yaitu
peringkat hasil keluaran implementasi metode dan peringkat yang disusun oleh
ahli berdasarkan evaluasi terhadap hasil keluaran implementasi metode. Pertama,
DataFrame results_df yang berisi kolom peringkat hasil implementasi metode
(Rank), Resume_ID, Position, Similarity_Score, dan peringkat
ground truth dari ahli (Rank_Expert) diinput. Selanjutnya, dihitung selisih
antara peringkat hasil implementasi metode dan ahli per resume untuk setiap
posisi. Selisih tersebut dikuadratkan dan dijumlahkan untuk memperoleh total
deviasi peringkat. Terakhir, hasil penjumlahan tersebut digunakan dalam rumus
SRCC untuk mendapatkan nilai korelasi yang menunjukkan sejauh mana hasil
implementasi metode sesuai dengan penilaian ahli. Diagram alur proses
perhitungan SRCC tertera pada Gambar 4.19 hingga 4.20.
Gambar 4.19 Diagram alur Spearman Rank Correlation Coefficient

# 40
Gambar 4.20 Diagram alur Spearman Rank Correlation Coefficient

# 41
## Perhitungan Relevansi dan Senioritas
Pada proses perhitungan relevansi dan senioritas, digunakan persentase untuk
mengukur seberapa sesuai antara resume-resume yang dihasilkan implementasi
metode dengan setiap kualifikasi lowongan kerja berdasarkan penilaian ahli.
Pertama, DataFrame results_df yang berisi kolom peringkat hasil
implementasi metode (Rank), Resume_ID, Position, Relevance, dan
Seniority diinput. Selanjutnya, untuk setiap kualifikasi lowongan kerja, hitung
berapa resume yang bernilai TRUE pada kolom Relevance dan berapa resume
yang bernilai TRUE pada kolom Seniority. Kemudian, hitung persentase
masing-masing relevansi dan senioritas dengan mengalikan 100 pada hasil
pembagian antara jumlah resume bernilai TRUE dan jumlah total resume. Diagram
alur proses perhitungan relevansi dan senioritas tertera pada Gambar 4.21 hingga

## 4.22
Gambar 4.21 Diagram alur relevansi dan senioritas

# 42
Gambar 4.22 Diagram alur relevansi dan senioritas

# 43
## Perhitungan Manual
### Data Uji
Data uji resume yang digunakan untuk perhitungan manualisasi merupakan
salah satu resume yang diambil dari dataset resume kolom ID, Resume_str,
dan Resume_html. Rincian isi data uji resume tertera pada Tabel 4.1
Tabel 4.1 Data uji resume untuk perhitungan manual

## ID Resume_str Resume_html
# INTERVENTION SPECIALIST <div class="fontsize fontface
TEACHER OF MATH AND vmargins hmargins linespacing
LANGUAGE ARTS Objective To gain pagesize" id="document"> <div
the position as the resource room class="section firstsection"
teacher at Howell Township Public id="SECTION_NAME537133600"
Schools. Summary of style="padding-top:5px;"> <div
Qualifications Demonstrated class="paragraph
ability to design developmentally PARAGRAPH_NAME
appropriate lessons and activities firstparagraph"
allowing integration of all learning id="PARAGRAPH_537133600_1_3
styles. Highly educated in 50680747" style="padding-
differentiated classrooms. top:0px;"> <div class="name
Determined to maximize the thinbottomborder"
educational achievement of each itemprop="name"> <span
student. Trained in Developmental class="field"
Reading Assessments, Common id="537133600FNAM1"> </span>
Core Standards, Standard <span> </span> <span
Solutions, Wonders, Anti-Bullying. class="field"
Hard-working and organized. id="537133600LNAM1">
Knowledge and respect for all INTERVENTION SPECIALIST
students and parental rights. TEACHER OF MATH AND
Professional leadership and LANGUAGE ARTS</span> </div>
management skills... <div class="myGap"> </div> <div
class="lowerborder
thinbottomborder"> </div> </div>
</div> <div class="section"
id="SECTION_SUMM537133602"
style="padding-top:0px;"> <div
class="heading"> <div
class="sectiontitle
thinbottomborder"
id="SECTNAME_SUMM537133602
"> Objective</div> </div> <div
class="paragraph firstparagraph"
id="PARAGRAPH_537133602_1_3

# "...
# 44
Data uji kualifikasi lowongan kerja yang digunakan untuk perhitungan
manualisasi merupakan salah satu kualifikasi lowongan kerja yang diambil dari
dataset kualifikasi lowongan kerja dengan kolom Position, Company, dan
Description. Rincian isi data uji kualifikasi lowongan kerja tertera pada Tabel

## 4.2
Tabel 4.2 Data uji kualifikasi lowongan kerja untuk perhitungan manual

## Position Company Description
Creative Director / PT Basic Entertainment Strong background in
Manager event design, branding,
and storytelling

## Ability to lead and inspire
a team of creatives and
event professionals

## Effectively present ideas to
clients and collaborate
with stakeholders

## Ability to understand the
project scope and
requirements as outlined
by clients or stakeholders.

## Ensure that all designs
comply with relevant
industry standards

## Bachelor Degree of any
major..

### Perhitungan Manual Ekstraksi Section
Pada proses ekstraksi bagian-bagian (section), diambil class sectiontitle
dari kolom Resume_html menggunakan library BeautifulSoup4. Setelah section
setiap resume diketahui, isian dari setiap section diambil dari kolom
Resume_str seperti pada Tabel 4.3.
Tabel 4.3 Hasil perhitungan manual ekstraksi section

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

# 45
Tabel 4.3 Hasil perhitungan manual ekstraksi section (lanjutan)

## Section Text
## Experience Intervention Specialist Teacher of Math
and Language Arts October 2013 to May

# Company Name － City , State
## Identified students with substantial
academic difficulties through evaluation
using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology , December

# Georgian Court University － City ,
State GPA: Cum Laude Coursework in

## Psychology and Sociology Coursework in
Intercultural and Group Communication...
Nicole Harrison Peters 732-513-7727 Nic_Harrison@aol.com

### Perhitungan Manual Preprocessing Resume
#### Menghapus Email
Data uji resume yang sudah melalui proses ekstraksi section dilakukan
preprocessing mulai dari menghapus email seperti pada Tabel 4.4.
Tabel 4.4 Hasil perhitungan manual preprocessing resume bagian menghapus
email

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts October 2013 to
May 2014 Company Name － City ,

## State Identified students with
substantial academic difficulties through
evaluation using Developmental Reading

## Assessments and consultation with staff
members of referred students...

# 46
Tabel 4.4 Hasil perhitungan manual preprocessing resume bagian menghapus
email (lanjutan)

## Section Text
Education, Certifications, Endorements Bachelor of Arts : Psychology ,

## December 2012 Georgian Court
University － City , State GPA:

## Cum Laude Coursework in Psychology
and Sociology Coursework in
Intercultural and Group Communication...
Nicole Harrison Peters 732-513-7727

### Menghapus Nomor Telepon
Data uji resume yang sudah melalui preprocessing menghapus email,
dilanjutkan menghapus nomor telepon seperti pada Tabel 4.5.
Tabel 4.5 Hasil perhitungan manual preprocessing resume bagian menghapus
nomor telepon

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts October 2013 to
May 2014 Company Name － City ,

## State Identified students with
substantial academic difficulties through
evaluation using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology ,

## December 2012 Georgian Court
University － City , State GPA:

## Cum Laude Coursework in Psychology
and Sociology Coursework in
Intercultural and Group Communication...

## Nicole Harrison Peters
# 47
## Menghapus Berbagai Tipe Tanda Minus (－, –, —)
Data uji resume yang sudah melalui preprocessing menghapus nomor telepon,
dilanjutkan menghapus berbagai tipe tanda minus yang kemungkinan digunakan
dalam penulisan informasi seperti lokasi, tanggal, atau rentang waktu. Hasil dari
proses penghapusan ini tertera pada Tabel 4.6.
Tabel 4.6 Hasil perhitungan manual preprocessing resume bagian menghapus
berbagai tipe tanda minus (－, –, —)

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts October 2013 to
May 2014 Company Name City ,

## State Identified students with
substantial academic difficulties through
evaluation using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology ,

## December 2012 Georgian Court
University City , State GPA: Cum

## Laude Coursework in Psychology and
## Sociology Coursework in Intercultural
and Group Communication...

## Nicole Harrison Peters
### Menghapus Nama Bulan
Data uji resume yang sudah melalui preprocessing menghapus berbagai tipe
tanda minus, dilanjutkan menghapus nama bulan. Hasil dari proses penghapusan
ini tertera pada Tabel 4.7.
Tabel 4.7 Hasil perhitungan manual preprocessing resume bagian menghapus
nama bulan

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.

# 48
Tabel 4.7 Hasil perhitungan manual preprocessing resume bagian menghapus
nama bulan (lanjutan)

## Section Text
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts 2013 to 2014
Company Name City , State

## Identified students with substantial
academic difficulties through evaluation
using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology , 2012
Georgian Court University City ,
State GPA: Cum Laude Coursework
in Psychology and Sociology Coursework
in Intercultural and Group
Communication...

## Nicole Harrison Peters
### Menghapus Kata “Present” dan “Current”
Data uji resume yang sudah melalui preprocessing menghapus nama bulan,
dilanjutkan menghapus kata atau istilah seperti “Present” dan “Current” yang
biasanya digunakan untuk menunjukkan rentang waktu. Hasil dari proses
penghapusan ini tertera pada Tabel 4.8.
Tabel 4.8 Hasil perhitungan manual preprocessing resume bagian menghapus
kata “Present” dan “Current”

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

# 49
Tabel 4.8 Hasil perhitungan manual preprocessing resume bagian menghapus
kata “Present” dan “Current” (lanjutan)

## Section Text
## Experience Intervention Specialist Teacher of Math
and Language Arts 2013 to 2014
Company Name City , State

## Identified students with substantial
academic difficulties through evaluation
using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology , 2012
Georgian Court University City ,
State GPA: Cum Laude Coursework
in Psychology and Sociology Coursework
in Intercultural and Group
Communication...

## Nicole Harrison Peters
### Menghapus Tanggal
Data uji resume yang sudah melalui preprocessing menghapus kata atau istilah
seperti “Present” dan “Current”, dilanjutkan dengan penghapusan format-format
tanggal dan rentang waktu. Hasil dari proses penghapusan ini tertera pada Tabel

## 4.9
Tabel 4.9 Hasil perhitungan manual preprocessing resume bagian menghapus
tanggal

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

# 50
Tabel 4.9 Hasil perhitungan manual preprocessing resume bagian menghapus
tanggal (lanjutan)

## Section Text
## Experience Intervention Specialist Teacher of Math
and Language Arts to Company
Name City , State Identified
students with substantial academic
difficulties through evaluation using

## Developmental Reading Assessments and
consultation with staff members of
referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology ,
Georgian Court University City ,
State GPA: Cum Laude Coursework
in Psychology and Sociology Coursework
in Intercultural and Group
Communication...

## Nicole Harrison Peters
### Menghapus Placeholder
Data uji resume yang sudah melalui preprocessing menghapus tanggal,
dilanjutkan menghapus placeholder yang biasanya digunakan untuk menunjukkan
lokasi atau perusahaan seperti “Company Name” dan “State”. Hasil dari proses
penghapusan ini tertera pada Tabel 4.10.
Tabel 4.10 Hasil perhitungan manual preprocessing resume bagian menghapus
placeholder

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles. Highly educated in
differentiated classrooms...

# 51
Tabel 4.10 Hasil perhitungan manual preprocessing resume bagian menghapus
placeholder (lanjutan)

## Section Text
## Experience Intervention Specialist Teacher of Math
and Language Arts to ,

## Identified students with substantial
academic difficulties through evaluation
using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts : Psychology ,
Georgian Court University , GPA:

## Cum Laude Coursework in Psychology
and Sociology Coursework in
Intercultural and Group Communication...

## Nicole Harrison Peters
### Menghapus Tanda Baca
Data uji resume yang sudah melalui preprocessing menghapus placeholder,
dilanjutkan menghapus tanda baca. Hasil dari proses penghapusan ini tertera pada
Tabel 4.11.
Tabel 4.11 Hasil perhitungan manual preprocessing resume bagian menghapus
tanda baca

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public

## Schools
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts to

## Identified students with substantial
academic difficulties through evaluation
using Developmental Reading

## Assessments and consultation with staff
members of referred students...

# 52
Tabel 4.11 Hasil perhitungan manual preprocessing resume bagian menghapus
tanda baca (lanjutan)

## Section Text
Education, Certifications, Endorements Bachelor of Arts Psychology

## Georgian Court University GPA
## Cum Laude Coursework in Psychology
and Sociology Coursework in
Intercultural and Group Communication...

## Nicole Harrison Peters
### Menghapus Angka
Data uji resume yang sudah melalui preprocessing menghapus tanda baca,
dilanjutkan menghapus angka. Hasil dari proses penghapusan ini tertera pada
Tabel 4.12.
Tabel 4.12 Hasil Perhitungan manual preprocessing resume bagian menghapus
angka

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public
Schools.
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts to

## Identified students with substantial
academic difficulties through evaluation
using Developmental Reading

## Assessments and consultation with staff
members of referred students...
Education, Certifications, Endorements Bachelor of Arts Psychology

## Georgian Court University GPA
## Cum Laude Coursework in Psychology
and Sociology Coursework in
Intercultural and Group Communication...

## Nicole Harrison Peters
# 53
## Menghapus Spasi Kosong Berlebih
Data uji resume yang sudah melalui preprocessing menghapus angka,
dilanjutkan menghapus spasi kosong berlebih yang biasanya muncul akibat
penghapusan karakter. Hasil dari proses penghapusan ini tertera pada Tabel 4.13.
Tabel 4.13 Hasil perhitungan manual preprocessing resume bagian menghapus
spasi kosong berlebih

## Section Text
Objective To gain the position as the resource room
teacher at Howell Township Public

## Schools
Summary of Qualifications Demonstrated ability to design
developmentally appropriate lessons and
activities allowing integration of all
learning styles Highly educated in
differentiated classrooms...

## Experience Intervention Specialist Teacher of Math
and Language Arts to Identified students
with substantial academic difficulties
through evaluation using Developmental

## Reading Assessments and consultation
with staff members of referred
students...
Education, Certifications, Endorements Bachelor of Arts Psychology Georgian

## Court University GPA Cum Laude
## Coursework in Psychology and Sociology
## Coursework in Intercultural and Group
Communication...

## Nicole Harrison Peters
### Lematisasi dan Menghapus Stop Words
Data uji resume yang sudah melalui preprocessing menghapus spasi kosong
berlebih, dilanjutkan menghapus stop word dari dari Bahasa Inggris menggunakan
daftar stop words yang tersedia pada library Natural Language Toolkit (NLTK). Hasil
dari proses penghapusan ini tertera pada Tabel 4.14.
Tabel 4.14 Hasil perhitungan manual preprocessing resume bagian lematisasi
dan menghapus stop words

## Section Text
## Objective gain position resource room teacher
## Howell Township Public Schools
# 54
Tabel 4.14 Hasil perhitungan manual preprocessing resume bagian lematisasi
dan menghapus stop words (lanjutan)

## Section Text
## Summary of Qualifications Demonstrated ability design
developmentally appropriate lesson
activity allow integration learning style
Highly educate differentiated classroom...

## Experience Intervention Specialist Teacher Math
## Language Arts Identified student
substantial academic difficulty evaluation
use Developmental Reading Assessments
consultation staff member referred
student...
Education, Certifications, Endorements Bachelor Arts Psychology Georgian Court

## University GPA Cum Laude Coursework
## Psychology Sociology Coursework
Intercultural Group Communication...

## Nicole Harrison Peters
### Mengonversi Nama Section Menjadi Huruf Kecil (Lower
Casing)
Data uji resume yang sudah melalui preprocessing menghapus tanda koma
berlebih, dilanjutkan mengonversi nama-nama section di kolom Section
menjadi huruf kecil untuk memudahkan proses selanjutnya dalam merapikan
nama-nama section. Hasil dari proses pengonversian ini tertera pada Tabel 4.15.
Tabel 4.15 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi nama section menjadi huruf kecil (lower casing)

## Section Text
objective gain position resource room teacher

## Howell Township Public Schools
summary of qualifications Demonstrated ability design
developmentally appropriate lesson
activity allow integration learning style
Highly educate differentiated classroom...
experience Intervention Specialist Teacher Math

## Language Arts Identified student
substantial academic difficulty evaluation
use Developmental Reading Assessments
consultation staff member referred
student...

# 55
Tabel 4.15 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi nama section menjadi huruf kecil (lower casing) (lanjutan)

## Section Text
education, certifications, endorements Bachelor Arts Psychology Georgian Court

## University GPA Cum Laude Coursework
## Psychology Sociology Coursework
Intercultural Group Communication...
nicole harrison peters

### Mencari Nilai Unik Section
Data uji resume yang sudah melalui preprocessing lower casing nama-nama
section, dilanjutkan dengan pencarian nama-nama section yang unik untuk
mengidentifikasi variasi nama section yang terdapat dalam seluruh dataset
resume. Hasil dari proses pencarian nama-nama section ini tertera pada Tabel

## 4.16
Tabel 4.16 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi nama section menjadi huruf kecil (lower casing)
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

### Standarisasi Nama Section
Setelah mengetahui variasi nama section yang terdapat dalam seluruh dataset
resume, dilakukan pemetaan nama-nama section untuk menyeragamkan agar
konsisten dengan nama-nama section yang telah ditentukan pada penelitian ini,
seperti “Summary”, “Accomplishments/Awards”, "Skills/Qualifications",
"Education", "Experience", "Organization", "Projects", "Certifications", "Portfolio",
"Others". Hasil dari proses penyetaraan nama-nama section ini untuk data uji
resume tertera pada Tabel 4.17.

# 56
Tabel 4.17 hasil perhitungan manual penyetaraan nama section bagian
menyeragamkan pengelompokan section berdasarkan pemetaan

## Section Text
## Education Bachelor Arts Psychology Georgian Court
## University GPA Cum Laude Coursework
## Psychology Sociology Coursework
Intercultural Group Communication...

## Experience Intervention Specialist Teacher Math
## Language Arts Identified student
substantial academic difficulty evaluation
use Developmental Reading Assessments
consultation staff member referred
student...

## Summary gain position resource room teacher
## Howell Township Public Schools
## Demonstrated ability design
developmentally appropriate lesson
activity allow integration learning style
Highly educate differentiated classroom...
nicole harrison peters

### Klasifikasi, Penghapusan, dan Pengelompokan Section Tidak
## Valid
Setelah penyeragaman nama-nama section, dilakukan proses klasifikasi,
penghapusan, dan pengelompokan section yang tidak valid. Proses ini diawali
dengan mengidentifikasi section yang tidak termasuk dalam daftar nama section
yang telah ditentukan. Jika ditemukan kata kunci tertentu dalam teks, seperti
“years”, “experience”, atau “I am”, maka section tersebut diklasifikasikan ke dalam
kategori “Summary”. Jika terdapat kata “LinkedIn”, maka dikategorikan ke dalam
“Portfolio”. Baris data yang memiliki isian kolom Section tidak sesuai dengan
daftar nama section yang sudah ditentukan dan kolom Text tidak ada isinya,
maka dihapus. Sedangkan, isian kolom Section yang tidak termasuk dalam
daftar nama section, tetapi memiliki isi di dalam kolom Text, maka dipetakan ke
dalam section “Others”. Selain itu, seluruh baris yang isian kolom Text-nya
kosong, hanya berisi spasi atau bernilai null juga dihapus untuk menjaga kualitas
data. Hasil dari proses klasifikasi, penghapusan, dan pengelompokan section ini
untuk data uji resume tertera pada Tabel 4.18.

# 57
Tabel 4.18 Hasil perhitungan manual penyetaraan nama section bagian
klasifikasi, penghapusan, dan pengelompokan section tidak valid

## Section Text
## Education Bachelor Arts Psychology Georgian Court
## University GPA Cum Laude Coursework
## Psychology Sociology Coursework
Intercultural Group Communication...

## Experience Intervention Specialist Teacher Math
## Language Arts Identified student
substantial academic difficulty evaluation
use Developmental Reading Assessments
consultation staff member referred
student...

## Summary gain position resource room teacher
## Howell Township Public Schools
## Demonstrated ability design
developmentally appropriate lesson
activity allow integration learning style
Highly educate differentiated classroom...

### Mengonversi Isi Resume Menjadi Huruf Kecil (Lower Casing)
Setelah merapikan section, dilakukan pengonversian isi kolom Text menjadi
huruf kecil untuk menyamakan format teks serta memudahkan proses
representasi teks pada tahap selanjutnya. Hasil dari proses ini untuk data uji
resume tertera pada Tabel 4.19.
Tabel 4.19 Hasil perhitungan manual penyetaraan nama section bagian
mengonversi isi resume menjadi huruf kecil (lower casing)

## Section Text
## Education bachelor arts psychology georgian court
university gpa cum laude coursework
psychology sociology coursework
intercultural group communication...

## Experience intervention specialist teacher math
language arts identified student
substantial academic difficulty evaluation
use developmental reading assessments
consultation staff member...

## Summary gain position resource room teacher
howell township public schools
demonstrated ability design
developmentally appropriate lesson
activity allow integration learning style
highly educate differentiated classroom...

# 58
## Perhitungan Manual Preprocessing Kualifikasi Lowongan Kerja
### Mengonversi Isi Kualifikasi Lowongan Kerja Menjadi Huruf
Kecil (Lower Casing)
Pada proses preprocessing kualifikasi lowongan kerja, dilakukan
pengonversian isi kolom Description menjadi huruf kecil untuk menyamakan
format teks serta memudahkan proses preprocessing selanjutnya. Hasil dari
proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.20.
Tabel 4.20 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian mengonversi isi kualifikasi lowongan kerja menjadi huruf kecil (lower
casing)

## Category Position Company Description
ARTS Creative Director / PT Basic strong background
Manager Entertainment in event design,
branding, and
storytelling
ability to lead and
inspire a team of
creatives and event
professionals...

### Menghapus Angka
Setelah proses lower casing isi kolom Description, dilakukan penghapusan
angka-angka. Hasil dari proses ini untuk data uji kualifikasi lowongan kerja tertera
pada Tabel 4.21.
Tabel 4.21 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian menghapus angka

## Category Position Company Description
ARTS Creative Director / PT Basic strong background
Manager Entertainment in event design,
branding, and
storytelling
ability to lead and
inspire a team of
creatives and event
professionals...

# 59
## Menghapus Tanda Baca
Setelah proses penghapusan angka, dilakukan penghapusan tanda baca. Hasil
dari proses ini untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.22.
Tabel 4.22 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian menghapus tanda baca

## Category Position Company Description
ARTS Creative Director / PT Basic strong background

## Manager Entertainment in event design
branding and
storytelling
ability to lead and
inspire a team of
creatives and event
professionals...

### Menghapus Spasi Kosong Berlebih
Setelah proses penghapusan tanda baca, dilakukan penghapusan spasi kosong
berlebih yang biasanya muncul akibat penghapusan karakter. Hasil dari proses ini
untuk data uji kualifikasi lowongan kerja tertera pada Tabel 4.23.
Tabel 4.23 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian menghapus spasi kosong berlebih

## Category Position Company Description
ARTS Creative Director / PT Basic strong background

## Manager Entertainment in event design
branding and
storytelling ability
to lead and inspire
a team of creatives
and event
professionals...

# 60
## Lematisasi dan Menghapus Stop Words
Setelah proses penghapusan spasi kosong berlebih, dilakukan penghapusan
stop words dari Bahasa Inggris. Hasil dari proses ini untuk data uji kualifikasi
lowongan kerja tertera pada Tabel 4.24.
Tabel 4.24 Hasil perhitungan manual preprocessing kualifikasi lowongan kerja
bagian lematisasi dan menghapus stop words

## Category Position Company Description
ARTS Creative Director / PT Basic strong background

## Manager Entertainment event design
branding
storytelling ability
lead inspire team
creatives event
professional...

### Perhitungan Manual Representasi Teks
#### Perhitungan Manual TF-IDF
Tujuan dari TF-IDF adalah menghitung tingkat kepentingan sebuah kata dalam
suatu dokumen dibandingkan dengan keseluruhan dokumen dalam korpus. Untuk
perhitungan manual pada resume, digunakan sample data dari section
“Experience” dengan rincian tertera pada Tabel 4.25.
Tabel 4.25 Korpus resume untuk perhitungan manual

## Dokumen 1 Dokumen 2 Dokumen 3
demonstrated ability digital production manager acted liaison senior
design developmentally responsible aspect digital business manager various
appropriate lesson activity production premium global stake holder
allow integration learning printing graphic design recruited analysts process
style highly educate company delivering high suggest best practice
differentiated classroom quality production meet effective method
determined maximize client direct deadline
educational achievement
student trained
developmental reading
assessments
Tahap pertama adalah menghitung Term Frequency (TF). Pada library Scikit-
learn, nilai TF merupakan jumlah kemunculan term pada setiap dokumen seperti
pada Persamaan 4.1.
𝑇𝐹 = 𝑓 (4.1)
(𝑡,𝑑) 𝑡,𝑑

# 61
Jumlah kemunculan (frekuensi) term setiap dokumen untuk data uji resume
tertera pada Tabel 4.26.
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

# 62
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

# 63
Tabel 4.26 Perhitungan manual frekuensi term setiap resume (lanjutan)
Term f di Dokumen 1 f di Dokumen 2 f di Dokumen 3
effective 0 0 1
method 0 0 1
Contoh perhitungan untuk kata “demonstrated” pada setiap dokumen tertera
mulai dari Persamaan 4.2

# 𝑇𝐹 = 1 (4.2)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1)

# 𝑇𝐹 = 0 (4.3)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2)

# 𝑇𝐹 = 0 (4.4)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3)
Hasil perhitungan TF untuk seluruh term pada ketiga dokumen tertera pada
Tabel 4.27.
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

# 64
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

# 65
Tabel 4.27 Perhitungan manual TF korpus resume (lanjutan)
Term TF di Dokumen 1 TF di Dokumen 2 TF di Dokumen 3
analysts 0 0 1
process 0 0 1
suggest 0 0 1
best 0 0 1
practice 0 0 1
effective 0 0 1
method 0 0 1
Selanjutnya menghitung Inverse Document Frequency (IDF) dengan
menghitung terlebih dahulu nilai Document Frequency (DF). Nilai DF didapatkan
dari menghitung jumlah dokumen yang memiliki suatu term, rumusnya tertera
pada Persamaan 4.5, mulai dari Persamaan 4.6 merupakan contoh perhitungan
IDF untuk term “demonstrated”.

# +𝑁
𝐼𝐷𝐹 = log( )+1 (4.5)
(𝑡)

# +𝑑𝑓
# +3
𝐼𝐷𝐹 = log( )+1 = log(2)+1 (4.6)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑)

# +1
# 𝐼𝐷𝐹 = 0,6931471806+1 = 1.693147181 (4.7)
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

# 66
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

# 67
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
Setelah mendapatkan nilai Term Frequency (TF) dan Inverse Document
Frequency (IDF), nilai TF-IDF dapat didapatkan dengan mengalikan nilai TF dengan
nilai IDF seperti pada Persamaan 4.8. Contoh perhitungan manual untuk term
“demonstrated” tertera mulai dari Persamaan 4.9

# 𝑇𝐹 −𝐼𝐷𝐹 = 𝑇𝐹 ×𝐼𝐷𝐹 (4.8)
(𝑡,𝑑) (𝑡,𝑑) (𝑡)

# 𝑇𝐹 −𝐼𝐷𝐹 = 1×1,693147181 = 1,693147181 (4.9)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1)

# 𝑇𝐹 −𝐼𝐷𝐹 = 0×1,693147181 = 0 (4.10)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2)

# 𝑇𝐹 −𝐼𝐷𝐹 = 0×1,693147181 = 0 (4.11)
(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3)
Hasil TF-IDF seluruh term pada ketiga dokumen tertera pada Tabel 4.29.
Tabel 4.29 Perhitungan manual TF-IDF korpus resume
Term TF-IDF Dokumen 1 TF-IDF Dokumen 2 TF-IDF Dokumen 3
demonstrated 1,693147181 0 0
ability 1,693147181 0 0
design 1,287682072 1,287682072 0
developmentally 1,693147181 0 0
appropriate 1,693147181 0 0
lesson 1,693147181 0 0

# 68
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

# 69
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

# 70
Secara bawaan, TfidfTransformer dari library Scikit-learn
mengimplementasikan L (Euclidean distance) norm pada hasil perhitungan TF-

# 2
IDF. Perhitungan normalisasi tertera pada Persamaan 4.12 dan contoh
perhitungannya untuk term “demonstrated” tertera mulai dari Persamaan 4.13
𝑣 𝑣
𝑣 = = (4.12)
𝑛𝑜𝑟𝑚 ‖𝑣‖ 2 √𝑣1 2+𝑣2 2+⋯+𝑣𝑛 2

# ,693147181
𝑣 = (4.13)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1) √(1,693147181)2+(1,693147181)2+⋯+(0)2

# ,693147181
𝑣 = = 0,2059410105 (4.14)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑1)

# ,221515356
# 0
𝑣 = (4.15)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2) √(0)2+(0)2+⋯+(0)2

# 0
𝑣 = = 0 (4.16)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑2)

# ,823360017
# 0
𝑣 = (4.17)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3) √(0)2+(0)2+⋯+(1,693147181)2

# 0
𝑣 = = 0 (4.18)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑚𝑜𝑛𝑠𝑡𝑟𝑎𝑡𝑒𝑑,𝑑3)

# ,893916385
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

# 71
Tabel 4.30 Perhitungan manual TF-IDF korpus resume setelah normalisasi
(lanjutan)
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

# 72
Tabel 4.30 Perhitungan manual TF-IDF korpus resume setelah normalisasi
(lanjutan)
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
Perhitungan manual pada kualifikasi lowongan kerja menggunakan beberapa
sample data dari kolom Description dengan rincian yang bisa dilihat pada
Tabel 4.31.
Tabel 4.31 Korpus kualifikasi lowongan kerja untuk perhitungan manual

## Dokumen 4 Dokumen 5 Dokumen 6
strong background event execute daytoday design play vital role support lead
design branding request internal external teacher create nurturing
storytelling ability lead communication material stimulate learning
inspire team creatives develop creative visual environment young
event professional content include motion student assist lead teacher
effectively present idea graphic static design planning implement
client collaborate engage educational
stakeholder activity
Nilai Term Frequency (TF) untuk deskripsi kualifikasi lowongan kerja dapat
dihitung berdasarkan term yang telah ditokenisasi sebelumnya dari korpus
resume, sehingga hasil perhitungan TF kualifikasi lowongan kerja tertera pada
Tabel 4.32
Tabel 4.32 Perhitungan manual TF korpus kualifikasi lowongan kerja
Term TF di Dokumen 4 TF di Dokumen 5 TF di Dokumen 6
demonstrated 0 0 0
ability 1 0 0
design 1 2 0

# 73
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

# 74
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

# 75
Nilai Inverse Document Frequency (IDF) bisa didapatkan dengan menghitung
document frequency (DF) terlebih dahulu. Kemudian, dihitung dengan formula
seperti pada Persamaan 4.19. Mulai dari Persamaan 4.20 mendemonstrasikan
perhitungan IDF untuk term “design”.

# +𝑁
𝐼𝐷𝐹 = log( )+1 (4.19)
(𝑡)

# +𝑑𝑓
# +3 4
𝐼𝐷𝐹 = log( )+1 = log( )+1 (4.20)
(𝑑𝑒𝑠𝑖𝑔𝑛)

# +2 3
# 𝐼𝐷𝐹 = 0,2876820725+1 = 1,287682072 (4.21)
(𝑑𝑒𝑠𝑖𝑔𝑛)
Hasil perhitungan IDF korpus kualifikasi lowongan kerja tertera pada Tabel

## 4.33
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

# 76
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

# 77
Tabel 4.33 Perhitungan manual IDF korpus kualifikasi lowongan kerja (lanjutan)

## Term DF IDF
practice 0 2,386294361
effective 0 2,386294361
method 0 2,386294361
Setelah mendapatkan nilai term frequency (TF) dan inverse document
frequency (IDF), TF-IDF untuk kualifikasi lowongan kerja dihitung menggunakan
formula pada Persamaan 4.22. Mulai dari Persamaan 4.23 merupakan
demonstrasi perhitungan TF-IDF untuk term “design”.

# 𝑇𝐹 −𝐼𝐷𝐹 = 𝑇𝐹 ×𝐼𝐷𝐹 (4.22)
(𝑡,𝑑) (𝑡,𝑑) (𝑡)

# 𝑇𝐹 −𝐼𝐷𝐹 = 1×1,287682072 = 1,287682072 (4.23)
(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑4)

# 𝑇𝐹 −𝐼𝐷𝐹 = 2×1,287682072 = 2,575364145 (4.24)
(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑5)

# 𝑇𝐹 −𝐼𝐷𝐹 = 0×1,287682072 = 0 (4.25)
(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑6)
Hasil perhitungan manual TF-IDF korpus kualifikasi lowongan kerja tertera
pada Tabel 4.34.
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

# 78
Tabel 4.34 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja
(lanjutan)
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

# 79
Tabel 4.34 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja
(lanjutan)
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
Hasil TF-IDF korpus kualifikasi lowongan kerja juga dilakukan normalisasi
menggunakan formula pada Persamaan 4.26. Mulai dari Persamaan 4.27
merupakan demonstrasi perhitungan normalisasi TF-IDF untuk term “design”
𝑣 𝑣
𝑣 = = (4.26)
𝑛𝑜𝑟𝑚 ‖𝑣‖ 2 √𝑣1 2+𝑣2 2+⋯+𝑣𝑛 2

# ,287682072
𝑣 = (4.27)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑4) √(0)2+(1,693147181)2+⋯+(0)2

# ,287682072
𝑣 = = 0,473629601 (4.28)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑4)

# ,718753367
# ,575364145
𝑣 = (4.29)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑5) √(0)2+(0)2+⋯+(0)2

# ,575364145
𝑣 = = 0,8355915419 (4.30)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑5)

# ,082084985
# 0
𝑣 = (4.31)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑6) √(0)2+(0)2+⋯+(0)2

# 0
𝑣 = = 0 (4.32)
𝑛𝑜𝑟𝑚(𝑑𝑒𝑠𝑖𝑔𝑛,𝑑6)

# ,386294361
Hasil perhitungan manual TF-IDF korpus kualifikasi lowongan kerja setelah
normalisasi tertera pada Tabel 4.35.
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja
setelah normalisasi
Term TF-IDF Dokumen 4 TF-IDF Dokumen 5 TF-IDF Dokumen 6
demonstrated 0 0 0
ability 0,6227660078 0 0
design 0,473629601 0,8355915419 0

# 80
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja
setelah normalisasi (lanjutan)
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

# 81
Tabel 4.35 Perhitungan manual TF-IDF korpus kualifikasi lowongan kerja
setelah normalisasi (lanjutan)
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

# 82
## Perhitungan Manual Word2Vec
Tujuan dari Skip-gram adalah memprediksi konteks (output) disekitar kata
target (input). Untuk demonstrasi perhitungan manual Word2Vec menggunakan
salah satu kalimat dari resume, yakni “demonstrated ability design
developmentally appropriate lesson activity allow integration learning style highly
educate differentiated classroom determined maximize educational achievement
student trained developmental reading assessments” dengan parameter dengan
vocab = 24, window size = 3, dan learning rate = 0,1.
Gambar 4.23 Pasangan target-konteks Word2Vec Skip-gram
Gambar 4.23 merupakan rincian pasangan target-konteks, kotak berwarna
biru merupakan kata target dan kotak berwarna merah merupakan konteks dari
kata target yang sesuai dengan nilai window size.
Tabel 4.36 merupakan one-hot encoding untuk setiap token dalam vocabulary
["Demonstrated", "ability", "design", "developmentally”, “appropriate”, “lesson",
"activity", "integration", "learning”, “style", "differentiated”, “classroom",
“determined”, “maximize”, "educational”, “achievement", "student", “trained”
"developmental”, “reading”, “assessments"].
Tabel 4.36 Perhitungan manual one-hot encoding
Term One-Hot Encoding
demonstrated [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
ability [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
design [0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
developmentally [0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
appropriate [0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
lesson [0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
# 83
Tabel 4.36 Perhitungan manual one-hot encoding (lanjutan)
Term One-Hot Encoding
activity [0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
allow [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
integration [0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
learning [0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
style [0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0

# 0 0 0 0 0 0]
highly [0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0

# 0 0 0 0 0 0]
educate [0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0

# 0 0 0 0 0 0]
differentiated [0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0

# 0 0 0 0 0 0]
classroom [0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0

# 0 0 0 0 0 0]
determined [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0

# 0 0 0 0 0 0]
maximize [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1

# 0 0 0 0 0 0]
educational [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 0]
achievement [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 1 0 0 0 0 0]
student [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 1 0 0 0 0]
trained [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 1 0 0 0]
developmental [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 1 0 0]
reading [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 1 0]
assessments [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 0 0 0 0 0 1]
# 84
Pada perhitungan manual ini, dilakukan penargetan pada kata “design” dan
menggunakan hidden layer = 3. Selanjutnya adalah melakukan inisialisasi acak
bobot input layer ke tiga hidden layer yang tertera pada Tabel 4.37.
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

# 85
Setelah menginisialisasi acak bobot input ke hidden layer, dapat
menginisialisasi acak bobot juga untuk hidden layer ke output layer yang tertera
pada Tabel 4.38 sampai dengan Tabel 4.41.
Tabel 4.38 Bobot hidden layer-output layer
Neuron demonstr ability design developm appropria lesson
ated entally te

# H1 0,3 -0,2 -0,2 0 -0,2 -0,1
# H2 -0,4 -0,3 -0,6 0,3 -0,1 -0,2
# H3 -0,1 -0,8 0,5 0,2 -0,4 0,3
Tabel 4.39 Bobot hidden layer-output layer
Neuron activity allow integratio learning style highly
n

# H1 -0,1 0,3 -0,2 -0,1 -0,1 0,3
# H2 0,3 -0,2 0,3 -0,2 0,3 -0,2
# H3 -0,2 -0,1 -0,1 0,3 -0,2 -0,1
Tabel 4.40 Bobot hidden layer-output layer
Neuron educate differenti classroo determin maximize education
ated m ed al

# H1 -0,2 -0,1 -0,1 0,3 -0,2 -0,1
# H2 0,3 -0,2 0,3 -0,2 0,3 -0,2
# H3 -0,1 0,3 -0,2 -0,1 -0,1 0,3
Tabel 4.41 Bobot hidden layer-output layer
Neuron achievem student trained developm reading assessme
ent ental nts

# H1 -0,1 0,3 -0,2 -0,4 -0,1 0,3
# H2 0,3 -0,2 0,3 -0,1 0,3 0
# H3 -0,2 -0,1 -0,1 0,3 0 -0,6
# 86
Telah didapatkan bobot untuk hidden layer ke output layer pada Tabel 4.38
sampai dengan Tabel 4.41. Perhitungan dilanjutkan ke feedforward dengan
mengalikan one-hot vector dari kata target “design” dengan matriks bobot input-
hidden seperti pada Persamaan 4.33 sampai dengan Persamaan 4.39.
−0,3

# ,2
# ,8
𝐻1 = [0 0 1 … 0 0]× (4.33)
⋮
−0,8
[−0,5]

# 𝐻1 = 0 (−0,3)+0 (0,2)+1(0,8)+⋯+0(−0,8)+0(−0,5) = 0,8 (4.34)
−0,8
−0,5
−0,6
𝐻2 = [0 0 1 … 0 0]× (4.35)
⋮

# ,2
[−0,3]

# 𝐻2 = 0 (−0,8)+0 (−0,5)+1(−0,6)+⋯+0(0,2)+0(−0,3) = −0,6 (4.36)
−0,3
−0,6
−0,2
𝐻3 = [0 0 1 … 0 0]× (4.37)
⋮
−0,3
[ 0,2 ]

# 𝐻3 = 0 (−0,3)+0 (−0,6)+1(−0,2)+⋯+0(−0,3)+0(0,2) = −0,2 (4.38)
ℎ = [0,8 −0,6 −0,2] (4.39)
𝑑𝑒𝑠𝑖𝑔𝑛
Kalikan ℎ dengan bobot hidden-output untuk menghitung skor prediksi
𝑑𝑒𝑠𝑖𝑔𝑛
kata target dengan konteksnya tertera pada Persamaan 4.40 sampai dengan
Persamaan 4.41.

# ,3 −0,2 −0,2 ⋯ 0,3
𝑢 = [0,8 −0,6 −0,2] × [−0,4 −0,3 0,3 ⋯ 0 ] (4.40)

# ,1
−0,1 −0,8 0,2 ⋯ −0,6
𝑢 = 0,8 (0,3)+(−0,6) (−0,4)+(−0,2)(−0,1) = 0,5 (4.41)

# ,1
Matriks hasil berbentuk 1×24 yang tertera pada Persamaan 4.42.
𝑧 = [0,5 0,18 0,1 −0,22 … −0,32 −0,26 0,36] (4.42)
𝑑𝑒𝑠𝑖𝑔𝑛

# 87
Setelah didapatkan skor prediksi, lakukan normalisasi dengan Softmax dengan
rumus seperti Persamaan 4.43.
𝑒𝑥𝑝(𝑘)
𝑦̂ = 𝑃(𝑘𝑎𝑡𝑎 |𝑘𝑎𝑡𝑎 ) = (4.43)
𝑘 𝑟 𝑘 𝑘𝑜𝑛𝑡𝑒𝑘𝑠
∑ 𝑛𝑒𝑥𝑝(𝑛)
Jumlahkan semua nilai eksponensial untuk denominator seperti Persamaan

## sampai dengan 4.45.
𝑒𝑥𝑝(0,5)+𝑒𝑥𝑝(0,18)+⋯+𝑒𝑥𝑝(−0,26)+𝑒𝑥𝑝(0,36) = 24.5489614 (4.44)

# ,648721271
𝑢 = = 0,06716053035 (4.45)

# ,1
# ,54896145
Matriks Softmax untuk kata target “design” berbentuk 1×24 tertera pada
Persamaan 4.46.
𝑦̂ = [0,0671605 0,04876856 … 0,0314087 0,0583866] (4.46)
𝑑𝑒𝑠𝑖𝑔𝑛
Selanjutnya dilakukan backpropagation untuk memperbaharui nilai bobot
matriks dengan rumus seperti Persamaan 4.47.
𝑑𝐿𝑜𝑠𝑠
= 𝑑𝑧 = 𝑦̂ −𝑦(1×𝑉) (4.47)
𝑑𝑧
Diketahui nilai 𝑦 untuk konteks “ability” pada Persamaan 4.48 dan
“development” pada Persamaan 4.49.
𝑦 = [0 1 0 0 … 0 0 0] (4.48)
𝑎𝑏𝑖𝑙𝑖𝑡𝑦
𝑦 = [0 0 0 1 … 0 0 0] (4.49)
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡
Maka, perhitungan error konteks “ability” pada kata target “design” tertera
pada Persamaan 4.50 sampai dengan Persamaan 4.51.
𝑒 = [0,0672 0,0488 … 0,0314 0,0584]−[0 1 … 0] (4.50)
𝑎𝑏𝑖𝑙𝑖𝑙𝑡𝑦
𝑒 = [0,0672 −0,9512 … 0,0314 0,0584] (4.51)
𝑎𝑏𝑖𝑙𝑖𝑙𝑡𝑦
Perhitungan error konteks “development” pada kata target “design” tertera
pada Persamaan 4.52 sampai dengan Persamaan 4.53.
𝑒 = [0,0672 0,0488 … 0,0314 0,0584]−[0 … 0] (4.52)
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡
𝑒 = [0,0672 0,0488 … 0,0314 0,0584] (4.53)
𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡

# 88
Perhitungan error rata-rata dari kedua konteks tertera pada Persamaan 4.54
sampai dengan Persamaan 4.56.
𝑒 +𝑒
𝑒 = 𝑎𝑏𝑖𝑙𝑖𝑡𝑦 𝑑𝑒𝑣𝑒𝑙𝑜𝑝𝑚𝑒𝑛𝑡 (4.54)
𝑐𝑜𝑛𝑡𝑒𝑥𝑡

# 2
# ,06716053035+0,06716053035
𝑒 = = 0,06716053035 (4.55)
𝑐𝑜𝑛𝑡𝑒𝑥𝑡1,1

# 2
−0,9512314456+0,04876855444
𝑒 = = −0,4512314456 (4.56)
𝑐𝑜𝑛𝑡𝑒𝑥𝑡1,2

# 2
Matriks error konteks tertera pada Persamaan 4.57.
𝑑𝑧 = [0,06716053 −0,4512314 … 0,03140873 0,05838656] (4.57)
Setelah mendapatkan hasil perhitungan error, dilanjutkan dengan perhitungan
gradien dari output layer ke hidden layer dengan rumus seperti pada Persamaan

## 4.58
𝑑𝐿𝑜𝑠𝑠 = 𝑑𝑈 = ℎ𝑇.𝑑𝑧(𝑁×𝑉) (4.58)
𝑑𝑈
Diketahui matriks ℎ dan dilakukan transpose pada Persamaan 4.59
𝑑𝑒𝑠𝑖𝑔𝑛
sampai dengan 4.60.
ℎ = [0,8 −0,6 −0,2] (4.59)
𝑑𝑒𝑠𝑖𝑔𝑛

# ,8
ℎ𝑇 = [−0,6] (4.60)
𝑑𝑒𝑠𝑖𝑔𝑛
−0,2
Maka, perhitungan 𝑑𝑈 tertera pada Persamaan 4.61.

# ,8
𝑑𝑈 = [−0,6]×[0,0672 −0,4512 … 0,0314 0,0584] (4.61)
−0,2
𝑑𝑈 = 0,8×0,067160530 = 0,05372842428 (4.62)

# ,1
𝑑𝑈 = 0,6×0,067160530 = −0,04029631821 (4.63)

# ,1
𝑑𝑈 = 0,8×−0,45123144 = −0,3609851564 (4.64)

# ,2
𝑑𝑈 = 0,6×−0,45123144 = 0,2707388673 (4.65)

# ,2
Matriks 𝑑𝑈 berbentuk 3×24 tertera pada Persamaan 4.66.

# ,05372842428 −0,3609851564 … 0,04670924812
𝑑𝑈 = [−0,04029631821 0,2707388673 … −0,03503193609] (4.66)
−0,01343210607 0,09024628911 … −0,01167731203

# 89
Setelah mendapatkan hasil perhitungan gradien dari output layer ke hidden
layer, dilanjutkan menghitung gradien dari hidden layer ke input layer dengan
rumus seperti pada Persamaan 4.67.ex
𝑑𝐿𝑜𝑠𝑠 = 𝑑𝐿𝑜𝑠𝑠 . 𝑑𝑧 = 𝑑𝑧.𝑈𝑇(1×𝑁) (4.67)
𝑑ℎ 𝑑𝑧 𝑑ℎ
Diketahui matriks hidden layer 1, 2, dan 3 dilakukan transpose pada Persamaan

## sampai dengan 4.73.
ℎ = [0,3 −0,2 −0,2 … 0,3] (4.68)

# 1
# ,2
−0,2
ℎ𝑇 = −0,2 (4.69)

# 1
⋮
[ 0,3 ]
ℎ = [−0,4 −0,3 −0,6 … 0] (4.70)

# 2
−0,4
−0,3
ℎ𝑇 = −0,6 (4.71)

# 2
⋮
[ 0 ]
ℎ = [−0,1 −0,8 −0,5 … −0,6] (4.72)

# 3
−0,1
−0,8
ℎ𝑇 = −0,5 (4.73)

# 3
⋮
[−0,6]
𝑑𝐿𝑜𝑠𝑠
Maka, perhitungan tertera pada Persamaan 4.74 sampai dengan
𝑑ℎ
Persamaan 4.76.

# ,2
−0,2
𝑑𝐿𝑜𝑠𝑠
= [0,0672 −0,4512 … 0,0314 0,0584]× −0,2 (4.74)
𝑑ℎ1
⋮
[ 0,3 ]
𝑑𝐿𝑜𝑠𝑠
= (0,0672×0,2)+(−0,4512 ×(−0,2))+ … +(0,0584 ×0,3) (4.75)
𝑑ℎ1
𝑑𝐿𝑜𝑠𝑠
= 0,1147162368 (4.76)
𝑑ℎ1

# 90
𝑑𝐿𝑜𝑠𝑠 𝑑𝐿𝑜𝑠𝑠
Hitung dengan persamaan yang sama untuk dan . Maka hasil
𝑑ℎ2 𝑑ℎ3
perhitungan gradien dari hidden layer ke input layer tertera pada Persamaan 4.77
sampai dengan 4.79.
𝑑𝐿𝑜𝑠𝑠
= 0,1147162368 (4.77)
𝑑ℎ1
𝑑𝐿𝑜𝑠𝑠
= −0,06109851674 (4.78)
𝑑ℎ2
𝑑𝐿𝑜𝑠𝑠
= 0,2272906395 (4.79)
𝑑ℎ3
Pembaharuan bobot dihitung menggunakan learning rate dan gradien dari
hidden layer ke input layer dilakukan seperti pada Persamaan 4.80 sampai dengan
Persamaan 4.82.

# 𝑊 = 0,8−(0,1×0,1147162368) = 0,7885283763 (4.80)
# ,1
# 𝑊 = (−0,6)−(0,1×−0,06109851674) = −0,5938901483 (4.81)
# ,2
# 𝑊 = (−0,2)−(0,1×0,2272906395) = −0,222729064 (4.82)
# ,3
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

# 91
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
Pembaharuan bobot dihitung menggunakan learning rate dan gradien dari
hidden layer ke input layer dilakukan seperti pada Persamaan Persamaan 4.83
sampai dengan Persamaan 4.90.
𝑊 = 𝑊 −(0,1×𝑑𝑈) (4.83)
𝑡+1 𝑡

# ,3 … 0,3 0,0537 … 0,0467
𝑊 = [−0,4 … 0 ]−(0,1×[−0,0403 … −0,0350]) (4.84)
𝑡+1
−0,1 … −0,6 −0,0134 … −0,0117

# 𝑊 = 0,3−(0,1×0,05372842428) = 0,2946271576 (4.85)
𝑡+11,1

# 𝑊 = 0,3−(0,1×0,04670924812) = 0,2953290752 (4.86)
𝑡+11,24

# 𝑊 = −0,4−(0,1(−0,04029631821)) = −0,3959703682 (4.87)
𝑡+12,1

# 𝑊 = 0−(0,1(−0,03503193609)) = 0,003503193609 (4.88)
𝑡+12,24

# 𝑊 = −0,1−(0,1(−0,01343210607) = −0,09865678939 (4.89)
𝑡+13,1

# 𝑊 = −0,6−(0,1(−0,01167731203)) = −0,5988322688 (4.90)
𝑡+13,24
Hasil pembaharuan bobot hidden layer ke output layer tertera pada Tabel 4.43
hingga Tabel 4.46.
Tabel 4.43 Pembaharuan bobot input layer-output layer
Neuron demonstr ability design developm appropria lesson
ated entally te

# H1 0,294627 -0,16390 -0,20360 0,037385 -0,20319 -0,10319
# H2 -0,39597 -0,32707 -0,5973 0,271961 -0,09760 -0,19760
# H3 -0,09866 -0,80902 0,500900 0,190654 -0,39920 0,300799
# 92
Tabel 4.44 Pembaharuan bobot input layer-output layer
Neuron activity allow integratio learning style highly
n

# H1 -0,10262 0,295235 -0,20237 -0,10319 -0,10262 0,295235
# H2 0,301961 -0,19643 0,301775 -0,19760 0,301961 -0,19643
# H3 -0,19935 -0,09881 -0,09941 0,3008 -0,19935 -0,09881
Tabel 4.45 Pembaharuan bobot input layer-output layer
Neuron educate differenti classroo determin maximize education
ated m ed al

# H1 -0,20237 -0,10319 -0,10262 0,295235 -0,20237 -0,10319
# H2 0,301775 -0,19760 0,301961 -0,19643 0,301775 -0,19760
# H3 -0,09941 0,300799 -0,19935 -0,09881 -0,09941 0,300799
Tabel 4.46 Pembaharuan bobot input layer-output layer
Neuron achievem student trained developm reading assessme
ent ental nts

# H1 -0,10262 0,295235 -0,20237 -0,40237 -0,10251 0,295329
# H2 0,301961 -0,19643 0,301775 -0,09823 0,301885 0,003503
# H3 -0,19935 -0,09881 -0,09941 0,300592 0,000628 -0,59883
# 93
## Perhitungan Manual Similaritas
Perhitungan manual similaritas dilakukan menggunakan vektor TF-IDF dan
Word2Vec dari resume dengan ID 15265464 dan section Experience. Sedangkan
untuk kualifikasi lowongan kerja menggunakan posisi Teacher dari PT Abadi
Cahaya Edukasi. Isian data sampel yang dimaksud tertera pada Tabel 4.47.
Tabel 4.47 Data sampel perhitungan manual similaritas

## Resume Kualifikasi Lowongan Kerja
intervention specialist teacher math play vital role support lead teacher create
language arts identified student nurturing stimulate learning environment
substantial academic difficulty evaluation young student assist lead teacher
use developmental reading assessments planning implement engage educational
consultation staff member referred activity child age 36 year help maintain
student developed differentiate lesson safe organised classroom environment
plan select appropriate instructional provide individual attention support
material reach individualized student goal student needed collaborate teach team
developed implement creative lesson monitor record childrens progress
clear objective link common core participate staff meeting professional
incorporate differentiated instruction development opportunity maintain open
attended gain knowledge numerous communication parent caregiver ensure
service improved overall lexiles test score compliance relevant childcare regulation
facilitated group lesson dependent policy diploma degree early childhood
student reading level determine run education related field least 1 year
record assessment evaluated student experience work childcare educational
growth progress monitoring formal setting strong interpersonal
informal assessment instructed student communication skill patience creativity
accordance schedule previously devise genuine passion work young child ability
enhanced lesson use smart board work collaboratively part team
technology computer assessed regular knowledge child development
basis objective student set led basic skill ageappropriate teaching method
class student time conducted small group proficiency bahasa indonesia english
individual classroom activity student base
differentiated learning need nd grade
replacement teacher implement positive
behavior management use color system
developed clear objective student parent
lesson activity designed differentiated
common core lesson plan activity meet
need learner enhanced lesson use
smartboard technology pads computer
lab assessed student growth informal
formal assessment developed lesson
accordance student reading level
determine quarterly running record
testing maintained positive collaboration
communication parent weekly newsletter
weekly student progress update email
conference attended service staff...

# 94
## Perhitungan Manual TF-IDF Dengan Improved Sqrt-Cosine
## Similarity
Untuk metode representasi teks menggunakan TF-IDF, langkah pertama
adalah mengambil nilai vektor 𝑥 (resume) dan vektor 𝑦 (kualifikasi lowongan kerja)
dari hasil TF-IDF. Vektor resume dan kualifikasi lowongan kerja tertera pada Tabel

## 4.48
Tabel 4.48 Vektor TF-IDF perhitungan manual Improved Sqrt-Cosine Similarity

## Resume Kualifikasi Lowongan Kerja
[0 ... 0 ... 0,03772064 ... 0 ... 0 ... [0 ... 0 ... 0,06593613 ... 0 ... 0 ...

# ,07763420 ... 0 ... 0 ... 0,11012862 ... 0] 0,06276407 ... 0 ... 0 ... 0,09679995 ... 0]
Hitung penjumlahan dari akar perkalian elemen-elemen yang sesuai antara
vektor 𝑥 dan 𝑦 sebagai numerator menggunakan formula seperti pada Persamaan

## 4.91
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = ∑𝑚 √𝑥 𝑦 (4.91)
𝑖=1 𝑖 𝑖
Demonstrasi perhitungan tertera mulai dari Persamaan 4.92 sampai dengan
Persamaan 4.94.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = √𝑥 𝑦 +√𝑥 𝑦 +⋯+√𝑥 𝑦 +⋯+√𝑥 𝑦 (4.92)

# 1 2 2 526 526 43331 43331
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = √0×0+√0×0+⋯+√0,110×0,063+⋯+√0×0 (4.93)
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = 1,4044 (4.94)
Hitung hasil kali dari akar penjumlahan semua elemen masing-masing vektor 𝑥
(resume) dan vektor 𝑦 (kualifikasi) sebagai denominator dengan formula seperti
pada Persamaan 4.95.
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(∑𝑚 𝑥 )√(∑𝑚 𝑦 ) (4.95)
𝑖=1 𝑖 𝑖=1 𝑖
Demonstrasi perhitungan tertera mulai dari Persamaan 4.96 sampai dengan
Persamaan 4.98.
𝒅𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(𝑥 +𝑥 +⋯+𝑥 +⋯+𝑥 )×

# 2 526 43331
√(𝑦 +𝑦 +⋯+𝑦 +⋯+𝑦 ) (4.96)

# 2 526 43331
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(0+0+⋯+0,1101+⋯+0)×
√(0+0+⋯+0,0628+⋯+0) (4.97)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = 8,4315 (4.98)

# 95
Skor similaritas Improved Sqrt-Cosine didapatkan dengan membagi numerator
dengan denominator seperti formula pada Persamaan 4.99.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟

# 𝐼𝑆𝐶 = (4.99)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟
Hasil pembagian antara numerator dengan denominator yang sudah
didapatkan tertera pada Persamaan 4.100.

# ,4044
# 𝐼𝑆𝐶 = = 0,1666 (4.100)
# ,4315
Hasil similaritas antara keseluruhan section resume ID 15265464 dengan
kualifikasi lowongan kerja posisi Teachers tertera pada Tabel 4.49.
Tabel 4.49 Hasil skor similaritas resume ID 15265464 perhitungan manual
Improved Sqrt-Cosine Similarity

## Section Skor Similaritas
Education 0,1365
Experience 0,1666
Summary 0,1460
Pengujian pada penelitian ini menggunakan dua skenario, yakni “Tanpa Bobot”
dan “Dengan Bobot”. Pada skenario “Tanpa Bobot”, skor similaritas untuk masing-
masing section di resume ID 15265464 langsung dijumlah dan dirata-ratakan
seperti pada Persamaan 4.101.

# ,1365+0,1666+0,1460
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = = 0,1497 (4.101)

# 3
Pada skenario “Dengan Bobot”, skor similaritas untuk masing-masing section
di resume ID 15265464 dikalikan dengan persentase bobot yang diberikan oleh
ahli, lalu ditotal dan dibagi dengan jumlah persentase section yang digunakan pada
resume. Pada kategori industri “TEACHER”, diketahui rincian bobot untuk setiap
section tertera pada Tabel 4.50.
Tabel 4.50 Bobot section kategori industri "TEACHER"
Industry Section Bobot (%)

## TEACHER Summary 5
TEACHER Accomplishments/Awards 15
TEACHER Skills/Qualifications 20

## TEACHER Education 20
## TEACHER Experience 20
# 96
Tabel 4.50 Bobot section kategori industri "TEACHER" (lanjutan)
Industry Section Bobot (%)

## TEACHER Organization 5
## TEACHER Projects 5
## TEACHER Certifications 10
## TEACHER Portfolio 10
Maka total skor similaritas untuk resume ID 15265464 dapat dihitung seperti
pada Persamaan 4.102 sampai dengan Persamaan 4.103.
(0,1365×0,2)+(0,1666×0,2)+(0,1460×0,05)
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = (4.102)
(0,2+0,2+0,05)

# ,0273+0,03332+0,0073
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = = 0,1509 (4.103)

# ,45
## Perhitungan Manual Word2Vec Dengan Cosine Similarity
Untuk metode representasi teks menggunakan Word2Vec, langkah pertama
adalah mengambil nilai rata-rata dokumen untuk keseluruhan vektor 𝑥 (resume)
dan keseluruhan vektor 𝑦 (kualifikasi lowongan kerja) dari hasil Word2Vec. Vektor
resume dan kualifikasi lowongan kerja tertera pada Tabel 4.51.
Tabel 4.51 Vektor Word2Vec perhitungan manual Cosine Similarity

## Resume Kualifikasi
[0,071130395 0,12649915 [-0,04582439 0,0966028
-0,1145207 -0,08985851 ... 0,19086754] -0,18032219 -0,11506447 ... 0,11572151]
Hitung penjumlahan dari perkalian elemen-elemen yang bersesuaian antara
vektor 𝑥 dan 𝑦 sebagai numerator menggunakan formula seperti pada Persamaan

## 4.104
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = ∑𝑚 𝑥 𝑦 (4.104)
𝑖=1 𝑖 𝑖
Demonstrasi perhitungan tertera mulai dari Persamaan 4.105 sampai dengan
Persamaan 4.107.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = 𝑥 𝑦 +𝑥 𝑦 +⋯+𝑥 𝑦 (4.105)

# 1 2 2 100 100
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = (0,0711×(−0,0458))+(0,1265×0,0966)+⋯+(0,1909×

# ,1157) (4.106)
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = (−0,00323)+0,01221+⋯+0,02208 = 1,9022 (4.107)

# 97
Hitung hasil kali dari akar semua elemen masing-masing vektor 𝑥 (resume) dan
vektor 𝑦 (kualifikasi) yang dikuadratkan sebagai denominator dengan formula
seperti pada Persamaan 4.108.
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(∑𝑚 𝑥 2)√(∑𝑚 𝑦 2) (4.108)
𝑖=1 𝑖 𝑖=1 𝑖
Demonstrasi perhitungan tertera mulai dari Persamaan 4.109 sampai dengan
Persamaan 4.111.
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(𝑥 2 +𝑥 2 +⋯+𝑥 2)×√(𝑦 2+𝑦 2 +⋯+𝑦 2)

# 2 100 1 2 100
(4.109)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(0,07112 +0,12652 +⋯+0,19092)×
√((−0,0458)2 +0,09662 +⋯+0,11572) (4.110)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = 2,1667 (4.111)
Skor Cosine Similarity didapatkan dengan membagi numerator dengan
denominator seperti formula pada Persamaan 4.112.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟
𝐶𝑜𝑠𝑆𝑖𝑚 = (4.112)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟
Hasil pembagian antara numerator dengan denominator yang sudah
didapatkan tertera pada Persamaan 4.113.

# ,9022
𝐶𝑜𝑠𝑆𝑖𝑚 = = 0,8779 (4.113)

# ,1667
Hasil similaritas antara keseluruhan section resume ID 15265464 dengan
kualifikasi lowongan kerja posisi Teachers tertera pada Tabel 4.52.
Tabel 4.52 Hasil skor similaritas resume ID 15265464 perhitungan manual

## Cosine Similarity
## Section Skor Similaritas
Education 0,7303
Experience 0,8779
Summary 0,9277

# 98
Pengujian pada penelitian ini menggunakan dua skenario, yakni “Tanpa Bobot”
dan “Dengan Bobot”. Pada skenario “Tanpa Bobot”, skor similaritas untuk resume
ID 15265464 bisa langsung dijumlah dan dirata-ratakan seperti pada Persamaan

## 4.114
# ,7303+0,8779+0,9277
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = = 0,8453 (4.114)

# 3
Pada skenario “Dengan Bobot”, skor similaritas untuk masing-masing section
di resume ID 15265464 dikalikan dengan persentase bobot yang diberikan oleh
ahli. Pada kategori industri “TEACHER”, diketahui rincian bobot untuk setiap
section tertera pada Tabel 4.50 sebelumnya.
Maka total skor similaritas untuk resume ID 15265464 dapat dihitung seperti
pada Persamaan 4.115 sampai dengan Persamaan 4.116.
(0,7303×0,2)+(0,8779×0,2)+(0,9277×0,05)
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = (4.115)
(0,2+0,2+0,05)

# ,14606+0,17558+0,046385
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = = 0,8178 (4.116)

# ,45
## Perhitungan Manual Word2Vec Dengan Improved Sqrt-
## Cosine Similarity
Pada perhitungan manual sebelumnya sudah dirincikan nilai rata-rata
dokumen untuk keseluruhan vektor 𝑥 (resume) dan keseluruhan vektor 𝑦
(kualifikasi lowongan kerja) dari hasil Word2Vec yang tertera pada Tabel 4.51.
Namun, untuk menghitung similaritasnya dengan Improved Sqrt-Cosine, perlu
mengonversi nilai vektor-vektornya menjadi absolut karena akan menjadi
bilangan imajiner jika nilai negatif diakarkan. Vektor resume dan kualifikasi
lowongan kerja tertera pada Tabel 4.53.
Tabel 4.53 Vektor Word2Vec perhitungan manual Improved Sqrt-Cosine

## Similarity
## Resume Kualifikasi
[0,071130395 0,12649915 0,1145207 [0,04582439 0,0966028 0,18032219

# ,08985851 ... 0,19086754] 0,11506447 ... 0,11572151]
Hitung penjumlahan dari akar perkalian elemen-elemen yang sesuai antara
vektor 𝑥 dan 𝑦 sebagai numerator menggunakan formula seperti pada Persamaan

## 4.117
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = ∑𝑚 √𝑥 𝑦 (4.117)
𝑖=1 𝑖 𝑖

# 99
Demonstrasi perhitungan tertera mulai dari Persamaan 4.118 sampai dengan
Persamaan 4.120.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = √𝑥 𝑦 +√𝑥 𝑦 +⋯+√𝑥 𝑦 (4.118)

# 1 2 2 100 100
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = √0,0711×−0,0458+√0,1265×0,0966+⋯+
√0,1909×0,1157 (4.119)
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟 = 11,2936 (4.120)
Hitung hasil kali dari akar penjumlahan semua elemen masing-masing vektor 𝑥
(resume) dan vektor 𝑦 (kualifikasi) sebagai denominator dengan formula seperti
pada Persamaan 4.121.
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(∑𝑚 𝑥 )√(∑𝑚 𝑦 ) (4.121)
𝑖=1 𝑖 𝑖=1 𝑖
Demonstrasi perhitungan tertera mulai dari Persamaan 4.122 sampai dengan
Persamaan 4.124.
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(𝑥 +𝑥 +⋯+𝑥 )×√(𝑦 +𝑦 +⋯+𝑦 ) (4.122)

# 2 100 1 2 100
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = √(0,0711+0,1265+⋯+0,1909)×
√(0,0458+0,0966+⋯+0,1157) (4.123)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟 = 11,861 (4.124)
Skor similaritas Improved Sqrt-Cosine didapatkan dengan membagi numerator
dengan denominator seperti formula pada Persamaan 4.125.
𝑛𝑢𝑚𝑒𝑟𝑎𝑡𝑜𝑟

# 𝐼𝑆𝐶 = (4.125)
𝑑𝑒𝑛𝑜𝑚𝑖𝑛𝑎𝑡𝑜𝑟
Hasil pembagian antara numerator dengan denominator yang sudah
didapatkan tertera pada Persamaan 4.126.

# ,2936
# 𝐼𝑆𝐶 = = 0,9521 (4.126)
# ,861
Hasil similaritas antara keseluruhan section resume ID 15265464 dengan
kualifikasi lowongan kerja posisi Teachers tertera pada Tabel 4.54.
Tabel 4.54 Hasil skor similaritas resume ID 15265464 perhitungan manual
Improved Sqrt-Cosine Similarity

## Section Skor Similaritas
Education 0,9065

# 100
Tabel 4.54 Hasil skor similaritas resume ID 15265464 perhitungan manual
Improved Sqrt-Cosine Similarity

## Section Skor Similaritas
Experience 0,9521
Summary 0,9657
Pengujian pada penelitian ini menggunakan dua skenario, yakni “Tanpa Bobot”
dan “Dengan Bobot”. Pada skenario “Tanpa Bobot”, skor similaritas untuk resume
ID 15265464 bisa langsung dijumlah dan dirata-ratakan seperti pada Persamaan

## 4.127
# ,9065+0,9521+0,9657
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = = 0,9414 (4.127)

# 3
Pada skenario “Dengan Bobot”, skor similaritas untuk masing-masing section
di resume ID 15265464 dikalikan dengan persentase bobot yang diberikan oleh
ahli. Pada kategori industri “TEACHER”, diketahui rincian bobot untuk setiap
section tertera pada Tabel 4.50 sebelumnya.
Maka total skor similaritas untuk resume ID 15265464 dapat dihitung seperti
pada Persamaan 4.128 sampai dengan Persamaan 4.129.
(0,9065×0,2)+(0,9521×0,2)+(0,9657×0,05)
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = (4.128)
(0,2+0,2+0,05)

# ,1813+0,19042+0,048285
𝑆𝑖𝑚𝑖𝑙𝑎𝑟𝑖𝑡𝑦 = = 0,93334 (4.129)

# ,45
## Skenario Pengujian
Pengujian akan dilakukan dengan human-level performance, dihitung
parameter setiap parameter penilaiannya, mulai dari korelasi peringkat dengan
Spearman Rank Correlation Coefficient (SRCC), persentase relevansi, dan
persentase senioritas.
Setelah implementasi metode menghasilkan skor similaritas resume terhadap
setiap kualifikasi lowongan kerja, diberikan pemeringkatan berdasarkan skor
similaritas tertinggi, lalu diambil lima resume teratas. Kemudian, lima resume
tersebut diberikan kepada seorang ahli di bidang rekrutmen untuk dinilai
relevansinya secara manual. Ahli akan memberikan peringkat secara ulang sebagai
ground truth dari peringkat satu sampai lima yang telah dihasilkan implementasi
metode terhadap kualifikasi lowongan kerja tersebut. Selain itu, ahli akan
mengevaluasi lima resume tersebut untuk memastikan relevansi dengan
kualifikasi lowongan kerja yang tertera pada deskripsi lowongan kerja serta
kesesuaian tingkat senioritas atau level posisi dengan deskripsi kualifikasi
lowongan kerja.

# 101
Korelasi antara peringkat yang dihasilkan oleh implementasi metode dan
peringkat dari ahli menunjukkan sejauh mana implementasi metode dapat meniru
penilaian manusia. Semakin tinggi nilai korelasi (mendekati 1), semakin baik
kinerja implementasi metode dalam menyelaraskan hasilnya dengan penilaian
ahli. Untuk setiap implementasi metode, dilakukan perhitungan SRCC yang sama,
maka untuk demonstrasi perhitungan SRCC akan menggunakan hasil
pemeringkatan dari implementasi TF-IDF dengan Improved Sqrt-Cosine Similarity
(ISC) pada kualifikasi lowongan kerja posisi “Teachers” skenario “Tanpa Bobot”
yang tertera pada Tabel 4.55.
Tabel 4.55 Peringkat 1-5 resume dengan skor similaritas terbesar untuk
perhitungan manual SRCC

## Resume_ID Peringkat Peringkat Ahli
# 1 3
# 2 1
# 3 4
# 4 2
# 5 5
Setelah diketahui peringkat lima resume dengan skor similaritas terbesar hasil
implementasi metode dan peringkat dari ahli, selanjutnya adalah menghitung
selisih peringkat dan dikuadratkan yang didemonstrasikan pada Tabel 4.56.
Tabel 4.56 Selisih peringkat 1-5 resume perhitungan manual SRCC
Resume_ID Peringkat Peringkat Ahli Selisih (𝒅 𝒊 ) 𝒅 𝒊 𝟐

# 1 3 1−3 = −2 4
# 2 1 2−1 = 1 1
# 3 4 3−4 = −1 1
# 4 2 4−2 = 2 4
# 5 5 5−5 = 0 0
Pada Tabel 4.56, diketahui hasil kuadrat dari selisih perangkat. Jumlahkah hasil
kuadrat tersebut untuk perhitungan SRCC sebagai numerator seperti pada
Persamaan 4.130.
∑𝑑 2 = 4+1+1+4+0 = 10 (4.130)
𝑖

# 102
Gunakan rumus SRCC seperti Persamaan 4.131 untuk menghitung korelasi
antara peringkat hasil implementasi dengan peringkat ahli.

# ∑𝑑
𝑆𝑅𝐶𝐶 = 1− 𝑖 (4.131)
𝑛(𝑛2−1)
Demonstrasi perhitungan untuk peringkat lima resume dijabarkan mulai dari
Persamaan 4.132 sampai dengan Persamaan 4.135.

# ×10
# 𝑆𝑅𝐶𝐶 = 1− (4.132)
# (52−1)
# 60
# 𝑆𝑅𝐶𝐶 = 1− (4.133)
# (24)
# 60
# 𝑆𝑅𝐶𝐶 = − (4.134)
# 120
# 60
# 𝑆𝑅𝐶𝐶 = = 0,5 (4.135)
# 120
Hasil evaluasi relevansi dari ahli dihitung dalam bentuk persentase. Semakin
besar persentase maka semakin baik suatu metode menghasilkan lima resume
yang relevan dengan deskripsi lowongan kerja. Sama halnya dengan hasil evaluasi
senioritas dari ahli, semakin besar persentase maka semakin baik suatu metode
mengenali lima resume dengan level posisi yang sesuai. Untuk setiap
implementasi metode, dilakukan perhitungan relevansi dan senirotas yang sama,
maka untuk demonstrasi perhitungan relevansi dan senioritas akan menggunakan
hasil pemeringkatan dari implementasi TF-IDF dengan Improved Sqrt-Cosine
Similarity (ISC) pada kualifikasi lowongan kerja posisi “Teachers” skenario “Tanpa
Bobot” yang tertera pada Tabel 4.57
Tabel 4.57 Peringkat 1-5 resume dengan hasil evaluasi relevansi dan senioritas
ahli terbesar untuk perhitungan manual

## Resume_ID Relevance Seniority
# TRUE TRUE
# TRUE TRUE
# TRUE TRUE
# TRUE TRUE
# FALSE TRUE
# 103
Untuk masing-masing parameter (relevansi dan senioritas), hitung pembagian
antara jumlah nilai “TRUE” dengan jumlah total resume, lalu kalikan 100% seperti
pada Persamaan 4.136 untuk relevansi dan 4.137 untuk senioritas.

# 𝑃 = (
𝑁𝑟)×100%
(4.136)
𝑅𝑒𝑙𝑒𝑣𝑎𝑛𝑐𝑒

# 𝑁
# 𝑃 = (
𝑁𝑠)×100%
(4.137)
𝑆𝑒𝑛𝑖𝑜𝑟𝑖𝑡𝑦

# 𝑁
## Keterangan
𝑃 = Persentase relevansi
𝑅𝑒𝑙𝑒𝑣𝑎𝑛𝑐𝑒
𝑃 = Persentase senioritas
𝑆𝑒𝑛𝑖𝑜𝑟𝑖𝑡𝑦
𝑁 = Jumlah resume dengan relevansi bernilai TRUE
𝑟
𝑁 = Jumlah resume dengan senioritas bernilai TRUE
𝑠
𝑁 = Total jumlah resume
Demonstrasi perhitungan untuk relevansi lima resume tertera pada
Persamaan 4.138.

# 4
𝑃 = ( )×100% = 0,8×100% = 80% (4.138)
𝑅𝑒𝑙𝑒𝑣𝑎𝑛𝑐𝑒

# 5
Demonstrasi perhitungan untuk senioritas lima resume tertera pada
Persamaan 4.139.

# 5
𝑃 = ( )×100% = 1×100% = 100% (4.139)
𝑆𝑒𝑛𝑖𝑜𝑟𝑖𝑡𝑦

# 5
# 104
# BAB 5 IMPLEMENTASI
# mplementasi berisi implementasi dari metode kalkulasi similaritas teks
pada resume pelamar dengan kualifikasi instansi yang digunakan pada penelitian
ini, seperti metode perhitungan similaritas Improved Sqrt-Cosine (ISC) dan Cosine
Similarity (CosSim), serta metode representasi teks TF-IDF dan Word2Vec.

## Implementasi Kode Program Import Libraries dan Load
## Dataset
Dalam kode program ini, dilakukan pemuatan dataset resume yang akan
dikelola dan dataset kualifikasi lowongan kerja yang dikumpulkan dari
https://id.jobstreet.com/ dengan 24 posisi kualifikasi lowongan kerja.
Implementasi kode program tertera pada Kode Program 5.1.
Kode Program 5.1 Implementasi kode program import libraries dan load
dataset

# import pandas as pd
# from bs4 import BeautifulSoup
# import re
# from gensim.models import Word2Vec
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.feature_extraction.text import TfidfVectorizer
# import string
# from tqdm import tqdm
# import time
# 11
# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('averaged_perceptron_tagger_eng')
# 18
# from nltk.corpus import wordnet
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# 24
# # Load dataset resume
# resume_df =
pd.read_csv(r'C:\...\archive2024\Resume\Resume.csv')

# resume_df
# 28
# # Load dataset kualifikasi lowongan kerja
# vacancy_df =
pd.read_csv(r'C:\...\archive2024\kualifikasi_loker.csv')

# vacancy_df
# 32
# 105
Kode Program 5.1 Implementasi kode program import libraries dan load
dataset (lanjutan)

# # Load dataset bobot section
# section_df =
pd.read_csv(r'C:\...\archive2024\bobot_section.csv')

# section_df
Penjelasan dari Kode Program 5.1 mengenai implementasi import libraries dan
load dataset, yaitu:

# Baris 1-10 merupakan proses import library yang diperlukan untuk:
a. pandas alias pd untuk manipulasi data dan analisis data,
b. BeautifulSoup dari library bs4 untuk ekstraksi teks dari HTML,

# re untuk ekspresi reguler atau regular expression (REGEX),
d. gensim.models import Word2Vec untuk menggunakan
library Gensim dalam implementasi representasi teks
menggunakan pendekatan Word2Vec,
e. numpy alias np untuk operasi numerik seperti perhitungan
matematis,
f. sklearn.metrics.pairwise import
cosine_similarity untuk menghitung kesamaan antar
vektor teks menggunakan Cosine Similarity dari library Scikit-learn,
g. sklearn.feature_extraction.text import
TfidfVectorizer untuk menggunakan library Scikit-learn
dalam implementasi representasi teks menggunakan pendekatan

# TF-IDF,
h. import string untuk menyediakan daftar karakter tanda baca
untuk preprocessing teks,

# from tqdm import tqdm untuk menampilkan progress bar
guna memantau progress dari suatu proses,
j. import time untuk mengukur waktu eksekusi.

# Baris 12-17 merupakan proses import library dari nltk (Natural Language
Toolkit) yang digunakan untuk pemrosesan teks, termasuk unduhan
resource yang diperlukan untuk tokenisasi, lematisasi, dan Part of Speech
(POS) tagging, seperti:
a. wordnet merupakan basis data leksikal Bahasa Inggris,
b. omw-1.4 merupakan Open Multilingual Wordnet versi 1.4 untuk
mendukung lematisasi dalam berbagai bahasa,

# Punkt untuk memecah teks atau tokenisasi teks
d. averaged_perceptron_tagger dan
averaged_perceptron_tagger_eng untuk POS tagging
yang memberi label jenis kata seperti kata benda (noun), kata kerja
(verb), kata sifat (adjective), dan kata keterangan (adverb).

# 106
# Baris 19-23 merupakan import tambahan dari library nltk, yaitu:
a. wordnet dari nltk.corpus untuk mengakses basis data
leksikal WordNet,
b. WordNetLemmatizer dari nltk.stem untuk melakukan
mengubah kata ke bentuk dasar atau lematisasi,

# word_tokenize dari nltk.tokenize untuk memecah teks
menjadi token,
d. stopwords dari nltk.corpus menyediakan daftar kata-kata
umum yang tidak bermakna dalam analisis teks untuk dihapus,
e. pos_tag untuk memberikan label POS tagging pada setiap kata
dalam teks.

# Baris 25-26 merupakan proses memuat dataset dari file dengan format .csv
bernama Resume.csv menggunakan pandas.read_csv() yang
berisi informasi resume kandidat dan mengubahnya menjadi DataFrame.

# Baris 27 merupakan sintaksis untuk menampilkan DataFrame
resume_df.

# Baris 29-30 merupakan proses memuat dataset dari file dengan format .csv
bernama kualifikasi_loker.csv menggunakan
pandas.read_csv() dan mengubahnya menjadi DataFrame yang
berisi informasi lowongan pekerjaan, termasuk nama posisi, nama
perusahaan, dan deskripsi kualifikasinya.

# Baris 31 merupakan sintaksis untuk menampilkan DataFrame
vacancy_df.

# Baris 33-34 merupakan proses memuat dataset dari file dengan format .csv
bernama bobot_section.csv menggunakan
pandas.read_csv() dan mengubahnya menjadi DataFrame yang
berisi bobot pemberian ahli untuk setiap section yang ada di resume.

# 107
## Implementasi Kode Program Preprocessing Resume
Dalam kode program ini, dilakukan untuk melakukan pra-pemrosesan dataset
Resume. Diawali dengan mengekstrak setiap section dari resume yang berformat
HTML dan disimpan dalam bentuk DataFrame dengan tambahan informasi
mengenai bagian (section) dan isi teks dari masing-masing section. Implementasi
kode program ekstraksi section tertera pada Kode Program 5.2.
Kode Program 5.2 Implementasi kode program preprocessing resume bagian
ekstraksi section

# # Melihat informasi kolom dan tipe data
# resume_df.info()
# 3
# # Cek missing values
# resume_df.isnull().sum()
# 6
# # Menghapus kolom yang tidak digunakan
# resume_df_1 = resume_df.drop(columns=["Category"])
# 9
# # List untuk menyimpan hasil sementara per section dengan semua
data dari df

# data = []
# 12
# # Loop untuk memproses setiap resume
# for index, row in resume_df.iterrows():
# # Ambil ID dan data lainnya dari DataFrame yang ada
# resume_data = row.to_dict() # Mengambil semua data di
baris ini

# 17
# # Ambil resume_str langsung dari kolom 'Resume_str'
# resume_str = row['Resume_str']
# 20
# # Menemukan semua <div> dengan class "sectiontitle" di
'Resume_html'

# soup = BeautifulSoup(row['Resume_html'], "html.parser")
# section_divs = soup.find_all("div", class_="sectiontitle")
# 24
# # Menyimpan teks dari setiap section
# sections = [div.get_text(strip=True) for div in
section_divs]

# 27
# # Menemukan posisi setiap section dalam resume_str
# for i, section in enumerate(sections):
# # Copy data resume agar setiap section mendapatkan data
asli resume

# section_data = resume_data.copy()
# 32
# # Cari posisi awal section
# start_index = resume_str.find(section)
# 35
# # Tentukan posisi akhir section
# if i + 1 < len(sections):
# end_index = resume_str.find(sections[i + 1],
start_index)

# 108
Kode Program 5.2 Implementasi kode program preprocessing resume bagian
ekstraksi section (lanjutan)

# else:
# end_index = len(resume_str) # Jika ini adalah
section terakhir

# 41
# # Ambil teks dari section tersebut dan hapus nama
section jika ada di awal teks

# section_text =
resume_str[start_index:end_index].strip()

# if section_text.startswith(section):
# section_text = section_text[len(section):].strip()
# 46
# # Tambahkan kolom Section dan Text
# section_data["Section"] = section
# section_data["Text"] = section_text
# 50
# # Tambahkan hasil ke expanded_data
# data.append(section_data)
# 53
# # Mengonversi list menjadi DataFrame
# resume_df_1 = pd.DataFrame(data)
Penjelasan dari Kode Program 5.2 mengenai implementasi kode program
ekstraksi section, yaitu:

# Baris 1-2 merupakan proses untuk menampilkan informasi mengenai
dataset resume, termasuk jumlah kolom, nama kolom, tipe data, dan
jumlah non-null menggunakan df.info().

# Baris 4-5 merupakan proses untuk memeriksa nilai yang hilang (missing
values) dalam dataset resume menggunakan df.isnull().sum().

# Baris 7-8 merupakan proses untuk menghapus kolom Category dari
dataset resume menggunakan df.drop(columns=["Category"])
dan menyimpan hasilnya ke DataFrame baru sebagai resume_df_1.

# Baris 10-11 merupakan proses untuk membuat list kosong bernama data
untuk menyimpan hasil pemrosesan ekstraksi section resume.

# Baris 13-14 merupakan proses untuk memulai iterasi melalui setiap baris
dataset resume menggunakan df.iterrows().

# Baris 15-16 merupakan proses untuk mengubah data baris menjadi
dictionary menggunakan row.to_dict() dan menyimpannya ke
variabel resume_data.

# Baris 18-19 merupakan proses untuk mengambil teks resume dari kolom
Resume_str menggunakan row['Resume_str'] dan
menyimpannya ke variabel resume_str.

# Baris 21-23 merupakan proses untuk mem-parsing kolom Resume_html
menggunakan BeautifulSoup(row['Resume_html'],
"html.parser") dan menemukan semua elemen <div> dengan kelas
sectiontitle menggunakan soup.find_all().

# 109
# Baris 25-26 merupakan proses untuk mengekstrak teks dari setiap elemen
<div> menggunakan div.get_text(strip=True) dan
menyimpannya dalam list sections.

# Baris 28-29 merupakan proses untuk memulai iterasi melalui setiap section
dalam list sections menggunakan enumerate(sections).

# Baris 30-31 merupakan proses untuk membuat salinan dictionary
resume_data menggunakan resume_data.copy() dan
menyimpannya ke variabel section_data.

# Baris 33-34 merupakan proses untuk mencari posisi awal nama section
dalam teks resume_str menggunakan
resume_str.find(section).

# Baris 36-40 merupakan proses untuk menentukan posisi akhir section
dengan memeriksa apakah ada section berikutnya menggunakan
resume_str.find(sections[i + 1], start_index) atau
menggunakan panjang resume_str jika section terakhir.

# Baris 42-45 merupakan proses untuk mengambil teks section dari
resume_str menggunakan slicing [start_index:end_index],
menghapus spasi berlebih dengan strip(), dan menghapus nama
section jika ada yang terdeteksi di awal kalimat pada teks menggunakan
section_text[len(section):].strip().

# Baris 47-49 merupakan proses untuk menambahkan key Section dan
Text ke dictionary section_data dengan value nama section dan teks
section yang telah diekstrak.

# Baris 51-52 merupakan proses untuk menambahkan dictionary
section_data ke list data menggunakan data.append().

# Baris 54-55 merupakan proses untuk mengonversi list data menjadi
DataFrame baru menggunakan pd.DataFrame(data) dan
menyimpannya sebagai resume_df_1.

# 110
Selanjutnya, isian resume dilakukan langkah-langkah pra-pemrosesan teks
seperti yang sudah dijelaskan pada diagram alur di bab Perancangan.
Implementasi kode program preprocessing isian resume tertera pada Kode
Program 5.3.
Kode Program 5.3 Implementasi kode program preprocessing resume bagian
preprocessing isian resume

# # Inisialisasi lemmatizer
# lemmatizer = WordNetLemmatizer()
# 3
# # Daftar stop words
# stop_words = set(stopwords.words('english'))
# 6
# # Fungsi untuk mendapatkan tipe kata untuk lemmatization
# def get_wordnet_pos(tag):
# if tag.startswith('J'):
# return wordnet.ADJ
# elif tag.startswith('V'):
# return wordnet.VERB
# elif tag.startswith('N'):
# return wordnet.NOUN
# elif tag.startswith('R'):
# return wordnet.ADV
# else:
# return wordnet.NOUN
# 19
# def preprocess(text):
# # Hapus email dan nomor telepon
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-
Za-z]{2,}\b'

# phone_pattern = r'\b(?:\+?\d{1,3}[-
.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{2,4}[-.\s]?\d{2,4}[-
.\s]?\d{2,4}\b'

# 24
# text = re.sub(email_pattern, '', text)
# text = re.sub(phone_pattern, '', text)
# 27
# # Hapus berbagai tipe tanda minus
# text = re.sub(r'[\u2010-
\u2015\u2212\uFF0D\uFF0E\uFE63\u002D]', ' ', text)

# 30
# # Regex untuk menghapus bulan (termasuk singkatan) &
present/current

# bulan_pattern =
r"\b(?:january|jan|february|feb|march|mar|april|apr|may|june|ju
n|july|jul|august|aug|september|sep|october|oct|november|nov|de
cember|dec)\b"

# present_pattern = r"\b(?:present|current)\b"
# 34
# text = re.sub(bulan_pattern, '', text, flags=re.IGNORECASE)
# Hapus bulan dan singkatan

# text = re.sub(present_pattern, '', text,
flags=re.IGNORECASE) # Hapus "present/current"

# 37
# # Regex untuk menangani berbagai format tanggal & rentang
# 111
Kode Program 5.3 Implementasi kode program preprocessing resume bagian
preprocessing isian resume (lanjutan)

# date_pattern = r"""
# \b(
# (?:\d{1,2}/(?:\d{4}|Current)) # Format "01/2024" atau
"01/ Current"

# |(?:\d{4}) # Tahun "2023"
# (?:\s?(?:-|to|－|–|—)\s?(?:\d{4}|Current|Present))? #
Rentang waktu "2022 - 2023" atau "2022 － Present"

# 44
)\b

# 45
"""

# 46
text = re.sub(date_pattern, '', text, flags=re.IGNORECASE |
re.VERBOSE)

# 47
# 48
# Hapus placeholder seperti "Company Name" dan "State"

# 49
text = re.sub(r'\b(?:Company Name|State|City)\b', '', text,
flags=re.IGNORECASE)

# 50
# 51
# Hapus tanda baca

# 52
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 53
# 54
# Hapus angka

# 55
text = re.sub(r'\d+', '', text)

# 56
# 57
# Hapus spasi berlebihan setelah penghapusan

# 58
text = re.sub(r'\s+', ' ', text).strip()

# 59
# 60
tokens = word_tokenize(text)

# 61
tokens_pos = pos_tag(tokens)

# 62
# 63
# Lemmatization dan hapus stop words

# 64
lemmatized_text = []

# 65
for token, pos in tokens_pos:

# 66
if token.lower() not in stop_words: # Menghapus stop
words

# 67
wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN

# 68
lemmatized_text.append(lemmatizer.lemmatize(token,
pos=wordnet_pos))

# 69
# 70
return ' '.join(lemmatized_text)

# 71
# 72
# Implementasikan preprocessing ke dataset

# 73
resume_df_1['Text'] = resume_df_1['Text'].apply(preprocess)

# 74
resume_df_1['Text'] = resume_df_1['Text'].apply(preprocess)
Penjelasan dari Kode Program 5.3 mengenai implementasi kode program
ekstraksi section, yaitu:

# Baris 1-2 merupakan proses untuk menginisialisasi object
## WordNetLemmatizer dari NLTK menggunakan
WordNetLemmatizer() dan menyimpannya ke variabel
lemmatizer untuk melakukan lemmatisasi kata.

# Baris 4-5 merupakan proses untuk membuat set stop words dalam Bahasa
Inggris menggunakan stopwords.words('english') dan
menyimpannya ke variabel stop_words.

# 112
# Baris 7-18 merupakan proses untuk mendefinisikan fungsi
get_wordnet_pos yang mengonversi tag part-of-speech (POS) ke tipe
kata WordNet seperti wordnet.ADJ, wordnet.VERB,
wordnet.NOUN, wordnet.ADV berdasarkan awalan tag, dengan
default wordnet.NOUN jika tidak sesuai.

# Baris 20 merupakan pendefinisian fungsi preprocess yang menerima
parameter text untuk mengeksekusi proses preprocessing teks.

# Baris 21-23 merupakan proses untuk mendefinisikan pola regex untuk
email menggunakan email_pattern dan nomor telepon menggunakan
phone_pattern untuk dihapus dari teks.

# Baris 25-26 merupakan proses untuk menghapus email dan nomor telepon
dari teks menggunakan re.sub() dengan pola regex yang telah
didefinisikan sebelumnya.

# Baris 28-29 merupakan proses untuk menghapus berbagai jenis tanda
minus dari teks menggunakan re.sub() dan menggantinya dengan
spasi.

# Baris 31-33 merupakan proses untuk mendefinisikan pola regex untuk
menghapus nama bulan menggunakan bulan_pattern dan kata
"present" atau "current" menggunakan present_pattern.

# Baris 35-36 merupakan proses untuk menghapus nama bulan dan kata
"present" atau "current" dari teks menggunakan re.sub() dengan pola
regex, mengabaikan huruf besar maupun kecil dengan
flags=re.IGNORECASE.

# Baris 38-46 merupakan proses untuk mendefinisikan pola regex untuk
berbagai format tanggal menggunakan date_pattern dan
menghapusnya dari teks menggunakan re.sub() dengan flag
re.IGNORECASE dan re.VERBOSE.

# Baris 48-49 merupakan proses untuk menghapus kata-kata placeholder
seperti "Company Name", "State", dan "City" dari teks menggunakan
re.sub() dengan flags=re.IGNORECASE.

# Baris 51-52 merupakan proses untuk menghapus semua tanda baca dan
karakter non-huruf.

# Baris 54-55 merupakan proses untuk menghapus semua angka dari teks.
# Baris 57-58 merupakan proses untuk mengganti spasi yang berlebihan
menjadi hanya satu spasi dan menggunakan strip() untuk menghapus
spasi di awal dan akhir string.

# Baris 60 merupakan proses untuk memecah teks menjadi daftar kata
(token) menggunakan word_tokenize() dari NLTK.

# Baris 61 merupakan proses untuk memberikan part-of-speech (POS) tag
pada setiap token menggunakan pos_tag() dari NLTK.

# Baris 63-68 merupakan proses untuk membuat list kosong
lemmatized_text, mengiterasi token dan tag POS-nya, menghapus
stop words jika token tidak ada di stop_words, mengonversi tag POS ke
format WordNet menggunakan get_wordnet_pos(), dan melakukan
lematisasi menggunakan lemmatizer.lemmatize().

# 113
# Baris 70 merupakan proses untuk menggabungkan token yang telah di-
lematisasi menjadi satu string dengan spasi sebagai pemisah
menggunakan ' '.join().

# Baris 72-74 merupakan proses untuk menerapkan fungsi preprocess ke
kolom Text pada DataFrame resume_df_1 menggunakan
df['Text'].apply(preprocess). Proses ini dilakukan dua kali
karena pada iterasi pertama ada beberapa nama bulan yang belum
sepenuhnya terhapus, lalu pada iterasi kedua menghasilkan teks bersih
yang sudah sesuai.
Selanjutnya adalah menstandarisasi kolom Section ke huruf kecil,
menyeragamkan nama section menggunakan keyword_mapping,
menggabungkan teks yang diketahui section-nya lebih dari satu berdasarkan per
ID resume-nya, melakukan pemetaan untuk section yang tidak valid berdasarkan
pola teks, dan menghapus baris dengan teks kosong. Implementasi kode program
preprocessing isian resume per section tertera pada Kode Program 5.4.
Kode Program 5.4 Implementasi kode program preprocessing resume bagian
preprocessing isian resume per section

# resume_df_1["Section"] = resume_df_1["Section"].str.lower()
# 2
# # Menampilkan nilai unik dari kolom 'Section'
# unique_sections = resume_df_1['Section'].unique()
# 5
# # Menampilkan hasil
# print("Unique Sections in the Resume:")
# for section in unique_sections:
# print(section)
# 10
# # Mapping kata kunci ke kategori yang diinginkan
# keyword_mapping = {
# "experience": "Experience",
# "skill": "Skills/Qualifications",
# "award": "Accomplishments/Awards",
# "project": "Projects",
# "education": "Education",
# "certification": "Certifications",
# "portfolio": "Portfolio",
# "organization": "Organization",
# "volunteer": "Organization",
# "accomplishment": "Accomplishments/Awards",
# "achievement": "Accomplishments/Awards",
# "summary": "Summary",
# "overview": "Summary",
# "course": "Education",
# "academ": "Education",
# "work": "Experience",
# "profile": "Summary",
# "strength": "Skills/Qualifications",
# 114
Kode Program 5.4 Implementasi kode program preprocessing resume bagian
preprocessing isian resume per section (lanjutan)

# "competencies": "Skills/Qualifications",
# "compentencies": "Skills/Qualifications",
# "quali": "Skills/Qualifications",
# "honor": "Certifications",
# "honour": "Certifications",
# "affiliation": "Certifications",
# "affliation": "Certifications",
# "language": "Skills/Qualifications",
# "community": "Organization",
# "about": "Summary",
# "training": "Certifications",
# "scholarship": "Education",
# "license": "Certifications",
# "highlight": "Skills/Qualifications",
# "expertise": "Skills/Qualifications",
# "focus": "Summary",
# "background": "Summary",
# "interest": "Skills/Qualifications",
# "military": "Experience",
# "presentation": "Skills/Qualifications",
# "objective": "Summary",
# "reference": "Skills/Qualifications",
# "referance": "Skills/Qualifications",
# "proficien": "Skills/Qualifications",
# "dissertation": "Projects",
# "publications": "Skills/Qualifications",
# "associat": "Skills/Qualifications",
# "professional": "Experience",
# "leadership": "Organization",
# "curricular": "Organization",
# "credential": "Skills/Qualifications",
# "information": "Others",
# "societ": "Organization",
# "research": "Skills/Qualifications",
# "employment": "Experience",
# "adjunct": "Skills/Qualifications",
# "personal": "Others",
# "characteristic": "Others",
# "goal": "Summary",
# "apply": "Summary",
# "role": "Experience",
# "general": "Others",
# "link": "Portfolio",
# "snap shot": "Experience",
# "tool": "Skills/Qualifications",
# "hobb": "Others",
# "activit": "Organization",
# "client": "Experience",
# "success": "Accomplishments/Awards",
# "computer": "Skills/Qualifications",
# "technical": "Skills/Qualifications",
# "acumen": "Skills/Qualifications",
# "development": "Skills/Qualifications",
# "knowledge": "Skills/Qualifications",
# "membership": "Skills/Qualifications",
# "speak": "Accomplishments/Awards",
# 115
Kode Program 5.4 Implementasi kode program preprocessing resume bagian
preprocessing isian resume per section (lanjutan)

# "participat": "Projects",
# "vocation": "Experience",
# "clearance": "Skills/Qualifications",
# "attribute": "Skills/Qualifications",
# "exhibit": "Projects",
# }
# 93
# # Ubah nilai 'Section' berdasarkan kata kunci
# for keyword, category in keyword_mapping.items():
# resume_df_1.loc[resume_df_1['Section'].str.contains(keyword,
case=False, na=False), 'Section'] = category

# 97
# # Gabungkan teks dari section terkait jika ada duplikasi dalam
satu resume

# resume_df_1 = resume_df_1.groupby(['ID', 'Section'],
as_index=False).agg({

# 'Text': ' '.join,
# 'Resume_str': 'first',
# 'Resume_html': 'first',
# })
# 104
# # Daftar section yang tidak boleh diubah
# allowed_sections = [
# "Summary", "Accomplishments/Awards",
"Skills/Qualifications",

# "Education", "Experience", "Organization", "Projects",
# "Certifications", "Portfolio", "Others"
# ]
# 111
# # Pola regex untuk kata-kata yang harus masuk ke
## Summary
# summary_pattern = r'\b(?:Summary|I
am|I\'m|years|experience|professional)\b'

# 114
# # Ubah ke "Summary" jika ada salah satu kata dalam
summary_pattern

# resume_df_1.loc[
# (~resume_df_1["Section"].isin(allowed_sections)) &
# (resume_df_1["Text"].str.contains(summary_pattern,
case=False, na=False, regex=True)),

# "Section"
# ] = "Summary"
# 121
# # Ubah ke "Portfolio" jika ada kata "LinkedIn" dalam
"Text"

# resume_df_1.loc[
# (~resume_df_1["Section"].isin(allowed_sections)) &
# (resume_df_1["Text"].str.contains(r'\bLinkedIn\b',
case=False, na=False, regex=True)),

# "Section"
# ] = "Portfolio"
# 128
# 116
Kode Program 5.4 Implementasi kode program preprocessing resume bagian
preprocessing isian resume per section (lanjutan)

# # Jika section tidak termasuk valid_sections dan kolom "Text"
kosong, hapus baris tersebut

# resume_df_1 =
resume_df_1[~((~resume_df_1['Section'].isin(allowed_sections))
& (resume_df_1['Text'].isna()))]

# 131
# # Jika section tidak termasuk valid_sections tetapi ada isian
di "Text", ubah menjadi "Others"

# resume_df_1.loc[~resume_df_1['Section'].isin(allowed_sections),
'Section'] = 'Others'

# 134
# # Hapus baris dengan Text yang NaN, kosong, atau hanya spasi
untuk semua Section

# resume_df_1 = resume_df_1[~(resume_df_1['Text'].isna() |
(resume_df_1['Text'].str.strip() == ''))]

# 137
# resume_df_1["Text"] = resume_df_1["Text"].str.lower()
# resume_df_1 = resume_df_1.drop(columns=["Resume_str"])
# resume_df_1 = resume_df_1.drop(columns=["Resume_html"])
Penjelasan dari Kode Program 5.4 mengenai implementasi kode program
ekstraksi section, yaitu:

# Baris 1 merupakan proses untuk mengubah semua nilai di kolom
Section pada DataFrame resume_df_1 menjadi huruf kecil
menggunakan str.lower() guna lebih mudah dalam menyeragamkan
nama-nama section.

# Baris 3-9 merupakan proses untuk mengambil nilai unik dari kolom
Section pada DataFrame resume_df_1 menggunakan unique()
dan menyimpannya ke variabel unique_sections guna memahami
ada apa saja nama-nama section yang digunakan seluruh resume di
dataset.

# Baris 11-92 merupakan proses untuk mendefinisikan dictionary
keyword_mapping yang berisi pasangan key dan value, di mana key
adalah nama section yang telah diketahui dari pemeriksaan nilai unik
kolom Section sebelumnya, lalu value adalah nama section yang
diinginkan untuk mengelompokkan nama-nama section resume.

# Baris 94-96 merupakan proses untuk mengiterasi setiap pasangan key dan
value di keyword_mapping menggunakan items(), lalu mengubah
nilai kolom Section yang mengandung kata kunci seperti di key menjadi
value seperti keyword_mapping dan mengabaikan huruf besar maupun
kecil.

# Baris 98-103 merupakan proses untuk mengelompokkan isi DataFrame
resume_df_1 berdasarkan kolom ID dan Section menggunakan
groupby(), lalu menggabungkan teks untuk kolom Text menggunakan
' '.join jika ada nilai di kolom Section yang sama.

# 117
# Baris 105-110 merupakan proses untuk mendefinisikan list
allowed_sections yang berisi daftar nama-nama section yang
diizinkan untuk tetap ada dalam DataFrame.

# Baris 112-113 merupakan proses untuk mendefinisikan pola regex
summary_pattern yang mencakup kata-kata seperti "Summary", "I
am", "I'm", "years", "experience", atau "professional" untuk
mengidentifikasi teks yang relevan dengan nama section "Summary".

# Baris 115-120 merupakan proses untuk mengubah nilai kolom Section
menjadi "Summary" jika section tidak ada di allowed_sections dan
kolom Text mengandung kata-kata dari summary_pattern.

# Baris 122-127 merupakan proses untuk mengubah nilai kolom Section
menjadi "Portfolio" jika section tidak ada di allowed_sections dan
kolom Text mengandung kata "LinkedIn".

# Baris 129-130 merupakan proses untuk menghapus baris dari
resume_df_1 jika kolom Section tidak ada di allowed_sections
dan kolom Text kosong.

# Baris 132-133 merupakan proses untuk mengubah nilai kolom Section
menjadi "Others" jika section tidak ada di allowed_sections tetapi
kolom Text tidak kosong.

# Baris 135-136 merupakan proses untuk menghapus baris dari
resume_df_1 jika kolom Text kosong atau jika hanya berisi spasi.

# Baris 138 merupakan proses untuk mengubah semua nilai di kolom Text
pada DataFrame resume_df_1 menjadi huruf kecil atau lower casing.

# Baris 139 merupakan proses untuk menghapus kolom Resume_str dari
DataFrame resume_df_1 karena sudah tidak digunakan.

# Baris 140 merupakan proses untuk menghapus kolom Resume_html dari
DataFrame resume_df_1 karena sudah tidak digunakan.

## Implementasi Kode Program Preprocessing Kualifikasi
## Lowongan Kerja
Dalam kode program ini, dilakukan untuk membersihkan teks pada kolom
Description yang merupakan deskripsi lowongan kerja dengan mengubah ke
huruf kecil, menghapus tanda baca dan spasi berlebih, melakukan tokenisasi, POS
tagging, menghapus stop words, dan lematisasi. Implementasi kode program
tertera pada Kode Program 5.5.
Kode Program 5.5 Implementasi kode program preprocessing kualifikasi
lowongan kerja

# def preprocess_vacancy(text):
# text = text.lower() # Ubah ke huruf kecil
# text = re.sub(r'\d+', '', text) # Hapus angka
# text = text.translate(str.maketrans('', '',
string.punctuation)) # Hapus tanda baca

# text = ' '.join(text.split()) # Hapus spasi berlebih
# 6
# 118
Kode Program 5.5 Implementasi kode program preprocessing kualifikasi
lowongan kerja (lanjutan)

# # Tokenisasi
# tokens = word_tokenize(text)
# 9
# # POS tagging
# tagged_tokens = pos_tag(tokens)
# 12
# # Hapus stop words & Lemmatization
# processed_tokens = [lemmatizer.lemmatize(word,
get_wordnet_pos(tag))

# for word, tag in tagged_tokens if word
not in stop_words]

# 16
# return ' '.join(processed_tokens)
# 18
# # Terapkan preprocessing pada kolom "Description" di vacancy_df
vacancy_df_1 = vacancy_df.copy()

# vacancy_df_1["Description"] =
# vacancy_df["Description"].apply(preprocess_vacancy)
Penjelasan dari Kode Program 5.5 mengenai implementasi preprocessing isian
teks deskripsi kualifikasi lowongan kerja, yaitu:

# Baris 1 merupakan proses untuk mendefinisikan fungsi
preprocess_vacancy yang menerima parameter text untuk
memproses teks deskripsi lowongan kerja.

# Baris 2 merupakan proses untuk mengubah teks input menjadi huruf kecil
menggunakan text.lower() untuk standarisasi.

# Baris 3 merupakan proses untuk menghapus angka-angka dari teks.
# Baris 4 merupakan proses untuk menghapus semua tanda baca dari teks
berdasarkan daftar punctuation dari string.punctuation.

# Baris 5 merupakan proses untuk menghapus spasi berlebih dengan
memecah teks menjadi kata-kata menggunakan split(), lalu
menggabungkannya kembali menggunakan ' '.join() dengan spasi
tunggal

# Baris 7-8 merupakan proses untuk memecah teks menjadi daftar kata
(token) menggunakan word_tokenize() dari NLTK dan
menyimpannya ke variabel tokens.

# Baris 10-11 merupakan proses untuk memberikan part-of-speech (POS) tag
pada setiap token menggunakan pos_tag() dari NLTK dan
menyimpannya ke variabel tagged_tokens.

# Baris 13-15 merupakan proses untuk membuat list processed_tokens
dengan mengiterasi tagged_tokens, menghapus kata-kata yang ada di
stop_words, dan melakukan lematisasi pada setiap kata menggunakan
lemmatizer.lemmatize() dengan tipe kata dari
get_wordnet_pos(tag).

# 119
# Baris 17 merupakan proses untuk menggabungkan token yang telah
diproses menjadi satu string dengan spasi sebagai pemisah menggunakan
' '.join() dan mengembalikannya sebagai hasil dari fungsi
preprocess_vacancy.

# Baris 19-20 merupakan proses untuk membuat salinan DataFrame
vacancy_df menggunakan copy() dan menyimpannya ke variabel
vacancy_df_1 guna menghindari modifikasi data asli.

# Baris 21 merupakan proses untuk menerapkan fungsi
preprocess_vacancy ke kolom Description pada DataFrame
vacancy_df dan menyimpan hasilnya ke kolom Description pada
DataFrame vacancy_df_1.

## Implementasi Kode Program Representasi Teks TF-IDF
Dalam kode program ini, dilakukan implementasi representasi teks
menggunakan TF-IDF dengan TfidfVectorizer dari library Scikit-learn untuk
mengubah teks pada kolom Text dari resume_df_1 dan kolom
Description dari vacancy_df_1 menjadi vektor TF-IDF. Vektor-vektor ini
disimpan sebagai list dalam kolom baru TFIDF_Vector pada kedua DataFrame.
Implementasi kode program tertera pada Kode Program 5.6.
Kode Program 5.6 Implementasi kode program representasi teks TF-IDF

# # Inisialisasi TF-IDF Vectorizer
# vectorizer = TfidfVectorizer()
# 3
# # Fit dan transform data
# tfidf_resume = vectorizer.fit_transform(resume_df_1["Text"])
# tfidf_vacancy =
vectorizer.transform(vacancy_df_1["Description"])

# 7
# # Simpan vektor dalam kolom baru
# resume_df_1["TFIDF_Vector"] = list(tfidf_resume.toarray())
# vacancy_df_1["TFIDF_Vector"] = list(tfidf_vacancy.toarray())
Penjelasan dari Kode Program 5.6 mengenai implementasi representasi teks
dengan pendekatan TF-IDF, yaitu:

# Baris 1-2 merupakan proses untuk menginisialisasi objek TfidfVectorizer
dari library Scikit-learn menggunakan TfidfVectorizer() dan
menyimpannya ke variabel vectorizer untuk mengubah teks menjadi
vektor TF-IDF.

# Baris 4-5 merupakan proses untuk mempelajari kosa kata dari kolom Text
pada DataFrame resume_df_1 dan mengubahnya menjadi matriks TF-
IDF menggunakan fit_transform(), lalu menyimpan hasilnya ke
variabel tfidf_resume.

# 120
# Baris 6 merupakan proses untuk mengubah kolom Description pada
DataFrame vacancy_df_1 menjadi matriks TF-IDF menggunakan
transform() berdasarkan kosa kata yang telah dipelajari dari
resume_df_1["Text"], lalu menyimpan hasilnya ke variabel
tfidf_vacancy.

# Baris 8-9 merupakan proses untuk mengonversi matriks TF-IDF
tfidf_resume menjadi array menggunakan toarray() dan
menyimpan setiap vektor sebagai list dalam kolom baru TFIDF_Vector
pada DataFrame resume_df_1.

# Baris 10 merupakan proses untuk mengonversi matriks TF-IDF
tfidf_vacancy menjadi array menggunakan toarray() dan
menyimpan setiap vektor sebagai list dalam kolom baru TFIDF_Vector
pada DataFrame vacancy_df_1.

## Implementasi Kode Program Representasi Teks Word2Vec
Dalam kode program ini, dilakukan implementasi representasi teks
menggunakan Word2Vec dari library Gensim. Kode ini memproses kolom Text
pada resume_df_1 dan kolom Description pada vacancy_df_1 untuk
pelatihan model Word2Vec dengan menggabungkan teks resume dan deskripsi
lowongan kerja. Model Word2Vec dilatih dengan parameter ukuran vektor kata
bernilai 100, jarak antar kata dalam konteks (window) bernilai 5, menggunakan
skip-gram, dan learning rate bernilai 0,1. Hasil vektor disimpan ke kolom baru
W2V_Vector pada kedua DataFrame. Implementasi kode program tertera pada
Kode Program 5.7.
Kode Program 5.7 Implementasi kode program representasi teks Word2Vec

# def tokenize_text(text):
# return word_tokenize(text.lower()) # Tokenisasi dan ubah
ke huruf kecil

# 3
# # Tokenisasi teks dari resume_df_1 dan vacancy_df_1
# resume_texts =
resume_df_1['Text'].dropna().apply(tokenize_text).tolist()

# vacancy_texts =
vacancy_df_1['Description'].dropna().apply(tokenize_text).tolis
t()

# 7
# # Gabungkan semua teks untuk pelatihan Word2Vec
# all_texts = resume_texts + vacancy_texts
# 10
# # Latih model Word2Vec
# word2vec_model = Word2Vec(
# sentences=all_texts,
# vector_size=100 #ukuran vektor kata
# window=5, #jarak maksimum antar kata dalam konteks
# workers=4, #jumlah thread untuk pelatihan
# sg=1,
# alpha=0,1
# 19
# 20
# # Menghitung vektor rata-rata dokumen
# def get_document_vector(text, model):
# 121
Kode Program 5.7 Implementasi kode program representasi teks Word2Vec
(lanjutan)

# words = tokenize_text(text)
# word_vectors = [model.wv[word] for word in words if word in
model.wv]

# if not word_vectors: # Jika tidak ada kata yang dikenali
# return np.zeros(model.vector_size)
# return np.mean(word_vectors, axis=0)
# 28
# # Penerapan ke dataset
# resume_df_1['W2V_Vector'] = resume_df_1['Text'].apply(lambda x:
get_document_vector(x, word2vec_model))

# vacancy_df_1['W2V_Vector'] =
vacancy_df_1['Description'].apply(lambda x:
get_document_vector(x, word2vec_model))
Penjelasan dari Kode Program 5.7 mengenai implementasi representasi teks
dengan pendekatan Word2Vec, yaitu:

# Baris 1-2 merupakan proses untuk mendefinisikan fungsi
tokenize_text yang mengambil text sebagai input, mengonversi ke
huruf kecil (lower casing) dengan text.lower(), dan melakukan
tokenisasi menggunakan word_tokenize dari library NLTK.

# Baris 3-4 merupakan proses untuk menghapus nilai kosong dari kolom
Text pada DataFrame resume_df_1 menggunakan dropna(),
melakukan tokenisasi kata dengan word_tokenize(), dan
mengonversi hasilnya menjadi list menggunakan tolist(), lalu
menyimpannya ke variabel resume_texts.

# Baris 5-6 merupakan proses untuk menghapus nilai kosong dari kolom
## Description pada DataFrame vacancy_df_1 menggunakan
dropna(), melakukan tokenisasi kata dengan word_tokenize(),
dan mengonversi hasilnya menjadi list menggunakan tolist(), lalu
menyimpannya ke variabel vacancy_texts.

# Baris 8-9 merupakan proses untuk menggabungkan list resume_texts
dan vacancy_texts menjadi satu list all_texts untuk digunakan
dalam pelatihan model Word2Vec.

# Baris 11-19 merupakan proses untuk melatih model Word2Vec
menggunakan Word2Vec() dari library Gensim dengan parameter:
sentences=all_texts (data teks), vector_size=100 (ukuran
vektor kata), window=5 (jarak konteks kata), workers=4 (jumlah
thread), sg=1 (menggunakan algoritma skip-gram), dan alpha=0,1
(learning rate), lalu menyimpan model ke variabel word2vec_model.

# 122
# Baris 21-27 merupakan proses untuk mendefinisikan fungsi
get_document_vector yang menghitung vektor rata-rata dokumen
dengan melakukan tokenisasi teks menggunakan tokenize_text(),
mengambil vektor kata dari model.wv untuk kata yang ada di model.
Fungsi ini mengembalikan vektor nol dengan panjang vector_size jika
tidak ada kata yang dikenali atau mengembalikan hasil rata-rata vektor
kata menggunakan np.mean().

# Baris 30 merupakan proses untuk menerapkan fungsi
get_document_vector ke kolom Text pada DataFrame
resume_df_1 menggunakan apply() dengan model
word2vec_model, lalu menyimpan vektor rata-rata dokumen ke kolom
baru W2V_Vector.

# Baris 231 merupakan proses untuk menerapkan fungsi
get_document_vector ke kolom Description pada DataFrame
vacancy_df_1 menggunakan apply() dengan model
word2vec_model, lalu menyimpan vektor rata-rata dokumen ke kolom
baru W2V_Vector.

## Implementasi Kode Program Perhitungan Similaritas
### Implementasi Kode Program Improved Sqrt-Cosine Similarity
Dalam kode program ini, dilakukan penghitungan kemiripan antara dua vektor
menggunakan pendekatan Improved Sqrt-Cosine (ISC) Similarity. Prosesnya
mencakup memeriksa validitas input, mengubah elemen vektor menjadi positif,
menghitung pembilang (jumlah akar kuadrat perkalian elemen) dan penyebut
(perkalian akar kuadrat jumlah elemen), lalu mengembalikan nilai kemiripan atau

# jika perhitungan tidak valid. Implementasi kode program tertera pada Kode
Program 5.8.
Kode Program 5.8 Implementasi kode program Improved Sqrt-Cosine Similarity

# # Fungsi Improved Sqrt-Cosine Similarity (ISC)
# def improved_sqrt_cosine_similarity(x, y):
# if x is None or y is None or len(x) != len(y):
# return 0
# 5
# # Mengambil nilai absolut untuk penggunaan dengan Word2Vec
# x = np.abs(x)
# y = np.abs(y)
# 9
# # Menghitung pembilang dan penyebut sesuai dengan rumus ISC
# numerator = np.sum(np.sqrt(x * y))
# denominator = np.sqrt(np.sum(x)) * np.sqrt(np.sum(y))
# 13
# # Menghitung ISC
# isc = numerator / denominator if denominator != 0 else 0
# return isc
# 123
Penjelasan dari Kode Program 5.8 mengenai implementasi perhitungan
Improved Sqrt-Cosine Similarity, yaitu:

# Baris 1-2 merupakan proses untuk mendefinisikan fungsi
improved_sqrt_cosine_similarity yang menerima dua
parameter, yakni x dan y (vektor) untuk menghitung kemiripan
menggunakan metrik Improved Sqrt-Cosine Similarity (ISC).

# Baris 3-4 merupakan proses untuk memeriksa apakah salah satu vektor x
atau y adalah None atau memiliki panjang yang berbeda menggunakan
kondisi if. Kemudian, mengembalikan nilai 0 jika kondisi tersebut true.

# Baris 6-8 merupakan proses untuk mengubah semua elemen vektor x atau
y menjadi nilai absolut menggunakan np.abs(). Absolut ini digunakan
ketika mengimplementasi pendekatan Word2Vec dengan ISC.

# Baris 10-11 merupakan proses untuk menghitung numerator (pembilang)
rumus ISC dengan mengalikan elemen-elemen vektor x dan y, mengambil
akar kuadrat dari hasil perkalian dengan np.sqrt(), dan menjumlahkan
semua hasilnya menggunakan np.sum().

# Baris 12 merupakan proses untuk menghitung denominator (penyebut)
rumus ISC dengan menjumlahkan elemen vektor x atau y menggunakan
np.sum(), mengambil akar kuadrat dari masing-masing jumlah dengan
np.sqrt(), lalu mengalikan kedua akar tersebut.

# Baris 14-16 merupakan proses untuk menghitung nilai ISC yang disimpan
pada variabel isc dengan membagi numerator dengan denominator jika
denominator tidak nol atau mengembalikan 0 jika denominator nol untuk
menghindari pembagian dengan nol. Kemudian, mengembalikan nilai
variabel isc yang telah dihitung sebagai hasil dari fungsi
improved_sqrt_cosine_similarity.

## Implementasi Kode Program TF-IDF dan Improved Sqrt-Cosine
## Similarity
Dalam kode program ini, dilakukan perhitungan kemiripan antara resume dan
kualifikasi lowongan kerja menggunakan Improved Sqrt-Cosine (ISC) Similarity
untuk vektor TF-IDF, dengan dua skenario, yakni “Tanpa Bobot” (hasil kemiripan
semua section dirata-ratakan) dan “Dengan Bobot” (hasil kemiripan semua section
diberikan bobot persentase berdasarkan section_df). Hasil disimpan dalam
DataFrame result_df_tfidf, dan lima resume teratas untuk setiap posisi
ditampilkan berdasarkan kemiripan “Tanpa Bobot” dan “Dengan Bobot”.
Implementasi kode program tertera pada Kode Program 5.9.
Kode Program 5.9 Implementasi kode program TF-IDF dan Improved Sqrt-

## Cosine Similarity
# start_time = time.time() # Catat waktu mulai
# 2
# # List untuk menyimpan hasil similarity setiap resume
# final_results_tfidf = []
# 5
# 124
Kode Program 5.9 Implementasi kode program TF-IDF dan Improved Sqrt-
Cosine Similarity (lanjutan)

# # Looping untuk setiap job vacancy
# for _, vacancy_row_tfidf in tqdm(vacancy_df_1.iterrows(),
total=len(vacancy_df_1), desc="Processing Vacancies"):

# vacancy_category_tfidf = vacancy_row_tfidf["Category"]
# job_vec_tfidf = vacancy_row_tfidf["TFIDF_Vector"]
# position_name = vacancy_row_tfidf["Position"]
# 11
# # Ambil bobot section sesuai kategori dan ubah ke skala
desimal

# category_weights = (section_df[section_df["Category"] ==
vacancy_category_tfidf]

# set_index("Section")["Bobot"]
# div(100)
# to_dict())
# 17
# # Looping untuk setiap resume
# for resume_id in resume_df_1["ID"].unique():
# resume_sections = resume_df_1[resume_df_1["ID"] ==
resume_id]

# similarity_scores_tfidf = {}
# 22
# # Hitung similarity untuk setiap section
# for _, section_row_tfidf in resume_sections.iterrows():
# section_name_tfidf = section_row_tfidf["Section"]
# section_vec_tfidf =
section_row_tfidf["TFIDF_Vector"]

# 27
# sim_tfidf =
improved_sqrt_cosine_similarity(section_vec_tfidf,
job_vec_tfidf)

# similarity_scores_tfidf[section_name_tfidf] =
sim_tfidf

# 30
# # Versi 1: Tanpa bobot (rata-rata similarity semua
section)

# sim_no_weight = sum(similarity_scores_tfidf.values()) /
len(similarity_scores_tfidf) if similarity_scores_tfidf else 0

# 33
# # Versi 2: Dengan bobot (weighted sum tanpa normalisasi
total weight)

# weighted_sum_v2 = 0
# total_weight_v2 = 0
# for sec in similarity_scores_tfidf:
# sim = similarity_scores_tfidf[sec]
# weight = category_weights.get(sec, 0)
# weighted_sum_v2 += sim * weight
# total_weight_v2 += weight
# sim_with_weight = weighted_sum_v2 / total_weight_v2 if
total_weight_v2 > 0 else 0

# 43
# # Simpan hasil
# final_results_tfidf.append((resume_id, position_name,
sim_no_weight, sim_with_weight))

# 46
# # Catat waktu selesai dan hitung durasi
# end_time = time.time()
# total_time = end_time - start_time
# 50
# # Konversi waktu ke format yang lebih mudah dibaca
# minutes = int(total_time // 60)
# seconds = int(total_time % 60)
# 125
Kode Program 5.9 Implementasi kode program TF-IDF dan Improved Sqrt-
Cosine Similarity (lanjutan)

# 54
# # Buat DataFrame hasil similarity
# result_df_tfidf = pd.DataFrame(
# final_results_tfidf,
# columns=["Resume_ID", "Position", "Similarity_No_Weight",
"Similarity_With_Weight"]

# 59
# 60
# # Tampilkan waktu total
# print(f"Total waktu pemrosesan: {minutes} menit {seconds}
detik")

# 63
# print("Similaritas Tanpa Bobot Section")
# 65
# top5_per_position_no_weight =
result_df_tfidf.groupby('Position', group_keys=False).apply(

# lambda x: x.nlargest(5, 'Similarity_No_Weight')
# 68
# 69
# grouped_no_weight =
top5_per_position_no_weight.groupby('Position')

# for position, group in grouped_no_weight:
# print(f"\nPosition: {position}")
# print(group[['Resume_ID', 'Similarity_No_Weight']])
# 74
# print("Similaritas Dengan Bobot Section")
# 76
# top5_per_position_with_weight =
result_df_tfidf.groupby('Position', group_keys=False).apply(

# lambda x: x.nlargest(5, 'Similarity_With_Weight')
# 79
# 80
# grouped_with_weight =
top5_per_position_with_weight.groupby('Position')

# for position, group in grouped_with_weight:
# print(f"\nPosition: {position}")
# print(group[['Resume_ID', 'Similarity_With_Weight']])
Penjelasan dari Kode Program 5.9 mengenai implementasi perhitungan
similaritas antara resume dan kualifikasi lowongan kerja dengan Improved Sqrt-
Cosine (ISC) Similarity jika menggunakan vektor TF-IDF, yaitu:

# Baris 1 merupakan proses untuk mencatat waktu mulai eksekusi
menggunakan time.time() dan menyimpannya ke variabel start_time.

# Baris 3-4 merupakan proses untuk membuat list kosong
final_results_tfidf untuk menyimpan hasil perhitungan
kemiripan (similarity) antara resume dan kualifikasi lowongan kerja.

# Baris 6-7 merupakan proses untuk memulai iterasi melalui setiap baris di
DataFrame vacancy_df_1 menggunakan iterrows() dengan
progress bar dari tqdm untuk menampilkan kemajuan pemrosesan.

# Baris 8 merupakan pengambilan nilai kolom Category dari baris
lowongan kerja pada iterasi terkini dan menyimpannya ke variabel
vacancy_category_tfidf.

# 126
# Baris 9 merupakan pengambilan vektor TF-IDF dari kolom
TFIDF_Vector pada baris lowongan kerja di iterasi terkini dan
menyimpannya ke variabel job_vec_tfidf.

# Baris 10 merupakan pengambilan nilai kolom Position dari baris
lowongan kerja pada iterasi terkini dan menyimpannya ke variabel
position_name.

# Baris 12-16 merupakan proses untuk memfilter DataFrame section_df
berdasarkan vacancy_category_tfidf, menetapkan kolom
Section sebagai indeks, mengambil kolom Bobot, membaginya dengan

# menggunakan div(100) untuk mengubah ke skala desimal (karena
bobot dalam persentase), dan mengonversinya menjadi dictionary
menggunakan to_dict(), lalu menyimpannya ke variabel
category_weights sebagai persentase bobot per section untuk
kualifikasi lowongan kerja pada iterasi terkini sesuai industrinya.

# Baris 18-19 merupakan proses untuk memulai iterasi melalui setiap nilai
unik di kolom ID pada DataFrame resume_df_1 menggunakan
unique().

# Baris 20 merupakan proses untuk memfilter DataFrame resume_df_1
untuk mendapatkan semua baris dengan kolom ID yang sesuai dengan
iterasi resume_id terkini dan menyimpannya ke variabel
resume_sections.

# Baris 21 merupakan pembuatan dictionary kosong
similarity_scores_tfidf untuk menyimpan skor kemiripan
setiap section dalam resume.

# Baris 23-24 merupakan proses untuk memulai iterasi melalui setiap baris
di resume_sections menggunakan iterrows() untuk memproses
setiap section dalam resume.

# Baris 25 merupakan proses untuk mengambil nilai kolom Section dari
baris section terkini dan menyimpannya ke variabel
section_name_tfidf.

# Baris 26 merupakan proses untuk mengambil vektor TF-IDF dari kolom
TFIDF_Vector pada baris section saat ini dan menyimpannya ke
variabel section_vec_tfidf.

# Baris 28 merupakan proses untuk menghitung kemiripan antara vektor
section pada resume (section_vec_tfidf) dan vektor kualifikasi
lowongan kerja (job_vec_tfidf) menggunakan fungsi
improved_sqrt_cosine_similarity, lalu menyimpan hasilnya
ke variabel sim_tfidf.

# Baris 29 merupakan proses untuk menyimpan skor kemiripan
sim_tfidf ke dictionary similarity_scores_tfidf.

# 127
# Baris 31-32 merupakan proses untuk menguji skenario “Tanpa Bobot”
dengan menghitung rata-rata kemiripan dengan menjumlahkan semua
skor kemiripan di similarity_scores_tfidf menggunakan sum()
dan membaginya dengan jumlah section menggunakan len(), atau
mengembalikan 0 jika dictionary kosong, lalu menyimpan hasilnya ke
variabel sim_no_weight.

# Baris 34-42 merupakan proses untuk menguji skenario “Dengan Bobot”,
dimana baris 35-36 menginisialisasi variabel weighted_sum_v2 dan
total_weight_v2 dengan nilai 0 untuk menghitung jumlah kemiripan
terbobot dan total bobot.

# Baris 37-41 merupakan proses untuk mengiterasi setiap section di
similarity_scores_tfidf, mengambil skor kemiripan yang
disimpan pada variabel sim, mendapatkan bobot section dari variabel
category_weights dengan default 0 menggunakan get(),
mengalikan skor “Dengan Bobot” untuk menambah ke
weighted_sum_v2, dan menambah bobot ke total_weight_v2.

# Baris 42 merupakan proses untuk menghitung total similarity pada
skenario “Dengan Bobot” dengan membagi weighted_sum_v2 dengan
total_weight_v2 jika total_weight_v2 lebih dari 0 atau
mengembalikan nilai 0 jika tidak. Kemudian, menyimpan hasilnya ke
variabel sim_with_weight.

# Baris 44-45 merupakan proses untuk menambahkan data resume_id,
position_name, sim_no_weight, dan sim_with_weight ke list
final_results_tfidf menggunakan append().

# Baris 47-49 merupakan proses untuk mencatat waktu selesai
menggunakan time.time(), menghitung durasi dengan mengurangkan
start_time dari end_time, dan menyimpan hasilnya ke variabel
total_time.

# Baris 51-53 merupakan proses untuk mengonversi total_time ke menit
dan detik, lalu menyimpannya ke variabel minutes dan seconds.

# Baris 55-59 merupakan proses untuk membuat DataFrame
result_df_tfidf dari list final_results_tfidf menggunakan
pd.DataFrame(), dengan kolom Resume_ID, Position,
Similarity_No_Weight, dan Similarity_With_Weight.

# Baris 61-62 merupakan proses untuk mencetak total waktu pemrosesan
dalam format menit dan detik menggunakan print().

# Baris 64 merupakan proses untuk mencetak judul "Similaritas Tanpa Bobot
Section" menggunakan print().

# Baris 66-68 merupakan proses untuk mengelompokkan DataFrame
result_df_tfidf berdasarkan kolom Position menggunakan
groupby(), lalu memilih 5 baris dengan nilai
Similarity_No_Weight tertinggi untuk setiap posisi menggunakan
nlargest(), dan menyimpan hasilnya ke variabel
top5_per_position_no_weight.

# 128
# Baris 70-73 merupakan proses untuk mengelompokkan
top5_per_position_no_weight berdasarkan kolom Position,
mengiterasi setiap kualifikasi lowongan kerja (Position), mencetak
nama posisi, mencetak nilai kolom Resume_ID, serta mencetak nilai
Similarity_No_Weight untuk setiap kualifikasi lowongan kerja.

# Baris 75 merupakan proses untuk mencetak judul "Similaritas Dengan
Bobot Section" menggunakan print().

# Baris 77-79 merupakan proses untuk mengelompokkan DataFrame
result_df_tfidf berdasarkan kolom Position menggunakan
groupby(), lalu memilih 5 baris dengan nilai

## Similarity_With_Weight tertinggi untuk setiap posisi
menggunakan nlargest(), dan menyimpan hasilnya ke variabel
top5_per_position_with_weight.

# Baris 81-84 merupakan proses untuk mengelompokkan
top5_per_position_with_weight berdasarkan Position,
mengiterasi setiap kualifikasi lowongan kerja (Position), mencetak
nama posisi, mencetak kolom Resume_ID, serta
Similarity_With_Weight untuk setiap kualifikasi lowongan kerja.

## Implementasi Kode Program Word2Vec dan Cosine Similarity
Dalam kode program ini, dilakukan menghitung kemiripan antara resume dan
kualifikasi lowongan kerja menggunakan metrik Cosine Similarity (CosSim) untuk
vektor Word2Vec, dengan dua skenario, yakni “Tanpa Bobot” (hasil kemiripan
semua section dirata-ratakan) dan “Dengan Bobot” (hasil kemiripan semua section
diberikan bobot persentase berdasarkan section_df). Hasil disimpan dalam
DataFrame result_df_w2v, dan lima resume teratas untuk setiap posisi
ditampilkan berdasarkan kemiripan “Tanpa Bobot” dan “Dengan Bobot”.
Implementasi kode program tertera pada Kode Program 5.10.
Kode Program 5.10 Implementasi kode program Word2Vec dan Cosine

## Similarity
# start_time = time.time() # Catat waktu mulai
# 2
# # List untuk menyimpan hasil
# final_results_w2v = []
# 5
# # Iterasi untuk setiap vacancy
# for vac_idx, vac_row in tqdm(vacancy_df_1.iterrows(),
total=len(vacancy_df_1), desc="Processing Vacancies"):

# position = vac_row['Position']
# vacancy_category = vac_row['Category']
# job_vec_w2v = np.array([vac_row['W2V_Vector']]) # Vektor
vacancy dalam bentuk 2D untuk cosine_similarity

# 11
# # Ambil bobot section sesuai kategori dan ubah ke skala
desimal

# category_weights = (section_df[section_df["Category"] ==
vacancy_category]

# set_index("Section")["Bobot"]
# div(100)
# 129
Kode Program 5.10 Implementasi kode program Word2Vec dan Cosine
Similarity (lanjutan)

# to_dict())
# 17
# # Iterasi untuk setiap resume
# for resume_id in resume_df_1['ID'].unique():
# resume_sections = resume_df_1[resume_df_1['ID'] ==
resume_id]

# similarity_scores = {}
# 22
# # Hitung similarity untuk setiap section
# for _, section_row in resume_sections.iterrows():
# section_name = section_row['Section']
# section_vector =
np.array([section_row['W2V_Vector']]) # Vektor section dalam
bentuk 2D

# 27
# # Hitung cosine similarity antara section dan
vacancy

# sim_score = cosine_similarity(section_vector,
job_vec_w2v)[0][0]

# similarity_scores[section_name] = sim_score
# 31
# # Versi 1: Tanpa bobot (rata-rata similarity semua
section)

# sim_no_weight = sum(similarity_scores.values()) /
len(similarity_scores) if similarity_scores else 0

# 34
# # Versi 2: Dengan bobot (weighted sum tanpa normalisasi
ketat)

# weighted_sum_v2 = 0
# total_weight_v2 = 0
# for section in similarity_scores:
# sim = similarity_scores.get(section, 0)
# weight = category_weights.get(section, 0)
# weighted_sum_v2 += sim * weight
# total_weight_v2 += weight
# sim_with_weight = weighted_sum_v2 / total_weight_v2 if
total_weight_v2 > 0 else 0

# 44
# # Simpan hasil
# final_results_w2v.append({
# 'Resume_ID': resume_id,
# 'Position': position,
# 'Similarity_No_Weight': sim_no_weight,
# 'Similarity_With_Weight': sim_with_weight,
# })
# 52
# # Catat waktu selesai dan hitung durasi
# end_time = time.time()
# total_time = end_time - start_time
# 56
# # Konversi waktu ke format yang lebih mudah dibaca
# minutes = int(total_time // 60)
# seconds = int(total_time % 60)
# 60
# # Konversi hasil ke DataFrame
# result_df_w2v = pd.DataFrame(final_results_w2v)
# 63
# # Tampilkan waktu total
# print(f"Total waktu pemrosesan: {minutes} menit {seconds}
detik")

# 66
# 130
Kode Program 5.10 Implementasi kode program Word2Vec dan Cosine
Similarity (lanjutan)

# print("Similaritas Tanpa Bobot Section")
# 68
# top5_per_position_no_weight = result_df_w2v.groupby('Position',
group_keys=False).apply(

# lambda x: x.nlargest(5, 'Similarity_No_Weight')
# 71
# 72
# grouped_no_weight =
top5_per_position_no_weight.groupby('Position')

# for position, group in grouped_no_weight:
# print(f"\nPosition: {position}")
# print(group[['Resume_ID', 'Similarity_No_Weight']])
# 77
# print("Similaritas Dengan Bobot Section")
# 79
# top5_per_position_with_weight =
result_df_w2v.groupby('Position', group_keys=False).apply(

# lambda x: x.nlargest(5, 'Similarity_With_Weight')
# 82
# 83
# grouped_with_weight =
top5_per_position_with_weight.groupby('Position')

# for position, group in grouped_with_weight:
# print(f"\nPosition: {position}")
# print(group[['Resume_ID', 'Similarity_With_Weight']])
Penjelasan dari Kode Program 5.10 mengenai implementasi perhitungan
similaritas antara resume dan kualifikasi lowongan kerja dengan Cosine Similarity
(CosSim) jika menggunakan vektor Word2Vec, yaitu:

# Baris 1 merupakan proses untuk mencatat waktu mulai eksekusi
menggunakan time.time() dan menyimpannya ke variabel start_time.

# Baris 3-4 merupakan proses untuk membuat list kosong
final_results_w2v untuk menyimpan hasil perhitungan kemiripan
(similarity) antara resume dan kualifikasi lowongan kerja.

# Baris 6-7 merupakan proses untuk memulai iterasi melalui setiap baris di
DataFrame vacancy_df_1 menggunakan iterrows() dengan
progress bar dari tqdm untuk menampilkan kemajuan pemrosesan.

# Baris 8 merupakan proses untuk mengambil nilai kolom Position dari
baris kualifikasi lowongan kerja terkini dan menyimpannya ke variabel
position.

# Baris 9 merupakan pengambilan nilai kolom Category dari baris
lowongan kerja pada iterasi terkini dan menyimpannya ke variabel
vacancy_category.

# Baris 10 merupakan pengambilan vektor Word2Vec dari kolom
W2V_Vector pada baris kualifikasi lowongan kerja di iterasi terkini dan
menyimpannya ke variabel job_vec_w2v.

# 131
# Baris 12-16 merupakan proses untuk memfilter DataFrame section_df
berdasarkan vacancy_category, menetapkan kolom Section
sebagai indeks, mengambil kolom Bobot, membaginya dengan 100
menggunakan div(100) untuk mengubah ke skala desimal (karena
bobot dalam persentase), dan mengonversinya menjadi dictionary
menggunakan to_dict(), lalu menyimpannya ke variabel
category_weights sebagai persentase bobot per section untuk
kualifikasi lowongan kerja pada iterasi terkini sesuai industrinya.

# Baris 18-19 merupakan proses untuk memulai iterasi melalui setiap nilai
unik di kolom ID pada DataFrame resume_df_1 menggunakan
unique().

# Baris 20 merupakan proses untuk memfilter DataFrame resume_df_1
untuk mendapatkan semua baris dengan kolom ID yang sesuai dengan
iterasi resume_id terkini dan menyimpannya ke variabel
resume_sections.

# Baris 21 merupakan pembuatan dictionary kosong
similarity_scores untuk menyimpan skor kemiripan setiap section
dalam resume.

# Baris 23-24 merupakan proses untuk memulai iterasi melalui setiap baris
di resume_sections menggunakan iterrows() untuk memproses
setiap section dalam resume.

# Baris 25 merupakan proses untuk mengambil nilai kolom Section dari
baris section terkini dan menyimpannya ke variabel section_name.

# Baris 26 merupakan proses untuk mengambil vektor Word2Vec dari kolom
W2V_Vector pada baris section saat ini dan menyimpannya ke variabel
section_vector.

# Baris 28-29 merupakan proses untuk menghitung kemiripan antara vektor
section pada resume (section_vector) dan vektor kualifikasi
lowongan kerja (vac_vector) menggunakan fungsi
cosine_similarity dari library Scikit-learn, lalu menyimpan hasilnya
ke variabel sim_score.

# Baris 30 merupakan proses untuk menyimpan skor kemiripan
sim_score ke dictionary similarity_scores.

# Baris 32-33 merupakan proses untuk menguji skenario “Tanpa Bobot”
dengan menghitung rata-rata kemiripan dengan menjumlahkan semua
skor kemiripan di similarity_scores menggunakan sum() dan
membaginya dengan jumlah section menggunakan len(), atau
mengembalikan 0 jika dictionary kosong, lalu menyimpan hasilnya ke
variabel sim_no_weight.

# Baris 35-43 merupakan proses untuk menguji skenario “Dengan Bobot”,
dimana baris 36-37 menginisialisasi variabel weighted_sum_v2 dan
total_weight_v2 dengan nilai 0 untuk menghitung jumlah kemiripan
terbobot dan total bobot.

# 132
# Baris 38-42 merupakan proses untuk mengiterasi setiap section di
similarity_scores, mengambil skor kemiripan yang disimpan pada
variabel sim, mendapatkan bobot section dari variabel
category_weights dengan default 0 menggunakan get(),
mengalikan skor “Dengan Bobot” untuk menambah ke
weighted_sum_v2, dan menambah bobot ke total_weight_v2.

# Baris 43 merupakan proses untuk menghitung total similarity pada
skenario “Dengan Bobot” dengan membagi weighted_sum_v2 dengan
total_weight_v2 jika total_weight_v2 lebih dari 0 atau
mengembalikan nilai 0 jika tidak. Kemudian, menyimpan hasilnya ke
variabel sim_with_weight.

# Baris 45-46 merupakan proses untuk menambahkan data resume_id,
position, sim_no_weight, dan sim_with_weight ke list
final_results_w2v menggunakan append().

# Baris 53-55 merupakan proses untuk mencatat waktu selesai
menggunakan time.time(), menghitung durasi dengan mengurangkan
start_time dari end_time, dan menyimpan hasilnya ke variabel
total_time.

# Baris 57-59 merupakan proses untuk mengonversi total_time ke menit
dan detik, lalu menyimpannya ke variabel minutes dan seconds.

# Baris 61-62 merupakan proses untuk membuat DataFrame
result_df_w2v dari list final_results_w2v menggunakan
pd.DataFrame(), dengan kolom Resume_ID, Position,
Similarity_No_Weight, dan Similarity_With_Weight.

# Baris 64-65 merupakan proses untuk mencetak total waktu pemrosesan
dalam format menit dan detik menggunakan print().

# Baris 67 merupakan proses untuk mencetak judul "Similaritas Tanpa Bobot
Section" menggunakan print().

# Baris 69-71 merupakan proses untuk mengelompokkan DataFrame
result_df_w2v berdasarkan kolom Position menggunakan
groupby(), lalu memilih 5 baris dengan nilai
Similarity_No_Weight tertinggi untuk setiap posisi menggunakan
nlargest(), dan menyimpan hasilnya ke variabel
top5_per_position_no_weight.

# Baris 73-76 merupakan proses untuk mengelompokkan
top5_per_position_no_weight berdasarkan kolom Position,
mengiterasi setiap kualifikasi lowongan kerja (Position), mencetak
nama posisi, mencetak nilai kolom Resume_ID, serta mencetak nilai
Similarity_No_Weight untuk setiap kualifikasi lowongan kerja.

# Baris 78 merupakan proses untuk mencetak judul "Similaritas Dengan
Bobot Section" menggunakan print().

# 133
# Baris 80-82 merupakan proses untuk mengelompokkan DataFrame
result_df_w2v berdasarkan kolom Position menggunakan
groupby(), lalu memilih 5 baris dengan nilai

## Similarity_With_Weight tertinggi untuk setiap posisi
menggunakan nlargest(), dan menyimpan hasilnya ke variabel
top5_per_position_with_weight.

# Baris 84-87 merupakan proses untuk mengelompokkan
top5_per_position_with_weight berdasarkan Position,
mengiterasi setiap kualifikasi lowongan kerja (Position), mencetak
nama posisi, mencetak kolom Resume_ID, serta
Similarity_With_Weight untuk setiap kualifikasi lowongan kerja.

## Implementasi Kode Program Word2Vec dan Improved Sqrt-
## Cosine Similarity
Dalam kode program ini, dilakukan kemiripan antara resume dan kualifikasi
lowongan kerja menggunakan metrik Improved Sqrt-Cosine (ISC) Similarity untuk
vektor Word2Vec, dengan dua skenario, yakni “Tanpa Bobot” (hasil kemiripan
semua section dirata-ratakan) dan “Dengan Bobot” (hasil kemiripan semua section
diberikan bobot persentase berdasarkan section_df). Hasil disimpan dalam
DataFrame result_df_w2v_isc, dan lima resume teratas untuk setiap posisi
ditampilkan berdasarkan kemiripan “Tanpa Bobot” dan ‘Dengan Bobot”.
Implementasi kode program tertera pada Kode Program 5.11.
Kode Program 5.11 Implementasi kode program Word2Vec dan Improved Sqrt-

## Cosine Similarity
# start_time = time.time() # Catat waktu mulai
# 2
# # List untuk menyimpan hasil
# final_results_w2v_isc = []
# 5
# # Iterasi untuk setiap vacancy
# for vac_idx, vac_row in tqdm(vacancy_df_1.iterrows(),
total=len(vacancy_df_1), desc="Processing Vacancies"):

# position = vac_row['Position']
# vacancy_category = vac_row['Category']
# job_vec_w2v = vac_row['W2V_Vector'] # Vektor vacancy dalam
bentuk 1D

# 11
# # Ambil bobot section sesuai kategori dan ubah ke skala
desimal

# category_weights = (section_df[section_df["Category"] ==
vacancy_category]

# set_index("Section")["Bobot"]
# div(100)
# to_dict())
# 17
# # Iterasi untuk setiap resume
# for resume_id in resume_df_1['ID'].unique():
# resume_sections = resume_df_1[resume_df_1['ID'] ==
resume_id]

# similarity_scores = {}
# 22
# # Hitung similarity untuk setiap section
# 134
Kode Program 5.11 Implementasi kode program Word2Vec dan Improved Sqrt-
Cosine Similarity (lanjutan)

# for _, section_row in resume_sections.iterrows():
# section_name = section_row['Section']
# section_vector = section_row['W2V_Vector'] #
## Vektor section dalam bentuk 1D
# 27
# # Hitung improved sqrt-cosine similarity antara
section dan vacancy

# sim_score =
improved_sqrt_cosine_similarity(section_vector, job_vec_w2v)

# similarity_scores[section_name] = sim_score
# 31
# # Versi 1: Tanpa bobot (rata-rata similarity semua
section)

# sim_no_weight = sum(similarity_scores.values()) /
len(similarity_scores) if similarity_scores else 0

# 34
# # Versi 2: Dengan bobot (weighted sum tanpa normalisasi
ketat)

# weighted_sum_v2 = 0
# total_weight_v2 = 0
# for section in similarity_scores:
# sim = similarity_scores.get(section, 0)
# weight = category_weights.get(section, 0)
# weighted_sum_v2 += sim * weight
# total_weight_v2 += weight
# sim_with_weight = weighted_sum_v2 / total_weight_v2 if
total_weight_v2 > 0 else 0

# 44
# # Simpan hasil
# final_results_w2v_isc.append({
# 'Resume_ID': resume_id,
# 'Position': position,
# 'Similarity_No_Weight': sim_no_weight,
# 'Similarity_With_Weight': sim_with_weight,
# })
# 52
# # Catat waktu selesai dan hitung durasi
# end_time = time.time()
# total_time = end_time - start_time
# 56
# # Konversi waktu ke format yang lebih mudah dibaca
# minutes = int(total_time // 60)
# seconds = int(total_time % 60)
# 60
# # Konversi hasil ke DataFrame
# result_df_w2v_isc = pd.DataFrame(final_results_w2v_isc)
# 63
# # Tampilkan waktu total
# print(f"Total waktu pemrosesan: {minutes} menit {seconds}
detik")

# 66
# print("Similaritas Tanpa Bobot Section")
# 68
# top5_per_position_no_weight =
result_df_w2v_isc.groupby('Position', group_keys=False).apply(

# lambda x: x.nlargest(5, 'Similarity_No_Weight')
# 71
# 72
# grouped_no_weight =
top5_per_position_no_weight.groupby('Position')

# for position, group in grouped_no_weight:
# 135
Kode Program 5.11 Implementasi kode program Word2Vec dan Improved Sqrt-
Cosine Similarity (lanjutan)

# print(f"\nPosition: {position}")
# print(group[['Resume_ID', 'Similarity_No_Weight']])
# 77
# print("Similaritas Dengan Bobot Section")
# 79
# top5_per_position_with_weight =
result_df_w2v_isc.groupby('Position', group_keys=False).apply(

# lambda x: x.nlargest(5, 'Similarity_With_Weight')
# 82
# 83
# grouped_with_weight =
top5_per_position_with_weight.groupby('Position')

# for position, group in grouped_with_weight:
# print(f"\nPosition: {position}")
# print(group[['Resume_ID', 'Similarity_With_Weight']])
Penjelasan dari Kode Program 5.11 mengenai implementasi perhitungan
similaritas antara resume dan kualifikasi lowongan kerja dengan Improved Sqrt-
Cosine (ISC) Similarity jika menggunakan vektor Word2Vec, yaitu:

# Baris 1 merupakan proses untuk mencatat waktu mulai eksekusi
menggunakan time.time() dan menyimpannya ke variabel start_time.

# Baris 3-4 merupakan proses untuk membuat list kosong
final_results_w2v_isc untuk menyimpan hasil perhitungan
kemiripan (similarity) antara resume dan kualifikasi lowongan kerja.

# Baris 6-7 merupakan proses untuk memulai iterasi melalui setiap baris di
DataFrame vacancy_df_1 menggunakan iterrows() dengan
progress bar dari tqdm untuk menampilkan kemajuan pemrosesan.

# Baris 8 merupakan proses untuk mengambil nilai kolom Position dari
baris kualifikasi lowongan kerja terkini dan menyimpannya ke variabel
position.

# Baris 9 merupakan pengambilan nilai kolom Category dari baris
lowongan kerja pada iterasi terkini dan menyimpannya ke variabel
vacancy_category.

# Baris 10 merupakan pengambilan vektor Word2Vec dari kolom
W2V_Vector pada baris kualifikasi lowongan kerja di iterasi terkini dan
menyimpannya ke variabel job_vec_w2v.

# Baris 12-16 merupakan proses untuk memfilter DataFrame section_df
berdasarkan vacancy_category, menetapkan kolom Section
sebagai indeks, mengambil kolom Bobot, membaginya dengan 100
menggunakan div(100) untuk mengubah ke skala desimal (karena
bobot dalam persentase), dan mengonversinya menjadi dictionary
menggunakan to_dict(), lalu menyimpannya ke variabel
category_weights sebagai persentase bobot per section untuk
kualifikasi lowongan kerja pada iterasi terkini sesuai industrinya.

# 136
# Baris 18-19 merupakan proses untuk memulai iterasi melalui setiap nilai
unik di kolom ID pada DataFrame resume_df_1 menggunakan
unique().

# Baris 20 merupakan proses untuk memfilter DataFrame resume_df_1
untuk mendapatkan semua baris dengan kolom ID yang sesuai dengan
iterasi resume_id terkini dan menyimpannya ke variabel
resume_sections.

# Baris 21 merupakan pembuatan dictionary kosong
similarity_scores untuk menyimpan skor kemiripan setiap section
dalam resume.

# Baris 23-24 merupakan proses untuk memulai iterasi melalui setiap baris
di resume_sections menggunakan iterrows() untuk memproses
setiap section dalam resume.

# Baris 25 merupakan proses untuk mengambil nilai kolom Section dari
baris section terkini dan menyimpannya ke variabel section_name.

# Baris 26 merupakan proses untuk mengambil vektor Word2Vec dari kolom
W2V_Vector pada baris section saat ini dan menyimpannya ke variabel
section_vector.

# Baris 28-29 merupakan proses untuk menghitung kemiripan antara vektor
section pada resume (section_vector) dan vektor kualifikasi
lowongan kerja (vac_vector) menggunakan fungsi
cosine_similarity dari library Scikit-learn, lalu menyimpan hasilnya
ke variabel sim_score.

# Baris 30 merupakan proses untuk menyimpan skor kemiripan
sim_score ke dictionary similarity_scores.

# Baris 32-33 merupakan proses untuk menguji skenario “Tanpa Bobot”
dengan menghitung rata-rata kemiripan dengan menjumlahkan semua
skor kemiripan di similarity_scores menggunakan sum() dan
membaginya dengan jumlah section menggunakan len(), atau
mengembalikan 0 jika dictionary kosong, lalu menyimpan hasilnya ke
variabel sim_no_weight.

# Baris 35-43 merupakan proses untuk menguji skenario “Dengan Bobot”,
dimana baris 36-37 menginisialisasi variabel weighted_sum_v2 dan
total_weight_v2 dengan nilai 0 untuk menghitung jumlah kemiripan
terbobot dan total bobot.

# Baris 38-42 merupakan proses untuk mengiterasi setiap section di
similarity_scores, mengambil skor kemiripan yang disimpan pada
variabel sim, mendapatkan bobot section dari variabel
category_weights dengan default 0 menggunakan get(),
mengalikan skor “Dengan Bobot” untuk menambah ke
weighted_sum_v2, dan menambah bobot ke total_weight_v2.

# 137
# Baris 43 merupakan proses untuk menghitung total similarity pada
skenario “Dengan Bobot” dengan membagi weighted_sum_v2 dengan
total_weight_v2 jika total_weight_v2 lebih dari 0 atau
mengembalikan nilai 0 jika tidak. Kemudian, menyimpan hasilnya ke
variabel sim_with_weight.

# Baris 45-46 merupakan proses untuk menambahkan data resume_id,
position, sim_no_weight, dan sim_with_weight ke list
final_results_w2v_isc menggunakan append().

# Baris 53-55 merupakan proses untuk mencatat waktu selesai
menggunakan time.time(), menghitung durasi dengan mengurangkan
start_time dari end_time, dan menyimpan hasilnya ke variabel
total_time.

# Baris 57-59 merupakan proses untuk mengonversi total_time ke menit
dan detik, lalu menyimpannya ke variabel minutes dan seconds.

# Baris 61-62 merupakan proses untuk membuat DataFrame
result_df_w2v_isc dari list final_results_w2v_isc
menggunakan pd.DataFrame(), dengan kolom Resume_ID,
Position, Similarity_No_Weight, dan
Similarity_With_Weight.

# Baris 64-65 merupakan proses untuk mencetak total waktu pemrosesan
dalam format menit dan detik menggunakan print().

# Baris 67 merupakan proses untuk mencetak judul "Similaritas Tanpa Bobot
Section" menggunakan print().

# Baris 69-71 merupakan proses untuk mengelompokkan DataFrame
result_df_w2v_isc berdasarkan kolom Position menggunakan
groupby(), lalu memilih 5 baris dengan nilai
Similarity_No_Weight tertinggi untuk setiap posisi menggunakan
nlargest(), dan menyimpan hasilnya ke variabel
top5_per_position_no_weight.

# Baris 73-76 merupakan proses untuk mengelompokkan
top5_per_position_no_weight berdasarkan kolom Position,
mengiterasi setiap kualifikasi lowongan kerja (Position), mencetak
nama posisi, mencetak nilai kolom Resume_ID, serta mencetak nilai
Similarity_No_Weight untuk setiap kualifikasi lowongan kerja.

# Baris 78 merupakan proses untuk mencetak judul "Similaritas Dengan
Bobot Section" menggunakan print().

# Baris 80-82 merupakan proses untuk mengelompokkan DataFrame
result_df_w2v_isc berdasarkan kolom Position menggunakan
groupby(), lalu memilih 5 baris dengan nilai

## Similarity_With_Weight tertinggi untuk setiap posisi
menggunakan nlargest(), dan menyimpan hasilnya ke variabel
top5_per_position_with_weight.

# 138
# Baris 84-87 merupakan proses untuk mengelompokkan
top5_per_position_with_weight berdasarkan Position,
mengiterasi setiap kualifikasi lowongan kerja (Position), mencetak
nama posisi, mencetak kolom Resume_ID, serta
Similarity_With_Weight untuk setiap kualifikasi lowongan kerja.

## Implementasi Kode Program Pengujian
### Implementasi Kode Program Perhitungan SRCC
Dalam kode program ini, dilakukan pemuatan enam DataFrame dengan format
CSV yang berisi peringkat resume dengan dan “Tanpa Bobot” untuk metode TF-
IDF dengan Improved Sqrt-Cosine (ISC) Similarity, Word2Vec dengan Cosine
Similarity (CosSim), dan Word2Vec dengan ISC. Fungsi calculate_srcc
menghitung Spearman Rank Correlation Coefficient (SRCC) untuk membandingkan
peringkat hasil implementasi metode dengan peringkat pakar per posisi. Hasil
SRCC digabungkan ke dalam DataFrame merged_df dengan kolom Position
sebagai indeks dan divisualisasikan melalui DataFrame styled_df dengan
pewarnaan berdasarkan nilai SRCC, ditandai dengan warna hijau jika nilai SRCC
pada suatu kualifikasi lowongan kerja (Position) bernilai di atas ambang batas
dan ditandai dengan warna merah jika nilai SRCC di bawah ambang batas.
Implementasi kode program tertera pada Kode Program 5.12.
Kode Program 5.12 Implementasi kode program perhitungan Spearman Rank

## Correlation Coefficient
# # Input DataFrame
# result_df_bobot_tfidf =
pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu
me2-23\rank_df_bobot_tfidf.csv')

# result_df_bobot_w2v =
pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu
me2-23\rank_df_bobot_w2v.csv')

# result_df_bobot_w2v_isc =
pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu
me2-23\rank_df_bobot_w2v_isc.csv')

# 5
# result_df_tanpa_bobot_tfidf =
pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu
me2-23\rank_df_tanpa_bobot_tfidf.csv')

# result_df_tanpa_bobot_w2v =
pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu
me2-23\rank_df_tanpa_bobot_w2v.csv')

# result_df_tanpa_bobot_w2v_isc =
pd.read_csv(r'C:\Users\mit.itsupport\Downloads\archive2024\Resu
me2-23\rank_df_tanpa_bobot_w2v_isc.csv')

# 9
# result_df_bobot_tfidf =
result_df_bobot_tfidf.drop(columns=["Link_Gdrive"])

# result_df_bobot_w2v =
result_df_bobot_w2v.drop(columns=["Link_Gdrive"])

# result_df_bobot_w2v_isc =
result_df_bobot_w2v_isc.drop(columns=["Link_Gdrive"])

# 13
# result_df_tanpa_bobot_tfidf =
result_df_tanpa_bobot_tfidf.drop(columns=["Link_Gdrive"])

# 139
Kode Program 5.12 Implementasi kode program perhitungan Spearman Rank
Correlation Coefficient (lanjutan)

# result_df_tanpa_bobot_w2v =
result_df_tanpa_bobot_w2v.drop(columns=["Link_Gdrive"])

# result_df_tanpa_bobot_w2v_isc =
result_df_tanpa_bobot_w2v_isc.drop(columns=["Link_Gdrive"])

# 17
# # Korelasi Ranking SRCC
# def calculate_srcc(df):
# df['d_i'] = df['Rank'] - df['Rank_Expert'] # Selisih
peringkat (d_i)

# 21
# df['d_i_squared'] = df['d_i'] ** 2 # Kuadrat selisih
peringkat (d_i^2)

# 23
# sum_d_i_squared = df['d_i_squared'].sum() # Total kuadrat
selisih peringkat (∑ d_i^2)

# 25
# n = len(df)
# 27
# # Hitung SRCC
# if n < 2 or n * (n**2 - 1) == 0: # Mengatasi pembagian
dengan 0

# return None
# srcc = 1 - ((6 * sum_d_i_squared) / (n * (n**2 - 1)))
# 32
# return srcc
# 34
# def calculate_srcc_per_position(df):
# results = {}
# for position, group in df.groupby('Position'): # Hitung
SRCC berdasarkan 'Position'

# srcc = calculate_srcc(group)
# if srcc is not None:
# results[position] = srcc
# return results
# 42
# # Implementasi Fungsi SRCC
# srcc_bobot_tfidf =
calculate_srcc_per_position(result_df_bobot_tfidf)

# srcc_bobot_w2v =
calculate_srcc_per_position(result_df_bobot_w2v)

# srcc_bobot_w2v_isc =
calculate_srcc_per_position(result_df_bobot_w2v_isc)

# 47
# srcc_tanpa_bobot_tfidf =
calculate_srcc_per_position(result_df_tanpa_bobot_tfidf)

# srcc_tanpa_bobot_w2v =
calculate_srcc_per_position(result_df_tanpa_bobot_w2v)

# srcc_tanpa_bobot_w2v_isc =
calculate_srcc_per_position(result_df_tanpa_bobot_w2v_isc)

# 51
# # Merge semua df ke satu df
# df_bobot_tfidf = pd.DataFrame(list(srcc_bobot_tfidf.items()),
columns=['Position', 'TFIDF_Bobot'])

# df_bobot_w2v = pd.DataFrame(list(srcc_bobot_w2v.items()),
columns=['Position', 'W2V_Bobot'])

# df_bobot_w2v_isc =
pd.DataFrame(list(srcc_bobot_w2v_isc.items()),
columns=['Position', 'W2V_ISC_Bobot'])

# df_tanpa_bobot_tfidf =
pd.DataFrame(list(srcc_tanpa_bobot_tfidf.items()),
columns=['Position', 'TFIDF_Tanpa_Bobot'])

# 140
Kode Program 5.12 Implementasi kode program perhitungan Spearman Rank
Correlation Coefficient (lanjutan)

# df_tanpa_bobot_w2v =
pd.DataFrame(list(srcc_tanpa_bobot_w2v.items()),
columns=['Position', 'W2V_Tanpa_Bobot'])

# df_tanpa_bobot_w2v_isc =
pd.DataFrame(list(srcc_tanpa_bobot_w2v_isc.items()),
columns=['Position', 'W2V_ISC_Tanpa_Bobot'])

# 59
# # Jadikan 'Position' sebagai index
# merged_df = df_bobot_tfidf.set_index('Position')
# merged_df = merged_df.join(df_bobot_w2v.set_index('Position'),
how='outer')

# merged_df =
merged_df.join(df_bobot_w2v_isc.set_index('Position'),
how='outer')

# merged_df =
merged_df.join(df_tanpa_bobot_tfidf.set_index('Position'),
how='outer')

# merged_df =
merged_df.join(df_tanpa_bobot_w2v.set_index('Position'),
how='outer')

# merged_df =
merged_df.join(df_tanpa_bobot_w2v_isc.set_index('Position'),
how='outer')

# 67
# # Pemberian warna untuk visualisasi
# def color_srcc(val):
# if pd.isna(val): # Jika ada NaN
# return ''
# if val >= 0,6: # Kuat (hijau)
# return 'background-color: lightgreen'
# else: # Lemah (merah)
# return 'background-color: lightcoral'
# 76
# styled_df =
merged_df.style.format("{:.16f}").applymap(color_srcc)

# styled_df
Penjelasan dari Kode Program 5.12 mengenai implementasi kode program
pengujian bagian perhitungan Spearman Rank Correlation Coefficient (SRCC),
yaitu:

# Baris 2 merupakan proses untuk menginput file dengan format CSV
rank_df_bobot_tfidf ke dalam DataFrame result_df_bobot_tfidf
menggunakan pd.read_csv().

# Baris 3 merupakan proses untuk menginput file dengan format CSV
rank_df_bobot_w2v ke dalam DataFrame result_df_bobot_w2v
menggunakan pd.read_csv().

# Baris 4 merupakan proses untuk menginput file dengan format CSV
rank_df_bobot_w2v_isc ke dalam DataFrame
result_df_bobot_w2v_isc menggunakan pd.read_csv().

# 141
# Baris 6 merupakan proses untuk menginput file dengan format CSV
rank_df_tanpa_bobot_tfidf ke dalam DataFrame
result_df_tanpa_bobot_tfidf menggunakan
pd.read_csv().

# Baris 7 merupakan proses untuk menginput file dengan format CSV
rank_df_tanpa_bobot_w2v ke dalam DataFrame
result_df_tanpa_bobot_w2v menggunakan pd.read_csv().

# Baris 8 merupakan proses untuk menginput file dengan format CSV
rank_df_tanpa_bobot_w2v_isc ke dalam DataFrame
result_df_tanpa_bobot_w2v_isc menggunakan
pd.read_csv().

# Baris 10-16 merupakan proses untuk menghapus kolom Link_Gdrive
dari enam DataFrame yang sudah diinput.

# Baris 18-19 merupakan proses untuk mendefinisikan fungsi
calculate_srcc yang menerima DataFrame df.

# Baris 20 merupakan proses untuk menghitung selisih antara kolom Rank
dan Rank_Expert yang disimpan pada kolom baru d_i.

# Baris 22 merupakan proses untuk menghitung kuadrat dari kolom d_i
yang disimpan ke kolom baru d_i_squared.

# Baris 24 merupakan proses untuk menjumlahkan semua nilai di kolom
d_i_squared menggunakan sum() dan disimpan ke variabel
sum_d_i_squared.

# Baris 26 merupakan proses untuk menghitung jumlah baris di DataFrame
df menggunakan len() dan menyimpannya ke variabel n.

# Baris 28-30 merupakan proses untuk memeriksa apakah n kurang dari 2
atau penyebut yang merupakan rumus SRCC (n * (n**2 - 1)) sama
dengan 0 lalu mengembalikan None jika kondisi terpenuhi (true) untuk
menghindari pembagian dengan nol.

# Baris 31 merupakan proses untuk menghitung Spearman Rank Correlation
Coefficient (SRCC) menggunakan persamaan 1 - (6 *
sum_d_i_squared) / (n * (n**2 - 1)) dan disimpan ke
variabel srcc.

# Baris 33 merupakan proses untuk mengembalikan nilai srcc sebagai hasil
dari fungsi calculate_srcc.

# Baris 35-36 merupakan proses untuk mendefinisikan fungsi
calculate_srcc_per_position dan pembuatan dictionary kosong
results untuk menyimpan nilai hasil perhitungan SRCC setiap kualifikasi
lowongan kerja.

# Baris 37-40 mengelompokkan DataFrame df berdasarkan kolom
Position, lalu menghitung SRCC untuk setiap kualifikasi lowongan kerja
(Position) dengan memanggil fungsi calculate_srcc dan disimpan
hasil-hasilnya ke dictionary results jika fungsi tersebut tidak
mengembalikan None.

# 142
# Baris 41 merupakan proses untuk mengembalikan isian dictionary
results yang merupakan nilai-nilai SRCC per kualifikasi lowongan kerja
sebagai hasil dari fungsi calculate_srcc_per_position.

# Baris 43-50 merupakan proses untuk menghitung SRCC per kualifikasi
lowongan kerja pada enam DataFrame, yaitu:
a. Hasil SRCC result_df_bobot_tfidf disimpan ke variabel
srcc_bobot_tfidf,
b. Hasil SRCC result_df_bobot_w2v disimpan ke variabel
srcc_bobot_w2v,

# Hasil SRCC result_df_bobot_w2v_isc disimpan ke variabel
srcc_bobot_w2v_isc,
d. Hasil SRCC result_df_tanpa_bobot_tfidf disimpan ke
variabel srcc_tanpa_bobot_tfidf,
e. Hasil SRCC result_df_tanpa_bobot_w2v disimpan ke
variabel srcc_tanpa_bobot_w2v,
f. Hasil SRCC result_df_tanpa_bobot_w2v_isc disimpan ke
variabel srcc_tanpa_bobot_w2v_isc.

# Baris 52-58 merupakan proses untuk membuat DataFrame menggunakan
pd.DataFrame() dari masing-masing hasil enam perhitungan SRCC per
posisi yang disimpan menjadi:
a. df_bobot_tfidf dari dictionary srcc_bobot_tfidf
dengan kolom Position dan TFIDF_Bobot,
b. df_bobot_w2v dari dictionary srcc_bobot_w2v dengan
kolom Position dan W2V_Bobot,

# df_bobot_w2v_isc dari dictionary srcc_bobot_w2v_isc
dengan kolom Position dan W2V_ISC_Bobot,
d. df_tanpa_bobot_tfidf dari dictionary
srcc_tanpa_bobot_tfidf dengan kolom Position dan
TFIDF_Tanpa_Bobot,
e. df_tanpa_bobot_w2v dari dictionary
srcc_tanpa_bobot_w2v dengan kolom Position dan
W2V_Tanpa_Bobot,
f. df_tanpa_bobot_w2v_isc dari dictionary
srcc_tanpa_bobot_w2v_isc dengan kolom Position dan
W2V_ISC_Tanpa_Bobot.

# Baris 60-66 merupakan proses mengatur kolom Position sebagai indeks
dan menggabungkan enam DataFrame untuk dijadikan satu menggunakan
df.join() dan disimpan ke DataFrame merged_df.

# Baris 68-75 merupakan proses untuk mendefinisikan fungsi color_srcc
yang memberikan warna pada isian nilai di DataFrame berdasarkan nilai
SRCC, di mana jika kosong atau NaN, maka tidak diberi warna; jika lebih
dari sama dengan 0,6, maka diberi warna hijau; dan jika kurang dari 0,6,
maka diberi warna merah.

# 143
# Baris 77 merupakan proses untuk memformat DataFrame merged_df
menggunakan style.format("{:.16f}") dan menerapkan fungsi
color_srcc untuk pemberian warna menggunakan applymap().
Kemudian, disimpan pada DataFrame baru dengan variabel styled_df.

# Baris 78 merupakan proses untuk menampilkan DataFrame styled_df.
## Implementasi Kode Program Perhitungan Relevansi dan
## Senioritas
Dalam kode program ini, dilakukan perhitungan persentase relevansi dan
senioritas per kualifikasi lowongan kerja (Position) untuk enam DataFrame
dengan dan “Tanpa Bobot” untuk metode TF-IDF dengan Improved Sqrt-Cosine
(ISC) Similarity, Word2Vec dengan Cosine Similarity (CosSim), dan Word2Vec
dengan ISC menggunakan fungsi
calculate_relevance_seniority_per_position. Tampilan hasilnya
dibuat menjadi dua DataFrame agar lebih mudah dalam segi pembacaan, yakni
df_relevance untuk relevansi dan df_seniority untuk senioritas. Kedua
DataFrame tersebut divisualisasikan dengan pewarnaan berdasarkan nilai
persentase, ditandai dengan warna hijau jika persentase pada suatu kualifikasi
lowongan kerja (Position) bernilai di atas ambang batas dan ditandai dengan
warna merah jika persentase di bawah ambang batas. Implementasi kode program
tertera pada Kode Program 5.13.
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan
senioritas

# # Menghitung persentase Relevansi dan Senioritas per posisi
# def calculate_relevance_seniority_per_position(df):
# results = {}
# for position, group in df.groupby('Position'):
# total_resumes = len(group)
# 6
# # Hitung jumlah TRUE untuk Relevansi dan Senioritas
# relevance_count = (group['Relevance'] == True).sum()
# seniority_count = (group['Seniority'] == True).sum()
# 10
# # Hitung persentase
# relevance_percent = (relevance_count / total_resumes) *
# 100
seniority_percent = (seniority_count / total_resumes) *

# 100
# # Simpan hasil
# results[position] = {'Relevance': relevance_percent,
'Seniority': seniority_percent}

# 17
# return results
# 19
# # Implementasi Fungsi Relevansi dan Senioritas
# relevance_seniority_bobot_tfidf =
calculate_relevance_seniority_per_position(result_df_bobot_tfid
f)

# relevance_seniority_bobot_w2v =
calculate_relevance_seniority_per_position(result_df_bobot_w2v)

# 144
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan
senioritas (lanjutan)

# relevance_seniority_bobot_w2v_isc =
calculate_relevance_seniority_per_position(result_df_bobot_w2v_
isc)

# relevance_seniority_tanpa_bobot_tfidf =
calculate_relevance_seniority_per_position(result_df_tanpa_bobo
t_tfidf)

# relevance_seniority_tanpa_bobot_w2v =
calculate_relevance_seniority_per_position(result_df_tanpa_bobo
t_w2v)

# relevance_seniority_tanpa_bobot_w2v_isc =
calculate_relevance_seniority_per_position(result_df_tanpa_bobo
t_w2v_isc)

# 27
# # Membedakan DataFrames untuk Relevansi dan Senioritas
# df_relevance_bobot_tfidf = pd.DataFrame(
# [(pos, val['Relevance']) for pos, val in
relevance_seniority_bobot_tfidf.items()],

# columns=['Position', 'TFIDF_Bobot']
# 32
# df_relevance_bobot_w2v = pd.DataFrame(
# [(pos, val['Relevance']) for pos, val in
relevance_seniority_bobot_w2v.items()],

# columns=['Position', 'W2V_Bobot']
# 36
# df_relevance_bobot_w2v_isc = pd.DataFrame(
# [(pos, val['Relevance']) for pos, val in
relevance_seniority_bobot_w2v_isc.items()],

# columns=['Position', 'W2V_ISC_Bobot']
# 40
# df_relevance_tanpa_bobot_tfidf = pd.DataFrame(
# [(pos, val['Relevance']) for pos, val in
relevance_seniority_tanpa_bobot_tfidf.items()],

# columns=['Position', 'TFIDF_Tanpa_Bobot']
# 44
# df_relevance_tanpa_bobot_w2v = pd.DataFrame(
# [(pos, val['Relevance']) for pos, val in
relevance_seniority_tanpa_bobot_w2v.items()],

# columns=['Position', 'W2V_Tanpa_Bobot']
# 48
# df_relevance_tanpa_bobot_w2v_isc = pd.DataFrame(
# [(pos, val['Relevance']) for pos, val in
relevance_seniority_tanpa_bobot_w2v_isc.items()],

# columns=['Position', 'W2V_ISC_Tanpa_Bobot']
# 52
# 53
# df_seniority_bobot_tfidf = pd.DataFrame(
# [(pos, val['Seniority']) for pos, val in
relevance_seniority_bobot_tfidf.items()],

# columns=['Position', 'TFIDF_Bobot']
# 57
# df_seniority_bobot_w2v = pd.DataFrame(
# [(pos, val['Seniority']) for pos, val in
relevance_seniority_bobot_w2v.items()],

# columns=['Position', 'W2V_Bobot']
# 61
# df_seniority_bobot_w2v_isc = pd.DataFrame(
# [(pos, val['Seniority']) for pos, val in
relevance_seniority_bobot_w2v_isc.items()],

# columns=['Position', 'W2V_ISC_Bobot']
# 65
# 145
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan
senioritas (lanjutan)

# df_seniority_tanpa_bobot_tfidf = pd.DataFrame(
# [(pos, val['Seniority']) for pos, val in
relevance_seniority_tanpa_bobot_tfidf.items()],

# columns=['Position', 'TFIDF_Tanpa_Bobot']
# 69
# df_seniority_tanpa_bobot_w2v = pd.DataFrame(
# [(pos, val['Seniority']) for pos, val in
relevance_seniority_tanpa_bobot_w2v.items()],

# columns=['Position', 'W2V_Tanpa_Bobot']
# 73
# df_seniority_tanpa_bobot_w2v_isc = pd.DataFrame(
# [(pos, val['Seniority']) for pos, val in
relevance_seniority_tanpa_bobot_w2v_isc.items()],

# columns=['Position', 'W2V_ISC_Tanpa_Bobot']
# 77
# 78
# merged_relevance_df =
df_relevance_bobot_tfidf.set_index('Position')

# merged_relevance_df =
merged_relevance_df.join(df_relevance_bobot_w2v.set_index('Posi
tion'), how='outer')

# merged_relevance_df =
merged_relevance_df.join(df_relevance_bobot_w2v_isc.set_index('
Position'), how='outer')

# merged_relevance_df =
merged_relevance_df.join(df_relevance_tanpa_bobot_tfidf.set_ind
ex('Position'), how='outer')

# merged_relevance_df =
merged_relevance_df.join(df_relevance_tanpa_bobot_w2v.set_index
('Position'), how='outer')

# merged_relevance_df =
merged_relevance_df.join(df_relevance_tanpa_bobot_w2v_isc.set_i
ndex('Position'), how='outer')

# 85
# merged_seniority_df =
df_seniority_bobot_tfidf.set_index('Position')

# merged_seniority_df =
merged_seniority_df.join(df_seniority_bobot_w2v.set_index('Posi
tion'), how='outer')

# merged_seniority_df =
merged_seniority_df.join(df_seniority_bobot_w2v_isc.set_index('
Position'), how='outer')

# merged_seniority_df =
merged_seniority_df.join(df_seniority_tanpa_bobot_tfidf.set_ind
ex('Position'), how='outer')

# merged_seniority_df =
merged_seniority_df.join(df_seniority_tanpa_bobot_w2v.set_index
('Position'), how='outer')

# merged_seniority_df =
merged_seniority_df.join(df_seniority_tanpa_bobot_w2v_isc.set_i
ndex('Position'), how='outer')

# 92
# # Pemberian warna untuk visualisasi
# def color_percentage(val):
# if pd.isna(val): # Jika ada NaN
# return ''
# if val >= 60: # Kuat (hijau)
# return 'background-color: lightgreen'
# else: # Lemah (merah)
# return 'background-color: lightcoral'
# 101
# 146
Kode Program 5.13 Implementasi kode program perhitungan relevansi dan
senioritas (lanjutan)

# styled_relevance_df =
merged_relevance_df.style.format("{:.2f}%").applymap(color_perc
entage)

# styled_seniority_df =
merged_seniority_df.style.format("{:.2f}%").applymap(color_perc
entage)

# 104
# styled_relevance_df
# 106
# styled_seniority_df
Penjelasan dari Kode Program 5.13 mengenai implementasi kode program
pengujian bagian perhitungan relevansi dan senioritas, yaitu:

# Baris 1-3 merupakan proses untuk mendefinisikan fungsi
calculate_relevance_seniority_per_position yang
menerima DataFrame df dan membuat dictionary kosong results
untuk menyimpan hasil perhitungan persentase relevansi dan senioritas.

# Baris 5 merupakan proses untuk mengelompokkan DataFrame df
berdasarkan kolom Position dan memulai iterasi untuk setiap
kualifikasi lowongan kerja (Position).

# Baris 6 merupakan proses untuk menghitung jumlah resume yang ada di
dalam kualifikasi lowongan kerja menggunakan len() dan
menyimpannya ke variabel total_resumes.

# Baris 8-9 merupakan proses untuk menghitung jumlah nilai True di kolom
Relevance menggunakan (group['Relevance'] ==
True).sum() dan di kolom Seniority menggunakan
(group['Seniority'] == True).sum(). Kemudian, disimpan ke
variabel relevance_count dan seniority_count.

# Baris 12-14 merupakan proses untuk menghitung persentase relevansi
dengan membagi relevance_count dengan total_resumes dan
mengalikan dengan 100 agar hasilnya dalam bentuk persen, lalu disimpan
ke variabel relevance_percent. Hal yang sama dilakukan pada
perhitungan persentase senioritas dengan membagi
seniority_count dengan total_resumes dan mengalikan dengan

# lalu disimpan ke variabel seniority_percent.
# Baris 15-18 merupakan proses untuk menambahkan nilai position,
relevance_percent, dan seniority_percent ke dictionary
results. Kemudian, dikonversi menjadi DataFrame menggunakan
pd.DataFrame().

# 147
# Baris 20-26 merupakan proses untuk menghitung persentase relevansi dan
senioritas per kualifikasi lowongan kerja pada enam DataFrame, yaitu:
a. Hasil perhitungan relevansi dan senioritas
result_df_bobot_tfidf disimpan ke variabel
relevance_seniority_bobot_tfidf,
b. Hasil perhitungan relevansi dan senioritas
result_df_bobot_w2v disimpan ke variabel
relevance_seniority_bobot_w2v,

# Hasil perhitungan relevansi dan senioritas
result_df_bobot_w2v_isc disimpan ke variabel
relevance_seniority_bobot_w2v_isc,
d. Hasil perhitungan relevansi dan senioritas
result_df_tanpa_bobot_tfidf disimpan ke variabel
relevance_seniority_tanpa_bobot_tfidf,
e. Hasil perhitungan relevansi dan senioritas
result_df_tanpa_bobot_w2v disimpan ke variabel
relevance_seniority_tanpa_bobot_w2v,
f. Hasil perhitungan relevansi dan senioritas
result_df_tanpa_bobot_w2v_isc disimpan ke variabel
relevance_seniority_tanpa_bobot_w2v_isc.

# Baris 28-52 merupakan proses untuk membuat enam DataFrame terpisah,
yakni menyimpan masing-masing data relevansi dari setiap hasil
perhitungan result_df dengan kolom Position, serta kolom nama
pendekatan dan skenario yang digunakan.

# Baris 54-77 merupakan proses untuk membuat enam DataFrame terpisah,
yakni menyimpan masing-masing data senioritas dari setiap hasil
perhitungan result_df dengan kolom Position, serta kolom nama
pendekatan dan skenario yang digunakan.

# Baris 79-84 merupakan proses mengatur kolom Position sebagai indeks
dan mengabungkan enam DataFrame hasil data relevansi menggunakan
df.join() dan disimpan ke DataFrame merged_relevance_df.

# Baris 86-91 merupakan proses mengatur kolom Position sebagai indeks
dan mengabungkan enam DataFrame hasil data senioritas menggunakan
df.join() dan disimpan ke DataFrame merged_relevance_df.

# Baris 93-100 merupakan proses untuk mendefinisikan fungsi
color_percentage yang memberikan warna pada isian nilai di
DataFrame berdasarkan persentanse relevansi atau senioritas, di mana jika
kosong atau NaN, maka tidak diberi warna; jika lebih dari sama dengan 60
maka diberi warna hijau; dan jika kurang dari 60 maka diberi warna merah.

# Baris 102 merupakan proses untuk memformat DataFrame
relevance_df menggunakan style.format("{:.2f}%") dan
menerapkan fungsi color_percentage untuk pemberian warna
menggunakan applymap(). Kemudian, disimpan pada DataFrame baru
dengan variabel styled_relevance_df.

# 148
# Baris 103 merupakan proses untuk memformat DataFrame
seniority_df menggunakan style.format("{:.2f}%") dan
menerapkan fungsi color_percentage untuk pemberian warna
menggunakan applymap(). Kemudian, disimpan hasilnya ke variabel
styled_seniority_df.

# Baris 105 merupakan proses untuk menampilkan DataFrame
styled_relevance_df.

# Baris 107 merupakan proses untuk menampilkan DataFrame
styled_seniority_df.

# 149
# BAB 6 PENGUJIAN DAN ANALISIS HASIL
Pemaparan hasil dari pengujian akan dijelaskan di bab pengujian, serta
pembahasan dan analisa dari hasil pengujian tersebut sebagai bahan evaluasi.

## Pengujian
Penelitian ini menggunakan dua pendekatan perhitungan representasi teks,
yakni TF-IDF dan Word2Vec. Untuk pendekatan perhitungan similaritasnya dibuat
menjadi tiga kombinasi pendekatan, yakni TF-IDF dengan Improved Sqrt-Cosine
(ISC) Similarity, Word2Vec dengan Cosine Similarity (CosSim), dan Word2Vec
dengan ISC. Masing-masing pendekatan diuji dengan dua skenario. Skenario
pertama adalah lima resume dengan skor similaritas terbesar jika tanpa
menggunakan pembobotan per section dari ahli dan skenario kedua adalah lima
resume dengan skor similaritas terbesar jika menggunakan pembobotan per
section dari ahli. Dalam masing-masing kombinasi pendekatan dan skenario
terdapat tiga parameter penilaian untuk ahli memberikan ground truth
berdasarkan hasil keluaran implementasi dan skenario, yakni peringkat (rank),
relevansi, dan senioritas, dengan fokus utama pada parameter peringkat.
Parameter relevansi dan senioritas berperan sebagai pendukung untuk
memperkaya evaluasi. Implementasi metode atau pendekatan menghasilkan skor
similaritas antara setiap resume dengan masing-masing kualifikasi lowongan kerja.
Untuk setiap kualifikasi lowongan kerja, dipilih lima resume dengan skor
similaritas tertinggi. Kelima resume tersebut selanjutnya dievaluasi oleh ahli
berdasarkan tiga parameter, yakni: (1) urutan peringkat yang dianggap paling
sesuai (ground truth), (2) relevansi isi resume terhadap kualifikasi lowongan kerja,
dan (3) kesesuaian level posisi resume dengan level posisi yang diminta dalam
kualifikasi.
Lima peringkat teratas hasil keluaran dari implementasi metode dipindahkan
ke dalam spreadsheet saat disajikan kepada ahli untuk memudahkan proses
evaluasi. Cuplikan template penyajian tersebut tertera pada Gambar 6.1 dan
Gambar 6.2
Gambar 6.1 Cuplikan template spreadsheet evaluasi ahli

# 150
Gambar 6.2 Cuplikan template spreadsheet evaluasi ahli
Hasil evaluasi dari ahli dihimpun dan dirapikan agar bisa dijadikan DataFrame
untuk perhitungan ketiga parameter penilaian seperti pada Gambar 6.3
Gambar 6.3 Cuplikan spreadsheet hasil evaluasi ahli

# 151
Parameter peringkat (rank) dievaluasi hasil pengujiannya dengan menghitung
Spearman Rank Correlation Coefficient (SRCC) untuk menunjukkan korelasi antara
peringkat yang dihasilkan implementasi metode dengan peringkat yang
dibenarkan (ground truth) oleh ahli. Semakin tinggi nilai korelasi, maka semakin
baik metode tersebut mengurutkan similaritas yang sesuai dengan pandangan ahli
(manusia). Pada penelitian ini, dilakukan deskripsi statistik melalui SPSS untuk
mengetahui persentil dari keseluruhan nilai korelasi seperti tertera pada Gambar

## dan diketahui persentil ke-75 adalah korelasi positif 0,6. Nilai 0,6 ini
menunjukkan bahwa 75% dari data lainnya memiliki nilai yang lebih rendah. Oleh
karena itu, nilai ≥ 0,6 ditentukan sebagai ambang batas parameter korelasi.
Gambar 6.4 Hasil descriptive statistics SPSS
Sebagai parameter pendukung, relevansi dan senioritas pada penelitian ini
dianggap baik jika setidaknya tiga dari lima resume memenuhi deskripsi kualifikasi
lowongan kerja berdasarkan evaluasi ahli. Sehingga, nilai persentase ≥ 60%
ditentukan sebagai ambang batas parameter relevansi dan senioritas.

# 152
Dari 24 kualifikasi lowongan kerja pada penelitian ini, SRCC dengan nilai ≥ 0,6
dianggap kuat (strong) yang ditandai dengan warna hijau. Sedangkan SRCC dengan
nilai < 0,6 dianggap lemah (weak) yang ditandai dengan warna merah. Gambar 6.5
merupakan visualisasi dari nilai korelasi setiap kombinasi pendekatan berdasarkan
posisi kualifikasi lowongan kerja.
Gambar 6.5 Visualisasi nilai korelasi

# 153
Parameter relevansi (relevance) dievaluasi hasil pengujiannya dengan
menghitung persentasenya untuk menunjukkan seberapa relevan resume-resume
yang menjadi keluaran implementasi metode dengan kualifikasi lowongan kerja.
Semakin tinggi persentasenya menunjukkan performa yang lebih baik dalam
konteks relevansi. Dari 24 kualifikasi lowongan kerja pada penelitian ini,
persentase dengan nilai ≥ 60% dianggap memiliki kesesuaian yang tinggi (high) dan
ditandai dengan warna hijau. Sedangkan persentase dengan nilai < 60% dianggap
memiliki kesesuaian yang kurang (low) dan ditandai dengan warna merah. Gambar

## merupakan visualisasi dari nilai persentase relevansi setiap kombinasi
pendekatan berdasarkan posisi kualifikasi lowongan kerja.
Gambar 6.6 Visualisasi persentase relevansi

# 154
Parameter senioritas (seniority) dievaluasi hasil pengujiannya dengan
menghitung persentasenya untuk menunjukkan seberapa sesuai level posisi yang
tercantum di resume-resume yang menjadi keluaran implementasi metode
dengan level posisi yang dibutuhkan pada kualifikasi lowongan kerja. Semakin
tinggi persentasenya menunjukkan tingkat kesesuaian yang lebih baik. Dari 24
kualifikasi lowongan kerja pada penelitian ini, persentase dengan nilai ≥ 60%
dianggap memiliki kesesuaian level posisi yang tinggi (high) dan ditandai dengan
warna hijau. Sedangkan persentase dengan nilai < 60% dianggap memiliki
kesesuaian level posisi yang rendah (low) dan ditandai dengan warna merah.
Gambar 6.7 merupakan visualisasi dari nilai persentase senioritas setiap kombinasi
pendekatan berdasarkan posisi kualifikasi lowongan kerja.
Gambar 6.7 Visualisasi persentase senioritas

# 155
## Analisis Hasil
Metode Improved Sqrt-Cosine (ISC) Similarity pada penelitian ini digunakan
untuk memeringkat lima resume berdasarkan skor similaritas tertinggi untuk
masing-masing 24 kualifikasi lowongan kerja. Perhitungan similaritas ISC
memungkinkan implementasi pada representasi teks TF-IDF yang berbasis
frekuensi. Namun, untuk yang berbasis semantik menggunakan Word2Vec, vektor
harus diambil nilai absolutnya karena vektor hasil Word2Vec dapat mengandung
bilangan negatif. Sedangkan, rumus ISC melibatkan operasi akar kuadrat yang
tidak dapat diterapkan langsung pada bilangan negatif. Oleh karena itu, Kombinasi
pendekatan Word2Vec dengan Cosine Similarity juga digunakan untuk
mempertahankan makna semantik asli dari vektor Word2Vec tanpa modifikasi
nilai absolut.
Performa masing-masing pendekatan dievaluasi melalui tiga parameter, yakni
Spearman Rank Correlation Coefficient (SRCC) untuk mengukur korelasi dengan
pemeringkatan dari hasil evaluasi ahli, relevansi untuk menilai kesesuaian resume
dengan kualifikasi lowongan kerja, dan senioritas untuk mengevaluasi kesesuaian
level posisi berdasarkan kata-kata kunci. Pengujian dilakukan dalam dua skenario,
yakni “Tanpa Bobot” dan “Dengan Bobot”, di mana bobot per section (misalnya,
Summary 5%, Experience 20%, Certification 15%) mencerminkan prioritas
penilaian seorang rekruter.
Berdasarkan hasil pengujian dengan skenario “Tanpa Bobot”, jumlah kualifikasi
lowongan kerja yang memenuhi ambang batas (SRCC ≥ 0,6; relevansi ≥ 60%;
senioritas ≥ 60%; ditandai hijau pada visualisasi) dan yang tidak memenuhi
ambang batas (ditandai merah) pada Tabel 6.1 dan Tabel 6.2.
Tabel 6.1 Hasil pengujian berwarna hijau skenario tanpa bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC

## CosSim
## Jumlah yang nilai 5 7 8
# SRCC ≥ 0,6
## Jumlah yang 15 9 11
persentase
Relevansi ≥ 60%

## Jumlah yang 14 10 16
persentase
Senioritas ≥ 60%

# 156
Tabel 6.2 Hasil pengujian berwarna merah skenario tanpa bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC

## CosSim
## Jumlah yang nilai 19 17 16
# SRCC < 0,6
## Jumlah yang 9 15 13
persentase
Relevansi < 60%

## Jumlah yang 10 14 8
persentase
SenioritasS < 60%
Pada parameter korelasi, pendekatan Word2Vec dengan ISC unggul
menempati urutan tertinggi berjumlah 8 kualifikasi lowongan kerja yang
memenuhi ambang batas, diikuti oleh Word2Vec dengan CosSim berjumlah 7, dan
TF-IDF dengan ISC di urutan terakhir berjumlah 5. Ini menunjukkan hasil
pemeringkatan yang dihasilkan implementasi metode Word2Vec dengan ISC lebih
dekat dengan penilaian ahli.
Pada parameter relevansi, pendekatan TF-IDF dengan ISC unggul dengan 15
kualifikasi lowongan kerja, disusul pendekatan Word2Vec dengan ISC berjumlah

# , dan Word2Vec dengan CosSim yang berada di urutan terakhir berjumlah 9. Ini
menunjukkan isi dari lima resume keluaran implementasi metode TF-IDF dengan
ISC lebih banyak yang sesuai dengan deskripsi kualifikasi lowongan kerja.
Sementara itu, dalam hal senioritas, pendekatan Word2Vec dengan ISC kembali
unggul di urutan pertama dengan 16 kualifikasi lowongan kerja, diikuti oleh
pendekatan TF-IDF dengan ISC berjumlah 14, dan Word2Vec dengan CosSim
berjumlah 10. Ini menunjukkan isi dari lima resume keluaran implementasi
Word2Vec dengan ISC lebih banyak yang level senioritasnya atau level posisinya
yang sesuai dengan deskripsi kualifikasi lowongan kerja.

# 157
Berdasarkan hasil pengujian dengan skenario “Dengan Bobot”, jumlah
kualifikasi lowongan kerja yang memenuhi ambang batas (SRCC ≥ 0,6; relevansi ≥

# %; senioritas ≥ 60%; ditandai hijau pada visualisasi) dan yang tidak memenuhi
ambang batas (ditandai merah).
Tabel 6.3 Hasil pengujian berwarna hijau skenario dengan bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC

## CosSim
## Jumlah yang nilai 6 9 4
# SRCC ≥ 0,6
## Jumlah yang 13 10 11
persentase
Relevansi ≥ 60%

## Jumlah yang 10 14 16
persentase
Senioritas ≥ 60%
Tabel 6.4 Hasil pengujian berwarna merah skenario dengan bobot section
Keterangan TF-IDF + ISC Word2Vec + Word2Vec + ISC

## CosSim
## Jumlah yang nilai 18 15 20
# SRCC < 0,6
## Jumlah yang 11 14 13
persentase
Relevansi < 60%

## Jumlah yang 14 10 8
persentase
Senioritas < 60%
Pada parameter korelasi, pendekatan Word2Vec dengan CosSim unggul
menempati urutan tertinggi dengan jumlah 9 kualifikasi, diikuti oleh TF-IDF dengan
ISC berjumlah 6, dan Word2Vec dengan ISC di urutan terakhir berjumlah 4. Ini
menunjukkan hasil pemeringkatan yang dihasilkan implementasi metode
Word2Vec dengan CosSim lebih dekat dengan penilaian ahli.
Pada parameter relevansi, pendekatan TF-IDF dengan ISC unggul dengan
jumlah 13 kualifikasi, disusul pendekatan Word2Vec dengan ISC berjumlah 11, dan
Word2Vec dengan CosSim yang berada di urutan terakhir berjumlah 10. Ini
menunjukkan isi dari lima resume keluaran implementasi metode TF-IDF dengan
ISC lebih banyak yang sesuai dengan deskripsi kualifikasi lowongan kerja.

# 158
Sementara itu, dalam hal senioritas, pendekatan Word2Vec dengan ISC unggul
di urutan pertama dengan jumlah 16 kualifikasi, diikuti oleh pendekatan
Word2Vec dengan CosSim berjumlah 14, dan TF-IDF dengan ISC berjumlah 10. Ini
menunjukkan isi dari lima resume keluaran implementasi metode Word2Vec
dengan ISC lebih banyak yang sesuai dengan deskripsi kualifikasi lowongan kerja.
Secara jumlah kualifikasi lowongan kerja yang memenuhi dan yang tidak
memenuhi ambang batas pada Tabel 6.1 hingga Tabel 6.4, dihitung menggunakan
weighted scoring, di mana jumlah yang di atas ambang batas diberikan poin +2.
Sedangkan, jumlah yang di bawah ambang batas diberikan poin -1. Hasil
perhitungan weighted score untuk setiap pendekatan dan skenario tertera pada
Tabel 6.5.
Tabel 6.5 Weighted score keseluruhan pendekatan dan skenario

## Pendekatan Korelasi Relevansi Senioritas Weighted
## Score
# TF-IDF + ISC 4×(2) 14×(2) 13×(2) 30
Tanpa Bobot +20×(−1) +10×(−1) +11×(−1)
= (−12) = 18 = 15
Word2Vec + 7×(2) 9×(2) 10×(2) 6
CosSim Tanpa +17×(−1) +15×(−1) +14×(−1)
Bobot = (−3) = 3 = 6
Word2Vec + 8×(2) 11×(2) 16×(2) 33
ISC Tanpa +16×(−1) +13×(−1) +8×(−1)
Bobot = 0 = 9 = 24

# TF-IDF + ISC 5×(2) 12×(2) 10×(2) 15
Dengan Bobot +19×(−1) +12×(−1) +14×(−1)
= −9 = 12 = 6
Word2Vec + 9×(2) 10×(2) 14×(2) 27
CosSim +15×(−1) +14×(−1) +10×(−1)
Dengan Bobot = 3 = 6 = 18
Word2Vec + 4×(2) 11×(2) 16×(2) 21
ISC Dengan +20×(−1) +13×(−1) +8×(−1)
Bobot = (−12) = 9 = 24
Dari Tabel 6.5, diurutkan berdasarkan weighted score tertinggi untuk masing-
masing skenario seperti pada Tabel 6.6.
Tabel 6.6 Urutan pendekatan berdasarkan weighted score tertinggi

## Tanpa Bobot Dengan Bobot
Word2Vec + ISC (33) Word2Vec + CosSim (27)
TF-IDF + ISC (30) Word2Vec + ISC (21)
Word2Vec + CosSim (6) TF-IDF + ISC (15)

# 159
Secara rata-rata, dihitung untuk setiap parameter pada masing-masing
kombinasi pendekatan dan skenario yang tertera hasilnya pada Tabel 6.7.
Tabel 6.7 Perhitungan rata-rata parameter setiap pendekatan dan skenario

## Pendekatan Korelasi Relevansi Senioritas
TF-IDF + ISC Tanpa 0,004348 58,33% 55,83%

## Bobot
Word2Vec + 0,079167 39,17% 49,17%

## CosSim Tanpa
## Bobot
Word2Vec + ISC 0,269565 45,83% 56,67%

## Tanpa Bobot
# TF-IDF + ISC 0,113636 55,83% 50,0%
## Dengan Bobot
Word2Vec + 0,183333 42,5% 50,0%

## CosSim Dengan
## Bobot
Word2Vec + ISC 0,077083 40,83% 56,67%

## Dengan Bobot
Terlihat bahwa Word2Vec dengan ISC unggul pada skenario “Tanpa Bobot”
dengan nilai korelasi rata-rata 0,269565. Namun, nilai tersebut tergolong sebagai
korelasi yang lemah. Di skenario “Dengan Bobot”, Word2Vec dengan CosSim
unggul dengan nilai korelasi rata-rata 0,183333 yang tergolong sebagai korelasi
sangat lemah.
Dalam skenario “Tanpa Bobot” maupun “Dengan Bobot”, pendekatan ISC
dengan representasi teks TF-IDF menunjukkan performa terbaik pada parameter
relevansi, mengungguli Word2Vec dengan ISC dan Word2Vec dengan CosSim. Hal
ini menunjukkan bahwa ISC dengan TF-IDF lebih baik dalam mengidentifikasi isi
resume yang relevan dengan kualifikasi lowongan kerja berdasarkan kesesuaian
kualifikasi lowongan kerja. Keunggulan TF-IDF dengan ISC pada relevansi
disebabkan oleh kemampuan TF-IDF dalam memberi bobot lebih tinggi pada kata-
kata penting yang jarang muncul, tetapi relevan dengan kualifikasi lowongan kerja,
seperti istilah-istilah teknis.

# 160
Pendekatan Word2Vec dengan ISC menunjukkan keterbatasan akibat distorsi
semantik dari penyesuaian nilai absolut, seperti terlihat dari visualisasi yang
menunjukkan pergeseran posisi kata pada Gambar 6.8.
Gambar 6.8 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli
dengan vektor nilai absolut
Lebih rincinya, dilakukan perhitungan similaritas antar term menggunakan
CosSim dengan hasil tertera pada Tabel 6.8.
Tabel 6.8 Perhitungan similaritas antar term Word2Vec vektor nilai asli dengan
vektor nilai absolut
Term 1 versus Similaritas (Nilai Similaritas (Nilai Perubahan
Term 2 Asli) Absolut)
technology versus 0,5711 0,7413 0,1701
engineering
technology versus 0,2471 0,7262 0,4791
fashion
design versus 0,6348 0,8274 0,1927
designer
software versus 0,4153 0,6950 0,2797
java
marketing versus 0,4816 0,6899 0,2083
sales
university versus 0,0751 0,6303 0,5552
cook
pastry versus cook 0,6423 0,7609 0,1185
pastry versus 0,2151 0,7557 0,5406
economy
bake versus 0,2106 0,6603 0,4497
diploma
law versus style 0,0141 0,7308 0,7167

# 161
Tabel 6.8 menunjukkan peningkatan atau penurunan nilai similaritas antar
term, misalnya antara “technology” dengan “fashion” seharusnya kedua term ini
secara semantik berjauhan dan dibuktikan dengan similaritasnya yang bernilai

# ,2471. Namun, setelah nilai vektor dibuat absolut, nilai similaritasnya menjadi
# ,7262 yang menyatakan kedua term ini berdekatan secara semantik,
perubahannya cukup drastis sebanyak 0,4791. Kemudian, ada juga term yang
sudah berdekatan secara semantik menjadi semakin dekat setelah nilainya dibuat
absolut, seperti “design” dan “designer” dari similaritasnya bernilai 0,6348
menjadi 0,8274 yang menyatakan posisi kedua term ini menjadi semakin dekat.
Visualisasi dari beberapa pasangan term yang dibandingkan pada Tabel 6.5
diilustrasikan pada Gambar 6.9.
Gambar 6.9 Visualisasi pergeseran posisi term Word2Vec vektor nilai asli
dengan vektor nilai absolut
Oleh karena itu, Word2Vec dengan ISC unggul dalam skenario “Tanpa Bobot”
disebabkan oleh kemampuan representasi semantik Word2Vec yang masih cukup
mampu menangkap hubungan antar kata kunci yang relevan, meskipun distorsi
terjadi.
Keunggulan Word2Vec dengan CosSim dalam skenario “Dengan Bobot”
menunjukkan bahwa pendekatan ini paling selaras dengan pandangan manusia
karena CosSim menjaga hubungan semantik asli vektor Word2Vec tanpa distorsi
akibat penyesuaian nilai absolut, dan bobot per section memungkinkan
penyesuaian skor sesuai prioritas rekruter, seperti penekanan pada pengalaman
kerja. Namun, perlu dicatat bahwa bobot per section di penelitian ini hanya
didasarkan pada satu ahli yang mungkin tidak mencerminkan variasi preferensi
rekruter dari berbagai industri atau budaya instansi terkait. Pemberian bobot
dengan melibatkan lebih banyak ahli akan meningkatkan hasil secara general.
Melihat lebih dekat setiap kualifikasi lowongan kerja, ketiga parameter dibuat
grafik garis, dengan parameter korelasi diwarnai biru, parameter relevansi
diwarnai hijau, dan paremeter senioritas diwarnai merah. Sumbu Y menunjukkan
nilai, sehingga nilai persentase relevansi dan senioritas dijadikan bilangan desimal.
Sumbu X menunjukkan pendekatan dan skenario yang digunakan. Grafik untuk
beberapa kualifikasi lowongan kerja tertera pada Gambar 6.10.

# 162
Gambar 6.10 Grafik garis tiga parameter setiap kualifikasi lowongan kerja
Nilai korelasi pada lowongan kerja posisi “Executive Chef” memiliki nilai
tertinggi 0,5 dan terlihat jauh di bawah nilai relevansi dan senioritasnya. Nilai
korelasi tertinggi tersebut tergolong sedang. Sementara itu, nilai korelasi lainnya
bernilai negatif dan tergolong sebagai korelasi sangat lemah. Hal ini menunjukkan
walaupun korelasi antara hasil implementasi dengan hasil evaluasi ahli tergolong
lemah, keluaran resume yang dihasilkan untuk posisi ini tetap sesuai dengan
deskripsi kualifikasi lowongan kerja berdasarkan kesesuaian kata kunci atau
istilah-istilah tertentu yang dimiliki resume maupun pada kebutuhan posisi.
Nilai korelasi pada posisi “Medical Doctor” cukup stabil dengan rata-rata

# ,2833 di antara berbagai implementasi pendekatan dan skenario, meskipun
tergolong sebagai korelasi lemah. Namun, nilai relevansi menunjukkan 0 yang
menandakan tidak ada resume yang isiannya sesuai dengan kebutuhan posisi
tersebut. Hal ini menunjukkan perlu adanya penyesuaian dataset resume dengan
menambahkan resume yang mencakup beragam spesialisasi dalam industri
healthcare atau sebaliknya dengan memperkaya dataset kualifikasi lowongan
kerja di industri healthcare yang lebih variatif spesialisasinya.
Nilai korelasi pada posisi “Unmanaged Merchant Engagement Senior
Associate, BPO Field Sales” tergolong korelasi sedang ke korelasi kuat berdasarkan
nilai rata-rata 0,5667 dan nilai tertinggi 0,7. Namun, untuk nilai senioritasnya
memiliki rata-rata 0,3667 atau sekitar 36%. Hal ini menunjukkan kurang
mampunya hasil implementasi dalam mengenali kesuaian level senioritas dengan
yang dibutuhkan pada posisi tersebut. Sehingga, perlu adanya penyesuaian
dataset resume maupun kualifikasi lowongan kerja yang lebih beragam level
senioritasnya atau pengelompokkan terpisah berdasarkan level senioritas
berdasarkan years of experience di dalam resume.

# 163
Nilai korelasi pada posisi “HR Specialist” tergolong korelasi sedang ke korelasi
kuat berdasarkan nilai rata-rata 0,5333 dan nilai tertinggi 0,8. Namun, untuk nilai
relevansinya memiliki rata-rata 0,3667 atau sekitar 36%. Hal ini menunjukkan
kurang mampunya hasil implementasi dalam mengenali kesesuaian kata kunci
atau istilah dengan yang dibutuhkan pada posisi tersebut. Sehingga, perlu adanya
penyesuaian dataset resume maupun kualifikasi lowongan kerja yang
memperbanyak kata-kata penting seperti kata kunci atau istilah teknis sesuai
industri atau bidang minat.

# 164
# BAB 7 PENUTUP
Pada bab penutup, bagian kesimpulan merangkum hasil penelitian untuk
menjawab rumusan masalah. Sedangkan, bagian saran memberikan masukan
untuk perbaikan dan pengembangan penelitian selanjutnya.

## Kesimpulan
Berikut merupakan kesimpulan dari penelitian ini untuk menjawab rumusan
masalah.

# Hasil pemeringkatan lima resume menggunakan Improved Sqrt-Cosine
(ISC) Similarity dalam mengkalkulasikan similaritas teks resume dengan
kualifikasi lowongan kerja menunjukkan bahwa pendekatan representasi
teks menggunakan Word2Vec lebih unggul dibandingkan dengan TF-IDF
untuk skenario “Tanpa Bobot”. Meskipun terdapat distorsi akibat
penyesuaian nilai absolut, mengingat adanya term yang jarak posisinya
sudah dekat dan menjadi semakin dekat, Word2Vec cukup mampu
menangkap hubungan semantik kata kunci. Pada skenario “Dengan
Bobot”, pendekatan perhitungan similaritas menggunakan Cosine
Similarity (CosSim) dengan representasi teks Word2Vec lebih unggul.
Namun, dalam penggunaan ISC, representasi teks Word2Vec tetap unggul
dibandingkan TF-IDF. Keunggulan Word2Vec dengan CosSim menunjukkan
bahwa pendekatan ini paling selaras dengan pandangan manusia karena
CosSim menjaga hubungan semantik asli vektor Word2Vec tanpa distorsi
akibat penyesuaian nilai absolut dan memungkinan penyesuaian bobot per
section sesuai prioritas seorang ahli dalam penelitian ini.

# Korelasi peringkat antara hasil pemeringkatan dari ISC dengan penilaian
ahli terhadap kesesuaian kualifikasi lowongan kerja menunjukkan
keunggulan yang bervariasi berdasarkan representasi teks dan skenario, di
mana pada skenario “Tanpa Bobot”, Word2Vec dengan ISC lebih unggul
menghasilkan pemeringkatan lima resume yang sesuai dengan hasil
evaluasi pemeringkatan ahli terhadap deskripsi lowongan kerja (SRCC >

# ,6). Kemudian, pada skenario “Dengan Bobot”, Word2Vec dengan CosSim
lebih unggul dalam menghasilkan pemeringkatan yang sesuai dengan
evaluasi ahli. Walaupun begitu, Word2Vec dengan ISC pada skenario tanpa
bobot section, memiliki nilai korelasi rata-rata 0,269565 yang
dikategorikan sebagai korelasi lemah. Pada skenario dengan bobot
section, Word2Vec dengan CosSim memiliki nilai korelasi rata-rata

# ,183333 yang dikategorikan sebagai korelasi sangat lemah.
# 165
## Saran
Berikut merupakan saran dari penelitian ini untuk penelitian berikutnya.

# Pemberian bobot per section berdasarkan penilaian seorang ahli dapat
menimbulkan bias, sehingga kurang mencerminkan variasi preferensi
rekruter pada umumnya. Pada penelitian selanjutnya, disarankan untuk
melibatkan lebih banyak ahli.

# Meskipun implementasi Improved Sqrt-Cosine (ISC) Similarity dengan
representasi teks Word2Vec unggul karena masih cukup mampu
menangkap hubungan semantik kata kunci, tetap kurang disarankan
karena mengaburkan hubungan semantik asli. Jika berpacu pada seberapa
relevan isian resume dengan kualifikasi lowongan kerja, maka
implementasi ISC dengan TF-IDF lebih disarankan untuk digunakan.

# Jumlah kualifikasi lowongan kerja dengan parameter-parameter yang di
atas ambang batas rata-rata lebih sedikit dibandingkan yang di bawah
ambang batas. Oleh karena itu, penelitian selanjutnya disarankan
mencantumkan kata-kata teknis spesifik terkait suatu posisi pada deskripsi
kualifikasi lowongan kerja agar deskripsi yang digunakan tidak terlalu
umum.

# Penelitian ini berfokus pada peringkat sebagai parameter utama,
parameter relevansi dan senioritas ditambahkan sebagai parameter
pendukung. Untuk penelitian selanjutnya, disarankan menganalisa
hubungan parameter peringkat dengan parameter relevansi dan
senioritas.

# Pemrosesan kata untuk mengelompokkan tingkat senioritas pada setiap
resume menjadi entry level, junior level, dan management level dapat
meningkatkan kesesuaian resume-resume dari keluaran implementasi
metode dengan tingkat senioritas yang dibutuhkan sesuai deskripsi
kualifikasi lowongan kerja.

# Pemrosesan ekstraksi section pada penelitian ini memanfaatkan kolom
Resume_html yang merupakan fitur asli dari dataset resume. Untuk
penelitian selanjutnya, disarankan mengembangkan proses ekstraksi
section tanpa memanfaatkan class dari struktur HTML.

# Penyeragaman nama-nama section pada penelitian ini dilakukan secara
manual. Untuk penelitian selanjutnya, disarankan mengembangkan proses
penyeragaman nama-nama section secara semantik.

# Penelitian ini hanya menggunakan dataset resume dan kualifikasi
lowongan kerja dengan Bahasa Inggris. Untuk penelitian selanjutnya,
disarankan mengembangkan dataset resume dan kualifikasi lowongan
kerja dengan Bahasa Indonesia.

# 166
# DAFTAR REFERENSI
Abdusyukur, F., 2023. PENERAPAN ALGORITMA SUPPORT VECTOR MACHINE
(SVM) UNTUK KLASIFIKASI PENCEMARAN NAMA BAIK DI MEDIA SOSIAL
TWITTER. KOMPUTA : Jurnal Ilmiah Komputer dan Informatika, 12(1), pp. 73-

# 82
Alsharef, A., Sonia, Nassour, H. & Sharma, J., 2023. Exploring the Efficiency of Text-
Similarity Measures in Automated Resume Screening for Recruitment. New
Delhi, India, IEEE, pp. 36-42.
Amin, M. D. et al., 2023. Real Time Data based Automated Resume Classification
and Job Matching using SVC, Jaccard Index and Cosine Similarity. Roorkee,
India, IEEE, pp. 1-6.
Ayuningtyas, P. & Tantyoko, H., 2024. Perbandingan Metode Word2vec Model
Skipgram pada Ulasan Aplikasi Linkaja menggunakan Algoritma Bidirectional
LSTM dan Support Vector Machine. JUSTIN (Jurnal Sistem dan Teknologi
Informasi), 12(1), pp. 189-196.
Badan Pengembangan dan Pembinaan Bahasa, Kementerian Pendidikan,
Kebudayaan, Riset, dan Teknologi Republik Indonesia, 2016. KBBI VI Daring.
[Online]
Tersedia di: <https://kbbi.kemdikbud.go.id/entri/resume>
Bhawal, S., 2021. Kaggle. [Online]
Tersedia di: <https://www.kaggle.com/datasets/snehaanbhawal/resume-
dataset>
Cambridge University Press & Assessment, 2024. Meaning of curriculum vitae in
English. [Online]
Tersedia di: <https://dictionary.cambridge.org/dictionary/essential-british-
english/curriculum-vitae>
Cholissodin, I. & Riyandani, E., 2018. Big Data vs Big Information vs Big Knowledge.
Malang: Fakultas Ilmu Komputer Universitas Brawijaya.
Cowley, H. P. et al., 2022. A framework for rigorous evaluation of human
performance in human and machine learning comparison studies. Scientific
Reports, 12(5444).
Daryani, C. et al., 2020. AN AUTOMATED RESUME SCREENING SYSTEM USING
NATURAL LANGUAGE PROCESSING AND SIMILARITY. Ethics and Information
Technology (ETIT), 2(2), pp. 99-103.
Dewan Perwakilan Rakyat Republik Indonesia - Komisi IX, 2023. Tingkat
Pengangguran Terbuka Masih Jauh di Atas Target RPJMN. [Online]

## Tersedia di
<https://www.dpr.go.id/berita/detail/id/47507/t/Tingkat%20Pengangguran
%20Terbuka%20Masih%20Jauh%20di%20Atas%20Target%20RPJMN>

# 167
Dwivedi, A. & Anand, S. K., 2023. Word Embedding using Skip Gram Approach.
Interdisciplinary Journal of Contemporary Research, 10(3), pp. 1-5.
Effendi, M. S., 2013. Desain Eksperimental dalam Penelitian Pendidikan. Jurnal
Perspektif Pendidikan, 6(1), pp. 87-102.
Guritno, S., S. & Rahardja, U., 2011. Theory and Application of IT RESEARCH.
Penerbit Andi.
He, Z., Dumdumaya, C. E. & Quimno, V. A., 2024. MEASUREMENT OF SEMANTIC
TEXT SIMILARITY. Journal of Theoretical and Applied Information
Technology, 102(5), pp. 1673-1685.
H. & H., 2024. SPEARMAN'S RANK CORRELATION ANALYSIS METHOD TO IDENTIFY
CHANGES IN THE GPA OF GRADUATES FROM THE 5TH BATCH OF THE

# TEACHING CAMPUS PROGRAM AT UNIVERSITAS BAKTI INDONESIA.
TRANSPUBLIKA INTERNATIONAL RESEARCH IN EXACT SCIENCES (TIRES), 30 8,

# (3), pp. 18-27.
International Monetary Fund, 2024. World Economic Outlook (April 2024) -
Unemployment Rate. [Online]

## Tersedia di
<https://www.imf.org/external/datamapper/LUR@WEO/OEMDC/ADVEC/

# WEOWORLD/DA>
Iskandar, D. & Kurniawan, A., 2025. ANALISIS PERBANDINGAN TEKNIK WORD2VEC

# DAN DOC2VECDALAM MENGUKUR KEMIRIPAN DOKUMEN MENGGUNAKAN
COSINE SIMILARITY. Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK),

# (1), pp. 133-144.
Jawale, D. S. et al., 2024. COSINE SIMILARITY: A KEY DRIVER FOR ENHANCED
RECOMMENDATION SYSTEMS. International Research Journal of
Modernization in Engineering Technology and Science, 06(04), pp. 1466-

# 1470
Kementerian Ketenagakerjaan RI - Badan Perencanaan dan Pengembangan
Ketenagakerjaan, 2021. REVIEW RENCANA TENAGA KERJA NASIONAL 2020-

# [Online]
Tersedia di: <https://satudata.kemnaker.go.id/satudata-
public/2022/04/files/publikasi/1649938621648_Buku%2520Review%2520R
TKN_2020_2024.pdf>
Kulshretha, S. & Lodha, L., 2023. Performance Evaluation of Word Embedding
Algorithms. International Journal of Innovative Science and Research
Technology, 8(12), pp. 1555-1561.
Kumaladewi, A. K., 2018. EFEKTIVITAS REKRUTMEN DAN SELEKSI DALAM

# MEMENUHI KEBUTUHAN TENAGA PERAWAT DI RSIA MUSLIMAT JOMBA.
PARSIMONIA Jurnal Akuntansi, Manajemen, dan Bisnis, 11 4, 5(1), pp. 29-40.
Lailasari, N. A. et al., 2024. Pengaruh Pengangguran Terhadap Pertumbuhan
Ekonomi. IJM: Indonesian Journal of Multidisciplinary, 2(5), pp. 275-286.

# 168
Musfiqon, 2016. Panduan Lengkap Metodologi Penelitian Pendidikan. PT. Prestasi
Pustakaraya.
Meyer, D., 2016. How exactly does word2vec work?
P, A., K, A. K., Bharadwaj, S. K. & Venugopalan, M., 2024. Semantic Similarity
Analysis for Resume Filtering using PySpark. Pune, India, IEEE, pp. 1-5
Prasetya, D. D., Wibawa, A. P. & Hirashima, T., 2018. The performance of text
similarity algorithms. International Journal of Advances in Intelligent
Informatics, 4(1), pp. 63-69.
Prasetya, M. A., Wulandari, M. & Nikmah, S. A., 2024. Implementasi NLP(Natural
Language Processing) Dasar pada Analisis Sentiment Review Spotify.
PROSIDING SEMINAR NASIONAL TEKNOLOGI DAN SAINS TAHUN 2024, pp.

# 153.
Pundir, R. S. et al., 2024. Enhancing Resume Recommendation System through
Skill-based Similarity using Deep Learning Models.
Ramadhan, R. F., Wijoyo, S. H. & Saputra, M. C., 2023. Penerapan Metode K-Means
Clustering pada Ulasan Perumahan PT XYZ di Google Maps untuk Formulasi
Strategi Bisnis dengan Analisis SWOT. Jurnal Pengembangan Teknologi
Informasi dan Ilmu Komputer, 7(6), pp. 2879-2888.
Řehůřek, R., 2024. Word2vec embeddings. [Online]
Tersedia di: <https://radimrehurek.com/gensim/models/word2vec.html>
scikit-learn developers, 2025. User Guide. [Online]
Tersedia di: <https://scikit-
learn.org/stable/modules/feature_extraction.html#text-feature-extraction>
Septiani, D. & Isabela, I., 2022. ANALISIS TERM FREQUENCY INVERSE DOCUMENT
FREQUENCY (TF-IDF). SINTESIA: Jurnal Sistem dan Teknologi Informasi
Indonesia, 01(2), pp. 81-88.
Sihombing, D. O., 2022. Implementasi Natural Language Processing (NLP) dan
Algoritma Cosine Similarity dalam Penilaian Ujian Esai Otomatis. Jurnal
Sistem Komputer dan Informatika (JSON), 4(2), pp. 396-406.
Sohangir, S. & Wang, D., 2017. Improved sqrt-cosine similarity measurement.
Journal of Big Data, 4(25), pp. 1-13.
Stanford Career Education, 2018. Pursuing Meaningful Work: A Strategies Guide
for PhDs and Postdocs. [Online]

## Tersedia di
<https://careered.stanford.edu/sites/g/files/sbiybj22801/files/media/file/st
anfordphd_pmw_18-19.pdf>
Stanford Career Education, 2024. Steps to Writing Your Resume. [Online]
Tersedia di: <https://careered.stanford.edu/resources/resources-
links#resume>

# 169
Suningsih, S. et al., 2024. Pelatihan Pembuatan Curriculum Vitae dalam Bahasa
Inggris yang Berbasis Application Tracking System. Jurnal Nusantara
Mengabdi, 3(2), pp. 85-93.
Temizhan, E., Mirtagioglu, H. & Mendes, M., 2022. Which Correlation Coefficient
Should Be Used for Investigating Relations between Quantitative Variables?.
American Academic Scientific Research Journal for Engineering, Technology,
and Sciences, 85(1), pp. 265-277.
Titisari, M. & Ikhwan, K., 2021. Proses Rekrutmen dan Seleksi: Potensi
Ketidakefektifan dan Faktornya. JMK (Jurnal Manajemen dan
Kewirausahaan), 6(3), pp. 11-27.
Wujarso, R., 2022. PERAN HUMAN CAPITAL DALAM PERTUMBUHAN EKONOMI.
Journal of Information System, Applied, Management, Accounting and
Research, 6(2), pp. 430-438.

# 170
# LAMPIRAN A SURAT PERNYATAAN VALIDITAS
# 171
# LAMPIRAN B BOBOT PER SECTION BERDASARKAN
# INDUSTRI
# 172
# 173
# 174
# 175
# 176
# 177
# 178
# 179
# LAMPIRAN C HASIL PEMERINGKATAN LIMA RESUME PER
# KUALIFIKASI LOWONGAN KERJA
# 1 Tanpa Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority

## Score Expert
# 38688388 Business 0,1919605 3 TRUE FALSE
## Developm 416
ent

## Executive
# 31638814 Business 0,1863253 2 TRUE FALSE
## Developm 744
ent

## Executive
# 18311419 Business 0,1783844 5 TRUE FALSE
## Developm 987
ent

## Executive
# 15535920 Business 0,1708420 1 TRUE FALSE
## Developm 879
ent

## Executive
# 17132168 Business 0,1682773 4 TRUE FALSE
## Developm 892
ent

## Executive
# 26932091 CLUB 0,1871587 5 TRUE TRUE
# GENERAL 776
# MANAGE
# R
# 17818707 CLUB 0,1794173 2 TRUE TRUE
# GENERAL 858
# MANAGE
# R
# 15535920 CLUB 0,1714170 4 TRUE TRUE
# GENERAL 333
# MANAGE
# R
# 38688388 CLUB 0,1605149 3 TRUE TRUE
# GENERAL 45
# MANAGE
# R
# 180
# 25162378 CLUB 0,1561663 1 TRUE TRUE
# GENERAL 095
# MANAGE
# R
# 27246366 Construct 0,2309432 2 TRUE TRUE
ion 449

## Superviso
r

# 39027764 Construct 0,2258310 1 TRUE TRUE
ion 516

## Superviso
r

# 12839152 Construct 0,2158709 3 TRUE TRUE
ion 047

## Superviso
r

# 22718826 Construct 0,2089757 4 TRUE FALSE
ion 732

## Superviso
r

# 26994282 Construct 0,1991065 5 FALSE TRUE
ion 198

## Superviso
r

# 68781345 Creative 0,1449183 3 TRUE TRUE
Director / 029

## Manager
# 13964744 Creative 0,1365746 5 FALSE FALSE
Director / 594

## Manager
# 308648 Creative 0,1303657 1 TRUE TRUE
# Director / 835
## Manager
# 17781039 Creative 0,1282461 4 FALSE FALSE
Director / 853

## Manager
# 22706174 Creative 0,1264199 2 TRUE TRUE
Director / 202

## Manager
# 22754014 Digital 0,1351744 4 FALSE TRUE
and Social 084

## Media
## Executive
# 181
# 16620172 Digital 0,1303300 1 TRUE TRUE
and Social 184

## Media
## Executive
# 18905648 Digital 0,1297599 5 FALSE TRUE
and Social

## Media
## Executive
# 18927233 Digital 0,1290032 3 TRUE FALSE
and Social 048

## Media
## Executive
# 16536141 Digital 0,1178854 2 TRUE FALSE
and Social 437

## Media
## Executive
# 14937492 Digital 0,1692186 4 FALSE FALSE
## Banking 127
## Officer
# 27080812 Digital 0,1653474 3 FALSE FALSE
## Banking 431
## Officer
# 26932091 Digital 0,1628028 5 FALSE FALSE
## Banking 08
## Officer
# 22423839 Digital 0,1595269 1 FALSE FALSE
## Banking 82
## Officer
# 25038571 Digital 0,1542614 2 FALSE FALSE
## Banking 74
## Officer
# 34252537 Executive 0,2393743 1 TRUE TRUE
## Chef 131
# 29775391 Executive 0,2362169 4 TRUE TRUE
## Chef 724
# 10653119 Executive 0,2324195 2 TRUE TRUE
## Chef 106
# 25924968 Executive 0,2310007 5 TRUE TRUE
## Chef 976
# 16924102 Executive 0,2229271 3 TRUE TRUE
## Chef 471
# 182
# 21338490 Finance 0,2365662 5 TRUE FALSE
## Executive 907
/

## Accounta
nt

# 25846894 Finance 0,2339642 4 TRUE FALSE
## Executive 328
/

## Accounta
nt

# 25862026 Finance 0,1916905 3 TRUE TRUE
## Executive 061
/

## Accounta
nt

# 29999135 Finance 0,1887091 1 TRUE TRUE
## Executive 447
/

## Accounta
nt

# 28969385 Finance 0,1883069 2 TRUE TRUE
## Executive 276
/

## Accounta
nt

# 23734441 Finance 0,2471592 3 TRUE TRUE
Officer ( 921
Jr/Sr.)

# 28298773 Finance 0,2255675 1 TRUE TRUE
Officer ( 767
Jr/Sr.)

# 29999135 Finance 0,2112704 2 TRUE TRUE
Officer ( 543
Jr/Sr.)

# 53640713 Finance 0,1999300 4 TRUE FALSE
Officer ( 064
Jr/Sr.)

# 21338490 Finance 0,1984463 5 TRUE FALSE
Officer ( 036
Jr/Sr.)

# 38946032 Financial 0,1817793 4 TRUE TRUE
## Consolida 037
tion

# 183
## Consultan
t

# 70541112 Financial 0,1811155 1 TRUE TRUE
## Consolida 551
tion

## Consultan
t

# 213384 Financial 0,1745877 5 TRUE TRUE
# Consolida 097
tion

## Consultan
t

# 29821051 Financial 0,1730965 2 TRUE TRUE
## Consolida 599
tion

## Consultan
t

# 25862026 Financial 0,1725639 3 TRUE TRUE
## Consolida 591
tion

## Consultan
t

# 18354623 Graphics 0,2102328 4 TRUE FALSE
## Designer 956
# 18460045 Graphics 0,1993908 2 TRUE TRUE
## Designer 853
# 20210676 Graphics 0,1793144 5 FALSE FALSE
## Designer 558
# 22560013 Graphics 0,1749108 1 TRUE TRUE
## Designer 248
# 26046064 Graphics 0,1747824 3 TRUE TRUE
## Designer 455
# 30862904 HR 0,2428395 1 TRUE TRUE
## Specialist 272
# 24508725 HR 0,2396608 2 TRUE TRUE
## Specialist 996
# 16877897 HR 0,2301432 5 FALSE TRUE
## Specialist 719
# 11480899 HR 0,2216053 3 FALSE TRUE
## Specialist 793
# 53701275 HR 0,2189996 4 FALSE TRUE
## Specialist 296
# 184
# 39413067 INFORMA 0,2356860 1 TRUE TRUE
# TION & 514
# TECHNOL
# OGY
# STAFF
# 17983957 INFORMA 0,2273222 4 FALSE FALSE
# TION & 616
# TECHNOL
# OGY
# STAFF
# 91635250 INFORMA 0,2184461 3 TRUE FALSE
# TION & 588
# TECHNOL
# OGY
# STAFF
# 15535920 INFORMA 0,2094339 5 FALSE FALSE
# TION & 334
# TECHNOL
# OGY
# STAFF
# 36434348 INFORMA 0,1971253 2 TRUE FALSE
# TION & 698
# TECHNOL
# OGY
# STAFF
# 36671891 Junior 0,1206467 3 FALSE FALSE
## Associate 025
## Lawyer
# 19557384 Junior 0,1203686 4 FALSE FALSE
## Associate 863
## Lawyer
# 10332998 Junior 0,1195592 1 TRUE TRUE
## Associate 716
## Lawyer
# 15100547 Junior 0,1180229 2 TRUE TRUE
## Associate 251
## Lawyer
# 11065180 Junior 0,1170764 5 FALSE FALSE
## Associate 78
## Lawyer
# 23719943 Junior 0,1771679 2 TRUE FALSE
## Designer 315
for

## Apparel
# 185
# 15746146 Junior 0,1627493 1 TRUE TRUE
## Designer 142
for

## Apparel
# 26503829 Junior 0,1479395 3 TRUE FALSE
## Designer 386
for

## Apparel
# 12122372 Junior 0,1410829 4 FALSE FALSE
## Designer 334
for

## Apparel
# 26932091 Junior 0,1367025 5 FALSE FALSE
## Designer 452
for

## Apparel
# 26932091 Manager 0,2015879 5 FALSE FALSE
## Aviation 825
Safety,

## Quality
and

## Security
# 11169163 Manager 0,2013763 2 TRUE TRUE
## Aviation 559
Safety,

## Quality
and

## Security
# 19796840 Manager 0,2010987 4 FALSE FALSE
## Aviation 541
Safety,

## Quality
and

## Security
# 28186635 Manager 0,1877334 3 TRUE FALSE
## Aviation 005
Safety,

## Quality
and

## Security
# 28383893 Manager 0,1862704 1 TRUE TRUE
## Aviation 602
Safety,

## Quality
# 186
and

## Security
# 16356151 Medical 0,2157386 1 FALSE TRUE
## Doctor 58
# 13565152 Medical 0,1875315 5 FALSE FALSE
## Doctor 396
# 17818707 Medical 0,1628595 4 FALSE FALSE
## Doctor 03
# 12544735 Medical 0,1595774 2 FALSE FALSE
## Doctor 142
# 43994605 Medical 0,1595204 3 FALSE FALSE
## Doctor 988
# 77828437 Productio 0,1264697 1 TRUE TRUE
n 128

## Engineeri
ng

# 55595908 Productio 0,1201321 5 FALSE FALSE
n 813

## Engineeri
ng

# 28803888 Productio 0,1154167 3 TRUE FALSE
n 25

## Engineeri
ng

# 30288581 Productio 0,1118393 4 FALSE FALSE
n 979

## Engineeri
ng

# 86828820 Productio 0,1101805 2 FALSE FALSE
n 298

## Engineeri
ng

# 21297828 Public 0,1907608 3 TRUE TRUE
## Relations 096
## Officer
# 13129275 Public 0,1802253 5 FALSE TRUE
## Relations 973
## Officer
# 28290448 Public 0,1736107 2 TRUE TRUE
## Relations 376
## Officer
# 187
# 31220062 Public 0,1732900 4 FALSE TRUE
## Relations 471
## Officer
# 20210676 Public 0,1725535 1 TRUE TRUE
## Relations 861
## Officer
# 26888302 Quality 0,1252811 2 FALSE TRUE
## Control 704
## Superviso
r - Corn

## Commodi
ty

# 26932091 Quality 0,1239398 4 FALSE TRUE
## Control 512
## Superviso
r - Corn

## Commodi
ty

# 20905088 Quality 0,1106055 3 FALSE FALSE
## Control 359
## Superviso
r - Corn

## Commodi
ty

# 28020046 Quality 0,1081390 1 FALSE TRUE
## Control 286
## Superviso
r - Corn

## Commodi
ty

# 22861181 Quality 0,1069757 5 FALSE FALSE
## Control 33
## Superviso
r - Corn

## Commodi
ty

# 26932091 Regional 0,2134135 5 FALSE TRUE
## Sales 079
## Manager
# 25038571 Regional 0,2032024 2 TRUE TRUE
## Sales 859
## Manager
# 27080812 Regional 0,2029929 3 FALSE TRUE
## Sales 331
## Manager
# 188
# 38688388 Regional 0,1964119 4 FALSE FALSE
## Sales 402
## Manager
# 17818707 Regional 0,1949221 1 TRUE TRUE
## Sales 894
## Manager
# 35474904 Spare part 0,1420329 5 FALSE FALSE
## Admin 913
# 22861181 Spare part 0,1379583 4 FALSE FALSE
## Admin 676
# 19473948 Spare part 0,1371374 1 FALSE TRUE
## Admin 364
# 71772815 Spare part 0,1371227 2 FALSE TRUE
## Admin 976
# 24670867 Spare part 0,1369340 3 FALSE FALSE
## Admin 491
# 15850434 Teachers 0,2201057 2 TRUE TRUE
# 854
# 96547039 Teachers 0,1978795 1 TRUE TRUE
# 776
# 28772892 Teachers 0,1889872 3 TRUE TRUE
# 465
# 58105060 Teachers 0,1869135 5 TRUE TRUE
# 69
# 37220856 Teachers 0,1804859 4 FALSE TRUE
# 322
# 26932091 Unmanag 0,2280308 1 TRUE TRUE
ed 996

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 68781345 Unmanag 0,2043528 5 FALSE FALSE
ed 088

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 189
# 17818707 Unmanag 0,1783846 4 FALSE FALSE
ed 929

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 27884470 Unmanag 0,1726401 3 FALSE FALSE
ed 754

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 38688388 Unmanag 0,1670092 2 TRUE FALSE
ed 401

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 2 Tanpa Bobot - Word2Vec dan Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority

## Score Expert
# 26932091 Business 0,8910836 4 TRUE FALSE
## Developm 577
ent

## Executive
# 10464113 Business 0,8697264 3 TRUE FALSE
## Developm 314
ent

## Executive
# 13352113 Business 0,8397827 5 TRUE TRUE
## Developm 595
ent

## Executive
# 17132168 Business 0,8354100 1 TRUE TRUE
## Developm 585
ent

## Executive
# 190
# 27715131 Business 0,8342830 2 TRUE FALSE
## Developm 539
ent

## Executive
# 26932091 CLUB 0,8795587 5 FALSE FALSE
# GENERAL 818
# MANAGE
# R
# 10464113 CLUB 0,8576420 4 FALSE FALSE
# GENERAL 188
# MANAGE
# R
# 13411858 CLUB 0,8569679 3 FALSE FALSE
# GENERAL 499
# MANAGE
# R
# 27715131 CLUB 0,8542478 2 FALSE TRUE
# GENERAL 204
# MANAGE
# R
# 12938389 CLUB 0,8491947 1 TRUE TRUE
# GENERAL 293
# MANAGE
# R
# 27246366 Construct 0,8558241 1 TRUE TRUE
ion 725

## Superviso
r

# 39027764 Construct 0,8522567 4 TRUE FALSE
ion 153

## Superviso
r

# 26932091 Construct 0,8479026 5 FALSE FALSE
ion 556

## Superviso
r

# 16203589 Construct 0,8425265 3 FALSE TRUE
ion 431

## Superviso
r

# 12839152 Construct 0,8412288 2 TRUE TRUE
ion 904

## Superviso
r

# 191
# 13115648 Creative 0,8481530 3 FALSE FALSE
Director / 845

## Manager
# 81508860 Creative 0,8427884 1 TRUE TRUE
Director / 43

## Manager
# 129383 Creative 0,8389229 4 FALSE FALSE
# Director / 774
## Manager
# 23917826 Creative 0,8372398 2 FALSE FALSE
Director / 466

## Manager
# 24588864 Creative 0,8319416 5 FALSE FALSE
Director / 642

## Manager
# 18905648 Digital 0,8833178 4 FALSE TRUE
and Social 282

## Media
## Executive
# 18354623 Digital 0,8470618 2 TRUE FALSE
and Social 427

## Media
## Executive
# 70750649 Digital 0,8403711 1 TRUE FALSE
and Social 468

## Media
## Executive
# 26932091 Digital 0,8330877 5 FALSE FALSE
and Social 423

## Media
## Executive
# 22754014 Digital 0,8241794 3 FALSE TRUE
and Social 109

## Media
## Executive
# 26932091 Digital 0,8829766 4 FALSE TRUE
## Banking 711
## Officer
# 98379112 Digital 0,8419138 1 FALSE FALSE
## Banking 193
## Officer
# 192
# 26167298 Digital 0,8403331 3 FALSE FALSE
## Banking 637
## Officer
# 18824120 Digital 0,8402394 2 FALSE TRUE
## Banking 056
## Officer
# 10464113 Digital 0,8382170 5 FALSE TRUE
## Banking 916
## Officer
# 35579812 Executive 0,8825965 5 TRUE TRUE
## Chef 822
# 29775391 Executive 0,8810187 3 TRUE TRUE
## Chef 817
# 34252537 Executive 0,8682833 4 TRUE TRUE
## Chef 076
# 21060367 Executive 0,8642790 1 TRUE TRUE
## Chef 198
# 25924968 Executive 0,8607410 2 TRUE TRUE
## Chef 938
# 20393721 Finance 0,8786240 3 TRUE TRUE
## Executive 816
/

## Accounta
nt

# 23636277 Finance 0,8532985 2 TRUE TRUE
## Executive 747
/

## Accounta
nt

# 70541112 Finance 0,8524324 1 TRUE TRUE
## Executive 417
/

## Accounta
nt

# 22861181 Finance 0,8475373 5 FALSE FALSE
## Executive 387
/

## Accounta
nt

# 26695839 Finance 0,8448839 4 FALSE TRUE
## Executive 585
/

# 193
## Accounta
nt

# 20393721 Finance 0,8747340 3 TRUE FALSE
Officer ( 639
Jr/Sr.)

# 23734441 Finance 0,8486161 1 TRUE TRUE
Officer ( 629
Jr/Sr.)

# 27558837 Finance 0,8390957 2 TRUE TRUE
Officer ( 117
Jr/Sr.)

# 25497147 Finance 0,8381744 4 FALSE TRUE
Officer ( 027
Jr/Sr.)

# 53640713 Finance 0,8285536 5 FALSE TRUE
Officer ( 528
Jr/Sr.)

# 70541112 Financial 0,8601319 1 TRUE TRUE
## Consolida 313
tion

## Consultan
t

# 18365443 Financial 0,8497776 2 FALSE TRUE
## Consolida 538
tion

## Consultan
t

# 269320 Financial 0,8467198 4 FALSE TRUE
# Consolida 412
tion

## Consultan
t

# 26695839 Financial 0,8388730 5 FALSE FALSE
## Consolida 884
tion

## Consultan
t

# 19446337 Financial 0,8272504 3 FALSE TRUE
## Consolida 449
tion

## Consultan
t

# 18354623 Graphics 0,8890629 3 TRUE FALSE
## Designer 709
# 194
# 22754014 Graphics 0,8265473 2 TRUE TRUE
## Designer 545
# 70750649 Graphics 0,8213165 4 FALSE FALSE
## Designer 402
# 37664296 Graphics 0,8205203 1 TRUE TRUE
## Designer 891
# 22848179 Graphics 0,8096640 5 FALSE FALSE
## Designer 706
# 16877897 HR 0,9091145 2 FALSE TRUE
## Specialist 694
# 26932091 HR 0,8979627 5 FALSE FALSE
## Specialist 291
# 30862904 HR 0,8975547 1 TRUE TRUE
## Specialist 701
# 29134372 HR 0,8676508 3 FALSE FALSE
## Specialist 904
# 11289482 HR 0,8629413 4 FALSE FALSE
## Specialist 128
# 26932091 INFORMA 0,8692647 5 FALSE TRUE
# TION & 02
# TECHNOL
# OGY
# STAFF
# 28672970 INFORMA 0,8644542 3 TRUE FALSE
# TION & 694
# TECHNOL
# OGY
# STAFF
# 10840430 INFORMA 0,8521312 2 TRUE FALSE
# TION & 773
# TECHNOL
# OGY
# STAFF
# 11957080 INFORMA 0,8495982 1 TRUE TRUE
# TION & 438
# TECHNOL
# OGY
# STAFF
# 15535920 INFORMA 0,8477472 4 FALSE FALSE
# TION & 961
# TECHNOL
# OGY
# STAFF
# 195
# 81508860 Junior 0,8411479 5 FALSE FALSE
## Associate 443
## Lawyer
# 98379112 Junior 0,8350052 4 FALSE FALSE
## Associate 088
## Lawyer
# 18297650 Junior 0,8287451 1 FALSE FALSE
## Associate 416
## Lawyer
# 22485475 Junior 0,8282045 2 FALSE FALSE
## Associate 275
## Lawyer
# 16877897 Junior 0,8276658 3 FALSE FALSE
## Associate 654
## Lawyer
# 26932091 Junior 0,8629954 5 FALSE FALSE
## Designer 656
for

## Apparel
# 15154822 Junior 0,8216761 1 TRUE FALSE
## Designer 589
for

## Apparel
# 19195747 Junior 0,8122268 3 FALSE FALSE
## Designer 17
for

## Apparel
# 23719943 Junior 0,8101501 2 FALSE FALSE
## Designer 614
for

## Apparel
# 18354623 Junior 0,8057058 4 FALSE FALSE
## Designer 156
for

## Apparel
# 13195436 Manager 0,8760108 1 TRUE TRUE
## Aviation 203
Safety,

## Quality
and

## Security
# 11169163 Manager 0,8636670 2 TRUE TRUE
## Aviation 262
Safety,

# 196
## Quality
and

## Security
# 12654876 Manager 0,8354426 4 FALSE TRUE
## Aviation 771
Safety,

## Quality
and

## Security
# 35651876 Manager 0,8326146 3 FALSE FALSE
## Aviation 305
Safety,

## Quality
and

## Security
# 26932091 Manager 0,8321723 5 FALSE FALSE
## Aviation 739
Safety,

## Quality
and

## Security
# 25328428 Medical 0,8549853 2 FALSE FALSE
## Doctor 325
# 96260484 Medical 0,8511528 1 FALSE TRUE
## Doctor 522
# 37402097 Medical 0,8448984 5 FALSE FALSE
## Doctor 325
# 15958967 Medical 0,8384091 3 FALSE FALSE
## Doctor 616
# 12544735 Medical 0,8357500 4 FALSE FALSE
## Doctor 881
# 54100393 Productio 0,7940523 5 FALSE FALSE
n 922

## Engineeri
ng

# 30288581 Productio 0,7927010 2 FALSE FALSE
n 179

## Engineeri
ng

# 12011623 Productio 0,7900994 1 TRUE TRUE
n 569

## Engineeri
ng

# 197
# 37751611 Productio 0,7888528 4 FALSE FALSE
n 109

## Engineeri
ng

# 10751444 Productio 0,7884584 3 FALSE FALSE
n 188

## Engineeri
ng

# 28290448 Public 0,8557876 1 TRUE TRUE
## Relations 945
## Officer
# 70750649 Public 0,8394137 2 TRUE FALSE
## Relations 621
## Officer
# 22861181 Public 0,8321976 5 FALSE FALSE
## Relations 066
## Officer
# 22754014 Public 0,8313117 3 TRUE TRUE
## Relations 474
## Officer
# 18354623 Public 0,8215153 4 TRUE FALSE
## Relations 068
## Officer
# 26932091 Quality 0,8515201 5 FALSE TRUE
## Control 807
## Superviso
r - Corn

## Commodi
ty

# 35651876 Quality 0,8261224 2 FALSE FALSE
## Control 329
## Superviso
r - Corn

## Commodi
ty

# 12011623 Quality 0,8161604 3 FALSE FALSE
## Control 106
## Superviso
r - Corn

## Commodi
ty

# 26070334 Quality 0,8140973 1 FALSE TRUE
## Control 449
## Superviso
r - Corn

# 198
## Commodi
ty

# 26888302 Quality 0,8107827 4 FALSE FALSE
## Control 604
## Superviso
r - Corn

## Commodi
ty

# 26932091 Regional 0,9135585 3 FALSE TRUE
## Sales 03
## Manager
# 28867567 Regional 0,8628078 1 TRUE TRUE
## Sales 401
## Manager
# 12059198 Regional 0,8436546 2 FALSE TRUE
## Sales 087
## Manager
# 18368613 Regional 0,8355645 4 TRUE FALSE
## Sales 984
## Manager
# 23917826 Regional 0,8340500 5 FALSE TRUE
## Sales 742
## Manager
# 26932091 Spare part 0,8606192 5 FALSE TRUE
## Admin 668
# 22861181 Spare part 0,8554830 3 FALSE FALSE
## Admin 7
# 16378091 Spare part 0,8486716 1 FALSE TRUE
## Admin 747
# 23917826 Spare part 0,8374442 4 FALSE TRUE
## Admin 756
# 37764298 Spare part 0,8364215 2 FALSE TRUE
## Admin 493
# 28772892 Teachers 0,9286252 4 TRUE TRUE
# 558
# 15850434 Teachers 0,9054198 2 TRUE TRUE
# 861
# 54100393 Teachers 0,9002476 5 TRUE TRUE
# 335
# 37220856 Teachers 0,8955650 3 FALSE TRUE
# 21
# 199
# 96547039 Teachers 0,8829045 1 TRUE TRUE
# 147
# 26932091 Unmanag 0,9265301 1 TRUE TRUE
ed 426

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 11289482 Unmanag 0,8595816 2 TRUE FALSE
ed 135

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 16877897 Unmanag 0,8374321 5 FALSE FALSE
ed 014

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 30862904 Unmanag 0,8252724 4 FALSE FALSE
ed 558

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 12938389 Unmanag 0,8237882 3 FALSE FALSE
ed 972

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 200
# 3 Tanpa Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority

## Score Expert
# 26932091 Business 0,9526863 2 TRUE FALSE
## Developm 545
ent

## Executive
# 10464113 Business 0,9469295 5 FALSE TRUE
## Developm 215
ent

## Executive
# 27715131 Business 0,9431682 4 TRUE FALSE
## Developm 632
ent

## Executive
# 91467795 Business 0,9431253 1 TRUE TRUE
## Developm 452
ent

## Executive
# 17132168 Business 0,9415056 3 TRUE TRUE
## Developm 337
ent

## Executive
# 26932091 CLUB 0,9499713 1 TRUE TRUE
# GENERAL 215
# MANAGE
# R
# 10464113 CLUB 0,9470196 5 FALSE FALSE
# GENERAL 187
# MANAGE
# R
# 13411858 CLUB 0,9465261 4 FALSE TRUE
# GENERAL 069
# MANAGE
# R
# 27715131 CLUB 0,9463747 3 FALSE TRUE
# GENERAL 964
# MANAGE
# R
# 12938389 CLUB 0,9449584 2 FALSE TRUE
# GENERAL 126
# MANAGE
# R
# 201
# 39027764 Construct 0,9464103 4 TRUE FALSE
ion 571

## Superviso
r

# 27246366 Construct 0,9418411 2 TRUE TRUE
ion 329

## Superviso
r

# 12839152 Construct 0,9405705 1 TRUE TRUE
ion 386

## Superviso
r

# 26932091 Construct 0,9388270 5 FALSE TRUE
ion 484

## Superviso
r

# 10176013 Construct 0,9355313 3 TRUE TRUE
ion 332

## Superviso
r

# 22861181 Creative 0,9488284 2 FALSE TRUE
Director / 06

## Manager
# 13115648 Creative 0,9476442 5 FALSE FALSE
Director / 985

## Manager
# 815088 Creative 0,9465295 1 TRUE TRUE
# Director / 591
## Manager
# 16899268 Creative 0,9464348 3 FALSE TRUE
Director / 445

## Manager
# 26932091 Creative 0,9457878 4 FALSE TRUE
Director / 553

## Manager
# 18905648 Digital 0,9541787 1 TRUE TRUE
and Social 533

## Media
## Executive
# 70750649 Digital 0,9476443 3 TRUE FALSE
and Social 214

## Media
## Executive
# 202
# 18354623 Digital 0,9467136 2 TRUE FALSE
and Social 247

## Media
## Executive
# 34712719 Digital 0,9436558 5 FALSE TRUE
and Social 5

## Media
## Executive
# 14304010 Digital 0,9412760 4 TRUE TRUE
and Social 663

## Media
## Executive
# 26932091 Digital 0,9548594 4 FALSE FALSE
## Banking 827
## Officer
# 18905648 Digital 0,9489372 2 FALSE FALSE
## Banking 807
## Officer
# 13352113 Digital 0,9462483 3 FALSE TRUE
## Banking 878
## Officer
# 10464113 Digital 0,9460302 5 FALSE TRUE
## Banking 848
## Officer
# 15423153 Digital 0,9442921 1 FALSE TRUE
## Banking 952
## Officer
# 35579812 Executive 0,9570838 5 FALSE TRUE
## Chef 092
# 29775391 Executive 0,9524580 2 TRUE TRUE
## Chef 434
# 10276858 Executive 0,9479883 4 TRUE FALSE
## Chef 343
# 16924102 Executive 0,9479701 3 TRUE TRUE
## Chef 332
# 65373280 Executive 0,9462183 1 TRUE TRUE
## Chef 423
# 20393721 Finance 0,9511945 3 FALSE TRUE
## Executive 992
/

## Accounta
nt

# 203
# 70541112 Finance 0,9456473 1 TRUE TRUE
## Executive 07
/

## Accounta
nt

# 25846894 Finance 0,9446961 2 TRUE TRUE
## Executive 732
/

## Accounta
nt

# 19446337 Finance 0,9443189 4 FALSE TRUE
## Executive 041
/

## Accounta
nt

# 25497147 Finance 0,9438716 5 FALSE TRUE
## Executive 017
/

## Accounta
nt

# 20393721 Finance 0,9600386 3 FALSE TRUE
Officer ( 8
Jr/Sr.)

# 23734441 Finance 0,9522399 2 TRUE TRUE
Officer ( 562
Jr/Sr.)

# 25497147 Finance 0,9517891 4 FALSE TRUE
Officer ( 475
Jr/Sr.)

# 53640713 Finance 0,9508016 5 FALSE TRUE
Officer ( 156
Jr/Sr.)

# 34816637 Finance 0,9463608 1 TRUE TRUE
Officer ( 681
Jr/Sr.)

# 70541112 Financial 0,9417991 2 TRUE TRUE
## Consolida 803
tion

## Consultan
t

# 27330027 Financial 0,9386546 4 FALSE FALSE
## Consolida 765
tion

# 204
## Consultan
t

# 153632 Financial 0,9359328 3 TRUE TRUE
# Consolida 764
tion

## Consultan
t

# 19446337 Financial 0,9342442 1 TRUE TRUE
## Consolida 62
tion

## Consultan
t

# 18365443 Financial 0,9331100 5 FALSE TRUE
## Consolida 827
tion

## Consultan
t

# 18354623 Graphics 0,9568201 1 TRUE FALSE
## Designer 853
# 70750649 Graphics 0,9531553 4 TRUE FALSE
## Designer 81
# 22754014 Graphics 0,9445030 2 TRUE FALSE
## Designer 836
# 28679359 Graphics 0,9435436 5 TRUE FALSE
## Designer 506
# 14304010 Graphics 0,9426000 3 TRUE FALSE
## Designer 143
# 16877897 HR 0,9579303 1 TRUE FALSE
## Specialist 028
# 30862904 HR 0,9561192 2 TRUE FALSE
## Specialist 703
# 26932091 HR 0,9515269 5 FALSE FALSE
## Specialist 99
# 22861181 HR 0,9453664 3 FALSE FALSE
## Specialist 87
# 11289482 HR 0,9444434 4 FALSE FALSE
## Specialist 517
# 10840430 INFORMA 0,9484859 2 TRUE FALSE
# TION & 45
# TECHNOL
# OGY
# STAFF
# 205
# 11676151 INFORMA 0,9474958 1 TRUE TRUE
# TION & 077
# TECHNOL
# OGY
# STAFF
# 26932091 INFORMA 0,9460883 5 FALSE FALSE
# TION & 964
# TECHNOL
# OGY
# STAFF
# 28672970 INFORMA 0,9457937 3 TRUE FALSE
# TION & 874
# TECHNOL
# OGY
# STAFF
# 17963031 INFORMA 0,9457588 4 FALSE FALSE
# TION & 681
# TECHNOL
# OGY
# STAFF
# 64589506 Junior 0,9402469 1 FALSE FALSE
## Associate 427
## Lawyer
# 26932091 Junior 0,9400253 2 FALSE FALSE
## Associate 197
## Lawyer
# 22861181 Junior 0,9393440 3 FALSE FALSE
## Associate 608
## Lawyer
# 16877897 Junior 0,9382883 4 FALSE FALSE
## Associate 659
## Lawyer
# 19557384 Junior 0,9380632 5 FALSE FALSE
## Associate 209
## Lawyer
# 23719943 Junior 0,9404868 2 FALSE FALSE
## Designer 792
for

## Apparel
# 26932091 Junior 0,9394543 5 FALSE FALSE
## Designer 595
for

## Apparel
# 206
# 23917826 Junior 0,9328362 4 FALSE FALSE
## Designer 478
for

## Apparel
# 15154822 Junior 0,9310774 1 TRUE FALSE
## Designer 192
for

## Apparel
# 70750649 Junior 0,9298330 3 FALSE FALSE
## Designer 345
for

## Apparel
# 13195436 Manager 0,9486718 1 TRUE TRUE
## Aviation 093
Safety,

## Quality
and

## Security
# 11169163 Manager 0,9479157 3 TRUE TRUE
## Aviation 24
Safety,

## Quality
and

## Security
# 12654876 Manager 0,9438178 4 FALSE FALSE
## Aviation 526
Safety,

## Quality
and

## Security
# 35651876 Manager 0,9438160 5 FALSE FALSE
## Aviation 536
Safety,

## Quality
and

## Security
# 17483843 Manager 0,9411606 2 TRUE TRUE
## Aviation 041
Safety,

## Quality
and

## Security
# 96260484 Medical 0,9365936 1 FALSE TRUE
## Doctor 609
# 207
# 37402097 Medical 0,9359483 3 FALSE TRUE
## Doctor 901
# 25328428 Medical 0,9357925 5 FALSE TRUE
## Doctor 524
# 15499825 Medical 0,9343298 4 FALSE TRUE
## Doctor 543
# 14667957 Medical 0,9322447 2 FALSE TRUE
## Doctor 061
# 13087952 Productio 0,9391430 2 FALSE TRUE
n 121

## Engineeri
ng

# 10504237 Productio 0,9358566 4 FALSE TRUE
n 737

## Engineeri
ng

# 11890896 Productio 0,9355367 1 TRUE FALSE
n 658

## Engineeri
ng

# 22861181 Productio 0,9352205 3 FALSE TRUE
n 072

## Engineeri
ng

# 11522068 Productio 0,9340292 5 FALSE TRUE
n 108

## Engineeri
ng

# 28290448 Public 0,9476316 1 TRUE TRUE
## Relations 491
## Officer
# 70750649 Public 0,9467867 2 TRUE FALSE
## Relations 469
## Officer
# 22861181 Public 0,9404439 4 FALSE FALSE
## Relations 705
## Officer
# 13115648 Public 0,9393615 5 FALSE FALSE
## Relations 415
## Officer
# 22732234 Public 0,9386659 3 TRUE TRUE
## Relations 303
## Officer
# 208
# 26888302 Quality 0,9380053 2 FALSE FALSE
## Control 431
## Superviso
r - Corn

## Commodi
ty

# 22861181 Quality 0,9358159 4 FALSE TRUE
## Control 329
## Superviso
r - Corn

## Commodi
ty

# 20905088 Quality 0,9323824 1 FALSE TRUE
## Control 831
## Superviso
r - Corn

## Commodi
ty

# 21629057 Quality 0,9320897 3 FALSE FALSE
## Control 127
## Superviso
r - Corn

## Commodi
ty

# 26932091 Quality 0,9292874 5 FALSE TRUE
## Control 126
## Superviso
r - Corn

## Commodi
ty

# 26932091 Regional 0,9526580 3 TRUE TRUE
## Sales 458
## Manager
# 28867567 Regional 0,9380075 4 TRUE TRUE
## Sales 485
## Manager
# 29306433 Regional 0,9375366 5 TRUE FALSE
## Sales 445
## Manager
# 27715131 Regional 0,9370184 1 TRUE TRUE
## Sales 881
## Manager
# 28051330 Regional 0,9363337 2 TRUE TRUE
## Sales 906
## Manager
# 209
# 22861181 Spare part 0,9482737 1 FALSE FALSE
## Admin 396
# 23917826 Spare part 0,9471226 3 FALSE TRUE
## Admin 141
# 26932091 Spare part 0,9467146 2 FALSE FALSE
## Admin 582
# 16378091 Spare part 0,9466934 4 FALSE TRUE
## Admin 216
# 10464113 Spare part 0,9449295 5 FALSE TRUE
## Admin 182
# 28772892 Teachers 0,9642666 5 TRUE TRUE
# 724
# 15850434 Teachers 0,9575843 2 TRUE TRUE
# 692
# 58105060 Teachers 0,9521600 4 TRUE FALSE
# 9
# 37220856 Teachers 0,9496124 3 TRUE FALSE
# 554
# 48547319 Teachers 0,9471607 1 TRUE FALSE
# 207
# 26932091 Unmanag 0,9621574 1 TRUE TRUE
ed 749

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 11289482 Unmanag 0,9439541 3 TRUE TRUE
ed 207

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 30862904 Unmanag 0,9380125 4 FALSE FALSE
ed 051

## Merchant
## Engagem
ent Senior
Associate,

# 210
## BPO Field
## Sales
# 13964744 Unmanag 0,9332395 2 FALSE FALSE
ed 557

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 24727739 Unmanag 0,9331051 5 FALSE FALSE
ed 675

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 4 Dengan Bobot - TF-IDF dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority

## Score Expert
# Business 0,205913 2 TRUE FALSE 38688388
## Developme 2303
nt

## Executive
# Business 0,202912 1 TRUE FALSE 31638814
## Developme 8525
nt

## Executive
# Business 0,192598 3 TRUE FALSE 47067533
## Developme 8694
nt

## Executive
# Business 0,187834 5 FALSE TRUE 26932091
## Developme 9723
nt

## Executive
# Business 0,183779 4 TRUE FALSE 17132168
## Developme 5536
nt

## Executive
# 211
# CLUB 0,204517 5 FALSE FALSE 26932091
# GENERAL 8615
# MANAGER
# CLUB 0,191228 1 TRUE TRUE 17818707
# GENERAL 4503
# MANAGER
# CLUB 0,185466 3 TRUE TRUE 18171955
# GENERAL 2893
# MANAGER
# CLUB 0,181416 4 FALSE FALSE 15535920
# GENERAL 6723
# MANAGER
# CLUB 0,180679 2 TRUE TRUE 31761591
# GENERAL 3312
# MANAGER
# Constructio 0,222458 1 TRUE FALSE 39027764
n 9589

## Supervisor
# Constructio 0,219571 4 TRUE TRUE 12839152
n 2303

## Supervisor
# Constructio 0,205773 3 TRUE FALSE 27246366
n 4896

## Supervisor
# Constructio 0,200795 2 TRUE TRUE 56525735
n 8072

## Supervisor
# Constructio 0,196674 5 FALSE FALSE 26932091
n 0695

## Supervisor
# Creative 0,177042 2 FALSE TRUE 68781345
Director / 6406

## Manager
# Creative 0,152407 3 TRUE FALSE 18460045
Director / 9329

## Manager
# Creativ 0,149001 4 FALSE FALSE 13964744
e Director / 695

## Manager
# Creative 0,138984 5 FALSE FALSE 17781039
Director / 5056

## Manager
# 212
# Creative 0,134054 1 TRUE TRUE 30864828
Director / 7236

## Manager
# Digital and 0,170029 5 FALSE TRUE 22754014
## Social 822
## Media
## Executive
# Digital and 0,161378 3 TRUE FALSE 15479281
## Social 88
## Media
## Executive
# Digital and 0,147463 1 TRUE TRUE 16620172
## Social 8205
## Media
## Executive
# Digital and 0,144642 4 TRUE FALSE 16536141
## Social 1125
## Media
## Executive
# Digital and 0,144450 2 TRUE TRUE 75329822
## Social 2095
## Media
## Executive
# Digital 0,200769 5 FALSE TRUE 26932091
## Banking 5753
## Officer
# Digital 0,181778 1 TRUE FALSE 98965485
## Banking 1123
## Officer
# Digital 0,159948 4 FALSE FALSE 14937492
## Banking 4431
## Officer
# Digital 0,157637 3 TRUE FALSE 27080812
## Banking 613
## Officer
# Digital 0,154671 2 TRUE FALSE 29406313
## Banking 2682
## Officer
# Executive 0,260834 4 TRUE TRUE 29775391
## Chef 3156
# Executive 0,260057 3 TRUE TRUE 20321582
## Chef 9128
# 213
# Executive 0,249323 1 TRUE TRUE 34252537
## Chef 4669
# Executive 0,246398 5 TRUE TRUE 25924968
## Chef 796
# Executive 0,246316 2 TRUE TRUE 25128608
## Chef 0122
# Finance 0,244852 5 TRUE FALSE 37370455
Executive / 904

## Accountant
# Finance 0,238935 4 TRUE FALSE 25846894
Executive / 8751

## Accountant
# Finance 0,229003 3 TRUE FALSE 21338490
Executive / 7916

## Accountant
# Finance 0,218988 2 TRUE FALSE 24670867
Executive / 459

## Accountant
# Finance 0,212373 1 TRUE TRUE 23387174
Executive / 8693

## Accountant
# Finance 0,223954 2 TRUE TRUE 23734441
Officer ( 8861
Jr/Sr.)

# Finance 0,216914 3 TRUE TRUE 29999135
Officer ( 026
Jr/Sr.)

# Finance 0,216765 5 TRUE FALSE 24670867
Officer ( 7361
Jr/Sr.)

# Finance 0,215849 1 TRUE TRUE 28298773
Officer ( 502
Jr/Sr.)

# Finance 0,204156 4 TRUE TRUE 53640713
Officer ( 394
Jr/Sr.)

# Financial 0,210191 5 FALSE FALSE 68781345
## Consolidati 4441
on

## Consultant
# Financial 0,194978 1 TRUE TRUE 95792386
## Consolidati 4098
# 214
on

## Consultant
# Financi 0,190158 3 TRUE TRUE 70541112
al 5017

## Consolidati
on

## Consultant
# Financial 0,189511 2 TRUE TRUE 38946032
## Consolidati 6438
on

## Consultant
# Financial 0,183903 4 TRUE FALSE 19234823
## Consolidati 2081
on

## Consultant
# Graphics 0,279561 2 TRUE TRUE 18460045
## Designer 5313
# Graphics 0,222008 3 TRUE FALSE 18354623
## Designer 2185
# Graphics 0,198927 1 TRUE TRUE 26676567
## Designer 8803
# Graphics 0,195168 4 TRUE FALSE 16893572
## Designer 6831
# Graphics 0,191999 5 FALSE TRUE 22754014
## Designer 01
# HR 0,266403 2 TRUE TRUE 24508725
## Specialist 927
# HR 0,263968 1 TRUE TRUE 30862904
## Specialist 2699
# HR 0,234010 4 FALSE TRUE 16877897
## Specialist 6126
# HR 0,227996 3 FALSE TRUE 24184357
## Specialist 3281
# HR 0,227032 5 FALSE TRUE 26932091
## Specialist 5052
# INFORMATI 0,221170 4 FALSE FALSE 17983957
# ON & 9312
# TECHNOLO
# GY STAFF
# INFORMATI 0,220545 1 TRUE TRUE 39413067
# ON & 8455
# 215
# TECHNOLO
# GY STAFF
# INFORMATI 0,215223 3 FALSE FALSE 17570634
# ON & 6294
# TECHNOLO
# GY STAFF
# INFORMATI 0,207111 2 TRUE FALSE 21283365
# ON & 8727
# TECHNOLO
# GY STAFF
# INFORMATI 0,202252 5 FALSE FALSE 38897568
# ON & 2526
# TECHNOLO
# GY STAFF
# Junior 0,124307 4 FALSE TRUE 29406313
## Associate 7984
## Lawyer
# Junior 0,121568 1 TRUE TRUE 10332998
## Associate 8418
## Lawyer
# Junior 0,120404 3 FALSE TRUE 69181350
## Associate 3196
## Lawyer
# Junior 0,117563 5 FALSE TRUE 23636277
## Associate 5815
## Lawyer
# Junior 0,117548 2 TRUE TRUE 15100547
## Associate 7301
## Lawyer
# Junior 0,166988 2 TRUE FALSE 23719943
## Designer 3684
for Apparel

# Junior 0,164602 1 TRUE TRUE 15746146
## Designer 35
for Apparel

# Junior 0,150207 5 FALSE FALSE 12122372
## Designer 8775
for Apparel

# Junior 0,144722 4 FALSE FALSE 26932091
## Designer 2826
for Apparel

# 216
# Junior 0,142571 3 FALSE FALSE 11722421
## Designer 9056
for Apparel

# Manager 0,234812 2 FALSE FALSE 26932091
## Aviation 8415
Safety,

## Quality and
## Security
# Manager 0,210154 1 TRUE FALSE 28186635
## Aviation 9087
Safety,

## Quality and
## Security
# Manager 0,207404 3 FALSE FALSE 24589765
## Aviation 6317
Safety,

## Quality and
## Security
# Manager 0,201492 4 FALSE FALSE 29406313
## Aviation 0559
Safety,

## Quality and
## Security
# Manager 0,194965 5 FALSE FALSE 11289482
## Aviation 5358
Safety,

## Quality and
## Security
# Medical 0,225712 1 FALSE TRUE 16356151
## Doctor 691
# Medical 0,174346 5 FALSE FALSE 13565152
## Doctor 7306
# Medical 0,172704 2 FALSE TRUE 43994605
## Doctor 0952
# Medical 0,161099 3 FALSE FALSE 24588864
## Doctor 4638
# Medical 0,152177 4 FALSE FALSE 49325370
## Doctor 5854
# Production 0,144448 2 TRUE FALSE 28803888
## Engineering 7571
# Production 0,130751 4 FALSE FALSE 30288581
## Engineering 2078
# 217
# Production 0,128543 1 TRUE TRUE 77828437
## Engineering 7933
# Production 0,123889 3 TRUE FALSE 17103000
## Engineering 6191
# Production 0,121891 5 FALSE FALSE 54100393
## Engineering 3506
# Public 0,200719 1 TRUE TRUE 21297828
## Relations 3257
## Officer
# Public 0,196597 5 FALSE TRUE 13129275
## Relations 6361
## Officer
# Public 0,195011 2 TRUE FALSE 27257013
## Relations 6308
## Officer
# Public 0,185810 4 FALSE FALSE 31220062
## Relations 0177
## Officer
# Public 0,183693 3 TRUE FALSE 27000192
## Relations 9263
## Officer
# Quality 0,140370 4 FALSE TRUE 26932091
## Control 3197
Supervisor -

## Corn
## Commodity
# Quality 0,127219 5 FALSE FALSE 28186635
## Control 2623
Supervisor -

## Corn
## Commodity
# Quality 0,126608 1 FALSE TRUE 16723524
## Control 0495
Supervisor -

## Corn
## Commodity
# Quality 0,123159 2 FALSE FALSE 28628090
## Control 2765
Supervisor -

## Corn
## Commodity
# Quality 0,121937 3 FALSE FALSE 20905088
## Control 0839
Supervisor -

# 218
## Corn
## Commodity
# Regional 0,243053 4 FALSE TRUE 26932091
## Sales 1858
## Manager
# Regional 0,224709 3 FALSE TRUE 27080812
## Sales 9765
## Manager
# Regional 0,217841 1 FALSE TRUE 25038571
## Sales 7617
## Manager
# Regional 0,212831 2 FALSE FALSE 38688388
## Sales 0977
## Manager
# Regional 0,210324 5 FALSE TRUE 26919036
## Sales 2631
## Manager
# Spare part 0,155213 5 FALSE FALSE 16911115
## Admin 3324
# Spare part 0,149973 4 FALSE FALSE 38897568
## Admin 7297
# Spare part 0,148060 1 TRUE TRUE 10189110
## Admin 5907
# Spare part 0,147032 2 TRUE TRUE 20504094
## Admin 3157
# Spare part 0,146112 3 FALSE FALSE 24670867
## Admin 3257
# Teachers 0,250745 4 TRUE TRUE 15850434
# 2502
# Teachers 0,213840 3 TRUE TRUE 20399718
# 2469
# Teachers 0,200342 5 TRUE TRUE 28772892
# 6776
# Teachers 0,196635 2 TRUE TRUE 22056333
# 771
# Teachers 0,196100 1 TRUE TRUE 96547039
# 2177
# Unmanage 0,222177 1 TRUE TRUE 26932091
d Merchant 0964

## Engagemen
t Senior
Associate,

# 219
## BPO Field
## Sales
# Unmanage 0,192196 3 FALSE FALSE 24589765
d Merchant 5525

## Engagemen
t Senior
Associate,

## BPO Field
## Sales
# Unmanage 0,186580 4 FALSE FALSE 68781345
d Merchant 6571

## Engagemen
t Senior
Associate,

## BPO Field
## Sales
# Unmanage 0,163489 2 TRUE FALSE 11289482
d Merchant 1955

## Engagemen
t Senior
Associate,

## BPO Field
## Sales
# Unmanage 0,161752 5 FALSE TRUE 26919036
d Merchant 4074

## Engagemen
t Senior
Associate,

## BPO Field
## Sales
# 5 Dengan Bobot - Word2Vec dan Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority

## Score Expert
# 26932091 Business 0,9016295 3 TRUE FALSE
## Developm 473
ent

## Executive
# 10464113 Business 0,8664782 2 TRUE TRUE
## Developm 882
ent

## Executive
# 220
# 14790629 Business 0,8652020 4 TRUE TRUE
## Developm 196
ent

## Executive
# 27715131 Business 0,8478853 1 TRUE FALSE
## Developm 941
ent

## Executive
# 16276121 Business 0,8414156 5 FALSE TRUE
## Developm 304
ent

## Executive
# 13411858 CLUB 0,8781417 1 TRUE TRUE
# GENERAL 949
# MANAGE
# R
# 26932091 CLUB 0,8773720 5 FALSE FALSE
# GENERAL 443
# MANAGE
# R
# 10464113 CLUB 0,8592673 4 FALSE TRUE
# GENERAL 114
# MANAGE
# R
# 27715131 CLUB 0,8545579 2 TRUE TRUE
# GENERAL 91
# MANAGE
# R
# 34033933 CLUB 0,8522922 3 FALSE FALSE
# GENERAL 794
# MANAGE
# R
# 26932091 Construct 0,8621428 5 FALSE FALSE
ion 311

## Superviso
r

# 12839152 Construct 0,8265170 2 TRUE TRUE
ion 306

## Superviso
r

# 24589765 Construct 0,8242714 3 FALSE FALSE
ion 703

## Superviso
r

# 221
# 27246366 Construct 0,8220116 1 TRUE TRUE
ion 446

## Superviso
r

# 39027764 Construct 0,8205659 4 TRUE FALSE
ion 688

## Superviso
r

# 34033933 Creative 0,8544749 2 FALSE FALSE
Director / 737

## Manager
# 23917826 Creative 0,8538641 3 FALSE FALSE
Director / 334

## Manager
# 295257 Creative 0,8505293 5 FALSE FALSE
# Director / 826
## Manager
# 28471099 Creative 0,8454253 1 FALSE TRUE
Director / 674

## Manager
# 13115648 Creative 0,8417996 4 FALSE TRUE
Director / 705

## Manager
# 18905648 Digital 0,8844326 5 FALSE TRUE
and Social 053

## Media
## Executive
# 16276121 Digital 0,8792089 4 FALSE TRUE
and Social 298

## Media
## Executive
# 18354623 Digital 0,8678290 2 TRUE FALSE
and Social 546

## Media
## Executive
# 22754014 Digital 0,8591275 3 FALSE TRUE
and Social 096

## Media
## Executive
# 70750649 Digital 0,8561320 1 TRUE FALSE
and Social 066

## Media
## Executive
# 222
# 26932091 Digital 0,8992728 4 FALSE TRUE
## Banking 761
## Officer
# 29406313 Digital 0,8862656 2 FALSE FALSE
## Banking 554
## Officer
# 11289482 Digital 0,8644934 3 TRUE FALSE
## Banking 257
## Officer
# 16276121 Digital 0,8610806 1 TRUE TRUE
## Banking 125
## Officer
# 10464113 Digital 0,8505692 5 FALSE TRUE
## Banking 522
## Officer
# 35579812 Executive 0,8859671 5 TRUE TRUE
## Chef 312
# 21060367 Executive 0,8854268 4 TRUE TRUE
## Chef 859
# 20321582 Executive 0,8789194 2 TRUE TRUE
## Chef 787
# 29775391 Executive 0,8756774 1 TRUE TRUE
## Chef 834
# 34252537 Executive 0,8704000 3 TRUE TRUE
## Chef 922
# 20393721 Finance 0,8825229 3 TRUE TRUE
## Executive 636
/

## Accounta
nt

# 23636277 Finance 0,8781847 2 TRUE TRUE
## Executive 954
/

## Accounta
nt

# 70541112 Finance 0,8773093 1 TRUE TRUE
## Executive 777
/

## Accounta
nt

# 28522529 Finance 0,8708689 4 TRUE FALSE
## Executive 809
/

# 223
## Accounta
nt

# 11289482 Finance 0,8649438 5 FALSE FALSE
## Executive 109
/

## Accounta
nt

# 34198885 Finance 0,8998344 1 TRUE TRUE
Officer ( 839
Jr/Sr.)

# 70541112 Finance 0,8726109 3 TRUE TRUE
Officer ( 783
Jr/Sr.)

# 28522529 Finance 0,8644792 4 TRUE FALSE
Officer ( 199
Jr/Sr.)

# 20393721 Finance 0,8589066 2 TRUE TRUE
Officer ( 515
Jr/Sr.)

# 25497147 Finance 0,8502537 5 FALSE TRUE
Officer ( 529
Jr/Sr.)

# 70541112 Financial 0,8643537 1 TRUE TRUE
## Consolida 442
tion

## Consultan
t

# 18365443 Financial 0,8542422 2 FALSE TRUE
## Consolida 007
tion

## Consultan
t

# 269320 Financial 0,8518766 3 FALSE TRUE
# Consolida 099
tion

## Consultan
t

# 26695839 Financial 0,8398145 4 FALSE FALSE
## Consolida 871
tion

## Consultan
t

# 16877897 Financial 0,8222200 5 FALSE TRUE
## Consolida 423
# 224
tion

## Consultan
t

# 18460045 Graphics 0,8983531 1 TRUE TRUE
## Designer 892
# 18354623 Graphics 0,8972359 2 TRUE TRUE
## Designer 945
# 33893326 Graphics 0,8583144 3 TRUE TRUE
## Designer 695
# 22754014 Graphics 0,8526434 5 FALSE FALSE
## Designer 749
# 16276121 Graphics 0,8444623 4 TRUE FALSE
## Designer 484
# 30862904 HR 0,9084293 1 TRUE TRUE
## Specialist 384
# 16877897 HR 0,9057623 2 FALSE TRUE
## Specialist 595
# 26932091 HR 0,9027255 5 FALSE FALSE
## Specialist 476
# 29134372 HR 0,8710555 3 FALSE TRUE
## Specialist 988
# 11289482 HR 0,8705781 4 FALSE FALSE
## Specialist 315
# 26932091 INFORMA 0,8806972 5 FALSE FALSE
# TION & 802
# TECHNOL
# OGY
# STAFF
# 28471099 INFORMA 0,8790658 3 TRUE FALSE
# TION & 832
# TECHNOL
# OGY
# STAFF
# 10839851 INFORMA 0,8555776 1 TRUE TRUE
# TION & 477
# TECHNOL
# OGY
# STAFF
# 28672970 INFORMA 0,8508172 4 TRUE FALSE
# TION & 572
# TECHNOL
# 225
# OGY
# STAFF
# 26341987 INFORMA 0,8465297 2 TRUE FALSE
# TION & 371
# TECHNOL
# OGY
# STAFF
# 26330995 Junior 0,8434696 3 FALSE FALSE
## Associate 848
## Lawyer
# 24589765 Junior 0,8409152 2 FALSE FALSE
## Associate 248
## Lawyer
# 11289482 Junior 0,8380842 4 FALSE FALSE
## Associate 897
## Lawyer
# 28871170 Junior 0,8340103 1 TRUE FALSE
## Associate 447
## Lawyer
# 81508860 Junior 0,8320689 5 FALSE FALSE
## Associate 852
## Lawyer
# 26932091 Junior 0,8670108 3 FALSE FALSE
## Designer 12
for

## Apparel
# 28471099 Junior 0,8221067 2 FALSE FALSE
## Designer 895
for

## Apparel
# 19195747 Junior 0,8096644 1 FALSE FALSE
## Designer 228
for

## Apparel
# 27715131 Junior 0,8087251 4 FALSE FALSE
## Designer 828
for

## Apparel
# 76196367 Junior 0,8084914 5 FALSE FALSE
## Designer 625
for

## Apparel
# 226
# 13195436 Manager 0,8608590 1 TRUE TRUE
## Aviation 662
Safety,

## Quality
and

## Security
# 24589765 Manager 0,8604515 2 FALSE TRUE
## Aviation 94
Safety,

## Quality
and

## Security
# 28186635 Manager 0,8446557 3 FALSE FALSE
## Aviation 224
Safety,

## Quality
and

## Security
# 26932091 Manager 0,8428457 5 FALSE FALSE
## Aviation 081
Safety,

## Quality
and

## Security
# 16877897 Manager 0,8410134 4 FALSE FALSE
## Aviation 763
Safety,

## Quality
and

## Security
# 15958967 Medical 0,8506042 3 FALSE FALSE
## Doctor 004
# 14667957 Medical 0,8470290 1 FALSE FALSE
## Doctor 78
# 28745844 Medical 0,8464838 4 FALSE FALSE
## Doctor 862
# 24588864 Medical 0,8438134 5 FALSE FALSE
## Doctor 193
# 96260484 Medical 0,8381138 2 FALSE TRUE
## Doctor 295
# 54100393 Productio 0,8348578 5 FALSE FALSE
n 215

## Engineeri
ng

# 227
# 24544244 Productio 0,8070656 3 FALSE FALSE
n 359

## Engineeri
ng

# 30288581 Productio 0,8064919 2 FALSE FALSE
n 114

## Engineeri
ng

# 37751611 Productio 0,8005253 4 FALSE FALSE
n 474

## Engineeri
ng

# 17312146 Productio 0,7976875 1 TRUE FALSE
n 544

## Engineeri
ng

# 28290448 Public 0,8546104 1 TRUE TRUE
## Relations 868
## Officer
# 22754014 Public 0,8373224 3 TRUE TRUE
## Relations 586
## Officer
# 16276121 Public 0,8306562 4 FALSE TRUE
## Relations 04
## Officer
# 70750649 Public 0,8303484 2 TRUE FALSE
## Relations 569
## Officer
# 22861181 Public 0,8297583 5 FALSE FALSE
## Relations 163
## Officer
# 26932091 Quality 0,8705424 4 FALSE TRUE
## Control 666
## Superviso
r - Corn

## Commodi
ty

# 35651876 Quality 0,8361086 2 FALSE FALSE
## Control 76
## Superviso
r - Corn

## Commodi
ty

# 228
# 26070334 Quality 0,8279247 1 FALSE TRUE
## Control 06
## Superviso
r - Corn

## Commodi
ty

# 21060367 Quality 0,8256160 5 FALSE FALSE
## Control 915
## Superviso
r - Corn

## Commodi
ty

# 12011623 Quality 0,8178911 3 FALSE FALSE
## Control 124
## Superviso
r - Corn

## Commodi
ty

# 26932091 Regional 0,9204637 3 FALSE TRUE
## Sales 706
## Manager
# 28867567 Regional 0,8558917 2 TRUE TRUE
## Sales
## Manager
# 18368613 Regional 0,8488336 4 TRUE FALSE
## Sales 618
## Manager
# 27715131 Regional 0,8465175 1 FALSE TRUE
## Sales 219
## Manager
# 14790629 Regional 0,8421503 5 FALSE FALSE
## Sales 535
## Manager
# 26932091 Spare part 0,8987249 5 FALSE TRUE
## Admin 136
# 16378091 Spare part 0,8544802 1 FALSE TRUE
## Admin 836
# 14790629 Spare part 0,8472287 4 FALSE FALSE
## Admin 589
# 23917826 Spare part 0,8446965 3 FALSE TRUE
## Admin 705
# 37764298 Spare part 0,8442025 2 FALSE TRUE
## Admin 726
# 229
# 28772892 Teachers 0,9297527 4 TRUE TRUE
# 121
# 15850434 Teachers 0,9152821 2 TRUE TRUE
# 211
# 54100393 Teachers 0,9012950 5 TRUE TRUE
# 182
# 37220856 Teachers 0,8875992 3 FALSE TRUE
# 112
# 20399718 Teachers 0,8841772 1 TRUE TRUE
# 63
# 26932091 Unmanag 0,9252712 1 TRUE TRUE
ed 045

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 11289482 Unmanag 0,8667385 3 TRUE FALSE
ed 379

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 24589765 Unmanag 0,8507761 4 FALSE FALSE
ed 608

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 29406313 Unmanag 0,8341917 2 TRUE FALSE
ed 147

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 16877897 Unmanag 0,8320381 5 FALSE FALSE
ed 194

## Merchant
# 230
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 6 Dengan Bobot - Word2Vec dan Improved Sqrt-Cosine Similarity
Rank Resume ID Position Similarity Rank Relevance Seniority

## Score Expert
# 26932091 Business 0,9539668 2 TRUE FALSE
## Developm 445
ent

## Executive
# 14790629 Business 0,9506780 4 TRUE FALSE
## Developm 856
ent

## Executive
# 91467795 Business 0,9475252 1 TRUE TRUE
## Developm 332
ent

## Executive
# 10464113 Business 0,9466634 5 FALSE TRUE
## Developm 695
ent

## Executive
# 27715131 0,9436823 3 TRUE TRUE
# 33
# 13411858 CLUB 0,9527268 4 FALSE TRUE
# GENERAL 773
# MANAGE
# R
# 28471099 CLUB 0,9490812 2 TRUE TRUE
# GENERAL 742
# MANAGE
# R
# 26932091 CLUB 0,9488134 1 TRUE TRUE
# GENERAL 43
# MANAGE
# R
# 10464113 CLUB 0,9477072 5 FALSE FALSE
# GENERAL 07
# 231
# MANAGE
# R
# 24727739 CLUB 0,9474657 3 FALSE FALSE
# GENERAL 096
# MANAGE
# R
# 26932091 Construct 0,9412927 5 FALSE TRUE
ion 301

## Superviso
r

# 39027764 Construct 0,9390667 3 TRUE FALSE
ion 24

## Superviso
r

# 12839152 Construct 0,9371928 1 TRUE TRUE
ion 374

## Superviso
r

# 21060367 Construct 0,9352513 4 FALSE FALSE
ion 378

## Superviso
r

# 27246366 Construct 0,9326540 2 TRUE TRUE
ion 113

## Superviso
r

# 28471099 Creative 0,9530115 4 FALSE TRUE
Director / 037

## Manager
# 17781039 Creative 0,9483212 5 FALSE FALSE
Director / 768

## Manager
# 139647 Creative 0,9477864 2 FALSE TRUE
# Director / 338
## Manager
# 24589765 Creative 0,9477007 3 FALSE TRUE
Director / 135

## Manager
# 81508860 Creative 0,9471895 1 TRUE TRUE
Director / 609

## Manager
# 18905648 Digital 0,9553223 2 TRUE TRUE
and Social 582

# 232
## Media
## Executive
# 18354623 Digital 0,9542773 3 TRUE TRUE
and Social 245

## Media
## Executive
# 16276121 Digital 0,9541360 1 FALSE FALSE
and Social 868

## Media
## Executive
# 34712719 Digital 0,9525442 5 FALSE TRUE
and Social 674

## Media
## Executive
# 70750649 Digital 0,9519086 4 TRUE FALSE
and Social 079

## Media
## Executive
# 26932091 Digital 0,9611610 5 FALSE FALSE
## Banking 445
## Officer
# 16276121 Digital 0,9536183 1 FALSE TRUE
## Banking 744
## Officer
# 29406313 Digital 0,9528114 3 FALSE TRUE
## Banking 795
## Officer
# 14790629 Digital 0,9514819 4 FALSE TRUE
## Banking 96
## Officer
# 28471099 Digital 0,9496212 2 FALSE FALSE
## Banking 248
## Officer
# 35579812 Executive 0,9591079 5 FALSE TRUE
## Chef 737
# 29775391 Executive 0,9519746 1 TRUE TRUE
## Chef 137
# 21060367 Executive 0,9517975 4 FALSE TRUE
## Chef 364
# 16924102 Executive 0,9497517 2 TRUE TRUE
## Chef 649
# 233
# 10276858 Executive 0,9491744 3 TRUE FALSE
## Chef 926
# 23636277 Finance 0,9531494 3 TRUE TRUE
## Executive 892
/

## Accounta
nt

# 20393721 Finance 0,9519314 4 FALSE TRUE
## Executive 231
/

## Accounta
nt

# 70541112 Finance 0,9514578 1 TRUE TRUE
## Executive 621
/

## Accounta
nt

# 24670867 Finance 0,9505766 2 TRUE TRUE
## Executive 607
/

## Accounta
nt

# 24953921 Finance 0,9484162 5 FALSE FALSE
## Executive 525
/

## Accounta
nt

# 34198885 Finance 0,9618073 1 TRUE TRUE
Officer ( 275
Jr/Sr.)

# 25497147 Finance 0,9601359 3 FALSE TRUE
Officer ( 54
Jr/Sr.)

# 20393721 Finance 0,9587329 2 FALSE TRUE
Officer ( 409
Jr/Sr.)

# 53640713 Finance 0,9536418 4 FALSE TRUE
Officer ( 681
Jr/Sr.)

# 28522529 Finance 0,9535884 5 FALSE FALSE
Officer ( 272
Jr/Sr.)

# 70541112 Financial 0,9419954 1 TRUE TRUE
## Consolida 621
# 234
tion

## Consultan
t

# 27330027 Financial 0,9392107 3 FALSE FALSE
## Consolida 855
tion

## Consultan
t

# 139647 Financial 0,9359215 4 FALSE TRUE
# Consolida 062
tion

## Consultan
t

# 18365443 Financial 0,9342627 5 FALSE TRUE
## Consolida 198
tion

## Consultan
t

# 15363277 Financial 0,9341559 2 FALSE TRUE
## Consolida 481
tion

## Consultan
t

# 18354623 Graphics 0,9600432 2 TRUE FALSE
## Designer 242
# 18460045 Graphics 0,9534482 1 TRUE TRUE
## Designer 538
# 16276121 Graphics 0,9531318 5 TRUE FALSE
## Designer 897
# 70750649 Graphics 0,9528303 4 TRUE FALSE
## Designer 428
# 22754014 Graphics 0,9518864 3 TRUE FALSE
## Designer 807
# 30862904 HR 0,9600555 3 TRUE FALSE
## Specialist 505
# 16877897 HR 0,9569724 2 TRUE FALSE
## Specialist 647
# 26932091 HR 0,9502614 5 FALSE FALSE
## Specialist 406
# 24508725 HR 0,9461360 1 TRUE TRUE
## Specialist 144
# 235
# 11289482 HR 0,9453240 4 FALSE FALSE
## Specialist 462
# 28471099 INFORMA 0,9529981 3 FALSE FALSE
# TION & 197
# TECHNOL
# OGY
# STAFF
# 16911115 INFORMA 0,9469800 2 FALSE TRUE
# TION & 961
# TECHNOL
# OGY
# STAFF
# 26932091 INFORMA 0,9466821 5 FALSE FALSE
# TION & 773
# TECHNOL
# OGY
# STAFF
# 10839851 INFORMA 0,9461330 1 TRUE TRUE
# TION & 73
# TECHNOL
# OGY
# STAFF
# 10549585 INFORMA 0,9442940 4 FALSE FALSE
# TION & 569
# TECHNOL
# OGY
# STAFF
# 24589765 Junior 0,9489688 5 FALSE FALSE
## Associate 544
## Lawyer
# 26330995 Junior 0,9456341 2 FALSE FALSE
## Associate 09
## Lawyer
# 27375577 Junior 0,9414918 4 FALSE FALSE
## Associate 355
## Lawyer
# 28471099 Junior 0,9398351 3 FALSE FALSE
## Associate 781
## Lawyer
# 11289482 Junior 0,9392279 1 FALSE FALSE
## Associate 01
## Lawyer
# 26932091 Junior 0,9411121 2 FALSE FALSE
## Designer 762
# 236
for

## Apparel
# 23917826 Junior 0,9351794 4 FALSE FALSE
## Designer 4
for

## Apparel
# 28745844 Junior 0,9344192 5 FALSE FALSE
## Designer 132
for

## Apparel
# 20553895 Junior 0,9317723 3 FALSE FALSE
## Designer 528
for

## Apparel
# 70750649 Junior 0,9313974 1 FALSE FALSE
## Designer 978
for

## Apparel
# 21060367 Manager 0,9459566 5 FALSE FALSE
## Aviation 999
Safety,

## Quality
and

## Security
# 13195436 Manager 0,9425360 1 TRUE TRUE
## Aviation 008
Safety,

## Quality
and

## Security
# 12333703 Manager 0,9420496 3 FALSE FALSE
## Aviation 615
Safety,

## Quality
and

## Security
# 29167286 Manager 0,9400526 2 TRUE TRUE
## Aviation 723
Safety,

## Quality
and

## Security
# 35651876 Manager 0,9394215 4 FALSE FALSE
## Aviation 969
Safety,

# 237
## Quality
and

## Security
# 14667957 Medical 0,9379945 2 FALSE TRUE
## Doctor 709
# 28745844 Medical 0,9371113 5 FALSE TRUE
## Doctor 42
# 15958967 Medical 0,9345641 1 FALSE TRUE
## Doctor 05
# 24588864 Medical 0,9319105 4 FALSE TRUE
## Doctor 3
# 96260484 Medical 0,9310241 3 FALSE TRUE
## Doctor 31
# 54100393 Productio 0,9440333 4 FALSE TRUE
n 022

## Engineeri
ng

# 22861181 Productio 0,9393731 3 FALSE TRUE
n 832

## Engineeri
ng

# 11890896 Productio 0,9386830 1 TRUE FALSE
n 222

## Engineeri
ng

# 15850434 Productio 0,9380816 3 FALSE TRUE
n 317

## Engineeri
ng

# 11522068 Productio 0,9367380 5 FALSE TRUE
n 258

## Engineeri
ng

# 28290448 Public 0,9475246 1 TRUE TRUE
## Relations 991
## Officer
# 70750649 Public 0,9442786 2 TRUE FALSE
## Relations 542
## Officer
# 13115648 Public 0,9423968 5 FALSE FALSE
## Relations 156
## Officer
# 238
# 27000192 Public 0,9418473 3 TRUE FALSE
## Relations 849
## Officer
# 22732234 Public 0,9413068 4 TRUE TRUE
## Relations 995
## Officer
# 26888302 Quality 0,9397145 3 FALSE FALSE
## Control 7
## Superviso
r - Corn

## Commodi
ty

# 28628090 Quality 0,9374573 1 FALSE FALSE
## Control 193
## Superviso
r - Corn

## Commodi
ty

# 22861181 Quality 0,9352906 4 FALSE TRUE
## Control 635
## Superviso
r - Corn

## Commodi
ty

# 20905088 Quality 0,9336073 2 FALSE TRUE
## Control 888
## Superviso
r - Corn

## Commodi
ty

# 21060367 Quality 0,9334563 5 FALSE FALSE
## Control 762
## Superviso
r - Corn

## Commodi
ty

# 26932091 Regional 0,9537964 3 TRUE TRUE
## Sales 128
## Manager
# 27715131 Regional 0,9388897 1 TRUE TRUE
## Sales 552
## Manager
# 14790629 Regional 0,9382742 4 FALSE FALSE
## Sales 131
## Manager
# 239
# 23917826 Regional 0,9381668 5 FALSE TRUE
## Sales 276
## Manager
# 14070138 Regional 0,9381297 2 TRUE TRUE
## Sales 179
## Manager
# 14790629 Spare part 0,9541040 5 FALSE FALSE
## Admin 064
# 26932091 Spare part 0,9529997 2 FALSE FALSE
## Admin 728
# 16378091 Spare part 0,9487359 3 FALSE TRUE
## Admin 951
# 28745844 Spare part 0,9476989 1 TRUE TRUE
## Admin 518
# 23917826 Spare part 0,9474161 4 FALSE TRUE
## Admin 594
# 28772892 Teachers 0,9650821 5 TRUE TRUE
# 12
# 15850434 Teachers 0,9614404 2 TRUE TRUE
# 383
# 58105060 Teachers 0,9525103 4 TRUE FALSE
# 733
# 20399718 Teachers 0,9482750 1 TRUE TRUE
# 764
# 46055835 Teachers 0,9476272 3 FALSE FALSE
# 471
# 26932091 Unmanag 0,9595202 1 TRUE TRUE
ed 941

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 29406313 Unmanag 0,9428494 2 TRUE TRUE
ed 614

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 240
# 11289482 Unmanag 0,9400499 4 TRUE TRUE
ed 924

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 30862904 Unmanag 0,9388757 5 FALSE FALSE
ed 821

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 24589765 Unmanag 0,9388679 3 TRUE TRUE
ed 936

## Merchant
## Engagem
ent Senior
Associate,

## BPO Field
## Sales
# 241
# LAMPIRAN D GRAFIK GARIS TIGA PARAMETER SETIAP
# KUALIFIKASI LOWONGAN KERJA
# 242
# 243
# 244
# 245
# 246
# 247
# 248
# 249
# 250
# 251
# 252
# 253