## Create a class called Bacon_count, which inherits or takes properties from MRJob Class. This will be called to run the full
## MapReduce job with MRJob;

##First import MrJob
## Create the class Bacon_Count
# Next, create a mapper()function that will take 
# (self, _, line) as parameters. The mapper() function will assign the input to key-value pairs:
## The underscore allows methods to be mapped together. Since we aren't chaining anything together yet, the underscore
# indicates we won't use this parameter. The line parameter will be the line of text taken from the raw input file.

from mrjob.job import MRJob

class Bacon_Count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1
    def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()


##BReaking down the for loop to value 1- the for loop is calling the split methods to parse through the text and 
## convert the words to lowercase. If the world matches 'bacon' then a key value pair will show as yield 'bacon', 1


## Calling functions with yeild will return what is called a generator object. Generators are iterator like a list,
## however unlike a list the contents are not stored in memory- so this is useful for large files. WHen yield is called
## the function is suspended and returns a value. A generator won't run another value until next() is called, which is something
## That mrJobs returns "bacon,1". If bacon appears three times then an output of bacon 1 will be produced three times.

## THERE IS A SHUFFLE STEP THAT OCCURS AFTER MAPPER THAT WE CANNOT SEE. THERE IS NO CODE WRITTEN FOR THIS STEP
## AND IT OCCURS BECAUSE THE CLASS INHERITS FROM THE MR JOB LIBRARY. THis shuffle step organizes key value pairs so that there
## Is only one key for each unique key and combines the values to a list.

##You might have noticed that nowhere in the code is a file imported or opened. The mrjob library works by reading in a file passed to it in the terminal.


## MODULEWORK ON COLAB HERE: https://colab.research.google.com/drive/1WDSpcAEvyZB88mgt-o9hPK1ZWSByjQqg?usp=sharing