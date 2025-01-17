#!/usr/bin/python3

import sys
import time

from activemqapi.activemqpublisher import ActiveMQPublisher



MESSAGE_DIR="/home/cc/official/FinalProject/DesignOfExperiments/messages/"
MESSAGE_SUFFIX = ".txt"

messages = [
    "small",
]



def main():
    hostname = sys.argv[1] if len(sys.argv) > 1 else '10.56.1.95'

    loops = 1000
    file = messages[0]
        
    publisher = ActiveMQPublisher(hostname=hostname)

    filename = MESSAGE_DIR + file + MESSAGE_SUFFIX
    
    with open(filename, "r") as f:
        data = f.read()
        
    run(publisher, data, loops)
    
def run(publisher, data, loops):
    count = 0
    for i in range(loops):
        publisher.publish(data)
        #time.sleep(1)
        
    publisher.done()

if __name__ == '__main__':
    main()
