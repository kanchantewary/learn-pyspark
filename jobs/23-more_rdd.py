#pycook1.py
#to run: spark-submit pycook1.py

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("create airport rdd").setMaster("local[3]")
    sc = SparkContext(conf = conf)
    sc.setLogLevel("ERROR")

#set up the RDD: airports, pyspark cookbook,leanringPyspark git repository
#airport file: column definition: ['City', 'State', 'Country', 'IATA']
#departure delays file: column definition: ['date', 'delay', 'distance', 'origin', 'destination']

#define file paths here

input_dir = '/home/user/workarea/projects/learningPySpark/Chapter03/flight-data/'
output_dir = '/home/user/workarea/projects/outdir'

airports = sc.textFile('/home/user/workarea/projects/learningPySpark/Chapter03/flight-data/airport-codes-na.txt').map(lambda x:x.split('\t'))

print(airports.take(5))

#set up the RDD: flights

flights = sc.textFile('/home/user/workarea/projects/learningPySpark/Chapter03/flight-data/departuredelays.csv').map(lambda x:x.split(','))

print(flights.take(5))

#use map to select a subset of columns from the rdd, further use a filter to select airports in WA

airportsWA = airports.map(lambda c: (c[0],c[1])).filter(lambda c:c[1]=='WA')

print(airportsWA.take(5))

#use flatmap to flattern the resultset

#use distinct to get unique list of countries in the set

country = airports.map(lambda c:c[2]).distinct()

print(country.take(5)) #This would return the header row as well, hence 'Country' would also be one of the distinct values, to remove this, use zipwithindex function

#use sample transformation to get a random subset

#use join transformation to join two rdds on a key, as we join airport and flight data on airport code
#get IATA code of the airport as the first column(key) of the RDD 
air = airports.map(lambda c:(c[3],c[0],c[1],c[2]))

#get destination airport code as the key
flt = flights.map(lambda c:(c[4],c[0],c[1],c[2],c[3]))

#join on airport code

print(flt.join(air).take(5))

#remove the header row using zipwithindex function followed by a filter.

#airports_noheader = airports.zipWithIndex().filter(lambda (row,idx) : idx>1) ---this does not work, spark fails with error, follow below approach instead.

airports_noheader = airports.zipWithIndex().filter(lambda c : c[1]>1)
#.map(lambda (row,idx):row)

print(airports_noheader.take(5))

#get the number of rows

print(f"airport file has {airports.count()} number of rows")

#use union transformation to combine data for two airports

#get airports in Washington state
WA_air = airports.filter(lambda c:c[1]=='WA')

#get airports in British Columbia
BC_air = airports.filter(lambda c:c[1]=='BC')

#union the two

WA_and_BC_combined = WA_air.union(BC_air)

print(f'here are airports from WA and BC states {WA_and_BC_combined.take(10)}')


#save the resultset in a text file

WA_and_BC_combined.saveAsTextFile("output_dir/airports")
