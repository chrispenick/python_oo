#!/usr/bin/python3

import customers as c
import accounts as a

#def main():
cust1 = c.Customer('Bob')
cust2 = c.Customer('Janet')
cust1._accounts.append(a.Checking('1234'))
cust2._accounts.append(a.Savings('4567',.005))

#if __name__ == '__main__':
#    main()




