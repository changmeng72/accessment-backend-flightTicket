import pytest 
from flaskr.flight import tickets


def test_get_all_flights(client,app):
    res= client.get( "/api/flights?startDate=2021-11-01&endDate=2021-11-07")
    print(res.data)
    assert res.status_code == 200 
    

def test_wrong_start_date_format(client,app):
    res= client.get( "/api/flights?startDate=2021/11/01&endDate=2021-11-05")
    print(res.data)
    assert res.status_code == 400 and b"startDate format is invalid" in res.data
    
def test_wrong_state_date_null(client,app):
    res= client.get( "/api/flights?startDate=&endDate=2021-11-05")
    print(res.data)
    assert res.status_code == 400 and b"startDate is empty" in res.data
    
def test_wrong_end_date_null(client,app):
    res= client.get( "/api/flights?startDate=2021-11-05&endDate=")
    print(res.data)
    assert res.status_code == 400 and b"endDate is empty" in res.data
    
def test_wrong_end_date_null(client,app):
    res= client.get( "/api/flights?startDate=2021-11-05&endDate=2021-05")
    print(res.data)
    assert res.status_code == 400 and b"endDate format is invalid" in res.data
    
def test_without_parameters(client,app):
    res= client.get( "/api/flights")
    print(res.data)
    assert res.status_code == 400 and b"StartDate is required" in res.data
    
def test_without_enddate_parameters(client,app):
    res= client.get( "/api/flights?startDate=2021-11-05&")
    print(res.data)
    assert res.status_code == 400 and b"EndDate is required" in res.data
    
def test_enddate_earlyer_than_startdate(client,app):
    res= client.get( "/api/flights?startDate=2021-11-02&endDate=2021-11-01")
    print(res.data)
    assert res.status_code == 400 and b"endDate cannot be before startDate" in res.data
    
