from math import*
while True:
          try:

              source=float(input("<<ENTER THE SOURCE>>"))
              destination=float(input("<<ENTER THE DESTINATION>>"))
 




              if source>=0 and destination>0:
                if source<destination:
                  print("Searching for a cab")
                  print("1.PRIME")
                  print("2.AUTO")
                  print("3.MICRO")
                  print("4.MINI")
                  choice=float(input("<<MAKE IT CLEAR>>"))
                  choice=round(choice);
                  if choice ==1: 
                      c=500
                      dis=(destination-source)
                      k=dis*c
                      print("FAIR",k)
                  elif choice==2:
                      c=100
                      dis=(destination-source)
                      k=dis*c
                      print("fair",k)
                  elif choice==3:
                      c=300
                      dis=(destination-source)
                      k=dis*c
                      print("fair",k)
                  elif choice==4:
                      c=400
                      dis=(destination-source)
                      k=dis*c
                      print("fair",k)
                  else:
                      print("INVALID")
                
                  
                  print("\n\n\t\t|-------------------------|")
                  print("\t\t|     DISTANCE BILL       |")
                  print("\t\t|                         |")
                  print("\t\t|-------------------------|")
                  print("\t\t|                         |")
                  print("\t\t|* TOTAL DISTANCE -",dis,"km|")
                  print("\t\t|* PER KILOMETER  -",c,"|")
                  print("\t\t|                         |")
                  print("\t\t|-------------------------|")
                  print("\t\t|* TOTAL FAIR     -",k,"|")
                  print("\t\t|-------------------------|")
                  
                else:
                  print("invalid")

              elif(source<0):
                  print("INVALID SOURCE")
              elif(destination<=0):
                  print("INVALID DESTINATION")
              else:
                  print("INVALID SOURCE AND DESTINATION ")
          except:
                print("invalid")        
