"""
    LODGEA OTA Service API Reference

    # Introduction  Whether you own your property or not, LODGEA provides the platform to provide accommodation services to your consumers through a variety of connectivity options and business models. LODGEA provides a flexible and open platform for many use cases.  This API allows you to search for availabilities or locations and get all available information about a specific property.  # API Endpoint  ``` https://api.eu.lodgea.io/v1/ ```  The API is only accessible via HTTPS, the base URL is <code>https://api.eu.lodgea.io/</code>, and the current version is <code>v1</code> which results in the base URL for all requests: <code>https://api.eu.lodgea.io/v1/</code>.  # Datacenters  The API is only accessible via HTTPS and the current version is <code>v1</code>, which results in a URL like: <code>https://api.lodgea.io/v1/</code>, depending on the datacenter.  ## EU Datacenter  ``` https://api.eu.lodgea.io/v1/ ```  This is the default datacenter.  ## US Datacenter  ``` https://api.us.lodgea.io/v2/ ```  ## German Datacenter  ``` https://api.uat.lodgea.io/v2/ ```  # Usage  [curl](http://curl.haxx.se/) is used primarily to send requests to LODGEA in the [Usage examples](#Usage examples) in this Readme.  For [Postman](https://www.postman.com/), the OpenAPI YAML definition can be imported as collection over the `Import` button. In the `variables` menu under `Collections`, you can set the `baseURL` value to the specific region. The API key can be set under each request in the `Authorization` tab.  There are SDKs for many popular languages available on GitHub:  - https://github.com/lodgea/lodgea-java - https://github.com/lodgea/lodgea-js - https://github.com/lodgea/lodgea-php - https://github.com/lodgea/lodgea-csharp - https://github.com/lodgea/lodgea-python  # Cross-Origin Resource Sharing  This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/), that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.  # Authentication  The LODGEA API offers authentication via API Key. Please create your own API Key in the management UI. Then add your key as `apiKey` header to the request. If you receive a `401` response, make sure your filled key is valid.  # Usage examples  Learn how to work more efficiently with LODGEA API v1 with these workflow-oriented examples.  ## Get Property by ID  ``` POST /v1/property/get ```  Get all information about a specific property by its ID.  #### Parameters  | Name                  | Type     | Description               | Example             | | --------------------- | -------- | ------------------------- | ------------------- | | `propertyId` required | `string` | ID of the property to get | strandresidenz-sylt |  #### Example Request  ``` curl --location --request POST 'https://api.eu.lodgea.io/v1/property/get' \\ --header 'Content-Type: application/json' \\ --header 'Accept: application/json' \\ --header 'apiKey: <YOUR_API_KEY>' \\ --data-raw '{   \"propertyId\": \"strandresidenz-sylt\" }' ```  ## Search for Location  ``` POST /v1/location/search ```  Get a location by search text in free-text form.  #### Parameters  | Name                  | Type     | Description | Example             | | --------------------- | -------- | ----------- | ------------------- | | `searchText` required | `string` | Search text | Hotel Stadt Hamburg |  #### Example Request  ``` curl --location --request POST 'https://api.eu.lodgea.io/v1/location/search' \\ --header 'Content-Type: application/json' \\ --header 'Accept: application/json' \\ --header 'apiKey: <YOUR_API_KEY>' \\ --data-raw '{   \"searchText\": \"Hotel Stadt Hamburg\" }' ```  ## Search for Availability  ``` POST /v1/availability/search ```  Get availability information based on search criteria. All parameter codes are listed in the [appendix](#Appendix).  #### Parameters  | Name                       | Type           | Description                                                  | Example    | | -------------------------- | -------------- | ------------------------------------------------------------ | ---------- | | `adultCount` optional      | integer        | Number of adults                                             | 2          | | `childCount` optional      | integer        | Number of childs                                             | 1          | | `childAgeList` optional    | array<integer> | Age of the childs as integer array                           | [3]        | | `currencyCode` optional    | string         | Currency code, see [currencyCode](##CurrencyCode)            | EUR        | | `minLengthOfStay` optional | integer        | Minimum days of stay                                         | 1          | | `maxLengthOfStay` optional | integer        | Maximum days of stay                                         | 27         | | `locationName` optional    | string         | Name of the location                                         | Sylt       | | `locationType` optional    | string         | Type of the location, see [locationType](##locationType)     | locality   | | `earliestArrival` optional | date           | Earliest arrival date, format is: YYYY-MM-DD                 | 2022-09-01 | | `latestReturn` optional    | date           | Latest return date, format is: YYYY-MM-DD                    | 2022-09-08 | | `sort` optional            | string         | Sort order, either `quality` or `price`                      | quality    | | `serviceList` optional     | array<string>  | List of service codes, see [serviceCode](##serviceCode)      | [242]      | | `typeList` optional        | array<string>  | List of type codes, see [typeCode](##typeCode)               | [20]       | | `unitTypeList` optional    | array<string>  | List of unit type codes, see [unitTypeCode](##unitTypeCode)  | [9]        | | `unitAmenityList` optional | array<string>  | List of unit amenity codes, see [unitAmenityCode](##unitAmenityCode) | [50]       | | `mealPlanList` optional    | array<string>  | List of meal plan codes, see [mealPlanCode](##mealPlanCode)  | [19]       |  #### Example Request  ``` curl --location --request POST 'https://api.eu.lodgea.io/v1/availability/search' \\ --header 'Content-Type: application/json' \\ --header 'Accept: application/json' \\ --header 'apiKey: <YOUR_API_KEY>' \\ --data-raw '{   \"adultCount\": 2,   \"childCount\": 1,   \"childAgeList\": [     3   ],   \"currencyCode\": \"EUR\",   \"minLengthOfStay\": 1,   \"maxLengthOfStay\": 27,   \"locationName\": \"Sylt\",   \"locationType\": \"locality\",   \"earliestArrival\": \"2022-09-01\",   \"latestReturn\": \"2022-09-08\",   \"sort\": \"quality\",   \"serviceList\": [     242   ],   \"typeList\": [     20   ],   \"unitTypeList\": [     9   ],   \"unitAmenityList\": [     50   ],   \"mealPlanList\": [     19   ] }' ```  # Appendix  ## Parameters  ### currencyCode  | Code | Name | | ---- | ---- | | 1    | EUR  | | 2    | GBP  | | 3    | AED  | | 4    | USD  | | 5    | INR  | | 6    | AUD  | | 7    | ARS  | | 8    | EGP  | | 9    | KWD  | | 10   | RUB  | | 11   | MYR  | | 12   | SAR  | | 13   | AZN  | | 14   | FJD  | | 15   | MXN  | | 16   | SGD  | | 17   | BHD  | | 18   | GEL  | | 19   | MDL  | | 20   | ZAR  | | 21   | BRL  | | 22   | HKD  | | 23   | NAD  | | 24   | SEK  | | 25   | BGN  | | 26   | HUF  | | 27   | TWD  | | 28   | CHF  | | 29   | CAD  | | 30   | NZD  | | 31   | THB  | | 32   | XOF  | | 33   | IDR  | | 34   | NOK  | | 35   | TRY  | | 36   | CLP  | | 37   | ILS  | | 38   | OMR  | | 39   | CNY  | | 40   | JPY  | | 41   | PLN  | | 42   | COP  | | 43   | JOD  | | 44   | UAH  | | 45   | CZK  | | 46   | KZT  | | 47   | QAR  | | 48   | DKK  | | 49   | KRW  | | 50   | RON  |  ### locationType  | Type                        | Name                        | Example                             | | --------------------------- | --------------------------- | ----------------------------------- | | formatted_address           | Formatted Address           | Nordhedig 20 25980 Sylt Deutschland | | place_id                    | Place ID                    | ChIJVaxqTevetEcRyfs8PGHK6mw         | | locality                    | Locality                    | Sylt                                | | administrative_area_level_1 | Administrative Area Level 1 | Schleswig-Holstein                  | | administrative_area_level_3 | Administrative Area Level 3 | Nordfriesland                       | | state_code                  | State Code                  | SH                                  | | country                     | Country                     | Deutschland                         | | country_code                | Country Code                | DE                                  | | postal_code                 | Postal Code                 | 25980                               | | language                    | Language                    | de                                  | | natural_feature             | Natural Feature             | Sylt                                | | establishment               | Establishment               | Sylt                                | | sublocality                 | Sublocality                 | Westerland                          | | sublocality_level_1         | Sublocality Level 1         | Westerland                          | | streetNumber                | Street Number               | 20                                  | | route                       | Route                       | Nordhedig                           |  ### serviceCode  | Code  | Name                                                    | | ----- | ------------------------------------------------------- | | 1     | 24-hour front desk                                      | | 2     | 24-hour room service                                    | | 3     | 24-hour security                                        | | 4     | Adjoining rooms                                         | | 5     | Air conditioning                                        | | 6     | Airline desk                                            | | 7     | ATM/Cash machine                                        | | 8     | Baby sitting                                            | | 9     | BBQ/Picnic area                                         | | 10    | Bilingual staff                                         | | 11    | Bookstore                                               | | 12    | Boutiques/stores                                        | | 13    | Brailed elevators                                       | | 14    | Business library                                        | | 15    | Car rental desk                                         | | 16    | Casino                                                  | | 17    | Check cashing policy                                    | | 18    | Check-in kiosk                                          | | 19    | Cocktail lounge                                         | | 20    | Coffee shop                                             | | 21    | Coin operated laundry                                   | | 22    | Concierge desk                                          | | 23    | Concierge floor                                         | | 24    | Conference facilities                                   | | 25    | Courtyard                                               | | 26    | Currency exchange                                       | | 27    | Desk with electrical outlet                             | | 28    | Doctor on call                                          | | 29    | Door man                                                | | 30    | Driving range                                           | | 31    | Drugstore/pharmacy                                      | | 32    | Duty free shop                                          | | 33    | Elevators                                               | | 34    | Executive floor                                         | | 35    | Exercise gym                                            | | 36    | Express check-in                                        | | 37    | Express check-out                                       | | 38    | Family plan                                             | | 39    | Florist                                                 | | 40    | Folios                                                  | | 41    | Free airport shuttle                                    | | 42    | Free parking                                            | | 43    | Free transportation                                     | | 44    | Game room                                               | | 45    | Gift/News stand                                         | | 46    | Hairdresser/barber                                      | | 47    | Accessible facilities                                   | | 48    | Health club                                             | | 49    | Heated pool                                             | | 50    | Housekeeping - daily                                    | | 51    | Housekeeping - weekly                                   | | 52    | Ice machine                                             | | 53    | Indoor parking                                          | | 54    | Indoor pool                                             | | 55    | Jacuzzi                                                 | | 56    | Jogging track                                           | | 57    | Kennels                                                 | | 58    | Laundry/Valet service                                   | | 59    | Liquor store                                            | | 60    | Live entertainment                                      | | 61    | Massage services                                        | | 62    | Nightclub                                               | | 63    | Off-Site parking                                        | | 64    | On-Site parking                                         | | 65    | Outdoor parking                                         | | 66    | Outdoor pool                                            | | 67    | Package/Parcel services                                 | | 68    | Parking                                                 | | 69    | Photocopy center                                        | | 70    | Playground                                              | | 71    | Pool                                                    | | 72    | Poolside snack bar                                      | | 73    | Public address system                                   | | 74    | Ramp access                                             | | 75    | Recreational vehicle parking                            | | 76    | Restaurant                                              | | 77    | Room service                                            | | 78    | Safe deposit box                                        | | 79    | Sauna                                                   | | 80    | Security                                                | | 81    | Shoe shine stand                                        | | 82    | Shopping mall                                           | | 83    | Solarium                                                | | 84    | Spa                                                     | | 85    | Sports bar                                              | | 86    | Steam bath                                              | | 87    | Storage space                                           | | 88    | Sundry/Convenience store                                | | 89    | Technical concierge                                     | | 90    | Theatre desk                                            | | 91    | Tour/sightseeing desk                                   | | 92    | Translation services                                    | | 93    | Travel agency                                           | | 94    | Truck parking                                           | | 95    | Valet cleaning                                          | | 96    | Dry cleaning                                            | | 97    | Valet parking                                           | | 98    | Vending machines                                        | | 99    | Video tapes                                             | | 100   | Wakeup service                                          | | 101   | Wheelchair access                                       | | 102   | Whirlpool                                               | | 103   | Multilingual staff                                      | | 104   | Wedding services                                        | | 105   | Banquet facilities                                      | | 106   | Bell staff/porter                                       | | 107   | Beauty shop/salon                                       | | 108   | Complimentary self service laundry                      | | 109   | Direct dial telephone                                   | | 110   | Female traveler room/floor                              | | 111   | Pharmacy                                                | | 112   | Stables                                                 | | 113   | 120 AC                                                  | | 114   | 120 DC                                                  | | 115   | 220 AC                                                  | | 116   | Accessible parking                                      | | 117   | 220 DC                                                  | | 118   | Barbeque grills                                         | | 119   | Women's clothing                                        | | 120   | Men's clothing                                          | | 121   | Children's clothing                                     | | 122   | Shops and commercial services                           | | 123   | Video games                                             | | 124   | Sports bar open for lunch                               | | 125   | Sports bar open for dinner                              | | 126   | Room service - full menu                                | | 127   | Room service - limited menu                             | | 128   | Room service - limited hours                            | | 129   | Valet same day dry cleaning                             | | 130   | Body scrub                                              | | 131   | Body wrap                                               | | 132   | Public area air conditioned                             | | 133   | Efolio available to company                             | | 134   | Individual Efolio available                             | | 135   | Video review billing                                    | | 136   | Butler service                                          | | 137   | Complimentary in-room coffee or tea                     | | 138   | Complimentary buffet breakfast                          | | 139   | Complimentary cocktails                                 | | 140   | Complimentary coffee in lobby                           | | 141   | Complimentary continental breakfast                     | | 142   | Complimentary full american breakfast                   | | 143   | Dinner delivery service from local restaurant           | | 144   | Complimentary newspaper delivered to room               | | 145   | Complimentary newspaper in lobby                        | | 146   | Complimentary shoeshine                                 | | 147   | Evening reception                                       | | 148   | Front desk                                              | | 149   | Grocery shopping service available                      | | 150   | Halal food available                                    | | 151   | Kosher food available                                   | | 152   | Limousine service                                       | | 153   | Managers reception                                      | | 154   | Medical Facilities Service                              | | 155   | Telephone jack adaptor available                        | | 156   | All-inclusive meal plan                                 | | 157   | Buffet breakfast                                        | | 158   | Communal bar area                                       | | 159   | Continental breakfast                                   | | 160   | Full meal plan                                          | | 161   | Full american breakfast                                 | | 162   | Meal plan available                                     | | 163   | Modified american meal plan                             | | 164   | Food and beverage outlets                               | | 165   | Lounges/bars                                            | | 166   | Barber shop                                             | | 167   | Video checkout                                          | | 168   | Onsite laundry                                          | | 169   | 24-hour food & beverage kiosk                           | | 170   | Concierge lounge                                        | | 171   | Parking fee managed by hotel                            | | 172   | Transportation                                          | | 173   | Breakfast served in restaurant                          | | 174   | Lunch served in restaurant                              | | 175   | Dinner served in restaurant                             | | 176   | Full service housekeeping                               | | 177   | Limited service housekeeping                            | | 178   | High speed internet access for laptop in public areas   | | 179   | Wireless internet connection in public areas            | | 180   | Additional services/amenities/facilities on property    | | 181   | Transportation services - local area                    | | 182   | Transportation services - local office                  | | 183   | DVD/video rental                                        | | 184   | Parking lot                                             | | 185   | Parking deck                                            | | 186   | Street side parking                                     | | 187   | Cocktail lounge with entertainment                      | | 188   | Cocktail lounge with light fare                         | | 189   | Motorcycle parking                                      | | 190   | Phone services                                          | | 191   | Ballroom                                                | | 192   | Bus parking                                             | | 193   | Children's play area                                    | | 194   | Children's nursery                                      | | 195   | Disco                                                   | | 196   | Early check-in                                          | | 197   | Locker room                                             | | 198   | Non-smoking rooms (generic)                             | | 199   | Train access                                            | | 200   | Aerobics instruction                                    | | 201   | Baggage hold                                            | | 202   | Bicycle rentals                                         | | 203   | Dietician                                               | | 204   | Late check-out available                                | | 205   | Pet-sitting services                                    | | 206   | Prayer mats                                             | | 207   | Sports trainer                                          | | 208   | Turndown service                                        | | 209   | DVDs/videos - children                                  | | 210   | Bank                                                    | | 211   | Lobby coffee service                                    | | 212   | Banking services                                        | | 213   | Stairwells                                              | | 214   | Pet amenities available                                 | | 215   | Exhibition/convention floor                             | | 216   | Long term parking                                       | | 217   | Children not allowed                                    | | 218   | Children welcome                                        | | 219   | Courtesy car                                            | | 220   | Hotel does not provide pornographic films/TV            | | 221   | Hotspots                                                | | 222   | Free high speed internet connection                     | | 223   | Internet services                                       | | 224   | Pets allowed                                            | | 225   | Gourmet highlights                                      | | 226   | Catering services                                       | | 227   | Complimentary breakfast                                 | | 228   | Business center                                         | | 229   | Business services                                       | | 230   | Secured parking                                         | | 231   | Racquetball                                             | | 232   | Snow sports                                             | | 233   | Tennis court                                            | | 234   | Water sports                                            | | 235   | Child programs                                          | | 236   | Golf                                                    | | 237   | Horseback riding                                        | | 238   | Oceanfront                                              | | 239   | Beachfront                                              | | 240   | Hair dryer                                              | | 241   | Ironing board                                           | | 242   | Heated guest rooms                                      | | 243   | Toilet                                                  | | 244   | Parlor                                                  | | 245   | Video game player                                       | | 246   | Thalassotherapy                                         | | 247   | Private dining for groups                               | | 248   | Hearing impaired services                               | | 249   | Carryout breakfast                                      | | 250   | Deluxe continental breakfast                            | | 251   | Hot continental breakfast                               | | 252   | Hot breakfast                                           | | 253   | Private pool                                            | | 254   | Connecting rooms                                        | | 255   | Data port                                               | | 256   | Exterior corridors                                      | | 257   | Gulf view                                               | | 258   | Accessible rooms                                        | | 259   | High speed internet access                              | | 260   | Interior corridors                                      | | 261   | High speed wireless                                     | | 262   | Kitchenette                                             | | 263   | Private bath or shower                                  | | 264   | Fire safety compliant                                   | | 265   | Welcome drink                                           | | 266   | Boarding pass print-out available                       | | 267   | Printing services available                             | | 268   | All public areas non-smoking                            | | 269   | Meeting rooms                                           | | 270   | Movies in room                                          | | 271   | Secretarial service                                     | | 272   | Snow skiing                                             | | 273   | Water skiing                                            | | 274   | Fax service                                             | | 275   | Great room                                              | | 276   | Lobby                                                   | | 277   | Multiple phone lines billed separately                  | | 278   | Umbrellas                                               | | 279   | Gas station                                             | | 280   | Grocery store                                           | | 281   | 24-hour coffee shop                                     | | 282   | Airport shuttle service                                 | | 283   | Luggage service                                         | | 284   | Piano Bar                                               | | 285   | VIP security                                            | | 286   | Complimentary wireless internet                         | | 287   | Concierge breakfast                                     | | 288   | Same gender floor                                       | | 289   | Children programs                                       | | 290   | Building meets local, state and country building codes  | | 291   | Internet browser On TV                                  | | 292   | Newspaper                                               | | 293   | Parking - controlled access gates to enter parking area | | 294   | Hotel safe deposit box (not room safe box)              | | 295   | Storage space available – fee                           | | 296   | Type of entrances to guest rooms                        | | 297   | Beverage/cocktail                                       | | 298   | Cell phone rental                                       | | 299   | Coffee/tea                                              | | 300   | Early check in guarantee                                | | 301   | Food and beverage discount                              | | 302   | Late check out guarantee                                | | 303   | Room upgrade confirmed                                  | | 304   | Room upgrade on availability                            | | 305   | Shuttle to local businesses                             | | 306   | Shuttle to local attractions                            | | 307   | Social hour                                             | | 308   | Video billing                                           | | 309   | Welcome gift                                            | | 310   | Hypoallergenic rooms                                    | | 311   | Room air filtration                                     | | 312   | Smoke-free property                                     | | 313   | Water purification system in use                        | | 314   | Poolside service                                        | | 315   | Clothing store                                          | | 316   | Electric car charging stations                          | | 317   | Office rental                                           | | 318   | Piano                                                   | | 319   | Incoming fax                                            | | 320   | Outgoing fax                                            | | 321   | Semi-private space                                      | | 322   | Loading dock                                            | | 323   | Baby kit                                                | | 324   | Children's breakfast                                    | | 325   | Cloakroom service                                       | | 326   | Coffee lounge                                           | | 327   | Events ticket service                                   | | 328   | Late check-in                                           | | 329   | Limited parking                                         | | 330   | Outdoor summer bar/café                                 | | 331   | No parking available                                    | | 332   | Beer garden                                             | | 333   | Garden lounge bar                                       | | 334   | Summer terrace                                          | | 335   | Winter terrace                                          | | 336   | Roof terrace                                            | | 337   | Beach bar                                               | | 338   | Helicopter service                                      | | 339   | Ferry                                                   | | 340   | Tapas bar                                               | | 341   | Café bar                                                | | 342   | Snack bar                                               | | 343   | Guestroom wired internet                                | | 344   | Guestroom wireless internet                             | | 345   | Fitness center                                          | | 348   | Health and beauty services                              | | 349   | Mobile/Digital Check-in                                 | | 350   | Mobile/Digital Check-out                                | | 351   | Choose a room                                           | | 5000  | Breakfast in the room                                   | | 5001  | Public transport tickets                                | | 5002  | Bikes available (free)                                  | | 5003  | Outdoor furniture                                       | | 5004  | Outdoor fireplace                                       | | 5005  | Garden                                                  | | 5006  | Terrace                                                 | | 5007  | Sun terrace                                             | | 5008  | Chapel/shrine                                           | | 5009  | Shared lounge/TV area                                   | | 5010  | Ironing service                                         | | 5011  | Trouser press                                           | | 5012  | Designated smoking area                                 | | 5013  | Pet basket                                              | | 5014  | Pet bowls                                               | | 5015  | Beach                                                   | | 5016  | Bowling                                                 | | 5017  | Darts                                                   | | 5018  | Fishing                                                 | | 5020  | Hiking                                                  | | 5021  | Minigolf                                                | | 5022  | Snorkeling                                              | | 5023  | Squash                                                  | | 5024  | Windsurfing                                             | | 5025  | Billiard                                                | | 5026  | Table tennis                                            | | 5027  | Canoeing                                                | | 5028  | Ski-to-door access                                      | | 5029  | Diving                                                  | | 5030  | Tennis equipment                                        | | 5031  | Badminton equipment                                     | | 5032  | Cycling                                                 | | 5033  | Ski storage                                             | | 5034  | Ski school                                              | | 5035  | Ski equipment hire (on site)                            | | 5036  | Ski pass vendor                                         | | 5037  | Private beach area                                      | | 5039  | Rooms/Facilities for Disabled                           | | 5040  | Hair dresser-beautician                                 | | 5041  | Family Rooms                                            | | 5042  | Viproom facilities                                      | | 5043  | Bridal Suite                                            | | 5044  | Spa & Wellness Centre                                   | | 5045  | Karaoke                                                 | | 5046  | Soundproof-rooms                                        | | 5047  | Packed Lunches                                          | | 5048  | Ticket service                                          | | 5049  | Entertainment Staff                                     | | 5050  | Private Check-in/Check-out                              | | 5051  | Special Diet Menus (on request)                         | | 5052  | Vending Machine (drinks)                                | | 5053  | Hot Spring Bath                                         | | 5054  | Kids' club                                              | | 5055  | Minimarket on site                                      | | 5056  | Water park                                              | | 5057  | Adult only                                              | | 5058  | Open-air bath                                           | | 5059  | Public bath                                             | | 5060  | Water slide                                             | | 5061  | Board games/puzzles                                     | | 5062  | Book/DVD/Music library for children                     | | 5063  | Indoor play area                                        | | 5064  | Kids' outdoor play equipment                            | | 5065  | Baby safety gates                                       | | 5066  | Children television networks                            | | 5067  | Kid meals                                               | | 5068  | Kid-friendly buffet                                     | | 5069  | Pool towels                                             | | 5070  | Wine/Champagne                                          | | 5071  | Bottle of water                                         | | 5072  | Fruits                                                  | | 5073  | Chocolate/Cookies                                       | | 5074  | Strollers                                               | | 5075  | On-site coffee house                                    | | 5076  | Sun loungers or beach chairs                            | | 5077  | Sun umbrellas                                           | | 5078  | Picnic area                                             | | 5079  | Beauty Services                                         | | 5080  | Spa Facilities                                          | | 5081  | Steam room                                              | | 5082  | Spa lounge/relaxation area                              | | 5083  | Foot bath                                               | | 5084  | Spa/wellness packages                                   | | 5085  | Massage chair                                           | | 5086  | Fitness                                                 | | 5087  | Yoga classes                                            | | 5088  | Fitness classes                                         | | 5089  | Personal trainer                                        | | 5090  | Fitness/spa locker rooms                                | | 5091  | Kids pool                                               | | 5092  | Shuttle Service                                         | | 5093  | Temporary art galleries                                 | | 5094  | Pub crawls                                              | | 5095  | Stand-up comedy                                         | | 5096  | Movie nights                                            | | 5097  | Walking tours                                           | | 5098  | Bike tours                                              | | 5099  | Themed dinner nights                                    | | 5100  | Happy hour                                              | | 5101  | Tour or class about local culture                       | | 5102  | Cooking class                                           | | 5103  | Live music/performance                                  | | 5104  | Live sports events (broadcast)                          | | 5105  | Archery                                                 | | 5106  | Aerobics                                                | | 5107  | Bingo                                                   | | 5108  | Ski Shuttle                                             | | 5109  | Outdoor Swimming Pool (all year)                        | | 5110  | Outdoor Swimming Pool (seasonal)                        | | 5111  | Indoor Swimming Pool (all year)                         | | 5112  | Indoor Swimming Pool (seasonal)                         | | 5113  | Swimming pool toys                                      | | 5114  | Rooftop pool                                            | | 5115  | Infinity pool                                           | | 5116  | Pool with view                                          | | 5117  | Salt-water pool                                         | | 5118  | Plunge pool                                             | | 5119  | Pool bar                                                | | 5120  | Shallow end pool                                        | | 5121  | Pool cover                                              | | 5122  | Fence around pool                                       | | 5123  | Airport Shuttle (surcharge)                             | | 5124  | Property is wheel chair accessible                      | | 5125  | Toilet with grab rails                                  | | 5126  | Higher level toilet                                     | | 5127  | Low bathroom sink                                       | | 5128  | Bathroom emergency pull cord                            | | 5129  | Visual aids: Braille                                    | | 5130  | Visual aids: Tactile Signs                              | | 5131  | Auditory Guidance                                       | | 5132  | Back massage                                            | | 5133  | Neck massage                                            | | 5134  | Foot massage                                            | | 5135  | Couples massage                                         | | 5136  | Head massage                                            | | 5137  | Hand massage                                            | | 5138  | Full body massage                                       | | 5139  | Facial treatments                                       | | 5140  | Waxing services                                         | | 5141  | Make up services                                        | | 5142  | Hair treatments                                         | | 5143  | Manicure                                                | | 5144  | Pedicure                                                | | 5145  | Hair cut                                                | | 5146  | Hair colouring                                          | | 5147  | Hair styling                                            | | 5148  | Body Treatments                                         | | 5149  | Body scrub                                              | | 5150  | Body wrap                                               | | 5151  | Light therapy                                           | | 5152  | Shuttle Service (free)                                  | | 5153  | Shuttle Service (surcharge)                             | | 5154  | Swimming pool                                           | | 5156  | No Single-Use Toiletries                                | | 5157  | Towels Changed Upon Request                             | | 5158  | 24-hour security                                        | | 5159  | Security alarm                                          | | 5160  | Smoke alarms                                            | | 5161  | CCTV in common areas                                    | | 5162  | CCTV outside property                                   | | 5163  | Fire extinguishers                                      | | 5164  | Key access                                              | | 5165  | Key card access                                         | | 5166  | Carbon monoxide detector                                | | 5167  | Carbon monoxide source                                  | | 5168  | No plastic stirrers                                     | | 5169  | No plastic straws                                       | | 5170  | No plastic cups                                         | | 5171  | No plastic bottles for water                            | | 5172  | No plastic bottles for non-water                        | | 5173  | No plastic cutlery                                      | | 5174  | Keycard for room electricity                            | | 5175  | Opt-out from daily room cleaning                        | | 5176  | Refillable water stations                               | | 5177  | Bike rental                                             | | 5178  | Bike parking                                            | | 6000  | Lunch                                                   | | 6001  | Dinner                                                  | | 90001 | Renewable energy                                        |  ### mealPlanCode  | Code  | Name                          | | ----- | ----------------------------- | | 0     | (NONE)                        | | 1     | All inclusive                 | | 2     | American                      | | 3     | Bed & breakfast               | | 4     | Buffet breakfast              | | 5     | Caribbean breakfast           | | 6     | Continental breakfast         | | 7     | English breakfast             | | 8     | European plan                 | | 9     | Family plan                   | | 10    | Full board                    | | 11    | Full breakfast                | | 12    | Half board                    | | 14    | Room only                     | | 15    | Self catering                 | | 16    | Bermuda                       | | 17    | Dinner bed and breakfast plan | | 18    | Family American               | | 19    | Breakfast                     | | 20    | Modified                      | | 21    | Lunch                         | | 22    | Dinner                        | | 23    | Breakfast & lunch             | | 24    | Lunch & Dinner                | | 90001 | 3/4 Plan                      |  ### typeCode  | Code | Name                          | | ---- | ----------------------------- | | 1    | All suite                     | | 2    | All-Inclusive resort          | | 3    | Apartment                     | | 4    | Bed and breakfast             | | 5    | Cabin or bungalow             | | 6    | Campground                    | | 7    | Chalet                        | | 8    | Condominium                   | | 9    | Conference center             | | 10   | Corporate                     | | 11   | Corporate business transient  | | 12   | Cruise                        | | 13   | Extended stay                 | | 14   | Ferry                         | | 15   | Guest farm                    | | 16   | Guest house limited service   | | 17   | Health spa                    | | 18   | Holiday resort                | | 19   | Hostel                        | | 20   | Hotel                         | | 21   | Inn                           | | 22   | Lodge                         | | 23   | Meeting resort                | | 24   | Meeting/Convention            | | 25   | Mobile-home                   | | 26   | Monastery                     | | 27   | Motel                         | | 28   | Ranch                         | | 29   | Residential apartment         | | 30   | Resort                        | | 31   | Sailing ship                  | | 32   | Self catering accommodation   | | 33   | Tent                          | | 34   | Vacation home                 | | 35   | Villa                         | | 36   | Wildlife reserve              | | 37   | Castle                        | | 38   | Convention Network Property   | | 39   | Golf                          | | 40   | Pension                       | | 41   | Ski                           | | 42   | Spa                           | | 43   | Time share                    | | 44   | Boatel                        | | 45   | Boutique                      | | 46   | Efficiency/studio             | | 47   | Full service                  | | 48   | Historical                    | | 49   | Limited service               | | 50   | Recreational vehicle park     | | 51   | Charm hotel                   | | 52   | Manor                         | | 53   | Vacation rental               | | 54   | Economy                       | | 55   | Midscale                      | | 56   | Upscale                       | | 57   | Luxury                        | | 58   | Union                         | | 59   | Leisure                       | | 60   | Wholesale                     | | 61   | Transient                     | | 62   | Other                         | | 5000 | ApartHotel                    | | 5001 | Riad                          | | 5002 | Ryokan                        | | 5003 | Love Hotel                    | | 5004 | Homestay                      | | 5005 | Japanese-style Business Hotel | | 5006 | Holiday Home                  | | 5007 | Country house                 | | 5008 | Capsule Hotel                 | | 5009 | Holiday Park                  |  ### unitTypeCode  | Code | Name             | | ---- | ---------------- | | 1    | Apartment        | | 4    | Quadruple        | | 5    | Suite            | | 7    | Triple           | | 8    | Twin             | | 9    | Double           | | 10   | Single           | | 12   | Studio           | | 13   | Family           | | 24   | Twin/Double      | | 25   | Dormitory room   | | 26   | Bed in Dormitory | | 27   | Bungalow         | | 28   | Chalet           | | 29   | Holiday home     | | 31   | Villa            | | 32   | Mobile home      | | 33   | Tent             |  ### unitAmenityCode  | Code  | Name                                                         | | ----- | ------------------------------------------------------------ | | 1     | Adjoining rooms                                              | | 2     | Air conditioning                                             | | 3     | Alarm clock                                                  | | 4     | All news channel                                             | | 5     | AM/FM radio                                                  | | 6     | Baby listening device                                        | | 7     | Balcony/Lanai/Terrace                                        | | 8     | Barbeque grills                                              | | 9     | Bath tub with spray jets                                     | | 10    | Bathrobe                                                     | | 11    | Bathroom amenities                                           | | 12    | Bathroom telephone                                           | | 13    | Bathtub                                                      | | 14    | Bathtub only                                                 | | 15    | Bathtub/shower combination                                   | | 16    | Bidet                                                        | | 17    | Bottled water                                                | | 18    | Cable television                                             | | 19    | Coffee/Tea maker                                             | | 20    | Color television                                             | | 21    | Computer                                                     | | 22    | Connecting rooms                                             | | 23    | Converters/ Voltage adaptors                                 | | 24    | Copier                                                       | | 25    | Cordless phone                                               | | 26    | Cribs                                                        | | 27    | Data port                                                    | | 28    | Desk                                                         | | 29    | Desk with lamp                                               | | 30    | Dining guide                                                 | | 31    | Direct dial phone number                                     | | 32    | Dishwasher                                                   | | 33    | Double beds                                                  | | 34    | Dual voltage outlet                                          | | 35    | Electrical current voltage                                   | | 36    | Ergonomic chair                                              | | 37    | Extended phone cord                                          | | 38    | Fax machine                                                  | | 39    | Fire alarm                                                   | | 40    | Fire alarm with light                                        | | 41    | Fireplace                                                    | | 42    | Free toll free calls                                         | | 43    | Free calls                                                   | | 44    | Free credit card access calls                                | | 45    | Free local calls                                             | | 46    | Free movies/video                                            | | 47    | Full kitchen                                                 | | 48    | Grab bars in bathroom                                        | | 49    | Grecian tub                                                  | | 50    | Hairdryer                                                    | | 51    | High speed internet connection                               | | 52    | Interactive web TV                                           | | 53    | International direct dialing                                 | | 54    | Internet access                                              | | 55    | Iron                                                         | | 56    | Ironing board                                                | | 57    | Whirpool                                                     | | 58    | King bed                                                     | | 59    | Kitchen                                                      | | 60    | Kitchen supplies                                             | | 61    | Kitchenette                                                  | | 62    | Knock light                                                  | | 63    | Laptop                                                       | | 64    | Large desk                                                   | | 65    | Large work area                                              | | 66    | Laundry basket/clothes hamper                                | | 67    | Loft                                                         | | 68    | Microwave                                                    | | 69    | Minibar                                                      | | 70    | Modem                                                        | | 71    | Modem jack                                                   | | 72    | Multi-line phone                                             | | 73    | Newspaper                                                    | | 74    | Non-smoking                                                  | | 75    | Notepads                                                     | | 76    | Office supplies                                              | | 77    | Oven                                                         | | 78    | Pay per view movies on TV                                    | | 79    | Pens                                                         | | 80    | Phone in bathroom                                            | | 81    | Plates and bowls                                             | | 82    | Pots and pans                                                | | 83    | Prayer mats                                                  | | 84    | Printer                                                      | | 85    | Private bathroom                                             | | 86    | Queen bed                                                    | | 87    | Recliner                                                     | | 88    | Refrigerator                                                 | | 89    | Refrigerator with ice maker                                  | | 90    | Remote control television                                    | | 91    | Rollaway bed                                                 | | 92    | Safe                                                         | | 93    | Scanner                                                      | | 94    | Separate closet                                              | | 95    | Separate modem line available                                | | 96    | Shoe polisher                                                | | 97    | Shower only                                                  | | 98    | Silverware/utensils                                          | | 99    | Sitting area                                                 | | 100   | Smoke detectors                                              | | 101   | Smoking                                                      | | 102   | Sofa bed                                                     | | 103   | Speaker phone                                                | | 104   | Stereo                                                       | | 105   | Stove                                                        | | 106   | Tape recorder                                                | | 107   | Telephone                                                    | | 108   | Telephone for hearing impaired                               | | 109   | Telephones with message light                                | | 110   | Toaster oven                                                 | | 111   | Trouser/Pant press                                           | | 112   | Turn down service                                            | | 113   | Twin bed                                                     | | 114   | Vaulted ceilings                                             | | 115   | VCR movies                                                   | | 116   | VCR player                                                   | | 117   | Video games                                                  | | 118   | Voice mail                                                   | | 119   | Wake-up calls                                                | | 120   | Water closet                                                 | | 121   | Water purification system                                    | | 122   | Wet bar                                                      | | 123   | Wireless internet connection                                 | | 124   | Wireless keyboard                                            | | 125   | Adaptor available for telephone PC use                       | | 126   | Air conditioning individually controlled in room             | | 127   | Bathtub &whirlpool separate                                  | | 128   | Telephone with data ports                                    | | 129   | CD player                                                    | | 130   | Complimentary local calls time limit                         | | 131   | Extra person charge for rollaway use                         | | 132   | Down/feather pillows                                         | | 133   | Desk with electrical outlet                                  | | 134   | ESPN available                                               | | 135   | Foam pillows                                                 | | 136   | HBO available                                                | | 137   | High ceilings                                                | | 138   | Marble bathroom                                              | | 139   | List of movie channels available                             | | 140   | Pets allowed                                                 | | 141   | Oversized bathtub                                            | | 142   | Shower                                                       | | 143   | Sink in-room                                                 | | 144   | Soundproofed room                                            | | 145   | Storage space                                                | | 146   | Tables and chairs                                            | | 147   | Two-line phone                                               | | 148   | Walk-in closet                                               | | 149   | Washer/dryer                                                 | | 150   | Weight scale                                                 | | 151   | Welcome gift                                                 | | 152   | Spare electrical outlet available at desk                    | | 153   | Non-refundable charge for pets                               | | 154   | Refundable deposit for pets                                  | | 155   | Separate tub and shower                                      | | 156   | Entrance type to guest room                                  | | 157   | Ceiling fan                                                  | | 158   | CNN available                                                | | 159   | Electrical adaptors available                                | | 160   | Buffet breakfast                                             | | 161   | Accessible room                                              | | 162   | Closets in room                                              | | 163   | DVD player                                                   | | 164   | Mini-refrigerator                                            | | 165   | Separate line billing for multi-line phone                   | | 166   | Self-controlled heating/cooling system                       | | 167   | Toaster                                                      | | 168   | Analog data port                                             | | 169   | Collect calls                                                | | 170   | International calls                                          | | 171   | Carrier access                                               | | 172   | Interstate calls                                             | | 173   | Intrastate calls                                             | | 174   | Local calls                                                  | | 175   | Long distance calls                                          | | 176   | Operator-assisted calls                                      | | 177   | Credit card access calls                                     | | 178   | Calling card calls                                           | | 179   | Toll free calls                                              | | 180   | Universal AC/DC adaptors                                     | | 181   | Bathtub seat                                                 | | 182   | Canopy/poster bed                                            | | 183   | Cups/glassware                                               | | 184   | Entertainment center                                         | | 185   | Family/oversized room                                        | | 186   | Hypoallergenic bed                                           | | 187   | Hypoallergenic pillows                                       | | 188   | Lamp                                                         | | 189   | Meal included: breakfast                                     | | 190   | Meal included: continental breakfast                         | | 191   | Meal included: dinner                                        | | 192   | Meal included: lunch                                         | | 193   | Shared bathroom                                              | | 194   | Telephone TDD/Textphone                                      | | 195   | Water bed                                                    | | 196   | Extra adult charge                                           | | 197   | Extra child charge                                           | | 198   | Extra child charge for rollaway use                          | | 199   | Meal included: full American breakfast                       | | 200   | Futon                                                        | | 201   | Murphy bed                                                   | | 202   | Tatami mats                                                  | | 203   | Single bed                                                   | | 204   | Annex room                                                   | | 205   | Free newspaper                                               | | 206   | Honeymoon suites                                             | | 207   | Complimentary high speed internet in room                    | | 208   | Maid service                                                 | | 209   | PC hook-up in room                                           | | 210   | Satellite television                                         | | 211   | VIP rooms                                                    | | 212   | Cell phone recharger                                         | | 213   | DVR player                                                   | | 214   | iPod docking station                                         | | 215   | Media center                                                 | | 216   | Plug & play panel                                            | | 217   | Satellite radio                                              | | 218   | Video on demand                                              | | 219   | Exterior corridors                                           | | 220   | Gulf view                                                    | | 221   | Accessible room                                              | | 222   | Interior corridors                                           | | 223   | Mountain view                                                | | 224   | Ocean view                                                   | | 225   | High speed internet access fee                               | | 226   | High speed wireless                                          | | 227   | Premium movie channels                                       | | 228   | Slippers                                                     | | 229   | First nighters' kit                                          | | 230   | Chair provided with desk                                     | | 231   | Pillow top mattress                                          | | 232   | Feather bed                                                  | | 233   | Duvet                                                        | | 234   | Luxury linen type                                            | | 235   | International channels                                       | | 236   | Pantry                                                       | | 237   | Dish-cleaning supplies                                       | | 238   | Double vanity                                                | | 239   | Lighted makeup mirror                                        | | 240   | Upgraded bathroom amenities                                  | | 241   | VCR player available at front desk                           | | 242   | Instant hot water                                            | | 243   | Outdoor space                                                | | 244   | Hinoki tub                                                   | | 245   | Private pool                                                 | | 246   | High Definition (HD) Flat Panel Television - 32 inches or greater | | 247   | Room windows open                                            | | 248   | Bedding type unknown or unspecified                          | | 249   | Full bed                                                     | | 250   | Round bed                                                    | | 251   | TV                                                           | | 252   | Child rollaway                                               | | 253   | DVD player available at front desk                           | | 254   | Video game player:                                           | | 255   | Video game player available at front desk                    | | 256   | Dining room seats                                            | | 257   | Full size mirror                                             | | 258   | Mobile/cellular phones                                       | | 259   | Movies                                                       | | 260   | Multiple closets                                             | | 261   | Plates/glassware                                             | | 262   | Safe large enough to accommodate a laptop                    | | 263   | Bed linen thread count                                       | | 264   | Blackout curtain                                             | | 265   | Bluray player                                                | | 266   | Device with mp3                                              | | 267   | No adult channels or adult channel lock                      | | 268   | Non-allergenic room                                          | | 269   | Pillow type                                                  | | 270   | Seating area with sofa/chair                                 | | 271   | Separate toilet area                                         | | 272   | Web enabled                                                  | | 273   | Widescreen TV                                                | | 274   | Other data connection                                        | | 275   | Phoneline billed separately                                  | | 276   | Separate tub or shower                                       | | 277   | Video games                                                  | | 278   | Roof ventilator                                              | | 279   | Children's playpen                                           | | 280   | Plunge pool                                                  | | 281   | DVD movies                                                   | | 282   | Air filtration                                               | | 283   | Exercise Equipment in Room                                   | | 5001  | Coffee/Tea maker                                             | | 5002  | Internet facilities                                          | | 5003  | Mini-bar                                                     | | 5004  | Shower                                                       | | 5005  | Bath                                                         | | 5006  | Safe Deposit Box                                             | | 5007  | Pay-per-view Channels                                        | | 5008  | TV                                                           | | 5009  | Telephone                                                    | | 5010  | Fax                                                          | | 5011  | Airconditioning                                              | | 5012  | Hair Dryer                                                   | | 5013  | Wake Up Service/Alarm-clock                                  | | 5014  | Hot Tub                                                      | | 5015  | Clothing Iron                                                | | 5016  | Kitchenette                                                  | | 5017  | Balcony                                                      | | 5018  | Trouser Press                                                | | 5019  | Bath-robe                                                    | | 5020  | Spa Bath                                                     | | 5021  | Radio                                                        | | 5022  | Refrigerator                                                 | | 5023  | Desk                                                         | | 5024  | Shared Bathroom                                              | | 5025  | Ironing facilities                                           | | 5026  | Seating area                                                 | | 5027  | Free Toiletries                                              | | 5028  | DVD-Player                                                   | | 5029  | CD-Player                                                    | | 5030  | Fan                                                          | | 5031  | Toilet                                                       | | 5032  | Microwave                                                    | | 5033  | Dishwasher                                                   | | 5034  | Washing machine                                              | | 5035  | Video                                                        | | 5036  | Video Games                                                  | | 5037  | Patio                                                        | | 5038  | Bathroom                                                     | | 5039  | Extra long beds (> 2 meter)                                  | | 5040  | Heating                                                      | | 5041  | Dressing room                                                | | 5042  | Guest toilet                                                 | | 5043  | Slippers                                                     | | 5044  | Satellite Channels                                           | | 5045  | Kitchen                                                      | | 5046  | Wireless internet                                            | | 5068  | Cable channels                                               | | 5069  | Bath or Shower                                               | | 5070  | Carpeted Floor                                               | | 5071  | Fireplace                                                    | | 5072  | Additional Toilet                                            | | 5073  | Interconnecting Room(s) available                            | | 5074  | Laptop Safe Box                                              | | 5075  | Flat-screen TV                                               | | 5076  | Private Entrance                                             | | 5077  | Sofa                                                         | | 5079  | Soundproofing                                                | | 5080  | Tiled / Marble floor                                         | | 5081  | View                                                         | | 5082  | Wooden / Parquet floor                                       | | 5083  | Wake Up Service                                              | | 5084  | Alarm Clock                                                  | | 5085  | Dining Area                                                  | | 5086  | Electric Kettle                                              | | 5087  | Executive Lounge Access                                      | | 5088  | iPod Docking Station                                         | | 5089  | Kitchenware                                                  | | 5090  | Mosquito Net                                                 | | 5091  | Towels/Linens at surcharge                                   | | 5092  | Sauna                                                        | | 5093  | Private Pool                                                 | | 5094  | Tumble dryer (machine)                                       | | 5095  | Wardrobe/Closet                                              | | 5096  | Oven                                                         | | 5097  | Stove                                                        | | 5098  | Toaster                                                      | | 5099  | Barbecue                                                     | | 5100  | Bidet                                                        | | 5101  | Computer                                                     | | 5102  | iPad                                                         | | 5103  | Game Console                                                 | | 5104  | Game Console - Xbox 360                                      | | 5105  | Game Console - PS2                                           | | 5106  | Game Console - PS3                                           | | 5107  | Game Console - Nintendo Wii                                  | | 5108  | Sea View                                                     | | 5109  | Lake View                                                    | | 5110  | Garden View                                                  | | 5111  | Pool View                                                    | | 5112  | Mountain View                                                | | 5113  | Landmark View                                                | | 5114  | Laptop                                                       | | 5115  | Allergy-Free                                                 | | 5116  | Cleaning products                                            | | 5117  | Electric blankets                                            | | 5118  | Additional Bathroom                                          | | 5119  | Blu-ray player                                               | | 5120  | Coffee Machine                                               | | 5121  | City View                                                    | | 5122  | River View                                                   | | 5123  | Terrace                                                      | | 5124  | Towels                                                       | | 5125  | Linen                                                        | | 5126  | Dining table                                                 | | 5127  | Children highchair                                           | | 5129  | Outdoor furniture                                            | | 5130  | Outdoor dining area                                          | | 5131  | Entire property on ground floor                              | | 5132  | Upper floor reachable by lift                                | | 5133  | Upper floor reachable by stairs only                         | | 5134  | Entire unit wheelchair accessible                            | | 5135  | Detached                                                     | | 5136  | Semi-detached                                                | | 5137  | Private flat in block of flats                               | | 5138  | Clothes Rack                                                 | | 5139  | Rollaway bed                                                 | | 5140  | Clothes drying rack                                          | | 5141  | Toilet paper                                                 | | 5142  | Child safety socket covers                                   | | 5143  | Board games/puzzles                                          | | 5144  | Book/DVD/Music library for children                          | | 5145  | Baby safety gates                                            | | 5146  | Sofa bed                                                     | | 5147  | Toilet with grab rails                                       | | 5148  | Adapted bath                                                 | | 5149  | Roll in shower                                               | | 5150  | Walk in shower                                               | | 5151  | Higher level toilet                                          | | 5152  | Low bathroom sink                                            | | 5153  | Bathroom emergency pull cord                                 | | 5154  | Shower chair                                                 | | 5157  | Rooftop pool                                                 | | 5158  | Infinity pool                                                | | 5159  | Pool with view                                               | | 5160  | Heated pool                                                  | | 5161  | Salt-water pool                                              | | 5162  | Plunge pool                                                  | | 5163  | Pool towels                                                  | | 5164  | Shallow end                                                  | | 5165  | Pool cover                                                   | | 5166  | Wine/champagne                                               | | 5167  | Bottle of water                                              | | 5168  | Fruits                                                       | | 5169  | Chocolate/cookies                                            | | 5170  | Trash cans                                                   | | 5171  | Wine glasses                                                 | | 5172  | Game console - Xbox One                                      | | 5173  | Game console - Wii U                                         | | 5174  | Game console - PS4                                           | | 5175  | Children crib/cots                                           | | 5176  | Toothbrush                                                   | | 5177  | Shampoo                                                      | | 5178  | Conditioner                                                  | | 5179  | Body soap                                                    | | 5180  | Shower cap                                                   | | 5181  | Pajamas                                                      | | 5182  | Yukata                                                       | | 5184  | Socket near the bed                                          | | 5185  | Adapter                                                      | | 5186  | Feather pillow                                               | | 5187  | Non-feather pillow                                           | | 5188  | Hypoallergenic pillow                                        | | 5189  | Accessible by Lift                                           | | 5190  | Inner courtyard view                                         | | 5191  | Quiet street view                                            | | 5196  | Portable Wifi                                                | | 5198  | Smartphone                                                   | | 5199  | Streaming service (such as Netflix)                          | | 5200  | Lockers                                                      | | 5201  | Fire alarms or smoke detectors                               | | 5202  | Fire extinguishers                                           | | 5203  | Metal keys access                                            | | 5204  | Electronic key card access                                   | | 5205  | Reading light                                                | | 5206  | Earplugs                                                     | | 5207  | Private curtain                                              | | 5211  | Carbon monoxide detector                                     | | 5212  | Carbon monoxide source                                       | | 90001 | Bread-bun delivery                                           | | 90002 | Breakfast delivery                                           | | 90003 | Grocery delivery service                                     | | 90004 | Beach chair or roofed wicker beach chair                     | | 90005 | Shared kitchen                                               | | 90006 | Bunk bed                                                     | | 90007 | Levee view                                                   | | 90008 | Pay television                                               | | 90009 | Extractor hood                                               | | 90010 | Vacuum cleaner                                               | | 90011 | Separated bedrooms                                           |  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@lodgea.com
    Generated by: https://openapi-generator.tech
"""


