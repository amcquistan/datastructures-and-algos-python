import pytest

from dsa.custom.datastructures import Stack


def test_push():
    # arrange
    stack = Stack()

    # act 1
    stack.push(1)

    # assert 1
    assert len(stack) == 1

    # act 2
    stack.push(2)

    # assert 2
    assert len(stack) == 2


def test_clear():
    # arrange
    stack = Stack()
    stack.push(2)

    # act
    stack.clear()

    # assert
    assert len(stack) == 0


def test_peek():
    # arrange
    stack = Stack()
    stack.push(10)
    stack.push(20)

    # act
    item = stack.peek()

    # assert
    assert item == 20
    assert len(stack) == 2


def test_pop():
    # arrange
    stack = Stack()
    stack.push(10)
    stack.push(20)

    # act
    item = stack.pop()

    # assert
    assert item == 20
    assert len(stack) == 1
