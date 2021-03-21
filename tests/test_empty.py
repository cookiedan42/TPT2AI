from tests import *


class Test_Initialise(unittest.TestCase):
    def test_emptyScript(self):
        intended = b'\x05empty\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        actual = Script("empty")
        assert intended == actual.asBytes()


class Test_Impulse(unittest.TestCase):
    def test_keypress(self):

        intended = b'\x05empty\x02\x00\x00\x00\x05key.1\x05key.q\x00\x00\x00\x00\x00\x00\x00\x00'
        actual = Script("empty")
        actual.addImpulse(KeyPress(1))
        actual.addImpulse(KeyPress("Q"))
        assert intended == actual.asBytes()


class Test_Comparator(unittest.TestCase):

    def test_True_Condition(self):
        intended = "BWVtcHR5AAAAAAMAAAAIY29uc3RhbnQBAQhjb25zdGFudAEBCGNvbnN0YW50AQEAAAAA"
        actual = Script("empty")
        actual.conditions = [TRUE(), TRUE(), TRUE()]
        assert intended == actual.export()

    def test_Boolean_Compare(self):
        intended = "BWVtcHR5AAAAAAEAAAAPY29tcGFyaXNvbi5ib29sCGNvbnN0YW50AQEIY29uc3RhbnQEAiE9CGNvbnN0YW50AQAAAAAA"
        actual = Script("empty")
        actual.conditions = [BoolCompare(TRUE(), String_("!="), FALSE())]
        assert intended == actual.export()

    def test_Int_Compare(self):
        intended = "BWVtcHR5AAAAAAEAAAAOY29tcGFyaXNvbi5pbnQIY29uc3RhbnQCAQAAAAhjb25zdGFudAQCPT0IY29uc3RhbnQCCQAAAAAAAAA="
        actual = Script("empty")
        actual.conditions = [IntCompare(1, "==", 9)]
        assert intended == actual.export()

    def test_Double_Compare(self):
        intended = "BWVtcHR5AAAAAAEAAAARY29tcGFyaXNvbi5kb3VibGUIY29uc3RhbnQDmpmZmZn5WMAIY29uc3RhbnQEAj09CGNvbnN0YW50A5qZmZmZ+VhAAAAAAA=="
        actual = Script("empty")
        actual.conditions = [DoubleCompare(-99.9, "==", 99.9)]
        assert intended == actual.export()

    def test_String_Compare(self):
        intended = "BWVtcHR5AAAAAAEAAAARY29tcGFyaXNvbi5zdHJpbmcIY29uc3RhbnQEA2FiYwhjb25zdGFudAQCPT0IY29uc3RhbnQEAzEyMwAAAAA="
        actual = Script("empty")
        actual.conditions = [StringCompare("abc", "==", "123")]
        assert intended == actual.export()


if __name__ == '__main__':
    unittest.main()
