import os
import smard

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "Realisierte_Erzeugung.csv")


def test_import_data_loads_dataframe():
    d = smard.SmartData()
    d.import_data(DATA)
    assert d.data is not None
    assert len(d.data) > 0
