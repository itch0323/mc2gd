import json
import pytest

from jismeshcode.jismeshcode import mc2geojson


@pytest.mark.parametrize(
    "geojson",
    [
        # 4
        {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[138, 36.0], [139, 36.0], [
            139, 36.666666666666664], [138, 36.666666666666664], [138, 36.0]]]}, 'properties': {'meshcode': '5438'}},
        # 6
        {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[138.375, 36.166666666666664], [
            138.5, 36.166666666666664], [138.5, 36.25], [138.375, 36.25], [138.375, 36.166666666666664]]]}, 'properties': {'meshcode': '543823'}},
        # 8
        {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[138.4125, 36.199999999999996], [
            138.42499999999998, 36.199999999999996], [138.42499999999998, 36.20833333333333], [138.4125, 36.20833333333333], [138.4125, 36.199999999999996]]]}, 'properties': {'meshcode': '54382343'}},
        # 9
        {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[138.4125, 36.199999999999996], [
            138.41875, 36.199999999999996], [138.41875, 36.204166666666666], [138.4125, 36.204166666666666], [138.4125, 36.199999999999996]]]}, 'properties': {'meshcode': '543823431'}},
        # 10
        {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[138.415625, 36.199999999999996], [
            138.41875000000002, 36.199999999999996], [138.41875000000002, 36.20208333333333], [138.415625, 36.20208333333333], [138.415625, 36.199999999999996]]]}, 'properties': {'meshcode': '5438234312'}},
        # 11
        {'type': 'Feature', 'geometry': {'type': 'Polygon', 'coordinates': [[[138.415625, 36.20104166666666], [
            138.4171875, 36.20104166666666], [138.4171875, 36.20208333333333], [138.415625, 36.20208333333333], [138.415625, 36.20104166666666]]]}, 'properties': {'meshcode': '54382343123'}}
    ]
)
def test_mc2geojson(geojson):
    meshcode = geojson['properties']['meshcode']
    result = mc2geojson(meshcode)
    assert result == json.dumps(geojson)


def test_invalid_input():
    with pytest.raises(ValueError):
        mc2geojson('invalid_meshcode')
    with pytest.raises(ValueError):
        mc2geojson('')
    with pytest.raises(TypeError):
        mc2geojson(None)


def test_invalid_meshcode():
    with pytest.raises(ValueError):
        mc2geojson('1')  # メッシュコードは4桁以上
    with pytest.raises(ValueError):
        mc2geojson('12')  # メッシュコードは4桁以上
    with pytest.raises(ValueError):
        mc2geojson('123')  # メッシュコードは4桁以上
