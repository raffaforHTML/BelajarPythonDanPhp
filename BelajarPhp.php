<?php
// Membuat sebuah array untuk menyimpan biodata
$biodata = array(
    "Nama" => "ARRAYA GANZ",
    "Umur" => 13,
    "Alamat" => "PADANG. PARIAMAN",
    "Pekerjaan" => "PELAJAR"
);

// Menampilkan biodata
foreach ($biodata as $key => $value) {
    echo $key . ": " . $value . "\n";
}
?>
