import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti=Maksukortti(1000)

    def test_maara_oikea(self):
        self.assertEqual((self.kassa.kassassa_rahaa, (self.kassa.maukkaat+self.kassa.edulliset)), (100000, 0))

    def test_osto_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(1000)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.edulliset), (100240, 1))

    def test_osto_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(1000)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.maukkaat), (100400, 1))

    def test_fail_osto_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(10)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.edulliset), (100000, 0))

    def test_fail_osto_maukas(self):
        self.kassa.syo_maukkaasti_kateisella(10)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.maukkaat), (100000, 0))
    
    def test_osto_edullinen_kort(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.edulliset), (100000, 1))

    def test_osto_maukas_kort(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.maukkaat), (100000, 1))

    def test_fail_osto_edullinen_kort(self):
        koyha=Maksukortti(10)
        self.kassa.syo_edullisesti_kortilla(koyha)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.edulliset, str(koyha)),(100000, 0, "Kortilla on rahaa 0.10 euroa"))

    def test_fail_osto_maukas_kort(self):
        koyha=Maksukortti(10)
        self.kassa.syo_maukkaasti_kortilla(koyha)
        self.assertEqual((self.kassa.kassassa_rahaa, self.kassa.maukkaat, str(koyha)),(100000, 0, "Kortilla on rahaa 0.10 euroa"))

    def test_kortin_lataus(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual((self.kassa.kassassa_rahaa, str(self.kortti)), (100100, "Kortilla on rahaa 11.00 euroa"))
        
    def test_kortin_lataus_fail(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual((self.kassa.kassassa_rahaa, str(self.kortti)), (100000, "Kortilla on rahaa 10.00 euroa"))