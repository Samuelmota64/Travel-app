car_choice = ""
trip_total_price = 0 
car_price = 100


#ask the location and amount of rooms and there price
print("Hello welcome to Samuel's swell travel agency")

location = input("Frist things frist where would you like to go ")

hotel_room = [["1 bed",50],["2 beds",100],["3 beds",150],["4 beds",200],["5 Beds",300]]

 
#ask for the room size and stores the value 
print("Okay now lets start planning your trip to ",location)

print("what size room would you like here are our selections and they're prices.",hotel_room)

room_index = input ("room bed amount ") 

#ask  for the time the trip will take and convernts the number into a integer
days_staying = input("how many days are you staying ")
trip_time=int(days_staying) 

#ask if the user would like to rent a car if they say yes it will add that to there total and if they say no it will not  
print("great now would you like to rent a car for this location")
car_choice = input("Yes or No ")
if car_choice == "yes":
  
  print("the car rent is 100 Dollars and will be added to your total")
elif car_choice == "No":
  
  print("Thats okay then nothing will be added to your total")


room_price = hotel_room[int(room_index)][1] 
