from .context import mango


def test_instruction_type_init_mango_group():
    actual = mango.InstructionType(0)
    assert actual == mango.InstructionType.InitMangoGroup


def test_instruction_type_init_margin_account():
    actual = mango.InstructionType(1)
    assert actual == mango.InstructionType.InitMarginAccount


def test_instruction_type_deposit():
    actual = mango.InstructionType(2)
    assert actual == mango.InstructionType.Deposit


def test_instruction_type_withdraw():
    actual = mango.InstructionType(3)
    assert actual == mango.InstructionType.Withdraw


def test_instruction_type_add_to_spot_market():
    actual = mango.InstructionType(4)
    assert actual == mango.InstructionType.AddSpotMarket


def test_instruction_type_add_to_basket():
    actual = mango.InstructionType(5)
    assert actual == mango.InstructionType.AddToBasket


def test_instruction_type_borrow():
    actual = mango.InstructionType(6)
    assert actual == mango.InstructionType.Borrow


def test_instruction_type_cache_prices():
    actual = mango.InstructionType(7)
    assert actual == mango.InstructionType.CachePrices


def test_instruction_type_cache_root_banks():
    actual = mango.InstructionType(8)
    assert actual == mango.InstructionType.CacheRootBanks


def test_instruction_type_place_spot_order():
    actual = mango.InstructionType(9)
    assert actual == mango.InstructionType.PlaceSpotOrder


def test_instruction_type_add_oracle():
    actual = mango.InstructionType(10)
    assert actual == mango.InstructionType.AddOracle


def test_instruction_type_add_perp_market():
    actual = mango.InstructionType(11)
    assert actual == mango.InstructionType.AddPerpMarket


def test_instruction_type_place_perp_order():
    actual = mango.InstructionType(12)
    assert actual == mango.InstructionType.PlacePerpOrder


def test_instruction_type_cancel_perp_order_by_client_id():
    actual = mango.InstructionType(13)
    assert actual == mango.InstructionType.CancelPerpOrderByClientId


def test_instruction_type_cancel_perp_order():
    actual = mango.InstructionType(14)
    assert actual == mango.InstructionType.CancelPerpOrder


def test_instruction_type_consume_events():
    actual = mango.InstructionType(15)
    assert actual == mango.InstructionType.ConsumeEvents


def test_instruction_type_cache_perp_markets():
    actual = mango.InstructionType(16)
    assert actual == mango.InstructionType.CachePerpMarkets


def test_instruction_type_update_funding():
    actual = mango.InstructionType(17)
    assert actual == mango.InstructionType.UpdateFunding


def test_instruction_type_set_oracle():
    actual = mango.InstructionType(18)
    assert actual == mango.InstructionType.SetOracle


def test_instruction_type_settle_funds():
    actual = mango.InstructionType(19)
    assert actual == mango.InstructionType.SettleFunds


def test_instruction_type_cancel_spot_order():
    actual = mango.InstructionType(20)
    assert actual == mango.InstructionType.CancelSpotOrder


def test_instruction_type_update_root_bank():
    actual = mango.InstructionType(21)
    assert actual == mango.InstructionType.UpdateRootBank


def test_instruction_type_settle_pnl():
    actual = mango.InstructionType(22)
    assert actual == mango.InstructionType.SettlePnl


def test_instruction_type_settle_borrow():
    actual = mango.InstructionType(23)
    assert actual == mango.InstructionType.SettleBorrow
