"""Here I wanna "explain" something
about variables in Phyton"""

#1, u create variables without describe the type, examples:

x=123;
y="hola mundo";
z=0x29;
t='A';
print x, y, z, t;

#2, if we have a "string" we can select in print what we want to show
print y;         #show us all the String
print y[2];      #show the char in position 2 of the String
print y[2:5];    #Show chars from 2 position to 5 position
print y[2:];     #Show chars from 2 position to the end of the String


#3, IMPORTANT , we can create vectors by 2 ways -> with () and with [], lets see....

list =["hola",234,0x16,'A']; # as u see we can enter what we want (type of data)
unit =("hola",234,0x16,'A');

print list;
print unit;  #As we can see...they are similiar, but the difference is... that dates in () type CANNOT be udated)

list[2]=25;
print list;   #change the valor of position 2 from 0x16 to 25

#unit(2)=25;
print unit;   #ERROR,we cant change it :)


#5, last one u can create a "table" , like a vector with valors, lets see..

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values
