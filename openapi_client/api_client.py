"""
    LODGEA OTA Service API Reference

    # Introduction  Whether you own your property or not, LODGEA provides the platform to provide accommodation services to your consumers through a variety of connectivity options and business models. LODGEA provides a flexible and open platform for many use cases.  This API allows you to search for availabilities or locations and get all available information about a specific property.  # API Endpoint  ``` https://api.eu.lodgea.io/v1/ ```  The API is only accessible via HTTPS, the base URL is <code>https://api.eu.lodgea.io/</code>, and the current version is <code>v1</code> which results in the base URL for all requests: <code>https://api.eu.lodgea.io/v1/</code>.  # Datacenters  The API is only accessible via HTTPS and the current version is <code>v1</code>, which results in a URL like: <code>https://api.lodgea.io/v1/</code>, depending on the datacenter.  ## EU Datacenter  ``` https://api.eu.lodgea.io/v1/ ```  This is the default datacenter.  ## US Datacenter  ``` https://api.us.lodgea.io/v2/ ```  ## German Datacenter  ``` https://api.uat.lodgea.io/v2/ ```  # Usage  [curl](http://curl.haxx.se/) is used primarily to send requests to LODGEA in the [Usage examples](#Usage examples) in this Readme.  For [Postman](https://www.postman.com/), the OpenAPI YAML definition can be imported as collection over the `Import` button. In the `variables` menu under `Collections`, you can set the `baseURL` value to the specific region. The API key can be set under each request in the `Authorization` tab.  There are SDKs for many popular languages available on GitHub:  - https://github.com/lodgea/lodgea-java - https://github.com/lodgea/lodgea-js - https://github.com/lodgea/lodgea-php - https://github.com/lodgea/lodgea-csharp - https://github.com/lodgea/lodgea-python  # Cross-Origin Resource Sharing  This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/), that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.  # Authentication  The LODGEA API offers authentication via API Key. Please create your own API Key in the management UI. Then add your key as `apiKey` header to the request. If you receive a `401` response, make sure your filled key is valid.  # Usage examples  Learn how to work more efficiently with LODGEA API v1 with these workflow-oriented examples.  ## Get Property by ID  ``` POST /v1/property/get ```  Get all information about a specific property by its ID.  #### Parameters  | Name                  | Type     | Description               | Example             | | --------------------- | -------- | ------------------------- | ------------------- | | `propertyId` required | `string` | ID of the property to get | strandresidenz-sylt |  #### Example Request  ``` curl --location --request POST 'https://api.eu.lodgea.io/v1/property/get' \\ --header 'Content-Type: application/json' \\ --header 'Accept: application/json' \\ --header 'apiKey: <YOUR_API_KEY>' \\ --data-raw '{   \"propertyId\": \"strandresidenz-sylt\" }' ```  ## Search for Location  ``` POST /v1/location/search ```  Get a location by search text in free-text form.  #### Parameters  | Name                  | Type     | Description | Example             | | --------------------- | -------- | ----------- | ------------------- | | `searchText` required | `string` | Search text | Hotel Stadt Hamburg |  #### Example Request  ``` curl --location --request POST 'https://api.eu.lodgea.io/v1/location/search' \\ --header 'Content-Type: application/json' \\ --header 'Accept: application/json' \\ --header 'apiKey: <YOUR_API_KEY>' \\ --data-raw '{   \"searchText\": \"Hotel Stadt Hamburg\" }' ```  ## Search for Availability  ``` POST /v1/availability/search ```  Get availability information based on search criteria. All parameter codes are listed in the [appendix](#Appendix).  #### Parameters  | Name                       | Type           | Description                                                  | Example    | | -------------------------- | -------------- | ------------------------------------------------------------ | ---------- | | `adultCount` optional      | integer        | Number of adults                                             | 2          | | `childCount` optional      | integer        | Number of childs                                             | 1          | | `childAgeList` optional    | array<integer> | Age of the childs as integer array                           | [3]        | | `currencyCode` optional    | string         | Currency code, see [currencyCode](##CurrencyCode)            | EUR        | | `minLengthOfStay` optional | integer        | Minimum days of stay                                         | 1          | | `maxLengthOfStay` optional | integer        | Maximum days of stay                                         | 27         | | `locationName` optional    | string         | Name of the location                                         | Sylt       | | `locationType` optional    | string         | Type of the location, see [locationType](##locationType)     | locality   | | `earliestArrival` optional | date           | Earliest arrival date, format is: YYYY-MM-DD                 | 2022-09-01 | | `latestReturn` optional    | date           | Latest return date, format is: YYYY-MM-DD                    | 2022-09-08 | | `sort` optional            | string         | Sort order, either `quality` or `price`                      | quality    | | `serviceList` optional     | array<string>  | List of service codes, see [serviceCode](##serviceCode)      | [242]      | | `typeList` optional        | array<string>  | List of type codes, see [typeCode](##typeCode)               | [20]       | | `unitTypeList` optional    | array<string>  | List of unit type codes, see [unitTypeCode](##unitTypeCode)  | [9]        | | `unitAmenityList` optional | array<string>  | List of unit amenity codes, see [unitAmenityCode](##unitAmenityCode) | [50]       | | `mealPlanList` optional    | array<string>  | List of meal plan codes, see [mealPlanCode](##mealPlanCode)  | [19]       |  #### Example Request  ``` curl --location --request POST 'https://api.eu.lodgea.io/v1/availability/search' \\ --header 'Content-Type: application/json' \\ --header 'Accept: application/json' \\ --header 'apiKey: <YOUR_API_KEY>' \\ --data-raw '{   \"adultCount\": 2,   \"childCount\": 1,   \"childAgeList\": [     3   ],   \"currencyCode\": \"EUR\",   \"minLengthOfStay\": 1,   \"maxLengthOfStay\": 27,   \"locationName\": \"Sylt\",   \"locationType\": \"locality\",   \"earliestArrival\": \"2022-09-01\",   \"latestReturn\": \"2022-09-08\",   \"sort\": \"quality\",   \"serviceList\": [     242   ],   \"typeList\": [     20   ],   \"unitTypeList\": [     9   ],   \"unitAmenityList\": [     50   ],   \"mealPlanList\": [     19   ] }' ```  # Appendix  ## Parameters  ### currencyCode  | Code | Name | | ---- | ---- | | 1    | EUR  | | 2    | GBP  | | 3    | AED  | | 4    | USD  | | 5    | INR  | | 6    | AUD  | | 7    | ARS  | | 8    | EGP  | | 9    | KWD  | | 10   | RUB  | | 11   | MYR  | | 12   | SAR  | | 13   | AZN  | | 14   | FJD  | | 15   | MXN  | | 16   | SGD  | | 17   | BHD  | | 18   | GEL  | | 19   | MDL  | | 20   | ZAR  | | 21   | BRL  | | 22   | HKD  | | 23   | NAD  | | 24   | SEK  | | 25   | BGN  | | 26   | HUF  | | 27   | TWD  | | 28   | CHF  | | 29   | CAD  | | 30   | NZD  | | 31   | THB  | | 32   | XOF  | | 33   | IDR  | | 34   | NOK  | | 35   | TRY  | | 36   | CLP  | | 37   | ILS  | | 38   | OMR  | | 39   | CNY  | | 40   | JPY  | | 41   | PLN  | | 42   | COP  | | 43   | JOD  | | 44   | UAH  | | 45   | CZK  | | 46   | KZT  | | 47   | QAR  | | 48   | DKK  | | 49   | KRW  | | 50   | RON  |  ### locationType  | Type                        | Name                        | Example                             | | --------------------------- | --------------------------- | ----------------------------------- | | formatted_address           | Formatted Address           | Nordhedig 20 25980 Sylt Deutschland | | place_id                    | Place ID                    | ChIJVaxqTevetEcRyfs8PGHK6mw         | | locality                    | Locality                    | Sylt                                | | administrative_area_level_1 | Administrative Area Level 1 | Schleswig-Holstein                  | | administrative_area_level_3 | Administrative Area Level 3 | Nordfriesland                       | | state_code                  | State Code                  | SH                                  | | country                     | Country                     | Deutschland                         | | country_code                | Country Code                | DE                                  | | postal_code                 | Postal Code                 | 25980                               | | language                    | Language                    | de                                  | | natural_feature             | Natural Feature             | Sylt                                | | establishment               | Establishment               | Sylt                                | | sublocality                 | Sublocality                 | Westerland                          | | sublocality_level_1         | Sublocality Level 1         | Westerland                          | | streetNumber                | Street Number               | 20                                  | | route                       | Route                       | Nordhedig                           |  ### serviceCode  | Code  | Name                                                    | | ----- | ------------------------------------------------------- | | 1     | 24-hour front desk                                      | | 2     | 24-hour room service                                    | | 3     | 24-hour security                                        | | 4     | Adjoining rooms                                         | | 5     | Air conditioning                                        | | 6     | Airline desk                                            | | 7     | ATM/Cash machine                                        | | 8     | Baby sitting                                            | | 9     | BBQ/Picnic area                                         | | 10    | Bilingual staff                                         | | 11    | Bookstore                                               | | 12    | Boutiques/stores                                        | | 13    | Brailed elevators                                       | | 14    | Business library                                        | | 15    | Car rental desk                                         | | 16    | Casino                                                  | | 17    | Check cashing policy                                    | | 18    | Check-in kiosk                                          | | 19    | Cocktail lounge                                         | | 20    | Coffee shop                                             | | 21    | Coin operated laundry                                   | | 22    | Concierge desk                                          | | 23    | Concierge floor                                         | | 24    | Conference facilities                                   | | 25    | Courtyard                                               | | 26    | Currency exchange                                       | | 27    | Desk with electrical outlet                             | | 28    | Doctor on call                                          | | 29    | Door man                                                | | 30    | Driving range                                           | | 31    | Drugstore/pharmacy                                      | | 32    | Duty free shop                                          | | 33    | Elevators                                               | | 34    | Executive floor                                         | | 35    | Exercise gym                                            | | 36    | Express check-in                                        | | 37    | Express check-out                                       | | 38    | Family plan                                             | | 39    | Florist                                                 | | 40    | Folios                                                  | | 41    | Free airport shuttle                                    | | 42    | Free parking                                            | | 43    | Free transportation                                     | | 44    | Game room                                               | | 45    | Gift/News stand                                         | | 46    | Hairdresser/barber                                      | | 47    | Accessible facilities                                   | | 48    | Health club                                             | | 49    | Heated pool                                             | | 50    | Housekeeping - daily                                    | | 51    | Housekeeping - weekly                                   | | 52    | Ice machine                                             | | 53    | Indoor parking                                          | | 54    | Indoor pool                                             | | 55    | Jacuzzi                                                 | | 56    | Jogging track                                           | | 57    | Kennels                                                 | | 58    | Laundry/Valet service                                   | | 59    | Liquor store                                            | | 60    | Live entertainment                                      | | 61    | Massage services                                        | | 62    | Nightclub                                               | | 63    | Off-Site parking                                        | | 64    | On-Site parking                                         | | 65    | Outdoor parking                                         | | 66    | Outdoor pool                                            | | 67    | Package/Parcel services                                 | | 68    | Parking                                                 | | 69    | Photocopy center                                        | | 70    | Playground                                              | | 71    | Pool                                                    | | 72    | Poolside snack bar                                      | | 73    | Public address system                                   | | 74    | Ramp access                                             | | 75    | Recreational vehicle parking                            | | 76    | Restaurant                                              | | 77    | Room service                                            | | 78    | Safe deposit box                                        | | 79    | Sauna                                                   | | 80    | Security                                                | | 81    | Shoe shine stand                                        | | 82    | Shopping mall                                           | | 83    | Solarium                                                | | 84    | Spa                                                     | | 85    | Sports bar                                              | | 86    | Steam bath                                              | | 87    | Storage space                                           | | 88    | Sundry/Convenience store                                | | 89    | Technical concierge                                     | | 90    | Theatre desk                                            | | 91    | Tour/sightseeing desk                                   | | 92    | Translation services                                    | | 93    | Travel agency                                           | | 94    | Truck parking                                           | | 95    | Valet cleaning                                          | | 96    | Dry cleaning                                            | | 97    | Valet parking                                           | | 98    | Vending machines                                        | | 99    | Video tapes                                             | | 100   | Wakeup service                                          | | 101   | Wheelchair access                                       | | 102   | Whirlpool                                               | | 103   | Multilingual staff                                      | | 104   | Wedding services                                        | | 105   | Banquet facilities                                      | | 106   | Bell staff/porter                                       | | 107   | Beauty shop/salon                                       | | 108   | Complimentary self service laundry                      | | 109   | Direct dial telephone                                   | | 110   | Female traveler room/floor                              | | 111   | Pharmacy                                                | | 112   | Stables                                                 | | 113   | 120 AC                                                  | | 114   | 120 DC                                                  | | 115   | 220 AC                                                  | | 116   | Accessible parking                                      | | 117   | 220 DC                                                  | | 118   | Barbeque grills                                         | | 119   | Women's clothing                                        | | 120   | Men's clothing                                          | | 121   | Children's clothing                                     | | 122   | Shops and commercial services                           | | 123   | Video games                                             | | 124   | Sports bar open for lunch                               | | 125   | Sports bar open for dinner                              | | 126   | Room service - full menu                                | | 127   | Room service - limited menu                             | | 128   | Room service - limited hours                            | | 129   | Valet same day dry cleaning                             | | 130   | Body scrub                                              | | 131   | Body wrap                                               | | 132   | Public area air conditioned                             | | 133   | Efolio available to company                             | | 134   | Individual Efolio available                             | | 135   | Video review billing                                    | | 136   | Butler service                                          | | 137   | Complimentary in-room coffee or tea                     | | 138   | Complimentary buffet breakfast                          | | 139   | Complimentary cocktails                                 | | 140   | Complimentary coffee in lobby                           | | 141   | Complimentary continental breakfast                     | | 142   | Complimentary full american breakfast                   | | 143   | Dinner delivery service from local restaurant           | | 144   | Complimentary newspaper delivered to room               | | 145   | Complimentary newspaper in lobby                        | | 146   | Complimentary shoeshine                                 | | 147   | Evening reception                                       | | 148   | Front desk                                              | | 149   | Grocery shopping service available                      | | 150   | Halal food available                                    | | 151   | Kosher food available                                   | | 152   | Limousine service                                       | | 153   | Managers reception                                      | | 154   | Medical Facilities Service                              | | 155   | Telephone jack adaptor available                        | | 156   | All-inclusive meal plan                                 | | 157   | Buffet breakfast                                        | | 158   | Communal bar area                                       | | 159   | Continental breakfast                                   | | 160   | Full meal plan                                          | | 161   | Full american breakfast                                 | | 162   | Meal plan available                                     | | 163   | Modified american meal plan                             | | 164   | Food and beverage outlets                               | | 165   | Lounges/bars                                            | | 166   | Barber shop                                             | | 167   | Video checkout                                          | | 168   | Onsite laundry                                          | | 169   | 24-hour food & beverage kiosk                           | | 170   | Concierge lounge                                        | | 171   | Parking fee managed by hotel                            | | 172   | Transportation                                          | | 173   | Breakfast served in restaurant                          | | 174   | Lunch served in restaurant                              | | 175   | Dinner served in restaurant                             | | 176   | Full service housekeeping                               | | 177   | Limited service housekeeping                            | | 178   | High speed internet access for laptop in public areas   | | 179   | Wireless internet connection in public areas            | | 180   | Additional services/amenities/facilities on property    | | 181   | Transportation services - local area                    | | 182   | Transportation services - local office                  | | 183   | DVD/video rental                                        | | 184   | Parking lot                                             | | 185   | Parking deck                                            | | 186   | Street side parking                                     | | 187   | Cocktail lounge with entertainment                      | | 188   | Cocktail lounge with light fare                         | | 189   | Motorcycle parking                                      | | 190   | Phone services                                          | | 191   | Ballroom                                                | | 192   | Bus parking                                             | | 193   | Children's play area                                    | | 194   | Children's nursery                                      | | 195   | Disco                                                   | | 196   | Early check-in                                          | | 197   | Locker room                                             | | 198   | Non-smoking rooms (generic)                             | | 199   | Train access                                            | | 200   | Aerobics instruction                                    | | 201   | Baggage hold                                            | | 202   | Bicycle rentals                                         | | 203   | Dietician                                               | | 204   | Late check-out available                                | | 205   | Pet-sitting services                                    | | 206   | Prayer mats                                             | | 207   | Sports trainer                                          | | 208   | Turndown service                                        | | 209   | DVDs/videos - children                                  | | 210   | Bank                                                    | | 211   | Lobby coffee service                                    | | 212   | Banking services                                        | | 213   | Stairwells                                              | | 214   | Pet amenities available                                 | | 215   | Exhibition/convention floor                             | | 216   | Long term parking                                       | | 217   | Children not allowed                                    | | 218   | Children welcome                                        | | 219   | Courtesy car                                            | | 220   | Hotel does not provide pornographic films/TV            | | 221   | Hotspots                                                | | 222   | Free high speed internet connection                     | | 223   | Internet services                                       | | 224   | Pets allowed                                            | | 225   | Gourmet highlights                                      | | 226   | Catering services                                       | | 227   | Complimentary breakfast                                 | | 228   | Business center                                         | | 229   | Business services                                       | | 230   | Secured parking                                         | | 231   | Racquetball                                             | | 232   | Snow sports                                             | | 233   | Tennis court                                            | | 234   | Water sports                                            | | 235   | Child programs                                          | | 236   | Golf                                                    | | 237   | Horseback riding                                        | | 238   | Oceanfront                                              | | 239   | Beachfront                                              | | 240   | Hair dryer                                              | | 241   | Ironing board                                           | | 242   | Heated guest rooms                                      | | 243   | Toilet                                                  | | 244   | Parlor                                                  | | 245   | Video game player                                       | | 246   | Thalassotherapy                                         | | 247   | Private dining for groups                               | | 248   | Hearing impaired services                               | | 249   | Carryout breakfast                                      | | 250   | Deluxe continental breakfast                            | | 251   | Hot continental breakfast                               | | 252   | Hot breakfast                                           | | 253   | Private pool                                            | | 254   | Connecting rooms                                        | | 255   | Data port                                               | | 256   | Exterior corridors                                      | | 257   | Gulf view                                               | | 258   | Accessible rooms                                        | | 259   | High speed internet access                              | | 260   | Interior corridors                                      | | 261   | High speed wireless                                     | | 262   | Kitchenette                                             | | 263   | Private bath or shower                                  | | 264   | Fire safety compliant                                   | | 265   | Welcome drink                                           | | 266   | Boarding pass print-out available                       | | 267   | Printing services available                             | | 268   | All public areas non-smoking                            | | 269   | Meeting rooms                                           | | 270   | Movies in room                                          | | 271   | Secretarial service                                     | | 272   | Snow skiing                                             | | 273   | Water skiing                                            | | 274   | Fax service                                             | | 275   | Great room                                              | | 276   | Lobby                                                   | | 277   | Multiple phone lines billed separately                  | | 278   | Umbrellas                                               | | 279   | Gas station                                             | | 280   | Grocery store                                           | | 281   | 24-hour coffee shop                                     | | 282   | Airport shuttle service                                 | | 283   | Luggage service                                         | | 284   | Piano Bar                                               | | 285   | VIP security                                            | | 286   | Complimentary wireless internet                         | | 287   | Concierge breakfast                                     | | 288   | Same gender floor                                       | | 289   | Children programs                                       | | 290   | Building meets local, state and country building codes  | | 291   | Internet browser On TV                                  | | 292   | Newspaper                                               | | 293   | Parking - controlled access gates to enter parking area | | 294   | Hotel safe deposit box (not room safe box)              | | 295   | Storage space available – fee                           | | 296   | Type of entrances to guest rooms                        | | 297   | Beverage/cocktail                                       | | 298   | Cell phone rental                                       | | 299   | Coffee/tea                                              | | 300   | Early check in guarantee                                | | 301   | Food and beverage discount                              | | 302   | Late check out guarantee                                | | 303   | Room upgrade confirmed                                  | | 304   | Room upgrade on availability                            | | 305   | Shuttle to local businesses                             | | 306   | Shuttle to local attractions                            | | 307   | Social hour                                             | | 308   | Video billing                                           | | 309   | Welcome gift                                            | | 310   | Hypoallergenic rooms                                    | | 311   | Room air filtration                                     | | 312   | Smoke-free property                                     | | 313   | Water purification system in use                        | | 314   | Poolside service                                        | | 315   | Clothing store                                          | | 316   | Electric car charging stations                          | | 317   | Office rental                                           | | 318   | Piano                                                   | | 319   | Incoming fax                                            | | 320   | Outgoing fax                                            | | 321   | Semi-private space                                      | | 322   | Loading dock                                            | | 323   | Baby kit                                                | | 324   | Children's breakfast                                    | | 325   | Cloakroom service                                       | | 326   | Coffee lounge                                           | | 327   | Events ticket service                                   | | 328   | Late check-in                                           | | 329   | Limited parking                                         | | 330   | Outdoor summer bar/café                                 | | 331   | No parking available                                    | | 332   | Beer garden                                             | | 333   | Garden lounge bar                                       | | 334   | Summer terrace                                          | | 335   | Winter terrace                                          | | 336   | Roof terrace                                            | | 337   | Beach bar                                               | | 338   | Helicopter service                                      | | 339   | Ferry                                                   | | 340   | Tapas bar                                               | | 341   | Café bar                                                | | 342   | Snack bar                                               | | 343   | Guestroom wired internet                                | | 344   | Guestroom wireless internet                             | | 345   | Fitness center                                          | | 348   | Health and beauty services                              | | 349   | Mobile/Digital Check-in                                 | | 350   | Mobile/Digital Check-out                                | | 351   | Choose a room                                           | | 5000  | Breakfast in the room                                   | | 5001  | Public transport tickets                                | | 5002  | Bikes available (free)                                  | | 5003  | Outdoor furniture                                       | | 5004  | Outdoor fireplace                                       | | 5005  | Garden                                                  | | 5006  | Terrace                                                 | | 5007  | Sun terrace                                             | | 5008  | Chapel/shrine                                           | | 5009  | Shared lounge/TV area                                   | | 5010  | Ironing service                                         | | 5011  | Trouser press                                           | | 5012  | Designated smoking area                                 | | 5013  | Pet basket                                              | | 5014  | Pet bowls                                               | | 5015  | Beach                                                   | | 5016  | Bowling                                                 | | 5017  | Darts                                                   | | 5018  | Fishing                                                 | | 5020  | Hiking                                                  | | 5021  | Minigolf                                                | | 5022  | Snorkeling                                              | | 5023  | Squash                                                  | | 5024  | Windsurfing                                             | | 5025  | Billiard                                                | | 5026  | Table tennis                                            | | 5027  | Canoeing                                                | | 5028  | Ski-to-door access                                      | | 5029  | Diving                                                  | | 5030  | Tennis equipment                                        | | 5031  | Badminton equipment                                     | | 5032  | Cycling                                                 | | 5033  | Ski storage                                             | | 5034  | Ski school                                              | | 5035  | Ski equipment hire (on site)                            | | 5036  | Ski pass vendor                                         | | 5037  | Private beach area                                      | | 5039  | Rooms/Facilities for Disabled                           | | 5040  | Hair dresser-beautician                                 | | 5041  | Family Rooms                                            | | 5042  | Viproom facilities                                      | | 5043  | Bridal Suite                                            | | 5044  | Spa & Wellness Centre                                   | | 5045  | Karaoke                                                 | | 5046  | Soundproof-rooms                                        | | 5047  | Packed Lunches                                          | | 5048  | Ticket service                                          | | 5049  | Entertainment Staff                                     | | 5050  | Private Check-in/Check-out                              | | 5051  | Special Diet Menus (on request)                         | | 5052  | Vending Machine (drinks)                                | | 5053  | Hot Spring Bath                                         | | 5054  | Kids' club                                              | | 5055  | Minimarket on site                                      | | 5056  | Water park                                              | | 5057  | Adult only                                              | | 5058  | Open-air bath                                           | | 5059  | Public bath                                             | | 5060  | Water slide                                             | | 5061  | Board games/puzzles                                     | | 5062  | Book/DVD/Music library for children                     | | 5063  | Indoor play area                                        | | 5064  | Kids' outdoor play equipment                            | | 5065  | Baby safety gates                                       | | 5066  | Children television networks                            | | 5067  | Kid meals                                               | | 5068  | Kid-friendly buffet                                     | | 5069  | Pool towels                                             | | 5070  | Wine/Champagne                                          | | 5071  | Bottle of water                                         | | 5072  | Fruits                                                  | | 5073  | Chocolate/Cookies                                       | | 5074  | Strollers                                               | | 5075  | On-site coffee house                                    | | 5076  | Sun loungers or beach chairs                            | | 5077  | Sun umbrellas                                           | | 5078  | Picnic area                                             | | 5079  | Beauty Services                                         | | 5080  | Spa Facilities                                          | | 5081  | Steam room                                              | | 5082  | Spa lounge/relaxation area                              | | 5083  | Foot bath                                               | | 5084  | Spa/wellness packages                                   | | 5085  | Massage chair                                           | | 5086  | Fitness                                                 | | 5087  | Yoga classes                                            | | 5088  | Fitness classes                                         | | 5089  | Personal trainer                                        | | 5090  | Fitness/spa locker rooms                                | | 5091  | Kids pool                                               | | 5092  | Shuttle Service                                         | | 5093  | Temporary art galleries                                 | | 5094  | Pub crawls                                              | | 5095  | Stand-up comedy                                         | | 5096  | Movie nights                                            | | 5097  | Walking tours                                           | | 5098  | Bike tours                                              | | 5099  | Themed dinner nights                                    | | 5100  | Happy hour                                              | | 5101  | Tour or class about local culture                       | | 5102  | Cooking class                                           | | 5103  | Live music/performance                                  | | 5104  | Live sports events (broadcast)                          | | 5105  | Archery                                                 | | 5106  | Aerobics                                                | | 5107  | Bingo                                                   | | 5108  | Ski Shuttle                                             | | 5109  | Outdoor Swimming Pool (all year)                        | | 5110  | Outdoor Swimming Pool (seasonal)                        | | 5111  | Indoor Swimming Pool (all year)                         | | 5112  | Indoor Swimming Pool (seasonal)                         | | 5113  | Swimming pool toys                                      | | 5114  | Rooftop pool                                            | | 5115  | Infinity pool                                           | | 5116  | Pool with view                                          | | 5117  | Salt-water pool                                         | | 5118  | Plunge pool                                             | | 5119  | Pool bar                                                | | 5120  | Shallow end pool                                        | | 5121  | Pool cover                                              | | 5122  | Fence around pool                                       | | 5123  | Airport Shuttle (surcharge)                             | | 5124  | Property is wheel chair accessible                      | | 5125  | Toilet with grab rails                                  | | 5126  | Higher level toilet                                     | | 5127  | Low bathroom sink                                       | | 5128  | Bathroom emergency pull cord                            | | 5129  | Visual aids: Braille                                    | | 5130  | Visual aids: Tactile Signs                              | | 5131  | Auditory Guidance                                       | | 5132  | Back massage                                            | | 5133  | Neck massage                                            | | 5134  | Foot massage                                            | | 5135  | Couples massage                                         | | 5136  | Head massage                                            | | 5137  | Hand massage                                            | | 5138  | Full body massage                                       | | 5139  | Facial treatments                                       | | 5140  | Waxing services                                         | | 5141  | Make up services                                        | | 5142  | Hair treatments                                         | | 5143  | Manicure                                                | | 5144  | Pedicure                                                | | 5145  | Hair cut                                                | | 5146  | Hair colouring                                          | | 5147  | Hair styling                                            | | 5148  | Body Treatments                                         | | 5149  | Body scrub                                              | | 5150  | Body wrap                                               | | 5151  | Light therapy                                           | | 5152  | Shuttle Service (free)                                  | | 5153  | Shuttle Service (surcharge)                             | | 5154  | Swimming pool                                           | | 5156  | No Single-Use Toiletries                                | | 5157  | Towels Changed Upon Request                             | | 5158  | 24-hour security                                        | | 5159  | Security alarm                                          | | 5160  | Smoke alarms                                            | | 5161  | CCTV in common areas                                    | | 5162  | CCTV outside property                                   | | 5163  | Fire extinguishers                                      | | 5164  | Key access                                              | | 5165  | Key card access                                         | | 5166  | Carbon monoxide detector                                | | 5167  | Carbon monoxide source                                  | | 5168  | No plastic stirrers                                     | | 5169  | No plastic straws                                       | | 5170  | No plastic cups                                         | | 5171  | No plastic bottles for water                            | | 5172  | No plastic bottles for non-water                        | | 5173  | No plastic cutlery                                      | | 5174  | Keycard for room electricity                            | | 5175  | Opt-out from daily room cleaning                        | | 5176  | Refillable water stations                               | | 5177  | Bike rental                                             | | 5178  | Bike parking                                            | | 6000  | Lunch                                                   | | 6001  | Dinner                                                  | | 90001 | Renewable energy                                        |  ### mealPlanCode  | Code  | Name                          | | ----- | ----------------------------- | | 0     | (NONE)                        | | 1     | All inclusive                 | | 2     | American                      | | 3     | Bed & breakfast               | | 4     | Buffet breakfast              | | 5     | Caribbean breakfast           | | 6     | Continental breakfast         | | 7     | English breakfast             | | 8     | European plan                 | | 9     | Family plan                   | | 10    | Full board                    | | 11    | Full breakfast                | | 12    | Half board                    | | 14    | Room only                     | | 15    | Self catering                 | | 16    | Bermuda                       | | 17    | Dinner bed and breakfast plan | | 18    | Family American               | | 19    | Breakfast                     | | 20    | Modified                      | | 21    | Lunch                         | | 22    | Dinner                        | | 23    | Breakfast & lunch             | | 24    | Lunch & Dinner                | | 90001 | 3/4 Plan                      |  ### typeCode  | Code | Name                          | | ---- | ----------------------------- | | 1    | All suite                     | | 2    | All-Inclusive resort          | | 3    | Apartment                     | | 4    | Bed and breakfast             | | 5    | Cabin or bungalow             | | 6    | Campground                    | | 7    | Chalet                        | | 8    | Condominium                   | | 9    | Conference center             | | 10   | Corporate                     | | 11   | Corporate business transient  | | 12   | Cruise                        | | 13   | Extended stay                 | | 14   | Ferry                         | | 15   | Guest farm                    | | 16   | Guest house limited service   | | 17   | Health spa                    | | 18   | Holiday resort                | | 19   | Hostel                        | | 20   | Hotel                         | | 21   | Inn                           | | 22   | Lodge                         | | 23   | Meeting resort                | | 24   | Meeting/Convention            | | 25   | Mobile-home                   | | 26   | Monastery                     | | 27   | Motel                         | | 28   | Ranch                         | | 29   | Residential apartment         | | 30   | Resort                        | | 31   | Sailing ship                  | | 32   | Self catering accommodation   | | 33   | Tent                          | | 34   | Vacation home                 | | 35   | Villa                         | | 36   | Wildlife reserve              | | 37   | Castle                        | | 38   | Convention Network Property   | | 39   | Golf                          | | 40   | Pension                       | | 41   | Ski                           | | 42   | Spa                           | | 43   | Time share                    | | 44   | Boatel                        | | 45   | Boutique                      | | 46   | Efficiency/studio             | | 47   | Full service                  | | 48   | Historical                    | | 49   | Limited service               | | 50   | Recreational vehicle park     | | 51   | Charm hotel                   | | 52   | Manor                         | | 53   | Vacation rental               | | 54   | Economy                       | | 55   | Midscale                      | | 56   | Upscale                       | | 57   | Luxury                        | | 58   | Union                         | | 59   | Leisure                       | | 60   | Wholesale                     | | 61   | Transient                     | | 62   | Other                         | | 5000 | ApartHotel                    | | 5001 | Riad                          | | 5002 | Ryokan                        | | 5003 | Love Hotel                    | | 5004 | Homestay                      | | 5005 | Japanese-style Business Hotel | | 5006 | Holiday Home                  | | 5007 | Country house                 | | 5008 | Capsule Hotel                 | | 5009 | Holiday Park                  |  ### unitTypeCode  | Code | Name             | | ---- | ---------------- | | 1    | Apartment        | | 4    | Quadruple        | | 5    | Suite            | | 7    | Triple           | | 8    | Twin             | | 9    | Double           | | 10   | Single           | | 12   | Studio           | | 13   | Family           | | 24   | Twin/Double      | | 25   | Dormitory room   | | 26   | Bed in Dormitory | | 27   | Bungalow         | | 28   | Chalet           | | 29   | Holiday home     | | 31   | Villa            | | 32   | Mobile home      | | 33   | Tent             |  ### unitAmenityCode  | Code  | Name                                                         | | ----- | ------------------------------------------------------------ | | 1     | Adjoining rooms                                              | | 2     | Air conditioning                                             | | 3     | Alarm clock                                                  | | 4     | All news channel                                             | | 5     | AM/FM radio                                                  | | 6     | Baby listening device                                        | | 7     | Balcony/Lanai/Terrace                                        | | 8     | Barbeque grills                                              | | 9     | Bath tub with spray jets                                     | | 10    | Bathrobe                                                     | | 11    | Bathroom amenities                                           | | 12    | Bathroom telephone                                           | | 13    | Bathtub                                                      | | 14    | Bathtub only                                                 | | 15    | Bathtub/shower combination                                   | | 16    | Bidet                                                        | | 17    | Bottled water                                                | | 18    | Cable television                                             | | 19    | Coffee/Tea maker                                             | | 20    | Color television                                             | | 21    | Computer                                                     | | 22    | Connecting rooms                                             | | 23    | Converters/ Voltage adaptors                                 | | 24    | Copier                                                       | | 25    | Cordless phone                                               | | 26    | Cribs                                                        | | 27    | Data port                                                    | | 28    | Desk                                                         | | 29    | Desk with lamp                                               | | 30    | Dining guide                                                 | | 31    | Direct dial phone number                                     | | 32    | Dishwasher                                                   | | 33    | Double beds                                                  | | 34    | Dual voltage outlet                                          | | 35    | Electrical current voltage                                   | | 36    | Ergonomic chair                                              | | 37    | Extended phone cord                                          | | 38    | Fax machine                                                  | | 39    | Fire alarm                                                   | | 40    | Fire alarm with light                                        | | 41    | Fireplace                                                    | | 42    | Free toll free calls                                         | | 43    | Free calls                                                   | | 44    | Free credit card access calls                                | | 45    | Free local calls                                             | | 46    | Free movies/video                                            | | 47    | Full kitchen                                                 | | 48    | Grab bars in bathroom                                        | | 49    | Grecian tub                                                  | | 50    | Hairdryer                                                    | | 51    | High speed internet connection                               | | 52    | Interactive web TV                                           | | 53    | International direct dialing                                 | | 54    | Internet access                                              | | 55    | Iron                                                         | | 56    | Ironing board                                                | | 57    | Whirpool                                                     | | 58    | King bed                                                     | | 59    | Kitchen                                                      | | 60    | Kitchen supplies                                             | | 61    | Kitchenette                                                  | | 62    | Knock light                                                  | | 63    | Laptop                                                       | | 64    | Large desk                                                   | | 65    | Large work area                                              | | 66    | Laundry basket/clothes hamper                                | | 67    | Loft                                                         | | 68    | Microwave                                                    | | 69    | Minibar                                                      | | 70    | Modem                                                        | | 71    | Modem jack                                                   | | 72    | Multi-line phone                                             | | 73    | Newspaper                                                    | | 74    | Non-smoking                                                  | | 75    | Notepads                                                     | | 76    | Office supplies                                              | | 77    | Oven                                                         | | 78    | Pay per view movies on TV                                    | | 79    | Pens                                                         | | 80    | Phone in bathroom                                            | | 81    | Plates and bowls                                             | | 82    | Pots and pans                                                | | 83    | Prayer mats                                                  | | 84    | Printer                                                      | | 85    | Private bathroom                                             | | 86    | Queen bed                                                    | | 87    | Recliner                                                     | | 88    | Refrigerator                                                 | | 89    | Refrigerator with ice maker                                  | | 90    | Remote control television                                    | | 91    | Rollaway bed                                                 | | 92    | Safe                                                         | | 93    | Scanner                                                      | | 94    | Separate closet                                              | | 95    | Separate modem line available                                | | 96    | Shoe polisher                                                | | 97    | Shower only                                                  | | 98    | Silverware/utensils                                          | | 99    | Sitting area                                                 | | 100   | Smoke detectors                                              | | 101   | Smoking                                                      | | 102   | Sofa bed                                                     | | 103   | Speaker phone                                                | | 104   | Stereo                                                       | | 105   | Stove                                                        | | 106   | Tape recorder                                                | | 107   | Telephone                                                    | | 108   | Telephone for hearing impaired                               | | 109   | Telephones with message light                                | | 110   | Toaster oven                                                 | | 111   | Trouser/Pant press                                           | | 112   | Turn down service                                            | | 113   | Twin bed                                                     | | 114   | Vaulted ceilings                                             | | 115   | VCR movies                                                   | | 116   | VCR player                                                   | | 117   | Video games                                                  | | 118   | Voice mail                                                   | | 119   | Wake-up calls                                                | | 120   | Water closet                                                 | | 121   | Water purification system                                    | | 122   | Wet bar                                                      | | 123   | Wireless internet connection                                 | | 124   | Wireless keyboard                                            | | 125   | Adaptor available for telephone PC use                       | | 126   | Air conditioning individually controlled in room             | | 127   | Bathtub &whirlpool separate                                  | | 128   | Telephone with data ports                                    | | 129   | CD player                                                    | | 130   | Complimentary local calls time limit                         | | 131   | Extra person charge for rollaway use                         | | 132   | Down/feather pillows                                         | | 133   | Desk with electrical outlet                                  | | 134   | ESPN available                                               | | 135   | Foam pillows                                                 | | 136   | HBO available                                                | | 137   | High ceilings                                                | | 138   | Marble bathroom                                              | | 139   | List of movie channels available                             | | 140   | Pets allowed                                                 | | 141   | Oversized bathtub                                            | | 142   | Shower                                                       | | 143   | Sink in-room                                                 | | 144   | Soundproofed room                                            | | 145   | Storage space                                                | | 146   | Tables and chairs                                            | | 147   | Two-line phone                                               | | 148   | Walk-in closet                                               | | 149   | Washer/dryer                                                 | | 150   | Weight scale                                                 | | 151   | Welcome gift                                                 | | 152   | Spare electrical outlet available at desk                    | | 153   | Non-refundable charge for pets                               | | 154   | Refundable deposit for pets                                  | | 155   | Separate tub and shower                                      | | 156   | Entrance type to guest room                                  | | 157   | Ceiling fan                                                  | | 158   | CNN available                                                | | 159   | Electrical adaptors available                                | | 160   | Buffet breakfast                                             | | 161   | Accessible room                                              | | 162   | Closets in room                                              | | 163   | DVD player                                                   | | 164   | Mini-refrigerator                                            | | 165   | Separate line billing for multi-line phone                   | | 166   | Self-controlled heating/cooling system                       | | 167   | Toaster                                                      | | 168   | Analog data port                                             | | 169   | Collect calls                                                | | 170   | International calls                                          | | 171   | Carrier access                                               | | 172   | Interstate calls                                             | | 173   | Intrastate calls                                             | | 174   | Local calls                                                  | | 175   | Long distance calls                                          | | 176   | Operator-assisted calls                                      | | 177   | Credit card access calls                                     | | 178   | Calling card calls                                           | | 179   | Toll free calls                                              | | 180   | Universal AC/DC adaptors                                     | | 181   | Bathtub seat                                                 | | 182   | Canopy/poster bed                                            | | 183   | Cups/glassware                                               | | 184   | Entertainment center                                         | | 185   | Family/oversized room                                        | | 186   | Hypoallergenic bed                                           | | 187   | Hypoallergenic pillows                                       | | 188   | Lamp                                                         | | 189   | Meal included: breakfast                                     | | 190   | Meal included: continental breakfast                         | | 191   | Meal included: dinner                                        | | 192   | Meal included: lunch                                         | | 193   | Shared bathroom                                              | | 194   | Telephone TDD/Textphone                                      | | 195   | Water bed                                                    | | 196   | Extra adult charge                                           | | 197   | Extra child charge                                           | | 198   | Extra child charge for rollaway use                          | | 199   | Meal included: full American breakfast                       | | 200   | Futon                                                        | | 201   | Murphy bed                                                   | | 202   | Tatami mats                                                  | | 203   | Single bed                                                   | | 204   | Annex room                                                   | | 205   | Free newspaper                                               | | 206   | Honeymoon suites                                             | | 207   | Complimentary high speed internet in room                    | | 208   | Maid service                                                 | | 209   | PC hook-up in room                                           | | 210   | Satellite television                                         | | 211   | VIP rooms                                                    | | 212   | Cell phone recharger                                         | | 213   | DVR player                                                   | | 214   | iPod docking station                                         | | 215   | Media center                                                 | | 216   | Plug & play panel                                            | | 217   | Satellite radio                                              | | 218   | Video on demand                                              | | 219   | Exterior corridors                                           | | 220   | Gulf view                                                    | | 221   | Accessible room                                              | | 222   | Interior corridors                                           | | 223   | Mountain view                                                | | 224   | Ocean view                                                   | | 225   | High speed internet access fee                               | | 226   | High speed wireless                                          | | 227   | Premium movie channels                                       | | 228   | Slippers                                                     | | 229   | First nighters' kit                                          | | 230   | Chair provided with desk                                     | | 231   | Pillow top mattress                                          | | 232   | Feather bed                                                  | | 233   | Duvet                                                        | | 234   | Luxury linen type                                            | | 235   | International channels                                       | | 236   | Pantry                                                       | | 237   | Dish-cleaning supplies                                       | | 238   | Double vanity                                                | | 239   | Lighted makeup mirror                                        | | 240   | Upgraded bathroom amenities                                  | | 241   | VCR player available at front desk                           | | 242   | Instant hot water                                            | | 243   | Outdoor space                                                | | 244   | Hinoki tub                                                   | | 245   | Private pool                                                 | | 246   | High Definition (HD) Flat Panel Television - 32 inches or greater | | 247   | Room windows open                                            | | 248   | Bedding type unknown or unspecified                          | | 249   | Full bed                                                     | | 250   | Round bed                                                    | | 251   | TV                                                           | | 252   | Child rollaway                                               | | 253   | DVD player available at front desk                           | | 254   | Video game player:                                           | | 255   | Video game player available at front desk                    | | 256   | Dining room seats                                            | | 257   | Full size mirror                                             | | 258   | Mobile/cellular phones                                       | | 259   | Movies                                                       | | 260   | Multiple closets                                             | | 261   | Plates/glassware                                             | | 262   | Safe large enough to accommodate a laptop                    | | 263   | Bed linen thread count                                       | | 264   | Blackout curtain                                             | | 265   | Bluray player                                                | | 266   | Device with mp3                                              | | 267   | No adult channels or adult channel lock                      | | 268   | Non-allergenic room                                          | | 269   | Pillow type                                                  | | 270   | Seating area with sofa/chair                                 | | 271   | Separate toilet area                                         | | 272   | Web enabled                                                  | | 273   | Widescreen TV                                                | | 274   | Other data connection                                        | | 275   | Phoneline billed separately                                  | | 276   | Separate tub or shower                                       | | 277   | Video games                                                  | | 278   | Roof ventilator                                              | | 279   | Children's playpen                                           | | 280   | Plunge pool                                                  | | 281   | DVD movies                                                   | | 282   | Air filtration                                               | | 283   | Exercise Equipment in Room                                   | | 5001  | Coffee/Tea maker                                             | | 5002  | Internet facilities                                          | | 5003  | Mini-bar                                                     | | 5004  | Shower                                                       | | 5005  | Bath                                                         | | 5006  | Safe Deposit Box                                             | | 5007  | Pay-per-view Channels                                        | | 5008  | TV                                                           | | 5009  | Telephone                                                    | | 5010  | Fax                                                          | | 5011  | Airconditioning                                              | | 5012  | Hair Dryer                                                   | | 5013  | Wake Up Service/Alarm-clock                                  | | 5014  | Hot Tub                                                      | | 5015  | Clothing Iron                                                | | 5016  | Kitchenette                                                  | | 5017  | Balcony                                                      | | 5018  | Trouser Press                                                | | 5019  | Bath-robe                                                    | | 5020  | Spa Bath                                                     | | 5021  | Radio                                                        | | 5022  | Refrigerator                                                 | | 5023  | Desk                                                         | | 5024  | Shared Bathroom                                              | | 5025  | Ironing facilities                                           | | 5026  | Seating area                                                 | | 5027  | Free Toiletries                                              | | 5028  | DVD-Player                                                   | | 5029  | CD-Player                                                    | | 5030  | Fan                                                          | | 5031  | Toilet                                                       | | 5032  | Microwave                                                    | | 5033  | Dishwasher                                                   | | 5034  | Washing machine                                              | | 5035  | Video                                                        | | 5036  | Video Games                                                  | | 5037  | Patio                                                        | | 5038  | Bathroom                                                     | | 5039  | Extra long beds (> 2 meter)                                  | | 5040  | Heating                                                      | | 5041  | Dressing room                                                | | 5042  | Guest toilet                                                 | | 5043  | Slippers                                                     | | 5044  | Satellite Channels                                           | | 5045  | Kitchen                                                      | | 5046  | Wireless internet                                            | | 5068  | Cable channels                                               | | 5069  | Bath or Shower                                               | | 5070  | Carpeted Floor                                               | | 5071  | Fireplace                                                    | | 5072  | Additional Toilet                                            | | 5073  | Interconnecting Room(s) available                            | | 5074  | Laptop Safe Box                                              | | 5075  | Flat-screen TV                                               | | 5076  | Private Entrance                                             | | 5077  | Sofa                                                         | | 5079  | Soundproofing                                                | | 5080  | Tiled / Marble floor                                         | | 5081  | View                                                         | | 5082  | Wooden / Parquet floor                                       | | 5083  | Wake Up Service                                              | | 5084  | Alarm Clock                                                  | | 5085  | Dining Area                                                  | | 5086  | Electric Kettle                                              | | 5087  | Executive Lounge Access                                      | | 5088  | iPod Docking Station                                         | | 5089  | Kitchenware                                                  | | 5090  | Mosquito Net                                                 | | 5091  | Towels/Linens at surcharge                                   | | 5092  | Sauna                                                        | | 5093  | Private Pool                                                 | | 5094  | Tumble dryer (machine)                                       | | 5095  | Wardrobe/Closet                                              | | 5096  | Oven                                                         | | 5097  | Stove                                                        | | 5098  | Toaster                                                      | | 5099  | Barbecue                                                     | | 5100  | Bidet                                                        | | 5101  | Computer                                                     | | 5102  | iPad                                                         | | 5103  | Game Console                                                 | | 5104  | Game Console - Xbox 360                                      | | 5105  | Game Console - PS2                                           | | 5106  | Game Console - PS3                                           | | 5107  | Game Console - Nintendo Wii                                  | | 5108  | Sea View                                                     | | 5109  | Lake View                                                    | | 5110  | Garden View                                                  | | 5111  | Pool View                                                    | | 5112  | Mountain View                                                | | 5113  | Landmark View                                                | | 5114  | Laptop                                                       | | 5115  | Allergy-Free                                                 | | 5116  | Cleaning products                                            | | 5117  | Electric blankets                                            | | 5118  | Additional Bathroom                                          | | 5119  | Blu-ray player                                               | | 5120  | Coffee Machine                                               | | 5121  | City View                                                    | | 5122  | River View                                                   | | 5123  | Terrace                                                      | | 5124  | Towels                                                       | | 5125  | Linen                                                        | | 5126  | Dining table                                                 | | 5127  | Children highchair                                           | | 5129  | Outdoor furniture                                            | | 5130  | Outdoor dining area                                          | | 5131  | Entire property on ground floor                              | | 5132  | Upper floor reachable by lift                                | | 5133  | Upper floor reachable by stairs only                         | | 5134  | Entire unit wheelchair accessible                            | | 5135  | Detached                                                     | | 5136  | Semi-detached                                                | | 5137  | Private flat in block of flats                               | | 5138  | Clothes Rack                                                 | | 5139  | Rollaway bed                                                 | | 5140  | Clothes drying rack                                          | | 5141  | Toilet paper                                                 | | 5142  | Child safety socket covers                                   | | 5143  | Board games/puzzles                                          | | 5144  | Book/DVD/Music library for children                          | | 5145  | Baby safety gates                                            | | 5146  | Sofa bed                                                     | | 5147  | Toilet with grab rails                                       | | 5148  | Adapted bath                                                 | | 5149  | Roll in shower                                               | | 5150  | Walk in shower                                               | | 5151  | Higher level toilet                                          | | 5152  | Low bathroom sink                                            | | 5153  | Bathroom emergency pull cord                                 | | 5154  | Shower chair                                                 | | 5157  | Rooftop pool                                                 | | 5158  | Infinity pool                                                | | 5159  | Pool with view                                               | | 5160  | Heated pool                                                  | | 5161  | Salt-water pool                                              | | 5162  | Plunge pool                                                  | | 5163  | Pool towels                                                  | | 5164  | Shallow end                                                  | | 5165  | Pool cover                                                   | | 5166  | Wine/champagne                                               | | 5167  | Bottle of water                                              | | 5168  | Fruits                                                       | | 5169  | Chocolate/cookies                                            | | 5170  | Trash cans                                                   | | 5171  | Wine glasses                                                 | | 5172  | Game console - Xbox One                                      | | 5173  | Game console - Wii U                                         | | 5174  | Game console - PS4                                           | | 5175  | Children crib/cots                                           | | 5176  | Toothbrush                                                   | | 5177  | Shampoo                                                      | | 5178  | Conditioner                                                  | | 5179  | Body soap                                                    | | 5180  | Shower cap                                                   | | 5181  | Pajamas                                                      | | 5182  | Yukata                                                       | | 5184  | Socket near the bed                                          | | 5185  | Adapter                                                      | | 5186  | Feather pillow                                               | | 5187  | Non-feather pillow                                           | | 5188  | Hypoallergenic pillow                                        | | 5189  | Accessible by Lift                                           | | 5190  | Inner courtyard view                                         | | 5191  | Quiet street view                                            | | 5196  | Portable Wifi                                                | | 5198  | Smartphone                                                   | | 5199  | Streaming service (such as Netflix)                          | | 5200  | Lockers                                                      | | 5201  | Fire alarms or smoke detectors                               | | 5202  | Fire extinguishers                                           | | 5203  | Metal keys access                                            | | 5204  | Electronic key card access                                   | | 5205  | Reading light                                                | | 5206  | Earplugs                                                     | | 5207  | Private curtain                                              | | 5211  | Carbon monoxide detector                                     | | 5212  | Carbon monoxide source                                       | | 90001 | Bread-bun delivery                                           | | 90002 | Breakfast delivery                                           | | 90003 | Grocery delivery service                                     | | 90004 | Beach chair or roofed wicker beach chair                     | | 90005 | Shared kitchen                                               | | 90006 | Bunk bed                                                     | | 90007 | Levee view                                                   | | 90008 | Pay television                                               | | 90009 | Extractor hood                                               | | 90010 | Vacuum cleaner                                               | | 90011 | Separated bedrooms                                           |  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@lodgea.com
    Generated by: https://openapi-generator.tech
"""


