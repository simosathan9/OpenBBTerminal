"""Finviz Fetcher Tests."""

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_finviz.models.compare_groups import FinvizCompareGroupsFetcher
from openbb_finviz.models.equity_profile import FinvizEquityProfileFetcher
from openbb_finviz.models.key_metrics import FinvizKeyMetricsFetcher
from openbb_finviz.models.price_performance import FinvizPricePerformanceFetcher
from openbb_finviz.models.price_target import FinvizPriceTargetFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [
            ("User-Agent", None),
            ("Cookie", "MOCK_COOKIE"),
            ("Set-Cookie", "MOCK_COOKIE"),
        ],
        "filter_query_parameters": [
            ("Cookie", "MOCK_COOKIE"),
            ("Set-Cookie", "MOCK_COOKIE"),
        ],
    }


@pytest.mark.record_http
def test_finviz_price_target_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = FinvizPriceTargetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_price_performance_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = FinvizPricePerformanceFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_key_metrics_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = FinvizKeyMetricsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_equity_profile_fetcher(credentials=test_credentials):
    params = {"symbol": "AAPL"}

    fetcher = FinvizEquityProfileFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_finviz_compare_groups_fetcher(credentials=test_credentials):
    params = {"group": "country", "metric": "performance"}

    fetcher = FinvizCompareGroupsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
