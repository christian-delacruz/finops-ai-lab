def token_cost(input_tokens, output_tokens, input_price_per_m, output_price_per_m):
    """Dollar cost of one LLM call, given prices per million tokens."""
    return (input_tokens * input_price_per_m + output_tokens * output_price_per_m) / 1_000_000
    