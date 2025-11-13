import Lab2.bmi as ABC


def test_bmi_under_weight():
    expected = -1
    result = ABC.calculate_bmi(1.73, 37)
    assert(result == expected)


def test_bmi_normal_weight():
    expected = 0
    result = ABC.calculate_bmi(1.73, 57)
    assert(result == expected)


def test_bmi_over_weight():
    expected = 1
    result = ABC.calculate_bmi(1.73, 97)
    assert(result == expected)
