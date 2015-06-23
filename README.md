# Bodgitt-and-Scarper
Desafio Python

Background
Bodgitt and Scarper, LLC. is a broker of home improvement contractors. They take requests from home owners for a type of service, and offer the homeowner one or more contractors that can provide the required services. Curently, Bodgitt and Scarper provides this service over the phone using a team of customer service representatives (CSRs). The CSRs interact with an ageing custom-written application that has been drawing increasing criticism from the CSRs.
The company's IT director has decided to migrate the existing application to a Python technology based system. Initially, the system will support only the CSRs. 
The company's IT department has a data file that contains the essential information for the company, the new system must reimplement the database code from scratch without altering the data file format.
Your first challenge is to generate a command line tool that outputs a dictionary of lists from each service provider available in the datafile by stripping the leading spaces if some. Empty fields, if some as well, are ignored at this first stage
.
Clarity and Maintainability
A clear design, such as will be readily understood by junior programmers, will be preferred to a complex one, even if the complex one is a little more efficient. Code complexity, including nesting depth, argument passing, and the number of classes and interfaces, should be reasonable. 
Follow object-oriented practices.

Data file Format
The format of data in the database file is as follows:

Start of file 
4 byte numeric, magic cookie value. Identifies this as a data file 
4 byte numeric, total overall length in bytes of each record 
2 byte numeric, number of fields in each record

Schema description section. 
Repeated for each field in a record: 
2 byte numeric, length in bytes of field name (o próprio arquivo retorna quantos bytes serão por campo)
n bytes (defined by previous entry), field name 
2 byte numeric, field length in bytes 

end of repeating block

Data section. 

Repeat to end of file: 
1 byte "deleted" flag. 0 implies valid record, 1 implies deleted record 
Record containing fields in order specified in schema section, no separators between fields, each field fixed length at maximum specified in schema information

End of file
All numeric values are stored in the header information use the formats of the DataInputStream and DataOutputStream classes. All text values, and all fields (which are text only), contain only 8 bit characters, null terminated if less than the maximum length for the field. The character encoding is 8 bit US ASCII.


Database schema
The database that Bodgitt and Scarper uses contains the following fields:
Field descriptive name
Database field name
Field length
Detailed description
Subcontractor Name
name
32
The name of the subcontractor this record relates to.
City
location
64
The locality in which this contractor works
Types of work performed
specialties
64
Comma separated list of types of work this contractor can perform.
Number of staff in organization
size
6
The number of workers available when this record is booked
Hourly charge
rate
8
Charge per hour for the subcontractor. This field includes the currency symbol
Customer holding this record
owner
8
The id value (an 8 digit number) of the customer who has booked this. Note that for this application, you should assume that customers and CSRs know their customer ids. The system you are writing does not interact with these numbers, rather it simply records them. If this field is all blanks, the record is available for sale.



