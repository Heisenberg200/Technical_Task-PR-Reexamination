## Technical_Task-PR-Reexamination
## Author: Corman Daniel
## Academic group: FAF-191
# Technical requirements:

 In order to get the minimum acceptable mark, which is 5, you have to present a project which includes:
 1. Two web servers which communicates over HTTP protocol between them.
 2. First web server is producer which produces some data on multiple threads (more than 5) and it sends these data from
    multiple threads to the second web server.
 3. Second server is consumer, which receives and consumes data from first server and populates shared resources, a queue
    or stack with received data.
 4. Second server also has multiple threads which extracts one element from shared resource and is sending that extracted
    data element from second server to the first.
