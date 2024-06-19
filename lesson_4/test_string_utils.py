import pytest
from string_utils import StringUtils
string_utils = StringUtils()

@pytest.mark.parametrize('str, result', [('avito', 'Avito'), ('123', '123'), ('война и мир', 'Война и мир')])
def test_capitalize_positive(str, result):
    str1 = StringUtils()
    res = str1.capitilize(str)
    assert res == result

@pytest.mark.parametrize('str', ["", " ", None])
def test_capitalize_negative(str):
    str2 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str2.capitilize(str)
 
@pytest.mark.parametrize('str, result', [(' чудный', 'чудный'), ('  хороший день', 'хороший день'), ('                        769769', '769769'), ('  POTTER', 'POTTER')])
def test_trim_positive(str, result):
    str3 = StringUtils()
    res = str3.trim(str)
    assert res == result

@pytest.mark.parametrize('str', ["", " ", None])
def test_trim_negative(str):
    str4 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str4.trim(str)

@pytest.mark.parametrize('str, delimetr, result', [("69:68:67", ":", ["69", "68", "67"]), ("aaa,bbb,ccc", ",", ["aaa", "bbb","ccc"]), \
                                                   ("л м н", " ", ["л", "м", "н"]), ("абр,а,кад,аб,ра",",", ["абр", "а", "кад", "аб", "ра"])])
def test_split_positive(str, delimetr, result):
    str5 = StringUtils()
    res = str5.to_list(str, delimetr)
    assert res == result 

def test_split_empty_str():
    str6 = StringUtils()
    res = str6.to_list(" ", "")
    assert res == []

@pytest.mark.parametrize('str, symbol, result', [("Юнона и Авось", "и", True), ("helicopter", "r", True), ("12*6%43", "p", False)])
def test_contains_positive(str, symbol, result):
    str7 = StringUtils()
    res = str7.contains(str, symbol)
    assert res == result

@pytest.mark.parametrize('str, symbol', [("", ""), (" ", " "), (None, None)])
def test_contains_negative(str, symbol):
    str8 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str8.contains(str, symbol)

@pytest.mark.parametrize('str, symbol, result', [("Кровавое воскресенье", "Кровавое ", "воскресенье"), ("кукушка", "ку", "шка"),\
                                                 ("88008888888", "88008888888", "")])
def test_delete_symbol_positive(str, symbol, result):
    str9 = StringUtils()
    res = str9.delete_symbol(str, symbol)
    assert res == result

@pytest.mark.parametrize('str, symbol, result', [("Lady", "t", "Lady"), ("%$%$%$%", "1", "%$%$%$%")])
def test_delete_symbol_negative(str, symbol, result):
    str10 = StringUtils()
    res = str10.delete_symbol(str, symbol)
    assert res == result

@pytest.mark.parametrize('str, symbol', [("", ""), (" ", " "), (None, None)])
def test_delete_symbol_negative_empty(str, symbol):
    str11 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str11.delete_symbol(str, symbol)

@pytest.mark.parametrize('str, symbol, result', [("Суперкубок", "С", True), ("корабли лавировали", "к", True), ("88008888888", "9", False)])
def test_starts_with_positive(str, symbol, result):
    str12 = StringUtils()
    res = str12.starts_with(str, symbol)
    assert res == result

@pytest.mark.parametrize('str, symbol', [("", ""), (" ", " "), (None, None)])
def test_starts_with_negative_empty(str, symbol):
    str13 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str13.starts_with(str, symbol)

@pytest.mark.parametrize('str, symbol, result', [("Хали-гали", "и", True), ("%^&%^&@", "@", True), ("Stay with me", "u", False)])
def test_end_with_positive(str, symbol, result):
    str14 = StringUtils()
    res = str14.end_with(str, symbol)
    assert res == result

@pytest.mark.parametrize('str, symbol', [("", ""), (" ", " "), (None, None)])
def test_end_with_positive_empty(str, symbol):
    str15 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str15.end_with(str, symbol)

@pytest.mark.parametrize('str, result', [("Хали-гали", False), ("------", False), ("", True), (" ", True), (None, True)])
def test_is_empty_positive(str, result):
    str16 = StringUtils()
    res = str16.is_empty(str)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [([7, 8, 9, 10], " ", "7 8 9 10"), (["q", "w", "e", "r", "t", "y"], ", ", "q, w, e, r, t, y"),\
                                                  (["Юлия", "Алексей", "Богдан"], "-", "Юлия-Алексей-Богдан")])
def test_list_to_string_positive(lst, joiner, result):
    str17 = StringUtils()
    res = str17.list_to_string(lst, joiner)
    assert res == result

@pytest.mark.parametrize('lst, joiner', [("", ""), (" ", " "), (None, None)])
def list_to_string_negative(lst, joiner):
    str18 = StringUtils()
    with pytest.raises(ValueError, match="must be 0 or None"):
        str18.list_to_string(lst, joiner)
