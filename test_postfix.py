import postfix_program


def test_post_str():
    ret = postfix_program.postfix("abcd")
    assert ret == False


def test_postfix():
    ret = postfix_program.postfix("452*+")
    assert ret == 14
