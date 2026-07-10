from benchmark.result_layout import make_hw_id


def test_make_hw_id_uses_stamped_sku_m1m():
    fp = {"product_name": "RPi5B",
          "npu": {"modules": [{"product": "M1M", "count": 1}], "sku": "M1M"}}
    assert make_hw_id(fp) == "RPi5B_M1M"


def test_make_hw_id_backfills_from_raw_h1():
    raw = ("\n".join([" * Device %d: M1, Accelerator type\n"
                      " * Memory : LPDDR5x 6000 Mbps, 3.92GiB\n"
                      " * Board  : H1, Rev 0.0" % i for i in range(4)]))
    fp = {"product_name": "BIOSTAR", "npu": {"raw": raw}}
    assert make_hw_id(fp) == "BIOSTAR_H1-Quattro"


def test_make_hw_id_two_m1_from_device_count():
    fp = {"product_name": "yjsong",
          "npu": {"modules": [{"product": "M1", "count": 2}], "sku": "M1x2"}}
    assert make_hw_id(fp) == "yjsong_M1x2"
