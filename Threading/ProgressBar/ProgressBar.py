"""
Create A Progress Bar for Downloads
Create a progress bar for applications that can keep track of a download in progress.
The progress bar will be on a separate thread and will communicate with the main thread using delegates.
"""
import urllib.request

url = "http://ftp.task.gda.pl/test/10mega"

fname = url.split('/')[-1]
u = urllib.request.urlopen(url)
meta = u.info()
fsize = int(meta.get("Content-Length"))
pbar_len = 40

print()
print("Downloading file from: {0}, size (bytes): {1}".format(
    url, fsize))

file_size_dl = 0
block_sz = 8192

with open(fname, 'wb') as fh:
    while True:
        buffer = u.read(block_sz)

        if not buffer:
            break
        file_size_dl += len(buffer)
        fh.write(buffer)
        status = file_size_dl * 100 / float(fsize)
        compl = int(pbar_len * file_size_dl) // fsize
        bar = "[" + "█" * compl + " " * (pbar_len - compl) + "]"
        print("{pbar}   {status:.2f}%".format(pbar=bar, status=status), end="\r")
    print()
