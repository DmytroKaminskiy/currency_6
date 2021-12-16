from unittest.mock import MagicMock

from currency.models import Rate
from currency.tasks import parse_privatbank


def test_parse_privatbank(mocker):
    privatbank_response = [
        {"ccy":"USD","base_ccy":"UAH","buy":"26.90000","sale":"27.39726"},
        {"ccy":"EUR","base_ccy":"UAH","buy":"30.50000","sale":"30.95975"},
        {"ccy":"RUR","base_ccy":"UAH","buy":"0.35600","sale":"0.38600"},
        {"ccy":"BTC","base_ccy":"USD","buy":"45814.5781","sale":"50637.1653"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_response),
    )
    initial_rate_count = Rate.objects.count()
    parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args_list[0][0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'

    parse_privatbank()
    assert Rate.objects.count() == initial_rate_count + 2
    assert requests_get_mock.call_count == 2
