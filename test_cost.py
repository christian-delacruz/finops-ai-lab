from cost import token_cost

def test_known_call():
    # 2,000 input tokens at $3/M plus 500 output tokens at $15/M = $0.0135
    assert round(token_cost(2000, 500, 3.00, 15.00), 6) == 0.0200

def test_zero_tokens_costs_nothing():
    assert token_cost(0, 0, 3.00, 15.00) == 0