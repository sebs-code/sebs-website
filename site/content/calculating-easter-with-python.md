Title: Calculating The Date of Easter with Python
Date: April 21, 2025
Tags: Software Development
Slug: calculating-easter-date-with-python
Summary: Wondering how to calculate the date of Easter with Python? Here's how...

```
from dateutil.easter import easter  
print(easter(2010))  
2010-04-04  
```
  
The function also has an argument, where you can specific the type of Easter calculation you would like:  
  
1 = Easter Julian  
2 = Easter Orthodox  
3 = East Western  
  
```
print(easter(2010, 1))
2010-03-22  
print(easter(2010, 2))
2010-04-04  
print(easter(2010, 3))  
2010-04-04    
```
  
You're welcome. Happy Easter. 🐰🐰🐰