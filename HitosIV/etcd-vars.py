import etcd3
from dotenv import load_dotenv

def main():
    etcd = etcd3.client()
    load_dotenv()
    etcd.put('PORT',PORT)



if __name__ == "__main__":
    main()