from datetime import date, datetime  # noqa: F401
from copy import deepcopy
import inspect
import io
import os
import pprint
import re
import tempfile
import uuid

from dateutil.parser import parse

from openapi_client.exceptions import (
    ApiKeyError,
    ApiAttributeError,
    ApiTypeError,
    ApiValueError,
)

none_type = type(None)
file_type = io.IOBase


def convert_js_args_to_python_args(fn):
    from functools import wraps
    @wraps(fn)
    def wrapped_init(_self, *args, **kwargs):
        """
        An attribute named `self` received from the api will conflicts with the reserved `self`
        parameter of a class method. During generation, `self` attributes are mapped
        to `_self` in models. Here, we name `_self` instead of `self` to avoid conflicts.
        """
        spec_property_naming = kwargs.get('_spec_property_naming', False)
        if spec_property_naming:
            kwargs = change_keys_js_to_python(
                kwargs, _self if isinstance(
                    _self, type) else _self.__class__)
        return fn(_self, *args, **kwargs)
    return wrapped_init


class cached_property(object):
    # this caches the result of the function call for fn with no inputs
    # use this as a decorator on function methods that you want converted
    # into cached properties
    result_key = '_results'

    def __init__(self, fn):
        self._fn = fn

    def __get__(self, instance, cls=None):
        if self.result_key in vars(self):
            return vars(self)[self.result_key]
        else:
            result = self._fn()
            setattr(self, self.result_key, result)
            return result


