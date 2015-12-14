from sys import argv
from os.path import exists

script, from_bile, to_file = argv

print "Copyting from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print "The imput file is %d bytes long" % len(indata)

print "The input file is %d bytes long" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open (o_file, 'w')
out_file.write(indata)

print "Alright, all done."

put_file.close()
in_file.close()