import json
import atexit
import mimetypes
from multiprocessing.pool import ThreadPool
import io
import os
import re
import typing
from urllib.parse import quote
from urllib3.fields import RequestField


from openapi_client import rest
from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiTypeError, ApiValueError, ApiException
from openapi_client.model_utils import (
    ModelNormal,
    ModelSimple,
    ModelComposed,
    check_allowed_values,
    check_validations,
    date,
    datetime,
    deserialize_file,
    file_type,
    model_to_dict,
    none_type,
    validate_and_convert_types
)


class ApiClient(object):
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    _pool = None

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1):
        if configuration is None:
            configuration = Configuration.get_default_copy()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)

    @property
    def pool(self):
        """Create thread pool on first request
         avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
        _content_type: typing.Optional[str] = None,
        _request_auths: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    ):

        config = self.configuration

        # header parameters
        header_params = header_params or {}
        header_params.update(self.default_headers)
        if self.cookie:
            header_params['Cookie'] = self.cookie
        if header_params:
            header_params = self.sanitize_for_serialization(header_params)
            header_params = dict(self.parameters_to_tuples(header_params,
                                                           collection_formats))

        # path parameters
        if path_params:
            path_params = self.sanitize_for_serialization(path_params)
            path_params = self.parameters_to_tuples(path_params,
                                                    collection_formats)
            for k, v in path_params:
                # specified safe chars, encode everything
                resource_path = resource_path.replace(
                    '{%s}' % k,
                    quote(str(v), safe=config.safe_chars_for_path_param)
                )

        # query parameters
        if query_params:
            query_params = self.sanitize_for_serialization(query_params)
            query_params = self.parameters_to_tuples(query_params,
                                                     collection_formats)

        # post parameters
        if post_params or files:
            post_params = post_params if post_params else []
            post_params = self.sanitize_for_serialization(post_params)
            post_params = self.parameters_to_tuples(post_params,
                                                    collection_formats)
            post_params.extend(self.files_parameters(files))
            if header_params['Content-Type'].startswith("multipart"):
                post_params = self.parameters_to_multipart(post_params,
                                                           (dict))

        # body
        if body:
            body = self.sanitize_for_serialization(body)

        # auth setting
        self.update_params_for_auth(header_params, query_params,
                                    auth_settings, resource_path, method, body,
                                    request_auths=_request_auths)

        # request url
        if _host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = _host + resource_path

        try:
            # perform request and return response
            response_data = self.request(
                method, url, query_params=query_params, headers=header_params,
                post_params=post_params, body=body,
                _preload_content=_preload_content,
                _request_timeout=_request_timeout)
        except ApiException as e:
            e.body = e.body.decode('utf-8')
            raise e

        self.last_response = response_data

        return_data = response_data

        if not _preload_content:
            return (return_data)
            return return_data

        # deserialize response data
        if response_type:
            if response_type != (file_type,):
                encoding = "utf-8"
                content_type = response_data.getheader('content-type')
                if content_type is not None:
                    match = re.search(r"charset=([a-zA-Z\-\d]+)[\s\;]?", content_type)
                    if match:
                        encoding = match.group(1)
                response_data.data = response_data.data.decode(encoding)

            return_data = self.deserialize(
                response_data,
                response_type,
                _check_type
            )
        else:
            return_data = None

        if _return_http_data_only:
            return (return_data)
        else:
            return (return_data, response_data.status,
                    response_data.getheaders())

    def parameters_to_multipart(self, params, collection_types):
        """Get parameters as list of tuples, formatting as json if value is collection_types

        :param params: Parameters as list of two-tuples
        :param dict collection_types: Parameter collection types
        :return: Parameters as list of tuple or urllib3.fields.RequestField
        """
        new_params = []
        if collection_types is None:
            collection_types = (dict)
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if isinstance(
                     v, collection_types): # v is instance of collection_type, formatting as application/json
                v = json.dumps(v, ensure_ascii=False).encode("utf-8")
                field = RequestField(k, v)
                field.make_multipart(content_type="application/json; charset=utf-8")
                new_params.append(field)
            else:
                new_params.append((k, v))
        return new_params

    @classmethod
    def sanitize_for_serialization(cls, obj):
        """Prepares data for transmission before it is sent with the rest client
        If obj is None, return None.
        If obj is str, int, long, float, bool, return directly.
        If obj is datetime.datetime, datetime.date
            convert to string in iso8601 format.
        If obj is list, sanitize each element in the list.
        If obj is dict, return the dict.
        If obj is OpenAPI model, return the properties dict.
        If obj is io.IOBase, return the bytes
        :param obj: The data to serialize.
        :return: The serialized form of data.
        """
        if isinstance(obj, (ModelNormal, ModelComposed)):
            return {
                key: cls.sanitize_for_serialization(val) for key,
                val in model_to_dict(
                    obj,
                    serialize=True).items()}
        elif isinstance(obj, io.IOBase):
            return cls.get_file_data_and_close_file(obj)
        elif isinstance(obj, (str, int, float, none_type, bool)):
            return obj
        elif isinstance(obj, (datetime, date)):
            return obj.isoformat()
        elif isinstance(obj, ModelSimple):
            return cls.sanitize_for_serialization(obj.value)
        elif isinstance(obj, (list, tuple)):
            return [cls.sanitize_for_serialization(item) for item in obj]
        if isinstance(obj, dict):
            return {key: cls.sanitize_for_serialization(val) for key, val in obj.items()}
        raise ApiValueError(
            'Unable to prepare type {} for serialization'.format(
                obj.__class__.__name__))

    def deserialize(self, response, response_type, _check_type):
        """Deserializes response into an object.

        :param response: RESTResponse object to be deserialized.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param _check_type: boolean, whether to check the types of the data
            received from the server
        :type _check_type: bool

        :return: deserialized object.
        """
        # handle file downloading
        # save response body into a tmp file and return the instance
        if response_type == (file_type,):
            content_disposition = response.getheader("Content-Disposition")
            return deserialize_file(response.data, self.configuration,
                                    content_disposition=content_disposition)

        # fetch data from response object
        try:
            received_data = json.loads(response.data)
        except ValueError:
            received_data = response.data

        # store our data under the key of 'received_data' so users have some
        # context if they are deserializing a string and the data type is wrong
        deserialized_data = validate_and_convert_types(
            received_data,
            response_type,
            ['received_data'],
            True,
            _check_type,
            configuration=self.configuration
        )
        return deserialized_data

    def call_api(
        self,
        resource_path: str,
        method: str,
        path_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        query_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        header_params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        body: typing.Optional[typing.Any] = None,
        post_params: typing.Optional[typing.List[typing.Tuple[str, typing.Any]]] = None,
        files: typing.Optional[typing.Dict[str, typing.List[io.IOBase]]] = None,
        response_type: typing.Optional[typing.Tuple[typing.Any]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        async_req: typing.Optional[bool] = None,
        _return_http_data_only: typing.Optional[bool] = None,
        collection_formats: typing.Optional[typing.Dict[str, str]] = None,
        _preload_content: bool = True,
        _request_timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
        _host: typing.Optional[str] = None,
        _check_type: typing.Optional[bool] = None,
        _request_auths: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    ):
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: For the response, a tuple containing:
            valid classes
            a list containing valid classes (for list schemas)
            a dict containing a tuple of valid classes as the value
            Example values:
            (str,)
            (Pet,)
            (float, none_type)
            ([int, none_type],)
            ({str: (bool, str, int, float, date, datetime, str, none_type)},)
        :param files: key -> field name, value -> a list of open file
            objects for `multipart/form-data`.
        :type files: dict
        :param async_req bool: execute request asynchronously
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :type collection_formats: dict, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _check_type: boolean describing if the data back from the server
            should have its type checked.
        :type _check_type: bool, optional
        :param _request_auths: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auths: list, optional
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """
        if not async_req:
            return self.__call_api(resource_path, method,
                                   path_params, query_params, header_params,
                                   body, post_params, files,
                                   response_type, auth_settings,
                                   _return_http_data_only, collection_formats,
                                   _preload_content, _request_timeout, _host,
                                   _check_type, _request_auths=_request_auths)

        return self.pool.apply_async(self.__call_api, (resource_path,
                                                       method, path_params,
                                                       query_params,
                                                       header_params, body,
                                                       post_params, files,
                                                       response_type,
                                                       auth_settings,
                                                       _return_http_data_only,
                                                       collection_formats,
                                                       _preload_content,
                                                       _request_timeout,
                                                       _host, _check_type, None, _request_auths))

    def request(self, method, url, query_params=None, headers=None,
                post_params=None, body=None, _preload_content=True,
                _request_timeout=None):
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        query_params=query_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         query_params=query_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            query_params=query_params,
                                            headers=headers,
                                            post_params=post_params,
                                            _preload_content=_preload_content,
                                            _request_timeout=_request_timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         query_params=query_params,
                                         headers=headers,
                                         post_params=post_params,
                                         _preload_content=_preload_content,
                                         _request_timeout=_request_timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        query_params=query_params,
                                        headers=headers,
                                        post_params=post_params,
                                        _preload_content=_preload_content,
                                        _request_timeout=_request_timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          query_params=query_params,
                                          headers=headers,
                                          post_params=post_params,
                                          _preload_content=_preload_content,
                                          _request_timeout=_request_timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           query_params=query_params,
                                           headers=headers,
                                           _preload_content=_preload_content,
                                           _request_timeout=_request_timeout,
                                           body=body)
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def parameters_to_tuples(self, params, collection_formats):
        """Get parameters as list of tuples, formatting collections.

        :param params: Parameters as dict or list of two-tuples
        :param dict collection_formats: Parameter collection formats
        :return: Parameters as list of tuples, collections formatted
        """
        new_params = []
        if collection_formats is None:
            collection_formats = {}
        for k, v in params.items() if isinstance(params, dict) else params:  # noqa: E501
            if k in collection_formats:
                collection_format = collection_formats[k]
                if collection_format == 'multi':
                    new_params.extend((k, value) for value in v)
                else:
                    if collection_format == 'ssv':
                        delimiter = ' '
                    elif collection_format == 'tsv':
                        delimiter = '\t'
                    elif collection_format == 'pipes':
                        delimiter = '|'
                    else:  # csv is the default
                        delimiter = ','
                    new_params.append(
                        (k, delimiter.join(str(value) for value in v)))
            else:
                new_params.append((k, v))
        return new_params

    @staticmethod
    def get_file_data_and_close_file(file_instance: io.IOBase) -> bytes:
        file_data = file_instance.read()
        file_instance.close()
        return file_data

    def files_parameters(self,
                         files: typing.Optional[typing.Dict[str,
                                                            typing.List[io.IOBase]]] = None):
        """Builds form parameters.

        :param files: None or a dict with key=param_name and
            value is a list of open file objects
        :return: List of tuples of form parameters with file data
        """
        if files is None:
            return []

        params = []
        for param_name, file_instances in files.items():
            if file_instances is None:
                # if the file field is nullable, skip None values
                continue
            for file_instance in file_instances:
                if file_instance is None:
                    # if the file field is nullable, skip None values
                    continue
                if file_instance.closed is True:
                    raise ApiValueError(
                        "Cannot read a closed file. The passed in file_type "
                        "for %s must be open." % param_name
                    )
                filename = os.path.basename(file_instance.name)
                filedata = self.get_file_data_and_close_file(file_instance)
                mimetype = (mimetypes.guess_type(filename)[0] or
                            'application/octet-stream')
                params.append(
                    tuple([param_name, tuple([filename, filedata, mimetype])]))

        return params

    def select_header_accept(self, accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'
        else:
            return ', '.join(accepts)

    def select_header_content_type(self, content_types, method=None, body=None):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :param method: http method (e.g. POST, PATCH).
        :param body: http body to send.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return None

        content_types = [x.lower() for x in content_types]

        if (method == 'PATCH' and
                'application/json-patch+json' in content_types and
                isinstance(body, list)):
            return 'application/json-patch+json'

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'
        else:
            return content_types[0]

    def update_params_for_auth(self, headers, queries, auth_settings,
                               resource_path, method, body, request_auths=None):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param queries: Query parameters tuple list to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :param resource_path: A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method.
        :param body: A object representing the body of the HTTP request.
            The object type is the return value of _encoder.default().
        :param request_auths: if set, the provided settings will
            override the token in the configuration.
        """
        if not auth_settings:
            return

        if request_auths:
            for auth_setting in request_auths:
                self._apply_auth_params(
                    headers, queries, resource_path, method, body, auth_setting)
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if auth_setting:
                self._apply_auth_params(
                    headers, queries, resource_path, method, body, auth_setting)

    def _apply_auth_params(self, headers, queries, resource_path, method, body, auth_setting):
        if auth_setting['in'] == 'cookie':
            headers['Cookie'] = auth_setting['key'] + "=" + auth_setting['value']
        elif auth_setting['in'] == 'header':
            if auth_setting['type'] != 'http-signature':
                headers[auth_setting['key']] = auth_setting['value']
        elif auth_setting['in'] == 'query':
            queries.append((auth_setting['key'], auth_setting['value']))
        else:
            raise ApiValueError(
                'Authentication token must be in `query` or `header`'
            )


class Endpoint(object):
    def __init__(self, settings=None, params_map=None, root_map=None,
                 headers_map=None, api_client=None, callable=None):
        """Creates an endpoint

        Args:
            settings (dict): see below key value pairs
                'response_type' (tuple/None): response type
                'auth' (list): a list of auth type keys
                'endpoint_path' (str): the endpoint path
                'operation_id' (str): endpoint string identifier
                'http_method' (str): POST/PUT/PATCH/GET etc
                'servers' (list): list of str servers that this endpoint is at
            params_map (dict): see below key value pairs
                'all' (list): list of str endpoint parameter names
                'required' (list): list of required parameter names
                'nullable' (list): list of nullable parameter names
                'enum' (list): list of parameters with enum values
                'validation' (list): list of parameters with validations
            root_map
                'validations' (dict): the dict mapping endpoint parameter tuple
                    paths to their validation dictionaries
                'allowed_values' (dict): the dict mapping endpoint parameter
                    tuple paths to their allowed_values (enum) dictionaries
                'openapi_types' (dict): param_name to openapi type
                'attribute_map' (dict): param_name to camelCase name
                'location_map' (dict): param_name to  'body', 'file', 'form',
                    'header', 'path', 'query'
                collection_format_map (dict): param_name to `csv` etc.
            headers_map (dict): see below key value pairs
                'accept' (list): list of Accept header strings
                'content_type' (list): list of Content-Type header strings
            api_client (ApiClient) api client instance
            callable (function): the function which is invoked when the
                Endpoint is called
        """
        self.settings = settings
        self.params_map = params_map
        self.params_map['all'].extend([
            'async_req',
            '_host_index',
            '_preload_content',
            '_request_timeout',
            '_return_http_data_only',
            '_check_input_type',
            '_check_return_type',
            '_content_type',
            '_spec_property_naming',
            '_request_auths'
        ])
        self.params_map['nullable'].extend(['_request_timeout'])
        self.validations = root_map['validations']
        self.allowed_values = root_map['allowed_values']
        self.openapi_types = root_map['openapi_types']
        extra_types = {
            'async_req': (bool,),
            '_host_index': (none_type, int),
            '_preload_content': (bool,),
            '_request_timeout': (none_type, float, (float,), [float], int, (int,), [int]),
            '_return_http_data_only': (bool,),
            '_check_input_type': (bool,),
            '_check_return_type': (bool,),
            '_spec_property_naming': (bool,),
            '_content_type': (none_type, str),
            '_request_auths': (none_type, list)
        }
        self.openapi_types.update(extra_types)
        self.attribute_map = root_map['attribute_map']
        self.location_map = root_map['location_map']
        self.collection_format_map = root_map['collection_format_map']
        self.headers_map = headers_map
        self.api_client = api_client
        self.callable = callable

    def __validate_inputs(self, kwargs):
        for param in self.params_map['enum']:
            if param in kwargs:
                check_allowed_values(
                    self.allowed_values,
                    (param,),
                    kwargs[param]
                )

        for param in self.params_map['validation']:
            if param in kwargs:
                check_validations(
                    self.validations,
                    (param,),
                    kwargs[param],
                    configuration=self.api_client.configuration
                )

        if kwargs['_check_input_type'] is False:
            return

        for key, value in kwargs.items():
            fixed_val = validate_and_convert_types(
                value,
                self.openapi_types[key],
                [key],
                kwargs['_spec_property_naming'],
                kwargs['_check_input_type'],
                configuration=self.api_client.configuration
            )
            kwargs[key] = fixed_val

    def __gather_params(self, kwargs):
        params = {
            'body': None,
            'collection_format': {},
            'file': {},
            'form': [],
            'header': {},
            'path': {},
            'query': []
        }

        for param_name, param_value in kwargs.items():
            param_location = self.location_map.get(param_name)
            if param_location is None:
                continue
            if param_location:
                if param_location == 'body':
                    params['body'] = param_value
                    continue
                base_name = self.attribute_map[param_name]
                if (param_location == 'form' and
                        self.openapi_types[param_name] == (file_type,)):
                    params['file'][base_name] = [param_value]
                elif (param_location == 'form' and
                        self.openapi_types[param_name] == ([file_type],)):
                    # param_value is already a list
                    params['file'][base_name] = param_value
                elif param_location in {'form', 'query'}:
                    param_value_full = (base_name, param_value)
                    params[param_location].append(param_value_full)
                if param_location not in {'form', 'query'}:
                    params[param_location][base_name] = param_value
                collection_format = self.collection_format_map.get(param_name)
                if collection_format:
                    params['collection_format'][base_name] = collection_format

        return params

    def __call__(self, *args, **kwargs):
        """ This method is invoked when endpoints are called
        Example:

        api_instance = AvailabilityApi()
        api_instance.v1_availability_search_post  # this is an instance of the class Endpoint
        api_instance.v1_availability_search_post()  # this invokes api_instance.v1_availability_search_post.__call__()
        which then invokes the callable functions stored in that endpoint at
        api_instance.v1_availability_search_post.callable or self.callable in this class

        """
        return self.callable(self, *args, **kwargs)

    def call_with_http_info(self, **kwargs):

        try:
            index = self.api_client.configuration.server_operation_index.get(
                self.settings['operation_id'], self.api_client.configuration.server_index
            ) if kwargs['_host_index'] is None else kwargs['_host_index']
            server_variables = self.api_client.configuration.server_operation_variables.get(
                self.settings['operation_id'], self.api_client.configuration.server_variables
            )
            _host = self.api_client.configuration.get_host_from_settings(
                index, variables=server_variables, servers=self.settings['servers']
            )
        except IndexError:
            if self.settings['servers']:
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s" %
                    len(self.settings['servers'])
                )
            _host = None

        for key, value in kwargs.items():
            if key not in self.params_map['all']:
                raise ApiTypeError(
                    "Got an unexpected parameter '%s'"
                    " to method `%s`" %
                    (key, self.settings['operation_id'])
                )
            # only throw this nullable ApiValueError if _check_input_type
            # is False, if _check_input_type==True we catch this case
            # in self.__validate_inputs
            if (key not in self.params_map['nullable'] and value is None
                    and kwargs['_check_input_type'] is False):
                raise ApiValueError(
                    "Value may not be None for non-nullable parameter `%s`"
                    " when calling `%s`" %
                    (key, self.settings['operation_id'])
                )

        for key in self.params_map['required']:
            if key not in kwargs.keys():
                raise ApiValueError(
                    "Missing the required parameter `%s` when calling "
                    "`%s`" % (key, self.settings['operation_id'])
                )

        self.__validate_inputs(kwargs)

        params = self.__gather_params(kwargs)

        accept_headers_list = self.headers_map['accept']
        if accept_headers_list:
            params['header']['Accept'] = self.api_client.select_header_accept(
                accept_headers_list)

        if kwargs.get('_content_type'):
            params['header']['Content-Type'] = kwargs['_content_type']
        else:
            content_type_headers_list = self.headers_map['content_type']
            if content_type_headers_list:
                if params['body'] != "":
                    content_types_list = self.api_client.select_header_content_type(
                        content_type_headers_list, self.settings['http_method'],
                        params['body'])
                    if content_types_list:
                        params['header']['Content-Type'] = content_types_list

        return self.api_client.call_api(
            self.settings['endpoint_path'], self.settings['http_method'],
            params['path'],
            params['query'],
            params['header'],
            body=params['body'],
            post_params=params['form'],
            files=params['file'],
            response_type=self.settings['response_type'],
            auth_settings=self.settings['auth'],
            async_req=kwargs['async_req'],
            _check_type=kwargs['_check_return_type'],
            _return_http_data_only=kwargs['_return_http_data_only'],
            _preload_content=kwargs['_preload_content'],
            _request_timeout=kwargs['_request_timeout'],
            _host=_host,
            _request_auths=kwargs['_request_auths'],
            collection_formats=params['collection_format'])
