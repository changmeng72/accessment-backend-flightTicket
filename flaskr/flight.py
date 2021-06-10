class Flight:
    def __init__(self,flightNum,flightDate):
        self.flightNum = flightNum
        self.flightDate = flightDate
     
     
    
    
    @staticmethod  
    def getAllFlights(startDate,endDate):
        allflights =  list(filter(lambda x: startDate<=x.flightDate<=endDate,flights))
        allflights.sort(key=lambda x: x.flightDate)
        return allflights
        
        
    @staticmethod 
    def validFlight(flightNum,flightDate):
        return len(list(filter(lambda x: flightDate==x.flightDate and flightNum==x.flightNum,flights)))!=0
    @staticmethod 
    def getFlight(flightNum,flightDate):
        r = None
        for element in filter(lambda x: flightDate==x.flightDate and flightNum==x.flightNum,flights):    
            r = element
            break
        return r
    
             
	

            

class Ticket:
    def __init__(self,flight,ticketId,seatNum,cost):
        self.flight  = flight
        self.seatNum=seatNum
        self.cost = cost
        self.ticketId = ticketId
        
    @staticmethod    
    def validId(id):         
        return  len(list(filter(lambda x: x.ticketId==id,tickets))) == 0 
    @staticmethod
    def validSeatNum(flight,seatNum):
        return  len(list(filter(lambda x: x.seatNum==seatNum and x.flight==flight,tickets)))==0 
    def generateNewTicket(newTicket):
        tickets.append(newTicket)
        
    @staticmethod 
    def getTickets(flight):
        return list(filter(lambda x: x.flight==flight,tickets))
                                         
        
flights=[   Flight('AC1','2021-11-01'),
            Flight('AC1','2021-11-02'),
            Flight('AC2','2021-11-02'),
            Flight('AC1','2021-11-04'),
            Flight('AC1','2021-11-05')]
tickets=[  Ticket(flights[0],1,'1A',3000000),
            Ticket(flights[0],2,'A05',8000000),
            Ticket(flights[1],3,'E31',1000000),
            Ticket(flights[2],4,'A31',2000000),
            Ticket(flights[1],5,'B01',3000000),
            Ticket(flights[3],6,'G51',4000000)
            ]
