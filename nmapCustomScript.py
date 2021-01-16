import nmap

ns = nmap.PortScanner()

print(ns.nmap_version())

ns.scan(argv[2] , '1-1024' , '-v')

print(ns.scaninfo())
print(ns.csv())
