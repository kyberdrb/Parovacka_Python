import unittest
import parovacka

def suDveDvojiceZhodne(prvaDvojica, inaDvojica):
    if len(prvaDvojica.intersection(inaDvojica)) == 2:
        return True

    return False

class TestParovacka_DvojiceSuUnikatne_BezReciprocity(unittest.TestCase):

    zoznamUcastnikov =              ["a", "b", "c", "d"]
    zoznamPriradenychDvojiciek =    ["b", "c", "d", "a"]

    prvaDvojica =       set(["a", "b"])
    druhaDvojica =      set(["b", "c"])
    tretiaDvojica =     set(["c", "b"])

    def testSuDvojiceUnikatne_Ano(self):
        self.assertTrue(parovacka.suDvojiceUnikatne(
            self.zoznamUcastnikov,
            self.zoznamPriradenychDvojiciek),
            True)

    def testSuDvojiceBezReciprocity_Ano(self):
        self.assertTrue(parovacka.suDvojiceBezReciprocity(
            self.zoznamUcastnikov,
            self.zoznamPriradenychDvojiciek),
            True)

    def testVytvorDvojicu(self):
        self.assertEqual(parovacka.vytvorDvojicu("a", "b"),
                         self.prvaDvojica)

    def testKolkoPrvkovObochDvojicJeZhodnych_2(self):
        self.assertEqual(
            parovacka.kolkoPrvkovObochDvojicJeZhodnych(
                self.druhaDvojica,
                self.tretiaDvojica),
            2)





















    # def testSuDveDvojiceZhodne_TeloMetody(self):
    #     self.assertTrue(len(self.druhaDvojica.intersection(self.tretiaDvojica)) == 2, 2)
    #
    # def testSuDveDvojiceZhodne_Inline(self):
    #     self.assertTrue(suDveDvojiceZhodne(self.druhaDvojica, self.tretiaDvojica), True)
    #
    # def testSuDveDvojiceZhodne_Inline(self):
    #     self.assertTrue(parovacka.suDveDvojiceZhodne(self.druhaDvojica,
    #                                                  self.tretiaDvojica),
    #                     True)
    #
    # def testSuDveDvojiceZhodne_ZoSetov_NieSu(self):
    #     self.assertTrue(suDveDvojiceZhodne(self.prvaDvojica,
    #                                        self.druhaDvojica),
    #                     False)
