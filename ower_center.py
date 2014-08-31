#!/usr/bin/python
import ower
import dashboard

bill = ower.Owee("Bill", "some email", "Shirt", "30 june 2014")
abdel = ower.Owee("ABdel", "some email", "Shirt", "30 june 2014")
ali = ower.Owee("Ali", "some email", "Shirt", "30 june 2014")


ali.change_status()

print(ali.status)
ali.change_status()

print(ali.status)
