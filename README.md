# sample-app
Explore CI/CD with GitHub and Jenkins
import urllib.parse
import requests as requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "R2zVjlxolFr5JhhKT3PhH06t7gnIFeZM"
while True:
 orig = input("Starting Location: ")
 if orig == "quit" or orig == "q":
     break
 dest = input("Destination: ")
 if dest == "quit" or dest == "q":
     break
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print("URL: " + (url))
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
if json_status == 0:
    for each in json_data["route"]["legs"][0]["maneuvers"]:
        print((each["narrative"]) + " (" +
str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
elif json_status == 402:
     print("**********************************************")
     print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both",
locations)
     print("**********************************************\n")
elif json_status == 611:
     print("**********************************************")
     print("Status Code: " + str(json_status) + "; Missing an entry for one or both",
locations)
     print("**********************************************\n")
else:
 print("************************************************************************")
 print("For Staus Code: " + str(json_status) + "; Refer to:")
 print("https://developer.mapquest.com/documentation/directions-api/status-codes")
 print("************************************************************************\n")
 print("API Status: " + str(json_status) + " = A successful route call.\n")
 print("=============================================")
 print("Directions from " + (orig) + " to " + (dest))
 print("Trip Duration: " + (json_data["route"]["formattedTime"]))
 print("Miles: " + str(json_data["route"]["distance"]))
 print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"]))
 print("=============================================")
 print("Kilometers: " + str((json_data["route"]["distance"])*1.61))
 print("Fuel Used (Ltr): " + str((json_data["route"]["fuelUsed"])*3.78))
print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
 print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
print("=============================================\n")
