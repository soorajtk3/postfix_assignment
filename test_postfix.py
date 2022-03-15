import postfix_program


def test_post_str():
    ret = postfix_program.postfix("abcd")
    assert ret == False


def test_postfix():
    ret = postfix_program.postfix("452*+")
    assert ret == 14


def test_postfixsub():
    ret = postfix_program.postfix("25-")
    assert ret == 3


def test_postfixdiv():
    ret = postfix_program.postfix("22/")
    assert ret == 1


def testonly_operator():
    ret = postfix_program.postfix("/*-+*-/-/-+")
    assert ret == "error"
