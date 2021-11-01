import pytest


from dsa.custom.datastructures import Queue


def test_add():
    # arrange
    queue = Queue()

    # act 1
    queue.add(1)

    # assert 1
    assert len(queue) == 1

    # act 2
    queue.add(2)

    # assert 2
    assert len(queue) == 2



def test_clear():
    # arrange
    queue = Queue()
    queue.add(10)
    queue.add(20)
    queue.add(30)

    # act
    queue.clear()

    # assert
    assert len(queue) == 0


def test_peek():
    # arrange
    queue = Queue()
    queue.add(10)
    queue.add(20)
    queue.add(30)

    # act
    item = queue.peek()

    # assert
    assert item == 10
    assert len(queue) == 3


def test_pop():
    # arrange
    queue = Queue()
    queue.add(10)
    queue.add(20)
    queue.add(30)

    # act
    item = queue.pop()

    # assert
    assert item == 10
    assert len(queue) == 2
