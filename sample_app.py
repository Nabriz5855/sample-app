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
 // Set up start and destination for the route
Coordinate nyc = new Coordinate(40.7326808, -73.9843407);
List<Coordinate> boston = Arrays.asList(new Coordinate(42.355097, -71.055464));

// Set up route options
RouteOptions routeOptions = new RouteOptions.Builder()
        .maxRoutes(3)
        .systemOfMeasurementForDisplayText(SystemOfMeasurement.UNITED_STATES_CUSTOMARY) // or specify METRIC
        .language("en_US") // NOTE: alternately, specify "es_US" for Spanish in the US
        .highways(RouteOptionType.ALLOW)
        .tolls(RouteOptionType.ALLOW)
        .ferries(RouteOptionType.DISALLOW)
        .internationalBorders(RouteOptionType.DISALLOW)
        .unpaved(RouteOptionType.DISALLOW)
        .seasonalClosures(RouteOptionType.AVOID)
        .build();

mRouteService.requestRoutes(nyc, boston, routeOptions, new RoutesResponseListener() {
    @Override
    public void onRoutesRetrieved(List<Route> routes) {
        if (routes.size() > 0) {
            mNavigationManager.startNavigation((Route) routes.get(0));
        }
    }

    @Override
    public void onRequestFailed(@Nullable Integer httpStatusCode, @Nullable IOException exception) {}

    @Override
    public void onRequestMade() {}
});
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
##conversing python to java
#dowloading or region
// Set up the OfflineManager
offlineManager = OfflineManager.getInstance(SimpleOfflineMapActivity.this);

// Create a bounding box for the offline region
LatLngBounds latLngBounds = new LatLngBounds.Builder()
  .include(new LatLng(40.307155, -105.378504)) // Northeast
  .include(new LatLng(39.328620, -104.583757)) // Southwest
  .build();

// Define the offline region
OfflineTilePyramidRegionDefinition definition = new OfflineTilePyramidRegionDefinition(
  mapboxMap.getStyleUrl(),
  latLngBounds,
  10,
  20,
  MainActivity.this.getResources().getDisplayMetrics().density);


// Implementation that uses JSON to store Denver as the offline region name.
byte[] metadata;
try {
  JSONObject jsonObject = new JSONObject();
  jsonObject.put(JSON_FIELD_REGION_NAME, "Denver Metro Area");
  String json = jsonObject.toString();
  metadata = json.getBytes(JSON_CHARSET);
} catch (Exception exception) {
  Log.e(TAG, "Failed to encode metadata: " + exception.getMessage());
  metadata = null;
}

// Create the region asynchronously
offlineManager.createOfflineRegion(definition, metadata,
  new OfflineManager.CreateOfflineRegionCallback() {
    @Override
    public void onCreate(OfflineRegion offlineRegion) {
      offlineRegion.setDownloadState(OfflineRegion.STATE_ACTIVE);

      // Monitor the download progress using setObserver
      offlineRegion.setObserver(new OfflineRegion.OfflineRegionObserver() {
        @Override
        public void onStatusChanged(OfflineRegionStatus status) {

          // Calculate the download percentage
          double percentage = status.getRequiredResourceCount() >= 0
          ? (100.0 * status.getCompletedResourceCount() / status.getRequiredResourceCount()) :
          0.0;

          if (status.isComplete()) {
            // Download complete
            Log.d(TAG, "Region downloaded successfully.");
          } else if (status.isRequiredResourceCountPrecise()) {
            Log.d(TAG, percentage);
          }
        }

        @Override
        public void onError(OfflineRegionError error) {
          // If an error occurs, print to logcat
          Log.e(TAG, "onError reason: " + error.getReason());
          Log.e(TAG, "onError message: " + error.getMessage());
        }

        @Override
        public void mapboxTileCountLimitExceeded(long limit) {
          // Notify if offline region exceeds maximum tile count
          Log.e(TAG, "Maps SDK Tile count limit exceeded: " + limit);
        }
      });
    }

  @Override
  public void onError(String error) {
    Log.e(TAG, "Error: " + error);
  }
});
# managing the dowloaded region
offlineManager.listOfflineRegions(new OfflineManager.ListOfflineRegionsCallback() {
        @Override
        public void onList(OfflineRegion[] offlineRegions) {
          if (offlineRegions.length > 0) {
            // delete the last item in the offlineRegions list
            offlineRegions[(offlineRegions.length - 1)].delete(new OfflineRegion.OfflineRegionDeleteCallback() {

              @Override
              public void onDelete() {
                Log.e(TAG, "Deleted region");
              }

              @Override
              public void onError(String error) {
                Log.e(TAG, "On Delete error: " + error);
              }
            });
          }
        }
    }