PRIMITIVE_TYPES = (list, float, int, bool, datetime, date, str, file_type)


def allows_single_value_input(cls):
    """
    This function returns True if the input composed schema model or any
    descendant model allows a value only input
    This is true for cases where oneOf contains items like:
    oneOf:
      - float
      - NumberWithValidation
      - StringEnum
      - ArrayModel
      - null
    TODO: lru_cache this
    """
    if (
        issubclass(cls, ModelSimple) or
        cls in PRIMITIVE_TYPES
    ):
        return True
    elif issubclass(cls, ModelComposed):
        if not cls._composed_schemas['oneOf']:
            return False
        return any(allows_single_value_input(c) for c in cls._composed_schemas['oneOf'])
    return False


def composed_model_input_classes(cls):
    """
    This function returns a list of the possible models that can be accepted as
    inputs.
    TODO: lru_cache this
    """
    if issubclass(cls, ModelSimple) or cls in PRIMITIVE_TYPES:
        return [cls]
    elif issubclass(cls, ModelNormal):
        if cls.discriminator is None:
            return [cls]
        else:
            return get_discriminated_classes(cls)
    elif issubclass(cls, ModelComposed):
        if not cls._composed_schemas['oneOf']:
            return []
        if cls.discriminator is None:
            input_classes = []
            for c in cls._composed_schemas['oneOf']:
                input_classes.extend(composed_model_input_classes(c))
            return input_classes
        else:
            return get_discriminated_classes(cls)
    return []


