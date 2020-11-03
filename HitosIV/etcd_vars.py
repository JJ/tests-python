import etcd3
from dotenv import load_dotenv
import os
import sys

def main( argv = [] ):
    PORT_VAR_NAME= 'hugitos:PORT'
    etcd = etcd3.client()
    if ( argv ):
        etcd.put(PORT_VAR_NAME,argv[0])
    else:
        load_dotenv()
        if (os.getenv('PORT')):
            etcd.put(PORT_VAR_NAME,os.getenv('PORT'))
        else:
            etcd.put(PORT_VAR_NAME,3000)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        main()
