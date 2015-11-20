#!/usr/bin/env python

from stem.descriptor.remote import DescriptorDownloader

downloader = DescriptorDownloader()

HSDirCnt = 0
relayCnt = 0
AuthorityCnt = 0
RunningCnt = 0

versions = dict()

try:
  for desc in downloader.get_consensus().run():
    relayCnt += 1
    if "HSDir" in desc.flags:
        HSDirCnt += 1
    if "Running" in desc.flags:
        RunningCnt +=1
    if "Authority" in desc.flags:
        AuthorityCnt += 1

    if desc.version not in versions.keys():
        versions[desc.version] = 0

    versions[desc.version] += 1

except Exception as exc:
  print("Unable to retrieve the consensus: %s" % exc)

# print out current stats

print "Num HSDirs:        ", HSDirCnt
print "Num Authorities    ", AuthorityCnt
print "Total relays:      ", relayCnt
print "Running relays:    ", RunningCnt
print
print "%17s    |    %s" % ("Versions", "Count")
print "%17s--------------" % ("--------")
for k in sorted(versions.keys()):
    print "%17s    |    %d" % (k, versions[k]) # 17



