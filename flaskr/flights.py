from  flask_restful import Resource, abort,reqparse,marshal_with,fields
from .flight import Ticket,Flight
from flask import request,jsonify  
import json
def pet_list_parser(pets):
    if type(pets) != list:
        raise ValueError('Expected a list!')

    # Do your validation of the pet objects here. For example:
    for pet in pets:
        if 'name' not in pet:
            raise ValueError('Pet name is required')

        # Also do any conversion of data types here
        pet['name'] = pet['name'].capitalize()

    return pets


resource_fields = {
     'status' : fields.String,
     'reason' : fields.String,
     
    }

flight_get_args = reqparse.RequestParser()
flight_get_args.add_argument("startDate",type=str,help="StartDate is required",required = True,location='args')
flight_get_args.add_argument("endDate",type=str,help="EndDate is required",required = True,location='args') 


class TicketRoute(Resource):
    
    
    def post(self):
       
        reqargs = json.loads(request.data) 
        args = reqargs["event"]
        
        if not args.get("ticketId",None):
            return  {'status': "failed",'reason': "ticketId is required"},400
        if not args.get("flightDate",None):
            return  {'status': "failed",'reason': "flightDate is required"},400
        if not args.get("flightNumber",None):
            return  {'status': "failed",'reason': "flightNumber is required"},400
        if not args.get("seatNumber",None):
            return  {'status': "failed",'reason': "seatNumber is required"},400
        if not args.get("ticketCost",None):
            return  {'status': "failed",'reason': "ticketCost is required"},400
        
        if not Ticket.validId(args["ticketId"]):
            return  {'status': "failed",'reason': "ticketId already exists"},400
        if not Flight.validFlight(args["flightNumber"],args["flightDate"]):
            return {'status': "failed",'reason': "the flight number on that flight date does not exist"},400
        flight = Flight.getFlight(args["flightNumber"],args["flightDate"])    
        if not Ticket.validSeatNum(flight,args["seatNumber"]):
            return {'status': "failed",'reason': "seatNumber already taken"},400
        
        
        ticket = Ticket(flight,args["ticketId"],args["seatNumber"],args["ticketCost"],)
        Ticket.generateNewTicket(ticket)
        
        return {"status": "success"},200
        
            
import datetime
def validateDate(date_text):
    ymd = date_text.split('-');
    if len(ymd) != 3:
        return False
    if not ( 2021<=int(ymd[0])<=2025 and  1<=int(ymd[1])<=12 and  1<=int(ymd[2])<=31):
        return False
    
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return False 
    return True
def nextDate(date_text):
    thisday = datetime.datetime.strptime(date_text, '%Y-%m-%d')
    nextday = thisday + datetime.timedelta(days = 1)
    return nextday.strftime('%Y-%m-%d')
 
class FlightRoute(Resource):
    def get(self):
        # valid the parameter: todo
        args = flight_get_args.parse_args() 
        startDate,endDate=args['startDate'],args['endDate']        
        if startDate=='':
            return {'status': "failed",'reason': "startDate is empty"},400
        if not validateDate(startDate):
            return {'status': "failed",'reason': "startDate format is invalid"},400
        if endDate=='':
            return {'status': "failed",'reason': "endDate is empty"},400
        if not validateDate(endDate):
            return {'status': "failed",'reason': "endDate format is invalid"},400
            
        if endDate<startDate:
            return {'status': "failed",'reason': "endDate cannot be before startDate"},400
        
        stard = datetime.datetime.strptime(startDate, '%Y-%m-%d')
        endd  = datetime.datetime.strptime(endDate, '%Y-%m-%d')
         
        result = []
        allflights = Flight.getAllFlights(startDate,endDate)
        if allflights:
            curDate = startDate
            flights = []
            for flight in allflights:                
                if flight.flightDate != curDate:                    
                    result.append({
                        'date':curDate,
                        'flights':flights
                        })
                    flights = []
                    nextd = nextDate(curDate)
                    while flight.flightDate!=nextd:
                        curDate = nextd
                        nextd = nextDate(nextd)
                        result.append({
                        'date':curDate,
                        'flights':[]
                        })
                        
                    curDate = flight.flightDate
                
                tickets = Ticket.getTickets(flight)
                seats = []
                revenu = 0
                if tickets:
                    revenu = sum([x.cost for x in tickets])
                    for ticket in tickets:
                        seats.append(ticket.seatNum)
                flights.append({'flightNumber':flight.flightNum,
                                 'revenu':revenu,
                                 'occupiedSeats':seats
                                })
            result.append({
                        'date':curDate,
                        'flights':flights
                        })
            while curDate< endDate:
                        curDate = nextDate(curDate)
                        result.append({
                        'date':curDate,
                        'flights':[]
                        })
              
        return {"dates":result},200
                    
                
            
        
        
        
        