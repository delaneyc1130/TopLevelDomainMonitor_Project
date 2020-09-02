"""
Monitor web accesses by top-level domain for a specified time window.
Author:  Delaney Carleton

Given a web log file and begin and end dates, compute the percentage of
web accesses, categorized by top-level domain, and display on the standard
output.
"""

import argparse

MONTHLEN = [ 0, # No month zero
    31, # 1. January
    29, # 2. February (ignoring leap years)
    31, # 3. March
    30, # 4. April
    31, # 5. May
    30, # 6. June
    31, # 7. July
    31, # 8. August
    30, # 9. September
    31, #10. October
    30, #11. November
    31, #12. December
    ]
    

class Date:

    def __init__(self, str):
        """
        The constructor for an instance of the Date class.
        It receives one argument, a string in the format 'mm/dd/yyyy'.
        If the string is in the wrong format (not three integers separated
            by '/'), or if mm < 1 or mm > 12, or if dd < 1 or dd > number
            of days in that month, or if yyyy < 1, the constructor
            should raise an Exception with a string of the form:
            'mm/dd/yyyy: incorrectly formatted date string', where mm/dd/yyyy
            is replaced by the string that was passed as an argument
        Args:
            str - string, date of the form 'mm/dd/yyyy'
        Returns:
            nothing
        Effects:
            stores away month, day, and year in 'self' for future use
        Raises:
            Exception if the string received is incorrectly formatted
        """
        self.str = str
        
        self.date = self.str.split('/')
        self.mm = int(self.date[0])
        self.dd = int(self.date[1])
        self.yyyy = int(self.date[2])
        
        try:
            int(self.mm)
            int(self.dd)
            int(self.yyyy)
            if '/' not in self.str:
                raise Exception('mm/dd/yyyy: incorrectly formatted date string')
            if len(self.date) != 3:
                raise Exception('mm/dd/yyyy: incorrectly formatted date string')
            if self.mm < 1 or self.mm > 12:
                raise Exception('mm/dd/yyyy: incorrectly formatted date string')
            elif self.dd < 1 or self.dd > MONTHLEN[self.mm]:
                raise Exception('mm/dd/yyyy: incorrectly formatted date string')
            elif self.yyyy < 1:
                raise Exception('mm/dd/yyyy: incorrectly formatted date string')
        except :
            raise Exception('mm/dd/yyyy: incorrectly formatted date string') 
            
    

    def __lt__(self, other):
        """
        Boolean function, returns True if self < other, False otherwise
        Args:
            self: Date instance to compare against other
            other: Date instance to which self is compared
        Returns:
            boolean, True if self < other, False otherwise
        """
        if (self.yyyy * 10000 + self.mm * 100 + self.dd) < (other.yyyy * 10000 + other.mm * 100 + other.dd):
            return True
        
        return False

    def __gt__(self, other):
        """
        Boolean function, returns True if self > other, False otherwise
        Args:
            self: Date instance to compare against other
            other: Date instance to which self is compared
        Returns:
            boolean, True if self > other, False otherwise
        """
        if (self.yyyy * 10000 + self.mm * 100 + self.dd) > (other.yyyy * 10000 + other.mm * 100 + other.dd):
            return True

        return False

    def __eq__(self, other):
        """
        Boolean function, returns True if self == other, False otherwise
        Args:
            self: Date instance to compare against other
            other: Date instance to which self is compared
        Returns:
            boolean, True if self == other, False otherwise
        """
        if (self.yyyy * 10000 + self.mm * 100 + self.dd) == (other.yyyy * 10000 + other.mm * 100 + other.dd):
            return True
            
        return False

def main():
    parser = argparse.ArgumentParser(description="Monitor net accesses by TLD")
    parser.add_argument("Start", type=str, help="Start date for statistics")
    parser.add_argument("Stop", type=str, help="End date for statistics")
    parser.add_argument('log_file', type=argparse.FileType('r'),
                help = "Name of web log file")
    args = parser.parse_args()

    beg_date = Date(args.Start)
    end_date = Date(args.Stop)
    log_file = args.log_file
     
    tld = [] 
     
    for line in log_file:
        line = line.strip()
        url = line.split('.')
        e = url[-1]
        date = Date(line[0:10])
        if beg_date < date and end_date > date:
            tld.append(e)
        elif beg_date == date:
            tld.append(e)
        elif end_date == date:
            tld.append(e)
    
    counts = {}
    tot_count = 0 
    for i in tld:
        try:
            counts[i] += 1
            tot_count += 1
        except:
            counts[i] = 1
            tot_count +=1
    
    count_dict = sorted(counts.keys())
    
    for t in count_dict:
        percent = counts[t] / tot_count * 100
        print('{:.2f} {}'.format(percent, t))

if __name__ == "__main__":
    main()
