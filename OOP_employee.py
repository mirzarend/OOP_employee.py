from abc import ABC,abstractmethod

class Karyawan(ABC) :
  def __init__(self,nama,gaji):
    self.__nama = nama
    self.__gaji = gaji
  def get_nama(self) :
    return self.__nama
  def get_gaji(self) :
    return self.__gaji
  def set_gaji(self,tambah) :
    if tambah >= 0 :
      self.__gaji = tambah
    else :
      print("tidak boleh kurang dari 0")
  @abstractmethod
  def kerja(self) :
    pass
  @abstractmethod
  def laporan(self) :
    pass

class Developer(Karyawan) :
  def kerja(self) :
    print("Sedang Mendebug")
  def laporan(self) :
    print(f"Nama : {self.get_nama()}")
    print(f"Gaji : {self.get_gaji()}")
class Designer(Karyawan) :
  def kerja(self) :
    print("Sedang Mendesain")
  def laporan(self) :
    print(f"Nama : {self.get_nama()}")
    print(f"Gaji : {self.get_gaji()}")
class Manager(Karyawan) :
  def kerja(self) :
    print("Sedang Mengatur Produk")
  def laporan(self) :
    print(f"Nama : {self.get_nama()}")
    print(f"Gaji : {self.get_gaji()}")

dev1 = Developer("Mirza",8000000)
dsg1 = Designer("Dirga",4000000)
mng1 = Manager("Rendika",5000000)
dsg1.set_gaji(6000000)
mng1.set_gaji(-10)
list_karyawan =[dev1,dsg1,mng1]
for karyawan in list_karyawan :
  karyawan.laporan()
  karyawan.kerja()
  