class OpenApiModel(object):
    """The base class for all OpenAPIModels"""

    def set_attribute(self, name, value):
        # this is only used to set properties on self

        path_to_item = []
        if self._path_to_item:
            path_to_item.extend(self._path_to_item)
        path_to_item.append(name)

        if name in self.openapi_types:
            required_types_mixed = self.openapi_types[name]
        elif self.additional_properties_type is None:
            raise ApiAttributeError(
                "{0} has no attribute '{1}'".format(
                    type(self).__name__, name),
                path_to_item
            )
        elif self.additional_properties_type is not None:
            required_types_mixed = self.additional_properties_type

        if get_simple_class(name) != str:
            error_msg = type_error_message(
                var_name=name,
                var_value=name,
                valid_classes=(str,),
                key_type=True
            )
            raise ApiTypeError(
                error_msg,
                path_to_item=path_to_item,
                valid_classes=(str,),
                key_type=True
            )

        if self._check_type:
            value = validate_and_convert_types(
                value, required_types_mixed, path_to_item, self._spec_property_naming,
                self._check_type, configuration=self._configuration)
        if (name,) in self.allowed_values:
            check_allowed_values(
                self.allowed_values,
                (name,),
                value
            )
        if (name,) in self.validations:
            check_validations(
                self.validations,
                (name,),
                value,
                self._configuration
            )
        self.__dict__['_data_store'][name] = value

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    def __setattr__(self, attr, value):
        """set the value of an attribute using dot notation: `instance.attr = val`"""
        self[attr] = value

    def __getattr__(self, attr):
        """get the value of an attribute using dot notation: `instance.attr`"""
        return self.__getitem__(attr)

    def __copy__(self):
        cls = self.__class__
        if self.get("_spec_property_naming", False):
            return cls._new_from_openapi_data(**self.__dict__)
        else:
            return cls.__new__(cls, **self.__dict__)

    def __deepcopy__(self, memo):
        cls = self.__class__

        if self.get("_spec_property_naming", False):
            new_inst = cls._new_from_openapi_data()
        else:
            new_inst = cls.__new__(cls)

        for k, v in self.__dict__.items():
            setattr(new_inst, k, deepcopy(v, memo))
        return new_inst


    def __new__(cls, *args, **kwargs):
        # this function uses the discriminator to
        # pick a new schema/class to instantiate because a discriminator
        # propertyName value was passed in

        if len(args) == 1:
            arg = args[0]
            if arg is None and is_type_nullable(cls):
                # The input data is the 'null' value and the type is nullable.
                return None

            if issubclass(cls, ModelComposed) and allows_single_value_input(cls):
                model_kwargs = {}
                oneof_instance = get_oneof_instance(cls, model_kwargs, kwargs, model_arg=arg)
                return oneof_instance

        visited_composed_classes = kwargs.get('_visited_composed_classes', ())
        if (
            cls.discriminator is None or
            cls in visited_composed_classes
        ):
            # Use case 1: this openapi schema (cls) does not have a discriminator
            # Use case 2: we have already visited this class before and are sure that we
            # want to instantiate it this time. We have visited this class deserializing
            # a payload with a discriminator. During that process we traveled through
            # this class but did not make an instance of it. Now we are making an
            # instance of a composed class which contains cls in it, so this time make an instance of cls.
            #
            # Here's an example of use case 2: If Animal has a discriminator
            # petType and we pass in "Dog", and the class Dog
            # allOf includes Animal, we move through Animal
            # once using the discriminator, and pick Dog.
            # Then in the composed schema dog Dog, we will make an instance of the
            # Animal class (because Dal has allOf: Animal) but this time we won't travel
            # through Animal's discriminator because we passed in
            # _visited_composed_classes = (Animal,)

            return super(OpenApiModel, cls).__new__(cls)

        # Get the name and value of the discriminator property.
        # The discriminator name is obtained from the discriminator meta-data
        # and the discriminator value is obtained from the input data.
        discr_propertyname_py = list(cls.discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if discr_propertyname_js in kwargs:
            discr_value = kwargs[discr_propertyname_js]
        elif discr_propertyname_py in kwargs:
            discr_value = kwargs[discr_propertyname_py]
        else:
            # The input data does not contain the discriminator property.
            path_to_item = kwargs.get('_path_to_item', ())
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '%s' is missing at path: %s" %
                (discr_propertyname_js, path_to_item)
            )

        # Implementation note: the last argument to get_discriminator_class
        # is a list of visited classes. get_discriminator_class may recursively
        # call itself and update the list of visited classes, and the initial
        # value must be an empty list. Hence not using 'visited_composed_classes'
        new_cls = get_discriminator_class(
            cls, discr_propertyname_py, discr_value, [])
        if new_cls is None:
            path_to_item = kwargs.get('_path_to_item', ())
            disc_prop_value = kwargs.get(
                discr_propertyname_js, kwargs.get(discr_propertyname_py))
            raise ApiValueError(
                "Cannot deserialize input data due to invalid discriminator "
                "value. The OpenAPI document has no mapping for discriminator "
                "property '%s'='%s' at path: %s" %
                (discr_propertyname_js, disc_prop_value, path_to_item)
            )

        if new_cls in visited_composed_classes:
            # if we are making an instance of a composed schema Descendent
            # which allOf includes Ancestor, then Ancestor contains
            # a discriminator that includes Descendent.
            # So if we make an instance of Descendent, we have to make an
            # instance of Ancestor to hold the allOf properties.
            # This code detects that use case and makes the instance of Ancestor
            # For example:
            # When making an instance of Dog, _visited_composed_classes = (Dog,)
            # then we make an instance of Animal to include in dog._composed_instances
            # so when we are here, cls is Animal
            # cls.discriminator != None
            # cls not in _visited_composed_classes
            # new_cls = Dog
            # but we know we know that we already have Dog
            # because it is in visited_composed_classes
            # so make Animal here
            return super(OpenApiModel, cls).__new__(cls)

        # Build a list containing all oneOf and anyOf descendants.
        oneof_anyof_classes = None
        if cls._composed_schemas is not None:
            oneof_anyof_classes = (
                cls._composed_schemas.get('oneOf', ()) +
                cls._composed_schemas.get('anyOf', ()))
        oneof_anyof_child = new_cls in oneof_anyof_classes
        kwargs['_visited_composed_classes'] = visited_composed_classes + (cls,)

        if cls._composed_schemas.get('allOf') and oneof_anyof_child:
            # Validate that we can make self because when we make the
            # new_cls it will not include the allOf validations in self
            self_inst = super(OpenApiModel, cls).__new__(cls)
            self_inst.__init__(*args, **kwargs)

        if kwargs.get("_spec_property_naming", False):
            # when true, implies new is from deserialization
            new_inst = new_cls._new_from_openapi_data(*args, **kwargs)
        else:
            new_inst = new_cls.__new__(new_cls, *args, **kwargs)
            new_inst.__init__(*args, **kwargs)

        return new_inst

    @classmethod
    @convert_js_args_to_python_args
    def _new_from_openapi_data(cls, *args, **kwargs):
        # this function uses the discriminator to
        # pick a new schema/class to instantiate because a discriminator
        # propertyName value was passed in

        if len(args) == 1:
            arg = args[0]
            if arg is None and is_type_nullable(cls):
                # The input data is the 'null' value and the type is nullable.
                return None

            if issubclass(cls, ModelComposed) and allows_single_value_input(cls):
                model_kwargs = {}
                oneof_instance = get_oneof_instance(cls, model_kwargs, kwargs, model_arg=arg)
                return oneof_instance

        visited_composed_classes = kwargs.get('_visited_composed_classes', ())
        if (
            cls.discriminator is None or
            cls in visited_composed_classes
        ):
            # Use case 1: this openapi schema (cls) does not have a discriminator
            # Use case 2: we have already visited this class before and are sure that we
            # want to instantiate it this time. We have visited this class deserializing
            # a payload with a discriminator. During that process we traveled through
            # this class but did not make an instance of it. Now we are making an
            # instance of a composed class which contains cls in it, so this time make an instance of cls.
            #
            # Here's an example of use case 2: If Animal has a discriminator
            # petType and we pass in "Dog", and the class Dog
            # allOf includes Animal, we move through Animal
            # once using the discriminator, and pick Dog.
            # Then in the composed schema dog Dog, we will make an instance of the
            # Animal class (because Dal has allOf: Animal) but this time we won't travel
            # through Animal's discriminator because we passed in
            # _visited_composed_classes = (Animal,)

            return cls._from_openapi_data(*args, **kwargs)

        # Get the name and value of the discriminator property.
        # The discriminator name is obtained from the discriminator meta-data
        # and the discriminator value is obtained from the input data.
        discr_propertyname_py = list(cls.discriminator.keys())[0]
        discr_propertyname_js = cls.attribute_map[discr_propertyname_py]
        if discr_propertyname_js in kwargs:
            discr_value = kwargs[discr_propertyname_js]
        elif discr_propertyname_py in kwargs:
            discr_value = kwargs[discr_propertyname_py]
        else:
            # The input data does not contain the discriminator property.
            path_to_item = kwargs.get('_path_to_item', ())
            raise ApiValueError(
                "Cannot deserialize input data due to missing discriminator. "
                "The discriminator property '%s' is missing at path: %s" %
                (discr_propertyname_js, path_to_item)
            )

        # Implementation note: the last argument to get_discriminator_class
        # is a list of visited classes. get_discriminator_class may recursively
        # call itself and update the list of visited classes, and the initial
        # value must be an empty list. Hence not using 'visited_composed_classes'
        new_cls = get_discriminator_class(
            cls, discr_propertyname_py, discr_value, [])
        if new_cls is None:
            path_to_item = kwargs.get('_path_to_item', ())
            disc_prop_value = kwargs.get(
                discr_propertyname_js, kwargs.get(discr_propertyname_py))
            raise ApiValueError(
                "Cannot deserialize input data due to invalid discriminator "
                "value. The OpenAPI document has no mapping for discriminator "
                "property '%s'='%s' at path: %s" %
                (discr_propertyname_js, disc_prop_value, path_to_item)
            )

        if new_cls in visited_composed_classes:
            # if we are making an instance of a composed schema Descendent
            # which allOf includes Ancestor, then Ancestor contains
            # a discriminator that includes Descendent.
            # So if we make an instance of Descendent, we have to make an
            # instance of Ancestor to hold the allOf properties.
            # This code detects that use case and makes the instance of Ancestor
            # For example:
            # When making an instance of Dog, _visited_composed_classes = (Dog,)
            # then we make an instance of Animal to include in dog._composed_instances
            # so when we are here, cls is Animal
            # cls.discriminator != None
            # cls not in _visited_composed_classes
            # new_cls = Dog
            # but we know we know that we already have Dog
            # because it is in visited_composed_classes
            # so make Animal here
            return cls._from_openapi_data(*args, **kwargs)

        # Build a list containing all oneOf and anyOf descendants.
        oneof_anyof_classes = None
        if cls._composed_schemas is not None:
            oneof_anyof_classes = (
                cls._composed_schemas.get('oneOf', ()) +
                cls._composed_schemas.get('anyOf', ()))
        oneof_anyof_child = new_cls in oneof_anyof_classes
        kwargs['_visited_composed_classes'] = visited_composed_classes + (cls,)

        if cls._composed_schemas.get('allOf') and oneof_anyof_child:
            # Validate that we can make self because when we make the
            # new_cls it will not include the allOf validations in self
            self_inst = cls._from_openapi_data(*args, **kwargs)

        new_inst = new_cls._new_from_openapi_data(*args, **kwargs)
        return new_inst


