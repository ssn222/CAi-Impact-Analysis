

'''
Object:
    ID
    Join date
    subscription end date
    Potential membership length (today - joinDate)
    Membership length (days)
   12 week average visits
    
'''

class member:
    
    def __init__(self, memberId):
        self._memberId = memberId
        self._joinDate = 0
        self._subscriptionEndDate = 0
        self._first12WeeksAverage = 0
        
    @property
    def memberId(self):
        return self._memberId
    #
    @memberId.setter
    def memberId(self, value):
        self._memberId = value
    #
    @property
    def joinDate(self):
        return self._joinDate
    #
    @joinDate.setter
    def joinDate(self, value):
        self._joinDate = value
        
    @property
    def subscriptionEndDate(self):
        return self._subscriptionEndDate
    #
    @subscriptionEndDate.setter
    def subscriptionEndDate(self, value):
        self._subscriptionEndDate = value
    #
    @property
    def first12WeeksAverage(self):
        return self._first12WeeksAverage
    #
    @first12WeeksAverage.setter
    def first12WeeksAverage(self, value):
        self._first12WeeksAverage = value