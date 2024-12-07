# Data panen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# Fungsi menampilkan detail panen
def tampilkan_detail_panen(data):
    print("LAPORAN DETAIL PANEN")
    for kode, info in data.items():
        print(f"Lokasi: {info['nama_lokasi']} ({kode})")
        for komoditas, jumlah in info['hasil_panen'].items():
            print(f"  {komoditas.capitalize()}: {jumlah} kg")
        print()

# Fungsi analisis panen
def analisis_panen(data):
    print("\nANALISIS KONDISI PANEN")
    padi_per_lokasi = {}
    kedelai_per_lokasi = {}

    for kode, info in data.items():
        padi = info['hasil_panen']['padi']
        jagung = info['hasil_panen']['jagung']
        kedelai = info['hasil_panen']['kedelai']

        padi_per_lokasi[kode] = padi
        kedelai_per_lokasi[kode] = kedelai

        print(f"EVALUASI {info['nama_lokasi']}:")
        print(f"  Padi: {padi} kg")
        print(f"  Jagung: {jagung} kg")
        print(f"  Kedelai: {kedelai} kg")

        if padi > 1300 or jagung > 800:
            print(f"  Status: PK Butuh Perhatian Khusus")
        else:
            print(f"  Status: KN Kondisi Normal")
        print("-" * 30)

    return padi_per_lokasi, kedelai_per_lokasi

# Eksekusi fungsi
tampilkan_detail_panen(data_panen)
padi_lokasi, kedelai_lokasi = analisis_panen(data_panen)

# Informasi khusus
print("\nINFORMASI KHUSUS")
print(f"Hasil jagung lokasi2: {data_panen['lokasi2']['hasil_panen']['jagung']} kg")
print(f"Nama lokasi3: {data_panen['lokasi3']['nama_lokasi']}")

# Rekap padi per lokasi
print("\nREKAP PADI PER LOKASI")
for lokasi, jumlah in padi_lokasi.items():
    print(f"{lokasi}: {jumlah} kg")

# Rekap kedelai per lokasi
print("\nREKAP KEDELAI PER LOKASI")
for lokasi, jumlah in kedelai_lokasi.items():
    print(f"{lokasi}: {jumlah} kg")