class ModelSimple(OpenApiModel):
    """the parent class of models whose type != object in their
    swagger/openapi"""

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        self.set_attribute(name, value)

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        return self.__dict__['_data_store'].get(name, default)

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        if name in self:
            return self.get(name)

        raise ApiAttributeError(
            "{0} has no attribute '{1}'".format(
                type(self).__name__, name),
            [e for e in [self._path_to_item, name] if e]
        )

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""
        if name in self.required_properties:
            return name in self.__dict__

        return name in self.__dict__['_data_store']

    def to_str(self):
        """Returns the string representation of the model"""
        return str(self.value)

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        this_val = self._data_store['value']
        that_val = other._data_store['value']
        types = set()
        types.add(this_val.__class__)
        types.add(that_val.__class__)
        vals_equal = this_val == that_val
        return vals_equal


class ModelNormal(OpenApiModel):
    """the parent class of models whose type == object in their
    swagger/openapi"""

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        self.set_attribute(name, value)

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        return self.__dict__['_data_store'].get(name, default)

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        if name in self:
            return self.get(name)

        raise ApiAttributeError(
            "{0} has no attribute '{1}'".format(
                type(self).__name__, name),
            [e for e in [self._path_to_item, name] if e]
        )

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""
        if name in self.required_properties:
            return name in self.__dict__

        return name in self.__dict__['_data_store']

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in self._data_store.items():
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if not vals_equal:
                return False
        return True


class ModelComposed(OpenApiModel):
    """the parent class of models whose type == object in their
    swagger/openapi and have oneOf/allOf/anyOf

    When one sets a property we use var_name_to_model_instances to store the value in
    the correct class instances + run any type checking + validation code.
    When one gets a property we use var_name_to_model_instances to get the value
    from the correct class instances.
    This allows multiple composed schemas to contain the same property with additive
    constraints on the value.

    _composed_schemas (dict) stores the anyOf/allOf/oneOf classes
    key (str): allOf/oneOf/anyOf
    value (list): the classes in the XOf definition.
        Note: none_type can be included when the openapi document version >= 3.1.0
    _composed_instances (list): stores a list of instances of the composed schemas
    defined in _composed_schemas. When properties are accessed in the self instance,
    they are returned from the self._data_store or the data stores in the instances
    in self._composed_schemas
    _var_name_to_model_instances (dict): maps between a variable name on self and
    the composed instances (self included) which contain that data
    key (str): property name
    value (list): list of class instances, self or instances in _composed_instances
    which contain the value that the key is referring to.
    """

    def __setitem__(self, name, value):
        """set the value of an attribute using square-bracket notation: `instance[attr] = val`"""
        if name in self.required_properties:
            self.__dict__[name] = value
            return

        """
        Use cases:
        1. additional_properties_type is None (additionalProperties == False in spec)
            Check for property presence in self.openapi_types
            if not present then throw an error
            if present set in self, set attribute
            always set on composed schemas
        2.  additional_properties_type exists
            set attribute on self
            always set on composed schemas
        """
        if self.additional_properties_type is None:
            """
            For an attribute to exist on a composed schema it must:
            - fulfill schema_requirements in the self composed schema not considering oneOf/anyOf/allOf schemas AND
            - fulfill schema_requirements in each oneOf/anyOf/allOf schemas

            schema_requirements:
            For an attribute to exist on a schema it must:
            - be present in properties at the schema OR
            - have additionalProperties unset (defaults additionalProperties = any type) OR
            - have additionalProperties set
            """
            if name not in self.openapi_types:
                raise ApiAttributeError(
                    "{0} has no attribute '{1}'".format(
                        type(self).__name__, name),
                    [e for e in [self._path_to_item, name] if e]
                )
        # attribute must be set on self and composed instances
        self.set_attribute(name, value)
        for model_instance in self._composed_instances:
            setattr(model_instance, name, value)
        if name not in self._var_name_to_model_instances:
            # we assigned an additional property
            self.__dict__['_var_name_to_model_instances'][name] = self._composed_instances + [self]
        return None

    __unset_attribute_value__ = object()

    def get(self, name, default=None):
        """returns the value of an attribute or some default value if the attribute was not set"""
        if name in self.required_properties:
            return self.__dict__[name]

        # get the attribute from the correct instance
        model_instances = self._var_name_to_model_instances.get(name)
        values = []
        # A composed model stores self and child (oneof/anyOf/allOf) models under
        # self._var_name_to_model_instances.
        # Any property must exist in self and all model instances
        # The value stored in all model instances must be the same
        if model_instances:
            for model_instance in model_instances:
                if name in model_instance._data_store:
                    v = model_instance._data_store[name]
                    if v not in values:
                        values.append(v)
        len_values = len(values)
        if len_values == 0:
            return default
        elif len_values == 1:
            return values[0]
        elif len_values > 1:
            raise ApiValueError(
                "Values stored for property {0} in {1} differ when looking "
                "at self and self's composed instances. All values must be "
                "the same".format(name, type(self).__name__),
                [e for e in [self._path_to_item, name] if e]
            )

    def __getitem__(self, name):
        """get the value of an attribute using square-bracket notation: `instance[attr]`"""
        value = self.get(name, self.__unset_attribute_value__)
        if value is self.__unset_attribute_value__:
            raise ApiAttributeError(
                "{0} has no attribute '{1}'".format(
                    type(self).__name__, name),
                    [e for e in [self._path_to_item, name] if e]
            )
        return value

    def __contains__(self, name):
        """used by `in` operator to check if an attribute value was set in an instance: `'attr' in instance`"""

        if name in self.required_properties:
            return name in self.__dict__

        model_instances = self._var_name_to_model_instances.get(
            name, self._additional_properties_model_instances)

        if model_instances:
            for model_instance in model_instances:
                if name in model_instance._data_store:
                    return True

        return False

    def to_dict(self):
        """Returns the model properties as a dict"""
        return model_to_dict(self, serialize=False)

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, self.__class__):
            return False

        if not set(self._data_store.keys()) == set(other._data_store.keys()):
            return False
        for _var_name, this_val in self._data_store.items():
            that_val = other._data_store[_var_name]
            types = set()
            types.add(this_val.__class__)
            types.add(that_val.__class__)
            vals_equal = this_val == that_val
            if not vals_equal:
                return False
        return True


