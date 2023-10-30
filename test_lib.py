from lib import read_dataset, desc_stats
import unittest
from pandas.testing import assert_frame_equal

# df = pd.read_csv("../dsets/automobiles.csv")

df = read_dataset()


class TestMain(unittest.TestCase):
    def test_col_exist(self):
        col_name = "Salesperson"
        message = col_name + " column does not exist"
        # assert if columns exist
        assert {"Salesperson", "Customer Name", "Commission Earned"}.issubset(
            df.columns
        ), message

    def test_my_stats(self):
        test_stats_df = desc_stats()
        assert_frame_equal(df.describe(), test_stats_df)


if __name__ == "__main__":
    unittest.main()
