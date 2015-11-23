#!/usr/bin/env python

from stem.descriptor.remote import DescriptorDownloader

downloader = DescriptorDownloader()

HSDirCnt = 0
relayCnt = 0
AuthorityCnt = 0
RunningCnt = 0

versions = dict()
releases = dict()

# get release history

with open("tor_release_history.txt") as f:
    lines = f.readlines()
    for line in lines:
        end = line.find(" ")
        start = line[:end].rfind("/") + 1
        date = line[end+1:].strip()

        releases[line[start:end].replace("tor-", "")] = date


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

print
print "Num HSDirs:        ", HSDirCnt
print "Num Authorities    ", AuthorityCnt
print "Total relays:      ", relayCnt
print "Running relays:    ", RunningCnt
print
print "%17s    |    %10s    |    %17s" % ("Versions", "Count", "Release date")
print "-" * 80
for k in sorted(versions.keys()):
    key_string = k.__str__()
    date_string = ''
    try:
        date_string = releases[key_string]
    except Exception:
        date_string = "Unknown"

    print "%17s    |    %10d    |    %17s" % (k, versions[k], date_string) # 17

print



