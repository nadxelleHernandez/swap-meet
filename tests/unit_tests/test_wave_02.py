import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

#@pytest.mark.skip
def test_items_have_default_uuid_length_id():
    item = Item()
    assert isinstance(item.id, int)
    assert len(str(item.id)) >= 32

#@pytest.mark.skip
def test_item_instances_have_different_default_ids():
    item_a = Item()
    item_b = Item()
    assert item_a.id != item_b.id

#@pytest.mark.skip
def test_items_use_custom_id_if_passed():
    item = Item(id=12345)
    assert isinstance(item.id, int)
    assert item.id == 12345

def test_item_init_raises_exception_when_invalid_custom_id_passed():
    with pytest.raises(TypeError):
        item = Item(id=1.234)
    
def test_item_init_raises_exception_when_given_non_numeric_condition():
    with pytest.raises(TypeError):
        item = Item(condition="New")

def test_item_init_raises_exception_when_given_condition_greater_than_5():
    with pytest.raises(ValueError):
        item = Item(condition=8.0)

def test_item_init_raises_exception_when_given_condition_lesser_than_0():
    with pytest.raises(ValueError):
        item = Item(condition=-1)

#@pytest.mark.skip
def test_item_obj_returns_text_item_for_category():
    item = Item()
    assert item.get_category() == "Item"

#@pytest.mark.skip
def test_get_item_by_id():
    test_id = 12345
    item_custom_id = Item(id=test_id)
    vendor = Vendor(
        inventory=[Item(), Item(), item_custom_id]
    )

    result_item = vendor.get_by_id(test_id)
    assert result_item is item_custom_id

#@pytest.mark.skip
def test_get_item_by_id_no_matching():
    test_id = 12345
    item_a = Item()
    item_b = Item()
    item_c = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result_item = vendor.get_by_id(test_id)
    assert result_item is None

    items = vendor.inventory
    assert len(items) == 3
    assert item_a in items
    assert item_b in items
    assert item_c in items

def test_get_item_by_id_empty_inventory():
    test_id = 12345
    vendor = Vendor()

    item = vendor.get_by_id(test_id)

    assert item is None
    assert len(vendor.inventory) == 0