COERCION_INDEX_BY_TYPE = {
    ModelComposed: 0,
    ModelNormal: 1,
    ModelSimple: 2,
    none_type: 3,    # The type of 'None'.
    list: 4,
    dict: 5,
    float: 6,
    int: 7,
    bool: 8,
    datetime: 9,
    date: 10,
    str: 11,
    file_type: 12,   # 'file_type' is an alias for the built-in 'file' or 'io.IOBase' type.
}

# these are used to limit what type conversions we try to do
# when we have a valid type already and we want to try converting
# to another type
UPCONVERSION_TYPE_PAIRS = (
    (str, datetime),
    (str, date),
    # A float may be serialized as an integer, e.g. '3' is a valid serialized float.
    (int, float),
    (list, ModelComposed),
    (dict, ModelComposed),
    (str, ModelComposed),
    (int, ModelComposed),
    (float, ModelComposed),
    (list, ModelComposed),
    (list, ModelNormal),
    (dict, ModelNormal),
    (str, ModelSimple),
    (int, ModelSimple),
    (float, ModelSimple),
    (list, ModelSimple),
)

COERCIBLE_TYPE_PAIRS = {
    False: (  # client instantiation of a model with client data
        # (dict, ModelComposed),
        # (list, ModelComposed),
        # (dict, ModelNormal),
        # (list, ModelNormal),
        # (str, ModelSimple),
        # (int, ModelSimple),
        # (float, ModelSimple),
        # (list, ModelSimple),
        # (str, int),
        # (str, float),
        # (str, datetime),
        # (str, date),
        # (int, str),
        # (float, str),
    ),
    True: (  # server -> client data
        (dict, ModelComposed),
        (list, ModelComposed),
        (dict, ModelNormal),
        (list, ModelNormal),
        (str, ModelSimple),
        (int, ModelSimple),
        (float, ModelSimple),
        (list, ModelSimple),
        # (str, int),
        # (str, float),
        (str, datetime),
        (str, date),
        # (int, str),
        # (float, str),
        (str, file_type)
    ),
}


def get_simple_class(input_value):
    """Returns an input_value's simple class that we will use for type checking
    Python2:
    float and int will return int, where int is the python3 int backport
    str and unicode will return str, where str is the python3 str backport
    Note: float and int ARE both instances of int backport
    Note: str_py2 and unicode_py2 are NOT both instances of str backport

    Args:
        input_value (class/class_instance): the item for which we will return
                                            the simple class
    """
    if isinstance(input_value, type):
        # input_value is a class
        return input_value
    elif isinstance(input_value, tuple):
        return tuple
    elif isinstance(input_value, list):
        return list
    elif isinstance(input_value, dict):
        return dict
    elif isinstance(input_value, none_type):
        return none_type
    elif isinstance(input_value, file_type):
        return file_type
    elif isinstance(input_value, bool):
        # this must be higher than the int check because
        # isinstance(True, int) == True
        return bool
    elif isinstance(input_value, int):
        return int
    elif isinstance(input_value, datetime):
        # this must be higher than the date check because
        # isinstance(datetime_instance, date) == True
        return datetime
    elif isinstance(input_value, date):
        return date
    elif isinstance(input_value, str):
        return str
    return type(input_value)


def check_allowed_values(allowed_values, input_variable_path, input_values):
    """Raises an exception if the input_values are not allowed

    Args:
        allowed_values (dict): the allowed_values dict
        input_variable_path (tuple): the path to the input variable
        input_values (list/str/int/float/date/datetime): the values that we
            are checking to see if they are in allowed_values
    """
    these_allowed_values = list(allowed_values[input_variable_path].values())
    if (isinstance(input_values, list)
            and not set(input_values).issubset(
                set(these_allowed_values))):
        invalid_values = ", ".join(
            map(str, set(input_values) - set(these_allowed_values))),
        raise ApiValueError(
            "Invalid values for `%s` [%s], must be a subset of [%s]" %
            (
                input_variable_path[0],
                invalid_values,
                ", ".join(map(str, these_allowed_values))
            )
        )
    elif (isinstance(input_values, dict)
            and not set(
                input_values.keys()).issubset(set(these_allowed_values))):
        invalid_values = ", ".join(
            map(str, set(input_values.keys()) - set(these_allowed_values)))
        raise ApiValueError(
            "Invalid keys in `%s` [%s], must be a subset of [%s]" %
            (
                input_variable_path[0],
                invalid_values,
                ", ".join(map(str, these_allowed_values))
            )
        )
    elif (not isinstance(input_values, (list, dict))
            and input_values not in these_allowed_values):
        raise ApiValueError(
            "Invalid value for `%s` (%s), must be one of %s" %
            (
                input_variable_path[0],
                input_values,
                these_allowed_values
            )
        )


def is_json_validation_enabled(schema_keyword, configuration=None):
    """Returns true if JSON schema validation is enabled for the specified
    validation keyword. This can be used to skip JSON schema structural validation
    as requested in the configuration.

    Args:
        schema_keyword (string): the name of a JSON schema validation keyword.
        configuration (Configuration): the configuration class.
    """

    return (configuration is None or
            not hasattr(configuration, '_disabled_client_side_validations') or
            schema_keyword not in configuration._disabled_client_side_validations)


def check_validations(
        validations, input_variable_path, input_values,
        configuration=None):
    """Raises an exception if the input_values are invalid

    Args:
        validations (dict): the validation dictionary.
        input_variable_path (tuple): the path to the input variable.
        input_values (list/str/int/float/date/datetime): the values that we
            are checking.
        configuration (Configuration): the configuration class.
    """

    if input_values is None:
        return

    current_validations = validations[input_variable_path]
    if (is_json_validation_enabled('multipleOf', configuration) and
            'multiple_of' in current_validations and
            isinstance(input_values, (int, float)) and
            not (float(input_values) / current_validations['multiple_of']).is_integer()):
        # Note 'multipleOf' will be as good as the floating point arithmetic.
        raise ApiValueError(
            "Invalid value for `%s`, value must be a multiple of "
            "`%s`" % (
                input_variable_path[0],
                current_validations['multiple_of']
            )
        )

    if (is_json_validation_enabled('maxLength', configuration) and
            'max_length' in current_validations and
            len(input_values) > current_validations['max_length']):
        raise ApiValueError(
            "Invalid value for `%s`, length must be less than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['max_length']
            )
        )

    if (is_json_validation_enabled('minLength', configuration) and
            'min_length' in current_validations and
            len(input_values) < current_validations['min_length']):
        raise ApiValueError(
            "Invalid value for `%s`, length must be greater than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['min_length']
            )
        )

    if (is_json_validation_enabled('maxItems', configuration) and
            'max_items' in current_validations and
            len(input_values) > current_validations['max_items']):
        raise ApiValueError(
            "Invalid value for `%s`, number of items must be less than or "
            "equal to `%s`" % (
                input_variable_path[0],
                current_validations['max_items']
            )
        )

    if (is_json_validation_enabled('minItems', configuration) and
            'min_items' in current_validations and
            len(input_values) < current_validations['min_items']):
        raise ValueError(
            "Invalid value for `%s`, number of items must be greater than or "
            "equal to `%s`" % (
                input_variable_path[0],
                current_validations['min_items']
            )
        )

    items = ('exclusive_maximum', 'inclusive_maximum', 'exclusive_minimum',
             'inclusive_minimum')
    if (any(item in current_validations for item in items)):
        if isinstance(input_values, list):
            max_val = max(input_values)
            min_val = min(input_values)
        elif isinstance(input_values, dict):
            max_val = max(input_values.values())
            min_val = min(input_values.values())
        else:
            max_val = input_values
            min_val = input_values

    if (is_json_validation_enabled('exclusiveMaximum', configuration) and
            'exclusive_maximum' in current_validations and
            max_val >= current_validations['exclusive_maximum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value less than `%s`" % (
                input_variable_path[0],
                current_validations['exclusive_maximum']
            )
        )

    if (is_json_validation_enabled('maximum', configuration) and
            'inclusive_maximum' in current_validations and
            max_val > current_validations['inclusive_maximum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value less than or equal to "
            "`%s`" % (
                input_variable_path[0],
                current_validations['inclusive_maximum']
            )
        )

    if (is_json_validation_enabled('exclusiveMinimum', configuration) and
            'exclusive_minimum' in current_validations and
            min_val <= current_validations['exclusive_minimum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value greater than `%s`" %
            (
                input_variable_path[0],
                current_validations['exclusive_maximum']
            )
        )

    if (is_json_validation_enabled('minimum', configuration) and
            'inclusive_minimum' in current_validations and
            min_val < current_validations['inclusive_minimum']):
        raise ApiValueError(
            "Invalid value for `%s`, must be a value greater than or equal "
            "to `%s`" % (
                input_variable_path[0],
                current_validations['inclusive_minimum']
            )
        )
    flags = current_validations.get('regex', {}).get('flags', 0)
    if (is_json_validation_enabled('pattern', configuration) and
            'regex' in current_validations and
            not re.search(current_validations['regex']['pattern'],
                          input_values, flags=flags)):
        err_msg = r"Invalid value for `%s`, must match regular expression `%s`" % (
            input_variable_path[0],
            current_validations['regex']['pattern']
        )
        if flags != 0:
            # Don't print the regex flags if the flags are not
            # specified in the OAS document.
            err_msg = r"%s with flags=`%s`" % (err_msg, flags)
        raise ApiValueError(err_msg)


def order_response_types(required_types):
    """Returns the required types sorted in coercion order

    Args:
        required_types (list/tuple): collection of classes or instance of
            list or dict with class information inside it.

    Returns:
        (list): coercion order sorted collection of classes or instance
            of list or dict with class information inside it.
    """

    def index_getter(class_or_instance):
        if isinstance(class_or_instance, list):
            return COERCION_INDEX_BY_TYPE[list]
        elif isinstance(class_or_instance, dict):
            return COERCION_INDEX_BY_TYPE[dict]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelComposed)):
            return COERCION_INDEX_BY_TYPE[ModelComposed]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelNormal)):
            return COERCION_INDEX_BY_TYPE[ModelNormal]
        elif (inspect.isclass(class_or_instance)
                and issubclass(class_or_instance, ModelSimple)):
            return COERCION_INDEX_BY_TYPE[ModelSimple]
        elif class_or_instance in COERCION_INDEX_BY_TYPE:
            return COERCION_INDEX_BY_TYPE[class_or_instance]
        raise ApiValueError("Unsupported type: %s" % class_or_instance)

    sorted_types = sorted(
        required_types,
        key=lambda class_or_instance: index_getter(class_or_instance)
    )
    return sorted_types


def remove_uncoercible(required_types_classes, current_item, spec_property_naming,
                       must_convert=True):
    """Only keeps the type conversions that are possible

    Args:
        required_types_classes (tuple): tuple of classes that are required
                          these should be ordered by COERCION_INDEX_BY_TYPE
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        current_item (any): the current item (input data) to be converted

    Keyword Args:
        must_convert (bool): if True the item to convert is of the wrong
                          type and we want a big list of coercibles
                          if False, we want a limited list of coercibles

    Returns:
        (list): the remaining coercible required types, classes only
    """
    current_type_simple = get_simple_class(current_item)

    results_classes = []
    for required_type_class in required_types_classes:
        # convert our models to OpenApiModel
        required_type_class_simplified = required_type_class
        if isinstance(required_type_class_simplified, type):
            if issubclass(required_type_class_simplified, ModelComposed):
                required_type_class_simplified = ModelComposed
            elif issubclass(required_type_class_simplified, ModelNormal):
                required_type_class_simplified = ModelNormal
            elif issubclass(required_type_class_simplified, ModelSimple):
                required_type_class_simplified = ModelSimple

        if required_type_class_simplified == current_type_simple:
            # don't consider converting to one's own class
            continue

        class_pair = (current_type_simple, required_type_class_simplified)
        if must_convert and class_pair in COERCIBLE_TYPE_PAIRS[spec_property_naming]:
            results_classes.append(required_type_class)
        elif class_pair in UPCONVERSION_TYPE_PAIRS:
            results_classes.append(required_type_class)
    return results_classes


def get_discriminated_classes(cls):
    """
    Returns all the classes that a discriminator converts to
    TODO: lru_cache this
    """
    possible_classes = []
    key = list(cls.discriminator.keys())[0]
    if is_type_nullable(cls):
        possible_classes.append(cls)
    for discr_cls in cls.discriminator[key].values():
        if hasattr(discr_cls, 'discriminator') and discr_cls.discriminator is not None:
            possible_classes.extend(get_discriminated_classes(discr_cls))
        else:
            possible_classes.append(discr_cls)
    return possible_classes


