currency_template = {
          "Rupiah": "indonesian rupiah",
          "Euro": "euro",
          "Poundsterling": "british pound sterling"
}

currency_convert = {}

while True:
          currency = dict.fromkeys(currency_template.keys())
          rupiah = int(input("Masukkan jumlah rupiah: "))
          rupiah_convert_to_euro = round(rupiah / 16592.30)
          rupiah_convert_to_poundsterling = round(rupiah / 19267.50)
          currency['Rupiah'] = rupiah
          currency['Euro'] = int(rupiah_convert_to_euro)
          currency['Poundsterling'] = int(rupiah_convert_to_poundsterling)
          KEY = len(currency_convert) + 1
          currency_convert.update({KEY: currency})
          print(f"{'Rupiah':16}{'Euro':<16}{'Poundsterling':<16}")
          print(50*"=")
          for currency in currency_convert:
                    KEY = currency
                    RUPIAH = currency_convert[KEY]["Rupiah"]
                    EURO = currency_convert[KEY]["Euro"]
                    POUNDSTERLING = currency_convert[KEY]['Poundsterling']
                    print(f"{RUPIAH:<10,}{EURO:>10.2f}{POUNDSTERLING:>16.2f}")
          print(50*"=")
          option_continue = input("\nApakah Anda ingin melanjutkan konversi angka? (y/n): ")
          if option_continue == 'n':
                    print("Terima kasih telah menggunakan program konversi mata uang.")
                    break
