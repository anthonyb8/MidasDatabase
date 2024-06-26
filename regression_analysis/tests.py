import json
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from account.models import CustomUser
from .models import RegressionAnalysis
from symbols.models import Symbol, SecurityType
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from market_data.models import BarData, QuoteData, Symbol

class Base(APITestCase):
    def setUp(self):
        # Set up the client
        self.client = APIClient()

        # Set up authentication
        self.user = CustomUser.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

class Regression(Base):
    def setUp(self):
        super().setUp()

        # url
        self.url="/api/regression_analysis/"

        # Create an asset class instance
        self.ticker="AAPL"
        self.security_type = SecurityType.objects.create(value="STOCK")
        self.symbol = Symbol.objects.create(ticker=self.ticker, security_type=self.security_type)
        self.bar_data = BarData.objects.create(symbol=self.symbol,
                                                    timestamp=1707307740000000000,
                                                    open=100.99999,
                                                    high=100.99999,
                                                    low=100.99999,
                                                    close=100.99999,
                                                    volume=100.99999,
                                                    )
        self.backtest_data={
                            "parameters": {
                                "strategy_name": "cointegrationzscore", 
                                "capital": 100000, 
                                "data_type": "BAR", 
                                "train_start": 1704862800, 
                                "train_end": 1704893000, 
                                "test_start": 1704903000, 
                                "test_end": 1705903000, 
                                "tickers": [self.ticker], 
                                "benchmark": ["^GSPC"]
                            },
                            "static_stats": [{
                                "net_profit": 330.0, 
                                "total_fees": 40.0, 
                                "ending_equity": 1330.0, 
                                "avg_trade_profit": 165.0, 
                                "total_return": 0.33, 
                                "annual_standard_deviation_percentage": 0.23, 
                                "max_drawdown_percentage": 0.0, 
                                "avg_win_percentage": 0.45, 
                                "avg_loss_percentage": 0, 
                                "percent_profitable": 1.0, 
                                "total_trades": 2, 
                                "number_winning_trades": 2, 
                                "number_losing_trades": 0, 
                                "profit_and_loss_ratio": 0.0, 
                                "profit_factor": 0.0, 
                                "sortino_ratio": 0.0,
                                "sharpe_ratio": 10.72015,
                            }],
                            "period_timeseries_stats": [
                                {
                                    "timestamp": 1704903000,
                                    "equity_value": 10000.0,
                                    "percent_drawdown": 9.9, 
                                    "cumulative_return": -0.09, 
                                    "period_return": 79.9,
                                    "daily_strategy_return": "0.330", 
                                    "daily_benchmark_return": "0.00499"
                                },
                                {
                                    "timestamp": 1704904000,
                                    "equity_value": 10000.0,
                                    "percent_drawdown": 9.9, 
                                    "cumulative_return": -0.09, 
                                    "period_return": 79.9,
                                    "daily_strategy_return": "0.087", 
                                    "daily_benchmark_return": "0.009"
                                }
                            ],
                            "daily_timeseries_stats": [
                                {
                                    "timestamp": 1704903000,
                                    "equity_value": 10000.0,
                                    "percent_drawdown": 9.9, 
                                    "cumulative_return": -0.09, 
                                    "period_return": 79.9,
                                    "daily_strategy_return": "0.330", 
                                    "daily_benchmark_return": "0.00499"
                                },
                                {
                                    "timestamp": 1704904000,
                                    "equity_value": 10000.0,
                                    "percent_drawdown": 9.9, 
                                    "cumulative_return": -0.09, 
                                    "period_return": 79.9,
                                    "daily_strategy_return": "0.087", 
                                    "daily_benchmark_return": "0.009"
                                }
                            ],
                            "trades": [{
                                "trade_id": 1, 
                                "leg_id": 1, 
                                "timestamp": 1704903000, 
                                "ticker": "AAPL", 
                                "quantity": 4, 
                                "avg_price": 130.74, 
                                "trade_value": -522.96, 
                                "action": "BUY", 
                                "fees": 0.0
                            }],
                            "signals": [{
                                "timestamp": 1704903000, 
                                "trade_instructions": [{
                                    "ticker": "AAPL", 
                                    "action": "BUY", 
                                    "trade_id": 1, 
                                    "leg_id": 1, 
                                    "weight": 0.05
                                }, 
                                {
                                    "ticker": "MSFT", 
                                    "action": "SELL", 
                                    "trade_id": 1, 
                                    "leg_id": 2, 
                                    "weight": 0.05
                                }]
                            }]
                            }

        response = self.client.post("/api/backtest/", data=self.backtest_data, format='json')
        self.backtest_id = response.data['id']

        # Mock Data
        self.regression_data={
                                "backtest":self.backtest_id,
                                "risk_free_rate":0.02,
                                "r_squared":0.95,
                                "adjusted_r_squared":0.94,
                                "RMSE":0.01,
                                "MAE":0.02,
                                "f_statistic":50.0,
                                "f_statistic_p_value":0.0001,
                                "durbin_watson":2.0,
                                "jarque_bera":5.0,
                                "jarque_bera_p_value":0.05,
                                "condition_number":10.0,
                                "vif":{'beta1': 1.5, 'beta2': 2.0},
                                "alpha":0.05,
                                "p_value_alpha":0.01,
                                "beta":{'beta1': 1.2, 'beta2': 0.8},
                                "p_value_beta":{'beta1': 0.05, 'beta2': 0.01},
                                "total_contribution":0.5,
                                "systematic_contribution":0.3,
                                "idiosyncratic_contribution":0.2,
                                "total_volatility":0.15,
                                "systematic_volatility":0.1,
                                "idiosyncratic_volatility":0.05,
                                "residuals":[0.1, -0.2, 0.05, -0.1], 
                                "timeseries_data": [
                                    {'timestamp': 1709874000000000000, 'daily_benchmark_return': -0.007275}, 
                                    {'timestamp': 1710129600000000000, 'daily_benchmark_return': 0.004111}, 
                                    {'timestamp': 1710216000000000000, 'daily_benchmark_return': -0.000783}, 
                                    {'timestamp': 1710302400000000000, 'daily_benchmark_return': 0.015980}, 
                                    {'timestamp': 1710388800000000000, 'daily_benchmark_return': 0.006242}, 
                                    {'timestamp': 1710475200000000000, 'daily_benchmark_return': 0.002596}, 
                                    {'timestamp': 1710734400000000000, 'daily_benchmark_return': 0.012271}, 
                                    {'timestamp': 1710820800000000000, 'daily_benchmark_return': 0.000875}, 
                                    {'timestamp': 1710907200000000000, 'daily_benchmark_return': -0.009881}
                                ]
                            }
        
    def test_create(self):
        # test
        response = self.client.post(self.url, data=self.regression_data, format='json')

        # validate
        self.assertEqual(response.status_code, 201)
        self.assertEqual(RegressionAnalysis.objects.count(), 1)

    def test_create_duplicate(self):
        # set-up
        self.client.post(self.url, data=self.regression_data, format='json')

        # test
        response = self.client.post(self.url, data=self.regression_data, format='json')

        # validate
        self.assertEqual(RegressionAnalysis.objects.count(), 1)

    def test_get(self):
        # set-up
        self.client.post(self.url, data=self.regression_data, format='json')
        url = f"{self.url}{self.backtest_id}/"

        # test
        response = self.client.get(url)

        # validate
        self.assertEqual(response.status_code, 200)
        self.assertIn('backtest', response.data)
        self.assertIn('r_squared', response.data)
        self.assertIn('alpha', response.data)
        self.assertIn('p_value_alpha', response.data)
        self.assertIn('beta', response.data)
        self.assertIn('p_value_beta', response.data)
        self.assertIn('risk_free_rate', response.data)
        self.assertIn('systematic_contribution', response.data)
        self.assertIn('idiosyncratic_contribution', response.data)
        self.assertIn('systematic_volatility', response.data)
        self.assertIn('idiosyncratic_volatility', response.data)
        self.assertIn('total_volatility', response.data)
        self.assertIn('timeseries_data', response.data)

    def test_delete(self):
        # set-up
        self.client.post(self.url, data=self.regression_data, format='json')
        url = f"{self.url}{self.backtest_id}/"

        # test
        response = self.client.delete(url)

        # validate
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(RegressionAnalysis.objects.count(), 0)



    