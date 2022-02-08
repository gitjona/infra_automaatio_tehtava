from postinumerot import find

start = "Postinumerot: "

def test_kiuruvesi():

    res = find("Kiuruvesi")
    assert res == start+("74701 74700")

def test_yli_olhava():

    res = find("Yli-Olhava")
    assert res == start+("91150")


def test_smartpost():
    space = find("SMART POST")
    post = find("SMARTPOST")
    
    res = True
    
    if len(space) != len(post):
        res = False
    
    assert res == True
