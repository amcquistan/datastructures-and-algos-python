
import pytest

from dsa.custom.datastructures import LinkedList


def test_add():
    # arrange
    ll = LinkedList()

    # act
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # assert
    actual = [x for x in ll]
    assert actual == [1, 2, 3]
    assert len(ll) == 3

def test_add_by_index():
    # arrange
    ll = LinkedList()

    # act
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(0.5, index=0)
    ll.add(1.5, index=1)
    ll.add(2.5, index=3)
    ll.add(4)

    # assert
    actual = [x for x in ll]
    assert actual == [0.5, 1, 1.5, 2, 2.5, 3, 4]
    assert len(ll) == 7


def test_add_with_index_exception():
    # arrange
    ll = LinkedList()

    # act / assert 1
    with pytest.raises(IndexError):
        ll.add(10, index=2)

    # act 2
    ll.add(1)
    ll.add(2)

    # assert 2
    with pytest.raises(IndexError):
        ll.add(10, index=5)


def test_remove():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)

    # act
    removed = ll.remove(2)

    # assert
    actual = [x for x in ll]
    assert removed is True
    assert actual == [1, 3, 4]
    assert len(ll) == 3


def test_remove_noop():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # act
    removed = ll.remove(4)

    # assert
    actual = [x for x in ll]
    assert removed is False
    assert actual == [1, 2, 3]
    assert len(ll) == 3


def test_reverse():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # act
    ll.reverse()

    # assert
    actual = [x for x in ll]
    assert actual == [3, 2, 1]
    assert len(ll) == 3


def test_empty_when_empty():
    # arrange
    ll = LinkedList()

    # assert
    assert ll.empty()


def test_empty_when_not_empty():
    # arrange
    ll = LinkedList()

    # act
    ll.add(1)

    # assert
    assert not ll.empty()


def test_clear():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # act
    ll.clear()

    # assert
    actual = [x for x in ll]
    assert actual == []
    assert len(ll) == 0
    assert ll.empty()


def test_index():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # act 1
    zeroth = ll.index(1)
    first = ll.index(2)
    last = ll.index(3)
    missing = ll.index(100)

    # assert
    assert zeroth == 0
    assert first == 1
    assert last == 2
    assert missing == -1


def test_setitem_getitem():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # act 1
    ll[0] = 10
    ll[1] = 20
    ll[2] = 30

    # assert
    assert ll[0] == 10
    assert ll[1] == 20
    assert ll[2] == 30


def test_getitem_with_index_exception():
    # arrange
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)

    # act / assert
    with pytest.raises(IndexError):
        ll[10]
