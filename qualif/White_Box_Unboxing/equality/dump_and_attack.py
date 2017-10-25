import numpy as np

print "#!/bin/bash"
print "# Run the script with BASH!!"
print ""
print "rm -f dumps.bin plaintexts.bin dumps.*.gz plaintexts.txt"
for idx_i, i in enumerate(range(32)):
  msg = "".join(["%02X" % v for v in np.random.randint(0, 256, 16)])
  print "valgrind --tool=tracergrind --output=trace.%05d --filter=0x462886-0x463D6C ../whitebox --stdin < <(echo " % idx_i + msg + " | xxd -r -p)"
  print "texttrace trace.%05d texttrace.%05d" % (idx_i, idx_i)
  print "awk '/\\[M/ {print \"0x\"$5\",0x\"$NF}' texttrace.%05d | gzip >> textdumps.%05d.gz" % (idx_i, idx_i)
  print "awk 'BEGIN {ORS=\"\"} /\\[M/ {print $NF}' texttrace.%05d | xxd -r -p >> dumps.bin" % idx_i
  print "echo " + msg + " | xxd -r -p >> plaintexts.bin"
  print "echo " + msg + " >> plaintexts.txt"

print "python ./attack.py"
