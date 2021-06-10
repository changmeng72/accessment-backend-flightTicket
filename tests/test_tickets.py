import pytest
import json
from flaskr.flight import tickets

 
def test_ticketid_already_exist(client,app):
    res= client.post( '/api/tickets',data=json.dumps({ 'event':{ 
                                        "ticketId":1,
                                        "flightDate": "2021-11-01",
                                        "flightNumber": "AC1",
                                        "seatNumber": "EE31",
"ticketCost": 100000
 }}),content_type="application/json")
    print(res.data)
    assert res.status_code == 400 and b"ticketId already exists" in res.data
     
def test_missing_ticketId(client,app):
    res= client.post( '/api/tickets',data=json.dumps({ 'event':{ 
                                        
                                        "flightDate": "2021-11-01",
                                        "flightNumber": "AC1",
                                        "seatNumber": "EE31",
"ticketCost": 100000
 }}),content_type="application/json")
    print(res.data)
    assert res.status_code == 400 and b"ticketId is required" in res.data    
    
def test_missing_flightDate(client,app):
    res= client.post( '/api/tickets',data=json.dumps({ 'event':{ 
                                        "ticketId":1,
                                        
                                        "flightNumber": "AC1",
                                        "seatNumber": "EE31",
"ticketCost": 100000
 }}),content_type="application/json")
    print(res.data)
    assert res.status_code == 400 and b"flightDate is required" in res.data    
   
##
def test_missing_flightNumber(client,app):
    res= client.post( '/api/tickets',data=json.dumps({  'event':{
                                        "ticketId":1,
                                        "flightDate": "2021-11-01",
                                        "flightNumber2": "AC1",
                                        "seatNumber": "EE31",
"ticketCost": 100000
 }}),content_type="application/json")
    print(res.data)
    assert res.status_code == 400 and b"flightNumber is required" in res.data    
##   
def test_missing_seatNumber(client,app):
    res= client.post( '/api/tickets',data=json.dumps({  'event':{
                                        "ticketId":1,
                                        "flightDate": "2021-11-01",
                                        "flightNumber": "AC1",                                       
                    "ticketCost": 100000
            }}),content_type="application/json")
    print(res.data)
    assert res.status_code == 400 and b"seatNumber is required" in res.data    
 
## 
def test_create_a_new_ticket_ok(client,app):
    
    ticketNum = len(tickets)
    ids = [ticket.ticketId for ticket in tickets]  
    assert  not 10 in ids
    res= client.post( '/api/tickets',data=json.dumps({  'event':{
                                        "ticketId":10,
                                        "flightDate": "2021-11-01",
                                        "flightNumber": "AC1",   
                                        "seatNumber": "EE31",
                      "ticketCost": 500000
            }}),content_type="application/json")
    print(res.data)
    assert res.status_code == 200 and b"success" in res.data  
    assert ticketNum+1==len(tickets)
 
#############
def test_assert_new_created_ticket(client,app):
    
    ids = [ticket.ticketId for ticket in tickets]    
    print(ids)
    assert  10 in ids

 