def get_possible_classes(cls, from_server_context):
    # TODO: lru_cache this
    possible_classes = [cls]
    if from_server_context:
        return possible_classes
    if hasattr(cls, 'discriminator') and cls.discriminator is not None:
        possible_classes = []
        possible_classes.extend(get_discriminated_classes(cls))
    elif issubclass(cls, ModelComposed):
        possible_classes.extend(composed_model_input_classes(cls))
    return possible_classes


def get_required_type_classes(required_types_mixed, spec_property_naming):
    """Converts the tuple required_types into a tuple and a dict described
    below

    Args:
        required_types_mixed (tuple/list): will contain either classes or
            instance of list or dict
        spec_property_naming (bool): if True these values came from the
            server, and we use the data types in our endpoints.
            If False, we are client side and we need to include
            oneOf and discriminator classes inside the data types in our endpoints

    Returns:
        (valid_classes, dict_valid_class_to_child_types_mixed):
            valid_classes (tuple): the valid classes that the current item
                                   should be
            dict_valid_class_to_child_types_mixed (dict):
                valid_class (class): this is the key
                child_types_mixed (list/dict/tuple): describes the valid child
                    types
    """
    valid_classes = []
    child_req_types_by_current_type = {}
    for required_type in required_types_mixed:
        if isinstance(required_type, list):
            valid_classes.append(list)
            child_req_types_by_current_type[list] = required_type
        elif isinstance(required_type, tuple):
            valid_classes.append(tuple)
            child_req_types_by_current_type[tuple] = required_type
        elif isinstance(required_type, dict):
            valid_classes.append(dict)
            child_req_types_by_current_type[dict] = required_type[str]
        else:
            valid_classes.extend(get_possible_classes(required_type, spec_property_naming))
    return tuple(valid_classes), child_req_types_by_current_type


def change_keys_js_to_python(input_dict, model_class):
    """
    Converts from javascript_key keys in the input_dict to python_keys in
    the output dict using the mapping in model_class.
    If the input_dict contains a key which does not declared in the model_class,
    the key is added to the output dict as is. The assumption is the model_class
    may have undeclared properties (additionalProperties attribute in the OAS
    document).
    """

    if getattr(model_class, 'attribute_map', None) is None:
        return input_dict
    output_dict = {}
    reversed_attr_map = {value: key for key, value in
                         model_class.attribute_map.items()}
    for javascript_key, value in input_dict.items():
        python_key = reversed_attr_map.get(javascript_key)
        if python_key is None:
            # if the key is unknown, it is in error or it is an
            # additionalProperties variable
            python_key = javascript_key
        output_dict[python_key] = value
    return output_dict


def get_type_error(var_value, path_to_item, valid_classes, key_type=False):
    error_msg = type_error_message(
        var_name=path_to_item[-1],
        var_value=var_value,
        valid_classes=valid_classes,
        key_type=key_type
    )
    return ApiTypeError(
        error_msg,
        path_to_item=path_to_item,
        valid_classes=valid_classes,
        key_type=key_type
    )


def deserialize_primitive(data, klass, path_to_item):
    """Deserializes string to primitive type.

    :param data: str/int/float
    :param klass: str/class the class to convert to

    :return: int, float, str, bool, date, datetime
    """
    additional_message = ""
    try:
        if klass in {datetime, date}:
            additional_message = (
                "If you need your parameter to have a fallback "
                "string value, please set its type as `type: {}` in your "
                "spec. That allows the value to be any type. "
            )
            if klass == datetime:
                if len(data) < 8:
                    raise ValueError("This is not a datetime")
                # The string should be in iso8601 datetime format.
                parsed_datetime = parse(data)
                date_only = (
                    parsed_datetime.hour == 0 and
                    parsed_datetime.minute == 0 and
                    parsed_datetime.second == 0 and
                    parsed_datetime.tzinfo is None and
                    8 <= len(data) <= 10
                )
                if date_only:
                    raise ValueError("This is a date, not a datetime")
                return parsed_datetime
            elif klass == date:
                if len(data) < 8:
                    raise ValueError("This is not a date")
                return parse(data).date()
        else:
            converted_value = klass(data)
            if isinstance(data, str) and klass == float:
                if str(converted_value) != data:
                    # '7' -> 7.0 -> '7.0' != '7'
                    raise ValueError('This is not a float')
            return converted_value
    except (OverflowError, ValueError) as ex:
        # parse can raise OverflowError
        raise ApiValueError(
            "{0}Failed to parse {1} as {2}".format(
                additional_message, repr(data), klass.__name__
            ),
            path_to_item=path_to_item
        ) from ex


def get_discriminator_class(model_class,
                            discr_name,
                            discr_value, cls_visited):
    """Returns the child class specified by the discriminator.

    Args:
        model_class (OpenApiModel): the model class.
        discr_name (string): the name of the discriminator property.
        discr_value (any): the discriminator value.
        cls_visited (list): list of model classes that have been visited.
            Used to determine the discriminator class without
            visiting circular references indefinitely.

    Returns:
        used_model_class (class/None): the chosen child class that will be used
            to deserialize the data, for example dog.Dog.
            If a class is not found, None is returned.
    """

    if model_class in cls_visited:
        # The class has already been visited and no suitable class was found.
        return None
    cls_visited.append(model_class)
    used_model_class = None
    if discr_name in model_class.discriminator:
        class_name_to_discr_class = model_class.discriminator[discr_name]
        used_model_class = class_name_to_discr_class.get(discr_value)
    if used_model_class is None:
        # We didn't find a discriminated class in class_name_to_discr_class.
        # So look in the ancestor or descendant discriminators
        # The discriminator mapping may exist in a descendant (anyOf, oneOf)
        # or ancestor (allOf).
        # Ancestor example: in the GrandparentAnimal -> ParentPet -> ChildCat
        #   hierarchy, the discriminator mappings may be defined at any level
        #   in the hierarchy.
        # Descendant example:  mammal -> whale/zebra/Pig -> BasquePig/DanishPig
        #   if we try to make BasquePig from mammal, we need to travel through
        #   the oneOf descendant discriminators to find BasquePig
        descendant_classes = model_class._composed_schemas.get('oneOf', ()) + \
            model_class._composed_schemas.get('anyOf', ())
        ancestor_classes = model_class._composed_schemas.get('allOf', ())
        possible_classes = descendant_classes + ancestor_classes
        for cls in possible_classes:
            # Check if the schema has inherited discriminators.
            if hasattr(cls, 'discriminator') and cls.discriminator is not None:
                used_model_class = get_discriminator_class(
                    cls, discr_name, discr_value, cls_visited)
                if used_model_class is not None:
                    return used_model_class
    return used_model_class


def deserialize_model(model_data, model_class, path_to_item, check_type,
                      configuration, spec_property_naming):
    """Deserializes model_data to model instance.

    Args:
        model_data (int/str/float/bool/none_type/list/dict): data to instantiate the model
        model_class (OpenApiModel): the model class
        path_to_item (list): path to the model in the received data
        check_type (bool): whether to check the data tupe for the values in
            the model
        configuration (Configuration): the instance to use to convert files
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.

    Returns:
        model instance

    Raise:
        ApiTypeError
        ApiValueError
        ApiKeyError
    """

    kw_args = dict(_check_type=check_type,
                   _path_to_item=path_to_item,
                   _configuration=configuration,
                   _spec_property_naming=spec_property_naming)

    if issubclass(model_class, ModelSimple):
        return model_class._new_from_openapi_data(model_data, **kw_args)
    elif isinstance(model_data, list):
        return model_class._new_from_openapi_data(*model_data, **kw_args)
    if isinstance(model_data, dict):
        kw_args.update(model_data)
        return model_class._new_from_openapi_data(**kw_args)
    elif isinstance(model_data, PRIMITIVE_TYPES):
        return model_class._new_from_openapi_data(model_data, **kw_args)


def deserialize_file(response_data, configuration, content_disposition=None):
    """Deserializes body to file

    Saves response body into a file in a temporary folder,
    using the filename from the `Content-Disposition` header if provided.

    Args:
        param response_data (str):  the file data to write
        configuration (Configuration): the instance to use to convert files

    Keyword Args:
        content_disposition (str):  the value of the Content-Disposition
            header

    Returns:
        (file_type): the deserialized file which is open
            The user is responsible for closing and reading the file
    """
    fd, path = tempfile.mkstemp(dir=configuration.temp_folder_path)
    os.close(fd)
    os.remove(path)

    if content_disposition:
        filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
                             content_disposition,
                             flags=re.I)
        if filename is not None:
            filename = filename.group(1)
        else:
            filename = "default_" + str(uuid.uuid4())

        path = os.path.join(os.path.dirname(path), filename)

    with open(path, "wb") as f:
        if isinstance(response_data, str):
            # change str to bytes so we can write it
            response_data = response_data.encode('utf-8')
        f.write(response_data)

    f = open(path, "rb")
    return f


def attempt_convert_item(input_value, valid_classes, path_to_item,
                         configuration, spec_property_naming, key_type=False,
                         must_convert=False, check_type=True):
    """
    Args:
        input_value (any): the data to convert
        valid_classes (any): the classes that are valid
        path_to_item (list): the path to the item to convert
        configuration (Configuration): the instance to use to convert files
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        key_type (bool): if True we need to convert a key type (not supported)
        must_convert (bool): if True we must convert
        check_type (bool): if True we check the type or the returned data in
            ModelComposed/ModelNormal/ModelSimple instances

    Returns:
        instance (any) the fixed item

    Raises:
        ApiTypeError
        ApiValueError
        ApiKeyError
    """
    valid_classes_ordered = order_response_types(valid_classes)
    valid_classes_coercible = remove_uncoercible(
        valid_classes_ordered, input_value, spec_property_naming)
    if not valid_classes_coercible or key_type:
        # we do not handle keytype errors, json will take care
        # of this for us
        if configuration is None or not configuration.discard_unknown_keys:
            raise get_type_error(input_value, path_to_item, valid_classes,
                                 key_type=key_type)
    for valid_class in valid_classes_coercible:
        try:
            if issubclass(valid_class, OpenApiModel):
                return deserialize_model(input_value, valid_class,
                                         path_to_item, check_type,
                                         configuration, spec_property_naming)
            elif valid_class == file_type:
                return deserialize_file(input_value, configuration)
            return deserialize_primitive(input_value, valid_class,
                                         path_to_item)
        except (ApiTypeError, ApiValueError, ApiKeyError) as conversion_exc:
            if must_convert:
                raise conversion_exc
            # if we have conversion errors when must_convert == False
            # we ignore the exception and move on to the next class
            continue
    # we were unable to convert, must_convert == False
    return input_value


def is_type_nullable(input_type):
    """
    Returns true if None is an allowed value for the specified input_type.

    A type is nullable if at least one of the following conditions is true:
    1. The OAS 'nullable' attribute has been specified,
    1. The type is the 'null' type,
    1. The type is a anyOf/oneOf composed schema, and a child schema is
       the 'null' type.
    Args:
        input_type (type): the class of the input_value that we are
            checking
    Returns:
        bool
    """
    if input_type is none_type:
        return True
    if issubclass(input_type, OpenApiModel) and input_type._nullable:
        return True
    if issubclass(input_type, ModelComposed):
        # If oneOf/anyOf, check if the 'null' type is one of the allowed types.
        for t in input_type._composed_schemas.get('oneOf', ()):
            if is_type_nullable(t):
                return True
        for t in input_type._composed_schemas.get('anyOf', ()):
            if is_type_nullable(t):
                return True
    return False


def is_valid_type(input_class_simple, valid_classes):
    """
    Args:
        input_class_simple (class): the class of the input_value that we are
            checking
        valid_classes (tuple): the valid classes that the current item
            should be
    Returns:
        bool
    """
    if issubclass(input_class_simple, OpenApiModel) and \
            valid_classes == (bool, date, datetime, dict, float, int, list, str, none_type,):
        return True
    valid_type = input_class_simple in valid_classes
    if not valid_type and (
            issubclass(input_class_simple, OpenApiModel) or
            input_class_simple is none_type):
        for valid_class in valid_classes:
            if input_class_simple is none_type and is_type_nullable(valid_class):
                # Schema is oneOf/anyOf and the 'null' type is one of the allowed types.
                return True
            if not (issubclass(valid_class, OpenApiModel) and valid_class.discriminator):
                continue
            discr_propertyname_py = list(valid_class.discriminator.keys())[0]
            discriminator_classes = (
                valid_class.discriminator[discr_propertyname_py].values()
            )
            valid_type = is_valid_type(input_class_simple, discriminator_classes)
            if valid_type:
                return True
    return valid_type


