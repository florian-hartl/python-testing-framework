import mock
import pytest
from python_testing_framework import increment


@pytest.fixture
def fake_data():
  return {
    'a': 1,
    'b': 2,
    'c': 3,
  }


def test_zero():
  assert increment.zero() == 0


@pytest.mark.parametrize('num,expected', [
  (3, 4),
  (-10, -9),
  (2.5, 3.5),
])
def test_inc(num, expected):
  assert increment.inc(num) == expected


def test_inc_bad_input():
  with pytest.raises(TypeError):
    increment.inc('uh oh')


def test_zero_dict_values(fake_data):
  increment.zero_dict_values(fake_data)
  assert fake_data == {'a': 0, 'b': 0, 'c': 0}


def test_inc_dict_values(fake_data):
  increment.inc_dict_values(fake_data)
  assert fake_data == {'a': 2, 'b': 3, 'c': 4}


def test_inc_dict_objects():
  obj1 = mock.Mock(spec_set=['inc'])
  obj2 = mock.Mock(spec_set=['inc'])
  increment.inc_dict_objects({1: obj1, 2: obj2})
  assert obj1.inc.call_count == 1
  assert obj2.inc.call_count == 1


@mock.patch.object(increment, 'write_json', autospec=True, spec_set=True)
@mock.patch.object(increment, 'read_json', autospec=True, spec_set=True)
def test_inc_dict_values_from_file(read_json_patch, write_json_patch, fake_data):
  read_json_patch.return_value = fake_data
  increment.inc_dict_values_from_file(mock.sentinel.test_path)
  assert read_json_patch.call_count == 1
  assert write_json_patch.call_count == 1
  assert write_json_patch.call_args == mock.call(
    mock.sentinel.test_path,
    {'a': 2, 'b': 3, 'c': 4}
  )


@mock.patch.object(
  increment,
  'open',
  mock.mock_open(read_data='{"1": "test"}'),
)
def test_read_json():
  assert increment.read_json('test path') == {'1': 'test'}


@mock.patch.object(increment.json, 'dump', autospec=True, spec_set=True)
def test_write_json(json_dump_patch):
  with mock.patch.object(increment, 'open', mock.mock_open()) as mock_open:
    increment.write_json('test path', {'1': 'test'})
    assert json_dump_patch.call_count == 1
    assert json_dump_patch.call_args == mock.call({'1': 'test'}, mock_open())
