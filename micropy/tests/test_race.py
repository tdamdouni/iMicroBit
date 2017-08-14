import pytest
import race


@pytest.fixture()
def init():
    return race.Init()


@pytest.fixture()
def game():
    return race.Game()


@pytest.fixture()
def endgame():
    return race.EndGame(42)


def test_init(init):
    h, o = init.run()
    assert h is init
    assert o.data == 'arrow_w'
    init.tick(400)
    h, o = init.run()
    assert h is init
    assert o.data == 'arrow_w'
    init.tick(400)
    h, o = init.run()
    assert h is init
    assert o.data == 'happy'
    init.tick(400)
    h, o = init.run()
    assert h is init
    assert o.data == 'arrow_w'


def test_init_a(init):
    h, o = init.run(button_a=True)
    assert isinstance(h, race.Game)
    assert o == ''


def test_game_start(game):
    h, o = game.run()
    assert h is game
    assert o.data == '00000:00000:00000:00000:00900'


def test_game_left(game):
    h, o = game.run(button_a=True)
    assert o.data.endswith('09000')
    h, o = game.run(button_a=True)
    assert o.data.endswith('90000')
    h, o = game.run(button_a=True)
    assert o.data.endswith('90000')


def test_game_right(game):
    h, o = game.run(button_b=True)
    assert o.data.endswith('00090')
    h, o = game.run(button_b=True)
    assert o.data.endswith('00009')
    h, o = game.run(button_b=True)
    assert o.data.endswith('00009')


def move_game(game, rows=1):
    for i in range(rows):
        game.tick(game.delay)
        h, o = game.run()
    return o


def test_game_move(game, mocker):
    mocker.patch('random.randint', return_value=0)
    o = move_game(game)
    assert o.data.startswith('50000:00000')
    assert game.delay == 490
    o = move_game(game)
    assert o.data.startswith('00000:50000')
    assert game.delay == 481
    o = move_game(game)
    assert o.data.startswith('50000:00000:50000')


def test_game_crash(game, mocker):
    mocker.patch('random.randint', return_value=2)
    o = move_game(game, rows=5)
    h, o = game.run()
    assert isinstance(h, race.EndGame)
    assert h.score == 5


def test_endgame(endgame):
    h, o = endgame.run()
    assert h is endgame
    assert o is None
    endgame.tick(1001)
    h, o = endgame.run()
    assert h is endgame
    assert o == 'score 42'
    h, o = endgame.run()
    assert h is endgame
    assert o is None


def test_endgame_button(endgame):
    h, o = endgame.run(button_a=True)
    assert h is endgame
    endgame.tick(1001)
    h, o = endgame.run(button_a=True)
    assert isinstance(h, race.Game)
