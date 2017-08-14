import life
import pytest


@pytest.fixture(scope='function')
def gol():
    data = [0b00010,
            0b01000,
            0b00110,
            0b00010,
            0b00111]
    return life.GameOfLife(size=5, data=data)


def test_get_pixel(gol):
    assert not gol.get_pixel(0, 0)
    assert gol.get_pixel(1, 1)
    assert gol.get_pixel(-1, -1)
    assert not gol.get_pixel(-1, -2)


def test_set_pixel(gol):
    gol.set_pixel(0, 0, 1)
    assert gol.get_pixel(0, 0)
    gol.set_pixel(0, 0, 0)
    assert not gol.get_pixel(0, 0)


def test_step(gol):
    expect = [0b00011,
              0b00010,
              0b00110,
              0b00000,
              0b00101]
    gol.step()
    assert gol.data == expect


def test_image(gol):
    expect = '00090:09000:00990:00090:00999'
    assert gol.gen_image().data == expect
    gol.move(2, 2)
    moved_expect = '99000:09000:99900:09000:00009'
    assert gol.gen_image().data == moved_expect
    gol.move(-2, -2)
    assert gol.gen_image().data == expect
    gol.move(-3, -3)
    assert gol.gen_image().data == moved_expect


def is_alive(gol):
    assert gol.is_alive()
    gol.data = [0] * 5
    assert not gol.is_alive()


def test_randomize(gol):
    gol.randomize(20)
    assert gol.is_alive()
    gol.step()