def validate_and_convert_types(input_value, required_types_mixed, path_to_item,
                               spec_property_naming, _check_type, configuration=None):
    """Raises a TypeError is there is a problem, otherwise returns value

    Args:
        input_value (any): the data to validate/convert
        required_types_mixed (list/dict/tuple): A list of
            valid classes, or a list tuples of valid classes, or a dict where
            the value is a tuple of value classes
        path_to_item: (list) the path to the data being validated
            this stores a list of keys or indices to get to the data being
            validated
        spec_property_naming (bool): True if the variable names in the input
            data are serialized names as specified in the OpenAPI document.
            False if the variables names in the input data are python
            variable names in PEP-8 snake case.
        _check_type: (boolean) if true, type will be checked and conversion
            will be attempted.
        configuration: (Configuration): the configuration class to use
            when converting file_type items.
            If passed, conversion will be attempted when possible
            If not passed, no conversions will be attempted and
            exceptions will be raised

    Returns:
        the correctly typed value

    Raises:
        ApiTypeError
    """
    results = get_required_type_classes(required_types_mixed, spec_property_naming)
    valid_classes, child_req_types_by_current_type = results

    input_class_simple = get_simple_class(input_value)
    valid_type = is_valid_type(input_class_simple, valid_classes)
    if not valid_type:
        if (configuration
                or (input_class_simple == dict
                    and dict not in valid_classes)):
            # if input_value is not valid_type try to convert it
            converted_instance = attempt_convert_item(
                input_value,
                valid_classes,
                path_to_item,
                configuration,
                spec_property_naming,
                key_type=False,
                must_convert=True,
                check_type=_check_type
            )
            return converted_instance
        else:
            raise get_type_error(input_value, path_to_item, valid_classes,
                                 key_type=False)

    # input_value's type is in valid_classes
    if len(valid_classes) > 1 and configuration:
        # there are valid classes which are not the current class
        valid_classes_coercible = remove_uncoercible(
            valid_classes, input_value, spec_property_naming, must_convert=False)
        if valid_classes_coercible:
            converted_instance = attempt_convert_item(
                input_value,
                valid_classes_coercible,
                path_to_item,
                configuration,
                spec_property_naming,
                key_type=False,
                must_convert=False,
                check_type=_check_type
            )
            return converted_instance

    if child_req_types_by_current_type == {}:
        # all types are of the required types and there are no more inner
        # variables left to look at
        return input_value
    inner_required_types = child_req_types_by_current_type.get(
        type(input_value)
    )
    if inner_required_types is None:
        # for this type, there are not more inner variables left to look at
        return input_value
    if isinstance(input_value, list):
        if input_value == []:
            # allow an empty list
            return input_value
        for index, inner_value in enumerate(input_value):
            inner_path = list(path_to_item)
            inner_path.append(index)
            input_value[index] = validate_and_convert_types(
                inner_value,
                inner_required_types,
                inner_path,
                spec_property_naming,
                _check_type,
                configuration=configuration
            )
    elif isinstance(input_value, dict):
        if input_value == {}:
            # allow an empty dict
            return input_value
        for inner_key, inner_val in input_value.items():
            inner_path = list(path_to_item)
            inner_path.append(inner_key)
            if get_simple_class(inner_key) != str:
                raise get_type_error(inner_key, inner_path, valid_classes,
                                     key_type=True)
            input_value[inner_key] = validate_and_convert_types(
                inner_val,
                inner_required_types,
                inner_path,
                spec_property_naming,
                _check_type,
                configuration=configuration
            )
    return input_value


def model_to_dict(model_instance, serialize=True):
    """Returns the model properties as a dict

    Args:
        model_instance (one of your model instances): the model instance that
            will be converted to a dict.

    Keyword Args:
        serialize (bool): if True, the keys in the dict will be values from
            attribute_map
    """
    result = {}

    def extract_item(item): return (
        item[0], model_to_dict(
            item[1], serialize=serialize)) if hasattr(
        item[1], '_data_store') else item

    model_instances = [model_instance]
    if model_instance._composed_schemas:
        model_instances.extend(model_instance._composed_instances)
    seen_json_attribute_names = set()
    used_fallback_python_attribute_names = set()
    py_to_json_map = {}
    for model_instance in model_instances:
        for attr, value in model_instance._data_store.items():
            if serialize:
                # we use get here because additional property key names do not
                # exist in attribute_map
                try:
                    attr = model_instance.attribute_map[attr]
                    py_to_json_map.update(model_instance.attribute_map)
                    seen_json_attribute_names.add(attr)
                except KeyError:
                    used_fallback_python_attribute_names.add(attr)
            if isinstance(value, list):
                if not value:
                    # empty list or None
                    result[attr] = value
                else:
                    res = []
                    for v in value:
                        if isinstance(v, PRIMITIVE_TYPES) or v is None:
                            res.append(v)
                        elif isinstance(v, ModelSimple):
                            res.append(v.value)
                        elif isinstance(v, dict):
                            res.append(dict(map(
                                extract_item,
                                v.items()
                            )))
                        else:
                            res.append(model_to_dict(v, serialize=serialize))
                    result[attr] = res
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    extract_item,
                    value.items()
                ))
            elif isinstance(value, ModelSimple):
                result[attr] = value.value
            elif hasattr(value, '_data_store'):
                result[attr] = model_to_dict(value, serialize=serialize)
            else:
                result[attr] = value
    if serialize:
        for python_key in used_fallback_python_attribute_names:
            json_key = py_to_json_map.get(python_key)
            if json_key is None:
                continue
            if python_key == json_key:
                continue
            json_key_assigned_no_need_for_python_key = json_key in seen_json_attribute_names
            if json_key_assigned_no_need_for_python_key:
                del result[python_key]

    return result


def type_error_message(var_value=None, var_name=None, valid_classes=None,
                       key_type=None):
    """
    Keyword Args:
        var_value (any): the variable which has the type_error
        var_name (str): the name of the variable which has the typ error
        valid_classes (tuple): the accepted classes for current_item's
                                  value
        key_type (bool): False if our value is a value in a dict
                         True if it is a key in a dict
                         False if our item is an item in a list
    """
    key_or_value = 'value'
    if key_type:
        key_or_value = 'key'
    valid_classes_phrase = get_valid_classes_phrase(valid_classes)
    msg = (
        "Invalid type for variable '{0}'. Required {1} type {2} and "
        "passed type was {3}".format(
            var_name,
            key_or_value,
            valid_classes_phrase,
            type(var_value).__name__,
        )
    )
    return msg


def get_valid_classes_phrase(input_classes):
    """Returns a string phrase describing what types are allowed
    """
    all_classes = list(input_classes)
    all_classes = sorted(all_classes, key=lambda cls: cls.__name__)
    all_class_names = [cls.__name__ for cls in all_classes]
    if len(all_class_names) == 1:
        return 'is {0}'.format(all_class_names[0])
    return "is one of [{0}]".format(", ".join(all_class_names))


def get_allof_instances(self, model_args, constant_args):
    """
    Args:
        self: the class we are handling
        model_args (dict): var_name to var_value
            used to make instances
        constant_args (dict):
            metadata arguments:
            _check_type
            _path_to_item
            _spec_property_naming
            _configuration
            _visited_composed_classes

    Returns
        composed_instances (list)
    """
    composed_instances = []
    for allof_class in self._composed_schemas['allOf']:

        try:
            if constant_args.get('_spec_property_naming'):
                allof_instance = allof_class._from_openapi_data(**model_args, **constant_args)
            else:
                allof_instance = allof_class(**model_args, **constant_args)
            composed_instances.append(allof_instance)
        except Exception as ex:
            raise ApiValueError(
                "Invalid inputs given to generate an instance of '%s'. The "
                "input data was invalid for the allOf schema '%s' in the composed "
                "schema '%s'. Error=%s" % (
                    allof_class.__name__,
                    allof_class.__name__,
                    self.__class__.__name__,
                    str(ex)
                )
            ) from ex
    return composed_instances


def get_oneof_instance(cls, model_kwargs, constant_kwargs, model_arg=None):
    """
    Find the oneOf schema that matches the input data (e.g. payload).
    If exactly one schema matches the input data, an instance of that schema
    is returned.
    If zero or more than one schema match the input data, an exception is raised.
    In OAS 3.x, the payload MUST, by validation, match exactly one of the
    schemas described by oneOf.

    Args:
        cls: the class we are handling
        model_kwargs (dict): var_name to var_value
            The input data, e.g. the payload that must match a oneOf schema
            in the OpenAPI document.
        constant_kwargs (dict): var_name to var_value
            args that every model requires, including configuration, server
            and path to item.

    Kwargs:
        model_arg: (int, float, bool, str, date, datetime, ModelSimple, None):
            the value to assign to a primitive class or ModelSimple class
            Notes:
            - this is only passed in when oneOf includes types which are not object
            - None is used to suppress handling of model_arg, nullable models are handled in __new__

    Returns
        oneof_instance (instance)
    """
    if len(cls._composed_schemas['oneOf']) == 0:
        return None

    oneof_instances = []
    # Iterate over each oneOf schema and determine if the input data
    # matches the oneOf schemas.
    for oneof_class in cls._composed_schemas['oneOf']:
        # The composed oneOf schema allows the 'null' type and the input data
        # is the null value. This is a OAS >= 3.1 feature.
        if oneof_class is none_type:
            # skip none_types because we are deserializing dict data.
            # none_type deserialization is handled in the __new__ method
            continue

        single_value_input = allows_single_value_input(oneof_class)

        try:
            if not single_value_input:
                if constant_kwargs.get('_spec_property_naming'):
                    oneof_instance = oneof_class._from_openapi_data(
                        **model_kwargs, **constant_kwargs)
                else:
                    oneof_instance = oneof_class(**model_kwargs, **constant_kwargs)
            else:
                if issubclass(oneof_class, ModelSimple):
                    if constant_kwargs.get('_spec_property_naming'):
                        oneof_instance = oneof_class._from_openapi_data(
                            model_arg, **constant_kwargs)
                    else:
                        oneof_instance = oneof_class(model_arg, **constant_kwargs)
                elif oneof_class in PRIMITIVE_TYPES:
                    oneof_instance = validate_and_convert_types(
                        model_arg,
                        (oneof_class,),
                        constant_kwargs['_path_to_item'],
                        constant_kwargs['_spec_property_naming'],
                        constant_kwargs['_check_type'],
                        configuration=constant_kwargs['_configuration']
                    )
            oneof_instances.append(oneof_instance)
        except Exception:
            pass
    if len(oneof_instances) == 0:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. None "
            "of the oneOf schemas matched the input data." %
            cls.__name__
        )
    elif len(oneof_instances) > 1:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. Multiple "
            "oneOf schemas matched the inputs, but a max of one is allowed." %
            cls.__name__
        )
    return oneof_instances[0]


def get_anyof_instances(self, model_args, constant_args):
    """
    Args:
        self: the class we are handling
        model_args (dict): var_name to var_value
            The input data, e.g. the payload that must match at least one
            anyOf child schema in the OpenAPI document.
        constant_args (dict): var_name to var_value
            args that every model requires, including configuration, server
            and path to item.

    Returns
        anyof_instances (list)
    """
    anyof_instances = []
    if len(self._composed_schemas['anyOf']) == 0:
        return anyof_instances

    for anyof_class in self._composed_schemas['anyOf']:
        # The composed oneOf schema allows the 'null' type and the input data
        # is the null value. This is a OAS >= 3.1 feature.
        if anyof_class is none_type:
            # skip none_types because we are deserializing dict data.
            # none_type deserialization is handled in the __new__ method
            continue

        try:
            if constant_args.get('_spec_property_naming'):
                anyof_instance = anyof_class._from_openapi_data(**model_args, **constant_args)
            else:
                anyof_instance = anyof_class(**model_args, **constant_args)
            anyof_instances.append(anyof_instance)
        except Exception:
            pass
    if len(anyof_instances) == 0:
        raise ApiValueError(
            "Invalid inputs given to generate an instance of %s. None of the "
            "anyOf schemas matched the inputs." %
            self.__class__.__name__
        )
    return anyof_instances


def get_discarded_args(self, composed_instances, model_args):
    """
    Gathers the args that were discarded by configuration.discard_unknown_keys
    """
    model_arg_keys = model_args.keys()
    discarded_args = set()
    # arguments passed to self were already converted to python names
    # before __init__ was called
    for instance in composed_instances:
        if instance.__class__ in self._composed_schemas['allOf']:
            try:
                keys = instance.to_dict().keys()
                discarded_keys = model_args - keys
                discarded_args.update(discarded_keys)
            except Exception:
                # allOf integer schema will throw exception
                pass
        else:
            try:
                all_keys = set(model_to_dict(instance, serialize=False).keys())
                js_keys = model_to_dict(instance, serialize=True).keys()
                all_keys.update(js_keys)
                discarded_keys = model_arg_keys - all_keys
                discarded_args.update(discarded_keys)
            except Exception:
                # allOf integer schema will throw exception
                pass
    return discarded_args


def validate_get_composed_info(constant_args, model_args, self):
    """
    For composed schemas, generate schema instances for
    all schemas in the oneOf/anyOf/allOf definition. If additional
    properties are allowed, also assign those properties on
    all matched schemas that contain additionalProperties.
    Openapi schemas are python classes.

    Exceptions are raised if:
    - 0 or > 1 oneOf schema matches the model_args input data
    - no anyOf schema matches the model_args input data
    - any of the allOf schemas do not match the model_args input data

    Args:
        constant_args (dict): these are the args that every model requires
        model_args (dict): these are the required and optional spec args that
            were passed in to make this model
        self (class): the class that we are instantiating
            This class contains self._composed_schemas

    Returns:
        composed_info (list): length three
            composed_instances (list): the composed instances which are not
                self
            var_name_to_model_instances (dict): a dict going from var_name
                to the model_instance which holds that var_name
                the model_instance may be self or an instance of one of the
                classes in self.composed_instances()
            additional_properties_model_instances (list): a list of the
                model instances which have the property
                additional_properties_type. This list can include self
    """
    # create composed_instances
    composed_instances = []
    allof_instances = get_allof_instances(self, model_args, constant_args)
    composed_instances.extend(allof_instances)
    oneof_instance = get_oneof_instance(self.__class__, model_args, constant_args)
    if oneof_instance is not None:
        composed_instances.append(oneof_instance)
    anyof_instances = get_anyof_instances(self, model_args, constant_args)
    composed_instances.extend(anyof_instances)
    """
    set additional_properties_model_instances
    additional properties must be evaluated at the schema level
    so self's additional properties are most important
    If self is a composed schema with:
    - no properties defined in self
    - additionalProperties: False
    Then for object payloads every property is an additional property
    and they are not allowed, so only empty dict is allowed

    Properties must be set on all matching schemas
    so when a property is assigned toa composed instance, it must be set on all
    composed instances regardless of additionalProperties presence
    keeping it to prevent breaking changes in v5.0.1
    TODO remove cls._additional_properties_model_instances in 6.0.0
    """
    additional_properties_model_instances = []
    if self.additional_properties_type is not None:
        additional_properties_model_instances = [self]

    """
    no need to set properties on self in here, they will be set in __init__
    By here all composed schema oneOf/anyOf/allOf instances have their properties set using
    model_args
    """
    discarded_args = get_discarded_args(self, composed_instances, model_args)

    # map variable names to composed_instances
    var_name_to_model_instances = {}
    for prop_name in model_args:
        if prop_name not in discarded_args:
            var_name_to_model_instances[prop_name] = [self] + list(
                filter(
                    lambda x: prop_name in x.openapi_types, composed_instances))

    return [
        composed_instances,
        var_name_to_model_instances,
        additional_properties_model_instances,
        discarded_args
    ]
