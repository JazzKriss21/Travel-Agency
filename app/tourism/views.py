from django.shortcuts import render
import requests
import traceback
import requests
from .dummy_data import *
import json
from .forms import FlightDetailsForm
from settings import sec



def home_view(request):

    headers = {
          'x-rapidapi-key': sec.A,
          'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }
    if request.method=='POST':
        form=FlightDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            originCity=form.cleaned_data['originCity']
            destinationCity=form.cleaned_data['destinationCity']
            Departure_date=form.cleaned_data['Departure_date']
            url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/"+originCity+"-sky/"+destinationCity+"-sky/"+str(Departure_date)+""
            querystring={"query":form.cleaned_data['Departure_date'],"query1":form.cleaned_data['originCity'],"query2":form.cleaned_data['destinationCity']}
            response = requests.request("GET", url, headers=headers, params=querystring)
            data=dict(response.json())

            Quotes=data['Quotes']
            Places=data['Places']
            Carriers=data['Carriers']
            Currencies=data['Currencies']
            Routes=data['Routes']
            flights=[]
            holder=[Quotes,Places,Carriers,Currencies,Routes]
            length=max(len(Quotes),len(Carriers),len(Currencies),len(Routes))
            for i in range(4):
                if len(holder[i])==length:
                    continue
                else:
                    num=length-len(holder[i])
                    for j in range(num):
                        holder[i].append(holder[i][0])

            for i in range(len(Quotes)):
                temp=[]
                for j in range(4):
                    temp.append(holder[j][i])
                flights.append(temp)
            list=['Direct','Name']
            list1=[]
            if originCity=='MAA'  or destinationCity =='MAA':
                list1.append('Chennai')
            if originCity=='DEL' or destinationCity =='DEL':
                list1.append('New Delhi')
            if originCity=='BLR' or destinationCity=='BLR':
                list1.append('Bengaluru')
            if originCity=='CCU' or destinationCity=='CCU':
                list1.append('Kolkata')
            if originCity=='HYD' or destinationCity=='HYD':
                list1.append('Hyderabad')



            context={'data':data,'flights':flights,'list':list,'list1':list1,'Departure_date':Departure_date}
            return render(request,'flight_details_routes.html',context=context)
    else:
        form=FlightDetailsForm()

    context={'email':request.user,'form':form}

    return render(request, "home.html",context=context)



def hotel_search(request):
    return render(request, 'hotels_form.html')

# online
# def hotel_detail(request):
#     checkin = request.GET.get('checkin')
#     checkout = request.GET.get('checkout')
#     hotel_id = request.GET.get('id')
#     rooms = request.GET.get('room')
#
#     url = "https://hotels-com-free.p.rapidapi.com/pde/property-details/v1/hotels.com/" + hotel_id
#
#     querystring = {"checkIn": checkin, "locale": "en_US", "rooms": rooms, "checkOut": checkout,
#                    "currency": "INR", "include": "neighborhood"}
#
#     headers = {
#         'x-rapidapi-key': "",
#         'x-rapidapi-host': "hotels-com-free.p.rapidapi.com"
#     }
#
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     print('-------------hoteldetails start-----------')
#     print(response.text)
#     print('-------------hotelsdetails end-------------')
#     # print(hotel_details_.text)
#     # json_string = json.dumps(hotel_details_)
#     # print(json_string)
#
#     # res = dict(hotel_details_)
#     res = dict(response.json())
#
#     # print(response)
#     # print(hotel_id)
#     address = res['data']['body']['propertyDescription']['address']['fullAddress']
#     saddress = res['data']['body']['propertyDescription']['address']['addressLine1']
#     hotel_name = res['data']['body']['smallPrint']['alternativeNames'][0]
#     rating = res['data']['body']['propertyDescription']['starRating']
#
#     maps = hotel_name + " " + address
#     try:
#         no_of_reviews = res['data']['body']['guestReviews']['brands']['total']
#     except Exception as e:
#         no_of_reviews = 0
#         trace_back = traceback.format_exc()
#         message = str(e) + " " + str(trace_back)
#         print(message)
#     places_nearby = res['data']['body']['overview']['overviewSections'][2]['content']
#     amenities = res['data']['body']['overview']['overviewSections'][0]['content']
#     hotel_policy = res['data']['body']['atAGlance']['keyFacts']['requiredAtCheckIn']
#     roomTypeNames_lst = res['data']['body']['propertyDescription']['roomTypeNames']
#     roomTypeNames = [x for x in roomTypeNames_lst if len(x.strip()) > 0]
#
#     # roomTypeNames_dict= {}
#     # for item in roomTypeNames:
#     #     x= item.split(',',2)
#     #     print(x)
#
#
#     no_room_ = len(res['data']['body']['roomsAndRates']['rooms'])
#     print('no_of_rooms '+str(no_room_))
#     print(len(res['data']['body']['roomsAndRates']['rooms']))
#
#     # no_room_=5
#
#     roomTypeNames_ = []
#     room_img_url_ = []
#     room_price_ = []
#     room_old_price_ = []
#     for i in range(no_room_):
#         roomTypeNames_.append(res['data']['body']['roomsAndRates']['rooms'][i]['name'])
#
#         try:
#             room_img_url_.append(res['data']['body']['roomsAndRates']['rooms'][i]['images'][0]['thumbnailUrl'])
#         except Exception as e:
#             room_old_price_.append(
#                 'https://recyclingbalers.s3.amazonaws.com/image/webp/150150/1502-NoImage.webp')
#             trace_back = traceback.format_exc()
#             message = str(e) + " " + str(trace_back)
#             print(message)
#
#         room_price_.append(
#             res['data']['body']['roomsAndRates']['rooms'][i]['ratePlans'][0]['price']['unformattedCurrent'])
#         try:
#             room_old_price_.append(res['data']['body']['roomsAndRates']['rooms'][i]['ratePlans'][0]['price']['old'])
#         except Exception as e:
#             room_old_price_.append( res['data']['body']['roomsAndRates']['rooms'][i]['ratePlans'][0]['price']['unformattedCurrent'])
#             trace_back = traceback.format_exc()
#             message = str(e) + " " + str(trace_back)
#             print(message)
#
#     print(roomTypeNames)
#
#     r_type = roomTypeNames_[0]
#     r_p = room_price_[0]
#     r_o = room_old_price_[0]
#
#     multi_list = zip(roomTypeNames_, room_img_url_, room_price_, room_old_price_)
#     context = {'hotel_name': hotel_name, 'address': address, 'rating': rating, 'no_of_reviews': no_of_reviews,
#                'saddress': saddress, 'places_nearby': places_nearby, 'amenities': amenities,
#                'hotel_policy': hotel_policy, 'multi_list': multi_list, 'maps': maps, 'r_type': r_type, 'r_p': r_p,
#                'r_o': r_o}
#
#     print(roomTypeNames_, room_img_url_)
#     # print(places_nearby)
#
#     return render(request, 'hotel_details.html', context)



# offline
def hotel_detail(request):
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    hotel_id = request.GET.get('id')
    rooms = request.GET.get('room')

    url = "https://hotels-com-free.p.rapidapi.com/pde/property-details/v1/hotels.com/" + hotel_id
    #
    querystring = {"checkIn": checkin, "locale": "en_US", "rooms": rooms, "checkOut": checkout,
                   "currency": "INR", "include": "neighborhood"}
    headers = {
        'x-rapidapi-key': sec.B,
        'x-rapidapi-host': "hotels-com-free.p.rapidapi.com"
    }


    #open weather

    url = "https://community-open-weather-map.p.rapidapi.com/onecall/timemachine"

    querystring = {"lat": "37.774929", "lon": "-122.419418", "dt": "1590094153 "}

    headers = {
        'x-rapidapi-key': sec.C,
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    respons = requests.request("GET", url, headers=headers, params=querystring)
     # print  -------------weather
    print("Weather----------------------")
    print(respons.text)
    print('---------------weather ed')
    # weather ---end


    response = requests.request("GET", url, headers=headers, params=querystring)
    print('-------------hoteldetails start-----------')
    print(response.text)
    print('-------------hotelsdetails end-------------')
    # print(hotel_details_.text)
    # json_string = json.dumps(hotel_details_)
    # print(json_string)

    # res = dict(hotel_details_)
    res = dict(response.json())

    # print(response)
    # print(hotel_id)
    address = res['data']['body']['propertyDescription']['address']['fullAddress']
    saddress = res['data']['body']['propertyDescription']['address']['addressLine1']
    hotel_name = res['data']['body']['smallPrint']['alternativeNames'][0]
    rating = res['data']['body']['propertyDescription']['starRating']

    maps = hotel_name + " " + address
    try:
        no_of_reviews = res['data']['body']['guestReviews']['brands']['total']
    except Exception as e:
        no_of_reviews = 0
        trace_back = traceback.format_exc()
        message = str(e) + " " + str(trace_back)
        print(message)
    places_nearby = res['data']['body']['overview']['overviewSections'][2]['content']
    amenities = res['data']['body']['overview']['overviewSections'][0]['content']
    hotel_policy = res['data']['body']['atAGlance']['keyFacts']['requiredAtCheckIn']
    roomTypeNames_lst = res['data']['body']['propertyDescription']['roomTypeNames']
    roomTypeNames = [x for x in roomTypeNames_lst if len(x.strip()) > 0]

    # roomTypeNames_dict= {}
    # for item in roomTypeNames:
    #     x= item.split(',',2)
    #     print(x)


    no_room_ = len(res['data']['body']['roomsAndRates']['rooms'])
    print('no_of_rooms '+str(no_room_))
    print(len(res['data']['body']['roomsAndRates']['rooms']))

    # no_room_=1

    roomTypeNames_ = []
    room_img_url_ = []
    room_price_ = []
    room_old_price_ = []
    for i in range(no_room_):
        roomTypeNames_.append(res['data']['body']['roomsAndRates']['rooms'][i]['name'])

        try:
            room_img_url_.append(res['data']['body']['roomsAndRates']['rooms'][i]['images'][0]['thumbnailUrl'])
        except Exception as e:
            room_old_price_.append(
                'https://recyclingbalers.s3.amazonaws.com/image/webp/150150/1502-NoImage.webp')
            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)

        room_price_.append(
            res['data']['body']['roomsAndRates']['rooms'][i]['ratePlans'][0]['price']['unformattedCurrent'])
        try:
            room_old_price_.append(res['data']['body']['roomsAndRates']['rooms'][i]['ratePlans'][0]['price']['old'])
        except Exception as e:
            room_old_price_.append( res['data']['body']['roomsAndRates']['rooms'][i]['ratePlans'][0]['price']['unformattedCurrent'])
            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)

    print(roomTypeNames)

    r_type = roomTypeNames_[0]
    r_p = room_price_[0]
    r_o = room_old_price_[0]

    multi_list = zip(roomTypeNames_, room_img_url_, room_price_, room_old_price_)
    context = {'hotel_name': hotel_name, 'address': address, 'rating': rating, 'no_of_reviews': no_of_reviews,
               'saddress': saddress, 'places_nearby': places_nearby, 'amenities': amenities,
               'hotel_policy': hotel_policy, 'multi_list': multi_list, 'maps': maps, 'r_type': r_type, 'r_p': r_p,
               'r_o': r_o,'checkin':checkin,'checkout':checkout}

    print(roomTypeNames_, room_img_url_)
    # print(places_nearby)

    return render(request, 'hotel_details.html', context)


def hotel_list(request):
    # 740515104
    # real start ----------------------------------------------------------------------
    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
    address = request.GET.get('city_')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    rooms = request.GET.get('rooms')

    # print(address,checkin,checkout)
    querystring = {"address": address, "language": "en"}

    headers = {
        'x-rapidapi-key': sec.B,
        'x-rapidapi-host': "hotels-com-free.p.rapidapi.com"
    }

    res = requests.request("GET", url, headers=headers, params=querystring)
    res = dict(res.json())

    print(res['results'][0]['location']['lat'])
    print(res['results'][0]['location']['lng'])

    lat = res['results'][0]['location']['lat']
    long = res['results'][0]['location']['lng']

    print('--------------------------' + 'hotel_list' + '-------------------------------------')
    print('----------------------------GeoCode--------------------------------------------')
    print('lat: ' + str(lat))
    print('long: ' + str(long))
    #
    # print('--------------------------search-----------------------------------------------')

    # d_rapi_api_---------------------------------------start

    url = "https://hotels-com-free.p.rapidapi.com/srle/listing/v1/brands/hotels.com"

    querystring = {"checkIn": checkin, "checkOut": checkout, "lat": lat,
                   "lon": long, "locale": "en_US", "rooms": rooms, "currency": "USD", "pageNumber": "1"}

    headers = {
        'x-rapidapi-key': sec.C,
        'x-rapidapi-host': "hotels-com-free.p.rapidapi.com"
    }

    res = requests.request("GET", url, headers=headers, params=querystring)

    # d_rapid_api_--------------------------------------------end

    # url = "https://hotels-com-free.p.rapidapi.com/srle/listing/v1/brands/hotels.com"
    #
    # querystring = {"checkIn": checkin, "checkOut": checkout, "lat": lat,
    #                "lon": long, "locale": "en_US", "rooms": rooms, "currency": "INR", "pageNumber": "1"}
    #
    # headers = {
    #     'x-rapidapi-key': "",
    #     'x-rapidapi-host': "hotels-com-free.p.rapidapi.com"
    # }
    #
    # res = requests.request("GET", url, headers=headers, params=querystring)
    #
    print(res.text)

    # print(res.text)
    #

    # dummy data from py file-----------------------------------------
    # print(dummy_data_)
    # res = dict(dummy_data_)
    res = dict(res.json())
    #
    # checkin = '2020-12-20'
    # checkout = '2020-12-23'
    # dummy data end

    length = len(res['data']['body']['searchResults']['results'])
    print('no. of items '+str(length))
    hotel_name = []
    address = []
    thumbnailUrl = []
    starRating = []
    guestReviews_total = []
    badgeText = []
    rate = []
    old_rate = []
    hotel_id = []
    for i in range(length):
        hotel_name.append(res['data']['body']['searchResults']['results'][i]['name'])
        thumbnailUrl.append(res['data']['body']['searchResults']['results'][i]['thumbnailUrl'])
        try:
            address.append(res['data']['body']['searchResults']['results'][i]['address']['streetAddress'] + " " +
                           res['data']['body']['searchResults']['results'][i]['address']['locality'])
        except Exception as e:
            address.append(
                res['data']['body']['searchResults']['results'][i]['address']['locality'])
            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)

        starRating.append(res['data']['body']['searchResults']['results'][i]['starRating'])
        try:
            guestReviews_total.append(res['data']['body']['searchResults']['results'][i]['guestReviews']['total'])
        except Exception as e:
            guestReviews_total.append(0)

            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)

        try:
            badgeText.append(res['data']['body']['searchResults']['results'][i]['guestReviews']['badgeText'])

        except Exception as e:
            badgeText.append('NA')

            trace_back = traceback.format_exc()
            message = str(e) + " " + str(trace_back)
            print(message)
        rate.append(round(res['data']['body']['searchResults']['results'][i]['ratePlan']['price']['exactCurrent']*75))

        hotel_id.append(res['data']['body']['searchResults']['results'][i]['id'])

        # print(old_rate)

    # print(hotel_name)
    # print(address)
    # print(range(length))
    multi_list = zip(hotel_name, address, thumbnailUrl, starRating, guestReviews_total, badgeText, rate, hotel_id)
    context = {'n': range(length), 'multi_list': multi_list, 'checkin': checkin, 'checkout': checkout}
    return render(request, 'hotel_list.html', context)


# def hotel_list(request):
#     res = {'result': 'OK', 'data': {'body': {'header': '22 Anthony St, San Francisco, CA 94105, USA', 'query': {
#         'destination': {'id': '1493604', 'value': '22 Anthony St, San Francisco, CA 94105, USA',
#                         'resolvedLocation': 'GEO_LOCATION:22 Anthony St, San Francisco, CA 94105, USA|37.78880310058594|-122.40035247802734:GEOCODE:UNKNOWN'}},
#                                              'searchResults': {'totalCount': 414, 'results': [
#                                                  {'id': 601827, 'name': 'Hotel 32One',
#                                                   'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/16000000/15400000/15399300/15399261/03a6ebaf_l.jpg',
#                                                   'starRating': 3.0, 'urls': {},
#                                                   'address': {'streetAddress': '321 Grant Avenue',
#                                                               'extendedAddress': '', 'locality': 'San Francisco',
#                                                               'postalCode': '94108', 'region': 'CA',
#                                                               'countryName': 'United States', 'countryCode': 'us',
#                                                               'obfuscate': False}, 'welcomeRewards': {'collect': True},
#                                                   'guestReviews': {'unformattedRating': 3.8, 'rating': '3.8',
#                                                                    'total': 38, 'scale': 5, 'badge': 'good',
#                                                                    'badgeText': 'Good'}, 'landmarks': [], 'ratePlan': {
#                                                      'price': {'current': '$95', 'exactCurrent': 95.2, 'old': '$119'},
#                                                      'features': {'freeCancellation': False, 'paymentPreference': False,
#                                                                   'noCCRequired': False}, 'type': 'EC'},
#                                                   'neighbourhood': 'Union Square',
#                                                   'deals': {'secretPrice': {'dealText': 'Save more with Secret Prices'},
#                                                             'priceReasoning': 'DRR-445'}, 'messaging': {},
#                                                   'badging': {}, 'pimmsAttributes': 'DoubleStamps|MESOTESTUS|D13|TESCO',
#                                                   'coordinate': {'lat': 37.790012, 'lon': -122.405544},
#                                                   'providerType': 'LOCAL', 'supplierHotelId': 15399261,
#                                                   'isAlternative': False},
#                                                  {'id': 230158, 'name': 'Cornell Hotel de France',
#                                                   'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/2000000/1230000/1222800/1222727/bfbcbf67_l.jpg',
#                                                   'starRating': 3.5, 'urls': {},
#                                                   'address': {'streetAddress': '715 Bush St', 'extendedAddress': '',
#                                                               'locality': 'San Francisco', 'postalCode': '94108',
#                                                               'region': 'CA', 'countryName': 'United States',
#                                                               'countryCode': 'us', 'obfuscate': False},
#                                                   'welcomeRewards': {'collect': True},
#                                                   'guestReviews': {'unformattedRating': 4.4, 'rating': '4.4',
#                                                                    'total': 721, 'scale': 5, 'badge': 'fabulous',
#                                                                    'badgeText': 'Fabulous'}, 'landmarks': [],
#                                                   'ratePlan': {'price': {'current': '$131', 'exactCurrent': 130.5,
#                                                                          'old': '$145'},
#                                                                'features': {'freeCancellation': True,
#                                                                             'paymentPreference': True,
#                                                                             'noCCRequired': False}, 'type': 'Dual'},
#                                                   'neighbourhood': 'Lower Nob Hill',
#                                                   'deals': {'secretPrice': {'dealText': 'Save more with Secret Prices'},
#                                                             'priceReasoning': 'DRR-443'}, 'messaging': {},
#                                                   'badging': {}, 'pimmsAttributes': 'DoubleStamps|MESOTESTUS|D13|TESCO',
#                                                   'coordinate': {'lat': 37.790145, 'lon': -122.409146},
#                                                   'providerType': 'LOCAL', 'supplierHotelId': 1222727,
#                                                   'isAlternative': False},
#                                                  {'id': 117069, 'name': 'Hotel Abri - Union Square',
#                                                   'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/1000000/20000/15800/15779/05098316_l.jpg',
#                                                   'starRating': 3.5, 'urls': {},
#                                                   'address': {'streetAddress': '127 Ellis Street',
#                                                               'extendedAddress': '', 'locality': 'San Francisco',
#                                                               'postalCode': '94102', 'region': 'CA',
#                                                               'countryName': 'United States', 'countryCode': 'us',
#                                                               'obfuscate': False}, 'welcomeRewards': {'collect': True},
#                                                   'guestReviews': {'unformattedRating': 4.3, 'rating': '4.3',
#                                                                    'total': 685, 'scale': 5, 'badge': 'fabulous',
#                                                                    'badgeText': 'Fabulous'}, 'landmarks': [],
#                                                   'ratePlan': {'price': {'current': '$107', 'exactCurrent': 107.28,
#                                                                          'old': '$119'},
#                                                                'features': {'freeCancellation': True,
#                                                                             'paymentPreference': True,
#                                                                             'noCCRequired': False}, 'type': 'Dual'},
#                                                   'neighbourhood': 'Union Square',
#                                                   'deals': {'secretPrice': {'dealText': 'Save more with Secret Prices'},
#                                                             'priceReasoning': 'DRR-443'},
#                                                   'messaging': {'scarcity': '3 left on our app'}, 'badging': {},
#                                                   'pimmsAttributes': 'DoubleStamps|priceRangeCA|D13|TESCO',
#                                                   'coordinate': {'lat': 37.78548, 'lon': -122.4083}, 'roomsLeft': 3,
#                                                   'providerType': 'LOCAL', 'supplierHotelId': 15779,
#                                                   'isAlternative': False},
#                                                  {'id': 210688, 'name': 'Club Quarters Hotel in San Francisco',
#                                                   'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/1000000/920000/913000/912982/832c79fe_l.jpg',
#                                                   'starRating': 4.0, 'urls': {},
#                                                   'address': {'streetAddress': '424 Clay St', 'extendedAddress': '',
#                                                               'locality': 'San Francisco', 'postalCode': '94111',
#                                                               'region': 'CA', 'countryName': 'United States',
#                                                               'countryCode': 'us', 'obfuscate': False},
#                                                   'welcomeRewards': {'collect': True},
#                                                   'guestReviews': {'unformattedRating': 4.2, 'rating': '4.2',
#                                                                    'total': 1592, 'scale': 5, 'badge': 'very-good',
#                                                                    'badgeText': 'Very Good'}, 'landmarks': [],
#                                                   'ratePlan': {
#                                                       'price': {'current': '$93', 'exactCurrent': 93.15, 'old': '$115'},
#                                                       'features': {'freeCancellation': True, 'paymentPreference': True,
#                                                                    'noCCRequired': False}, 'type': 'Dual'},
#                                                   'neighbourhood': 'Financial District',
#                                                   'deals': {'secretPrice': {'dealText': 'Save more with Secret Prices'},
#                                                             'priceReasoning': 'DRR-445'}, 'messaging': {},
#                                                   'badging': {}, 'pimmsAttributes': 'DoubleStamps|MESOTESTUS|D13|TESCO',
#                                                   'coordinate': {'lat': 37.794972, 'lon': -122.400809},
#                                                   'providerType': 'LOCAL', 'supplierHotelId': 912982,
#                                                   'isAlternative': False}, {'id': 207080, 'name': 'Grant Hotel',
#                                                                             'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/1000000/910000/907700/907617/44c99f50_l.jpg',
#                                                                             'starRating': 2.0, 'urls': {},
#                                                                             'address': {'streetAddress': '753 Bush St',
#                                                                                         'extendedAddress': '',
#                                                                                         'locality': 'San Francisco',
#                                                                                         'postalCode': '94108',
#                                                                                         'region': 'CA',
#                                                                                         'countryName': 'United States',
#                                                                                         'countryCode': 'us',
#                                                                                         'obfuscate': False},
#                                                                             'welcomeRewards': {'collect': True},
#                                                                             'guestReviews': {'unformattedRating': 3.9,
#                                                                                              'rating': '3.9',
#                                                                                              'total': 1024, 'scale': 5,
#                                                                                              'badge': 'good',
#                                                                                              'badgeText': 'Good'},
#                                                                             'landmarks': [], 'ratePlan': {
#                                                          'price': {'current': '$71', 'exactCurrent': 71.2,
#                                                                    'old': '$89'}, 'features': {'freeCancellation': True,
#                                                                                                'paymentPreference': True,
#                                                                                                'noCCRequired': False},
#                                                          'type': 'Dual'}, 'neighbourhood': 'Lower Nob Hill', 'deals': {
#                                                          'secretPrice': {'dealText': 'Save more with Secret Prices'},
#                                                          'priceReasoning': 'DRR-445'}, 'messaging': {
#                                                          'scarcity': '4 left on our app'}, 'badging': {},
#                                                                             'pimmsAttributes': 'DoubleStamps|D13|TESCO',
#                                                                             'coordinate': {'lat': 37.790056,
#                                                                                            'lon': -122.409652},
#                                                                             'roomsLeft': 4, 'providerType': 'LOCAL',
#                                                                             'supplierHotelId': 907617,
#                                                                             'isAlternative': False},
#                                                  {'id': 208040, 'name': 'White Swan Inn',
#                                                   'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/1000000/30000/25100/25027/f9ddee91_l.jpg',
#                                                   'starRating': 3.5, 'urls': {},
#                                                   'address': {'streetAddress': '845 Bush St', 'extendedAddress': '',
#                                                               'locality': 'San Francisco', 'postalCode': '94108',
#                                                               'region': 'CA', 'countryName': 'United States',
#                                                               'countryCode': 'us', 'obfuscate': False},
#                                                   'welcomeRewards': {'collect': True},
#                                                   'guestReviews': {'unformattedRating': 4.5, 'rating': '4.5',
#                                                                    'total': 293, 'scale': 5, 'badge': 'superb',
#                                                                    'badgeText': 'Superb'}, 'landmarks': [],
#                                                   'ratePlan': {'price': {'current': '$127', 'exactCurrent': 126.75,
#                                                                          'old': '$169'},
#                                                                'features': {'freeCancellation': True,
#                                                                             'paymentPreference': True,
#                                                                             'noCCRequired': False}, 'type': 'Dual'},
#                                                   'neighbourhood': 'Lower Nob Hill',
#                                                   'deals': {'secretPrice': {'dealText': 'Save more with Secret Prices'},
#                                                             'priceReasoning': 'DRR-445'}, 'messaging': {},
#                                                   'badging': {'hotelBadge': {'type': 'vipBasic', 'label': 'VIP'}},
#                                                   'pimmsAttributes': 'DoubleStamps|D13|TESCO',
#                                                   'coordinate': {'lat': 37.78993, 'lon': -122.41115},
#                                                   'providerType': 'LOCAL', 'supplierHotelId': 25027,
#                                                   'isAlternative': False}, {'id': 141179,
#                                                                             'name': 'Palace Hotel, a Luxury Collection Hotel, San Francisco',
#                                                                             'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/1000000/30000/27300/27274/cb8526cf_l.jpg',
#                                                                             'starRating': 5.0, 'urls': {}, 'address': {
#                                                          'streetAddress': '2 New Montgomery St', 'extendedAddress': '',
#                                                          'locality': 'San Francisco', 'postalCode': '94105',
#                                                          'region': 'CA', 'countryName': 'United States',
#                                                          'countryCode': 'us', 'obfuscate': False},
#                                                                             'welcomeRewards': {'collect': True},
#                                                                             'guestReviews': {'unformattedRating': 4.4,
#                                                                                              'rating': '4.4',
#                                                                                              'total': 1152, 'scale': 5,
#                                                                                              'badge': 'fabulous',
#                                                                                              'badgeText': 'Fabulous'},
#                                                                             'landmarks': [], 'ratePlan': {
#                                                          'price': {'current': '$259', 'exactCurrent': 259.0},
#                                                          'features': {'freeCancellation': True,
#                                                                       'paymentPreference': True, 'noCCRequired': False},
#                                                          'type': 'Dual'}, 'neighbourhood': 'Financial District',
#                                                                             'deals': {}, 'messaging': {}, 'badging': {},
#                                                                             'pimmsAttributes': 'DoubleStamps|priceRangeCA|priceRangeUK|TESCO',
#                                                                             'coordinate': {'lat': 37.788682,
#                                                                                            'lon': -122.401919},
#                                                                             'providerType': 'LOCAL',
#                                                                             'supplierHotelId': 27274,
#                                                                             'isAlternative': False}, {'id': 129368,
#                                                                                                       'name': 'Galleria Park Hotel, a Joie de Vivre Boutique Hotel',
#                                                                                                       'thumbnailUrl': 'https://exp.cdn-hotels.com/hotels/1000000/30000/22400/22303/ba451360_l.jpg',
#                                                                                                       'starRating': 4.0,
#                                                                                                       'urls': {},
#                                                                                                       'address': {
#                                                                                                           'streetAddress': '191 Sutter St',
#                                                                                                           'extendedAddress': '',
#                                                                                                           'locality': 'San Francisco',
#                                                                                                           'postalCode': '94104',
#                                                                                                           'region': 'CA',
#                                                                                                           'countryName': 'United States',
#                                                                                                           'countryCode': 'us',
#                                                                                                           'obfuscate': False},
#                                                                                                       'welcomeRewards': {
#                                                                                                           'collect': True},
#                                                                                                       'guestReviews': {
#                                                                                                           'unformattedRating': 4.4,
#                                                                                                           'rating': '4.4',
#                                                                                                           'total': 871,
#                                                                                                           'scale': 5,
#                                                                                                           'badge': 'fabulous',
#                                                                                                           'badgeText': 'Fabulous'},
#                                                                                                       'landmarks': [],
#                                                                                                       'ratePlan': {
#                                                                                                           'price': {
#                                                                                                               'current': '$161',
#                                                                                                               'exactCurrent': 160.55,
#                                                                                                               'old': '$169'},
#                                                                                                           'features': {
#                                                                                                               'freeCancellation': True,
#                                                                                                               'paymentPreference': True,
#                                                                                                               'noCCRequired': False},
#                                                                                                           'type': 'Dual'},
#                                                                                                       'neighbourhood': 'Financial District',
#                                                                                                       'deals': {
#                                                                                                           'secretPrice': {
#                                                                                                               'dealText': 'Save more with Secret Prices'},
#                                                                                                           'priceReasoning': 'DRR-443'},
#                                                                                                       'messaging': {},
#                                                                                                       'badging': {
#                                                                                                           'hotelBadge': {
#                                                                                                               'type': 'vipBasic',
#                                                                                                               'label': 'VIP'}},
#                                                                                                       'pimmsAttributes': 'DoubleStamps|MESOTESTUS|D13|TESCO',
#                                                                                                       'coordinate': {
#                                                                                                           'lat': 37.78983,
#                                                                                                           'lon': -122.4037},
#                                                                                                       'providerType': 'LOCAL',
#                                                                                                       'supplierHotelId': 22303,
#                                                                                                       'isAlternative': False}],
#                                                                'pagination': {'currentPage': 1,
#                                                                               'pageGroup': 'EXPEDIA_IN_POLYGON',
#                                                                               'nextPageStartIndex': 9,
#                                                                               'nextPageNumber': 2,
#                                                                               'nextPageGroup': 'EXPEDIA_IN_POLYGON'}},
#                                              'sortResults': {'options': [{'label': 'Featured', 'itemMeta': 'popular',
#                                                                           'choices': [{'label': 'Featured',
#                                                                                        'value': 'BEST_SELLER',
#                                                                                        'selected': False}],
#                                                                           'enhancedChoices': []},
#                                                                          {'label': 'Star rating', 'itemMeta': 'star',
#                                                                           'choices': [{'label': 'Stars (high to low)',
#                                                                                        'value': 'STAR_RATING_HIGHEST_FIRST',
#                                                                                        'selected': False},
#                                                                                       {'label': 'Stars (low to high)',
#                                                                                        'value': 'STAR_RATING_LOWEST_FIRST',
#                                                                                        'selected': False}],
#                                                                           'enhancedChoices': []},
#                                                                          {'label': 'Distance', 'itemMeta': 'distance',
#                                                                           'selectedChoiceLabel': 'Distance',
#                                                                           'choices': [{'label': 'Distance',
#                                                                                        'value': 'DISTANCE_FROM_LANDMARK',
#                                                                                        'selected': True}],
#                                                                           'enhancedChoices': [{'label': 'Landmarks',
#                                                                                                'itemMeta': 'landmarks',
#                                                                                                'choices': [
#                                                                                                    {'label': 'Alameda',
#                                                                                                     'id': 1490117.0},
#                                                                                                    {'label': 'Albany',
#                                                                                                     'id': 1421819.0}, {
#                                                                                                        'label': 'Alcatraz Island',
#                                                                                                        'id': 1596.0},
#                                                                                                    {'label': 'Berkeley',
#                                                                                                     'id': 1636697.0}, {
#                                                                                                        'label': 'Bill Graham Civic Auditorium',
#                                                                                                        'id': 1707433.0},
#                                                                                                    {'label': 'Brisbane',
#                                                                                                     'id': 1529187.0},
#                                                                                                    {'label': 'Colma',
#                                                                                                     'id': 11047185.0}, {
#                                                                                                        'label': 'Daly City',
#                                                                                                        'id': 1445779.0},
#                                                                                                    {
#                                                                                                        'label': 'Emeryville',
#                                                                                                        'id': 1485086.0},
#                                                                                                    {
#                                                                                                        'label': 'Golden Gate Bridge',
#                                                                                                        'id': 1001.0}, {
#                                                                                                        'label': 'Marin City',
#                                                                                                        'id': 11047122.0},
#                                                                                                    {
#                                                                                                        'label': 'Moscone Convention Center',
#                                                                                                        'id': 1407964.0},
#                                                                                                    {'label': 'Oakland',
#                                                                                                     'id': 1538105.0}, {
#                                                                                                        'label': 'Oracle Park',
#                                                                                                        'id': 583.0},
#                                                                                                    {'label': 'Pier 39',
#                                                                                                     'id': 1652926.0}, {
#                                                                                                        'label': 'San Francisco',
#                                                                                                        'id': 1493604.0},
#                                                                                                    {
#                                                                                                        'label': 'Sausalito',
#                                                                                                        'id': 1525555.0},
#                                                                                                    {
#                                                                                                        'label': 'South San Francisco',
#                                                                                                        'id': 1490656.0},
#                                                                                                    {'label': 'Tiburon',
#                                                                                                     'id': 1513223.0}, {
#                                                                                                        'label': 'UCSF Medical Center',
#                                                                                                        'id': 11129819.0}]},
#                                                                                               {'label': 'Stations',
#                                                                                                'itemMeta': 'stations',
#                                                                                                'choices': [{
#                                                                                                                'label': '16th Street Mission Station',
#                                                                                                                'id': 1726781.0},
#                                                                                                            {
#                                                                                                                'label': '24th Street Mission Station',
#                                                                                                                'id': 1726783.0},
#                                                                                                            {
#                                                                                                                'label': 'Balboa Park Station',
#                                                                                                                'id': 1726787.0},
#                                                                                                            {
#                                                                                                                'label': 'Daly City Station',
#                                                                                                                'id': 1726789.0},
#                                                                                                            {
#                                                                                                                'label': 'Embarcadero Station',
#                                                                                                                'id': 1726771.0},
#                                                                                                            {
#                                                                                                                'label': 'Emeryville Station',
#                                                                                                                'id': 1734874.0},
#                                                                                                            {
#                                                                                                                'label': 'Fruitvale Station',
#                                                                                                                'id': 1758996.0},
#                                                                                                            {
#                                                                                                                'label': 'Glen Park Station',
#                                                                                                                'id': 1726784.0},
#                                                                                                            {
#                                                                                                                'label': 'Hyde St & Beach St Stop',
#                                                                                                                'id': 1725592.0},
#                                                                                                            {
#                                                                                                                'label': 'MacArthur Station',
#                                                                                                                'id': 1758999.0},
#                                                                                                            {
#                                                                                                                'label': 'Montgomery St. Station',
#                                                                                                                'id': 1726772.0},
#                                                                                                            {
#                                                                                                                'label': 'North Berkeley Station',
#                                                                                                                'id': 1759013.0},
#                                                                                                            {
#                                                                                                                'label': 'Oakland-Jack London Square Station',
#                                                                                                                'id': 1734390.0},
#                                                                                                            {
#                                                                                                                'label': 'Powell St & Market St Stop',
#                                                                                                                'id': 1725570.0},
#                                                                                                            {
#                                                                                                                'label': 'Powell St. Station',
#                                                                                                                'id': 1726773.0},
#                                                                                                            {
#                                                                                                                'label': 'San Francisco Station',
#                                                                                                                'id': 1725529.0},
#                                                                                                            {
#                                                                                                                'label': 'South San Francisco Metro Station',
#                                                                                                                'id': 1726792.0},
#                                                                                                            {
#                                                                                                                'label': 'South San Francisco Station',
#                                                                                                                'id': 1724054.0},
#                                                                                                            {
#                                                                                                                'label': 'Taylor St & Bay St Stop',
#                                                                                                                'id': 10903812.0},
#                                                                                                            {
#                                                                                                                'label': 'West Oakland Station',
#                                                                                                                'id': 1759004.0}]}]},
#                                                                          {'label': 'Guest rating', 'itemMeta': 'rating',
#                                                                           'choices': [{'label': 'Guest rating',
#                                                                                        'value': 'GUEST_RATING',
#                                                                                        'selected': False}],
#                                                                           'enhancedChoices': []},
#                                                                          {'label': 'Price', 'itemMeta': 'price',
#                                                                           'choices': [{'label': 'Price (high to low)',
#                                                                                        'value': 'PRICE_HIGHEST_FIRST',
#                                                                                        'selected': False},
#                                                                                       {'label': 'Price (low to high)',
#                                                                                        'value': 'PRICE',
#                                                                                        'selected': False}],
#                                                                           'enhancedChoices': []}]}, 'pointOfSale': {
#             'currency': {'code': 'USD', 'symbol': '$', 'separators': ',.', 'format': '${0}'}}, 'miscellaneous': {
#             'pageViewBeaconUrl': 'https://www.egadvertising.com/travelAds/v1/TravelAdPageView?deviceType=App-Phone&sort-order=DISTANCE_FROM_LANDMARK&rooms=1&hotelIds=601827,230158,163750,117069,210688,207080,208040,141179,129368&adults=1&userAgent=Hotels.com/Android%2056.1.1.9.release-56_1%20(56010472)&userGuid=7907534a-f458-4f4d-94f7-9057ed3e62ba&pageName=Hotel-Search&slots=HSR_A,HSR_B,HSR_C,HSR_D,HSR_E&checkIn=2021-01-27&children=0&culture=en_US&testVersionOverride=4961.0,904.0,7561.0,7215.0,8218.0,8711.0,8928.0,9008.0,8347.0,9004.0,8952.0,7992.2,8915.0,9729.0,9716.0,9803.0,9824.0,9864.0&domain=www.hotels.com&tac=true&userIP=127.0.0.1&action=pageview&publisher=expedia&checkOut=2021-01-28&programId=1',
#             'showLegalInfoForStrikethroughPrices': True,
#             'legalInfoForStrikethroughPrices': 'The struck-out price is based on the property’s standard rate on our app, as determined and supplied by the property.'},
#                                              'pageInfo': {'pageType': 'dateful'}},
#                                     'common': {'pointOfSale': {'numberSeparators': ',.', 'brandName': 'Hotels.com'},
#                                                'tracking': {'omniture': {'s.prop33': 'D=v33', 's.prop32': 'D=v43',
#                                                                          's.products': 'LOCAL;15399261,MULTISOURCE;1222727,LOCAL;3552',
#                                                                          's.eVar41': 'USD',
#                                                                          's.eVar63': '69a4a444-88a7-49d6-b6e6-a707b0464a54',
#                                                                          's.eVar42': '48|1|20210127|20210128',
#                                                                          's.eVar4': '|SI:anonymous|VS:returnVisitor|HCR:notApplicable|FC:notApplicable|NS:unknown|TI:notApplicable|SM:notApplicable|IR:anonymous|',
#                                                                          's.eVar43': 'en_US|HCOM_US|www.hotels.com',
#                                                                          's.eVar3': '1|0',
#                                                                          's.eVar22': '1|USD|24:601827:119.0000:95.2000:0|24:230158:145.0000:130.5000:0|24:163750:::0|24:117069:119.2000:107.2800:0|24:210688:115.0000:93.1500:0',
#                                                                          's.eVar2': '22 Anthony St, San Francisco, CA 94105, USA',
#                                                                          's.eVar23': '1|USD|24:207080:89.0000:71.2000:0|24:208040:169.0000:126.7500:0|24:141179:259.0000:259.0000:0|24:129368:169.0000:160.5500:0',
#                                                                          's.eVar24': 'MCTC=20;TU=NA;PDID=NULL;MVT=',
#                                                                          's.eVar7': '48', 's.server': 'www.hotels.com',
#                                                                          's.eVar6': 'geo|22 Anthony St, San Francisco, CA 94105, USA|37.789|-122.4',
#                                                                          's.prop29': 'D=v42', 's.eVar5': '1',
#                                                                          's.prop27': '7907534a-f458-4f4d-94f7-9057ed3e62ba',
#                                                                          's.eVar9': 'Distance from address',
#                                                                          's.prop21': '0', 's.prop20': '1',
#                                                                          's.currencyCode': 'USD', 's.prop9': '414',
#                                                                          's.eVar95': 'Unknown', 's.prop7': '414',
#                                                                          's.eVar33': 'search result with dates',
#                                                                          's.eVar34': 'H277:017.002,H1871:007.002,M376:000.000,M555:005.003,M904:000.000,M1167:000.000,M1291:000.000,M1292:000.000,M1293:000.000,M1294:000.000,M3736:000.000,M4200:000.000,M4440.0,M4869:001.000,M4952:032.001,M4961:001.000,M5167.0,M5342:000.000,M5663:000.000,M6388:000.000,M6775:000.000,M6779:000.000,M7015.0,M7066:000.000,M7192:000.001,M7214:000.000,M7215:000.000,M7296:000.000,M7305:000.000,M7353:000.000,M7362.0,M7384:000.000,M7552:023.001,M7561:000.000,M7763:000.000,M7870:000.000,M7895:000.000,M8130:000.001,M8336:000.000,M8347:000.000,M8483:000.000,M8485:007.001,M8698:000.000,M8708:000.000,M8714:000.000,M8718:000.000,M8758:000.000,M8915:000.000,M8928:000.000,M8952:000.000,M8969:000.000,M8976:000.000,M8992:000.000,M9004:000.000,M9035:000.000,M9065:000.000,M9100:000.000,M9220:000.000,M9281:000.000,M9282:000.000,M9297:000.000,M9351:000.000,M9420:000.000,M9424:002.002,M9427:000.000,M9431:000.000,M9434:000.000,M9469:000.000,M9549:000.000,M9567.0,M9606:012.002,M9693:000.000,M9716:000.000,M9729:000.000,M9752:000.000,M9771:000.000,M9853:000.000,M9864:000.000,M9924:000.000,M9961:000.000,M9971:000.000,M10001:000.000,M10010:000.000,M10013:000.000,M10068:000.000,M10077:000.000,M10121:000.000,M10125:000.000,M9215:001.000',
#                                                                          's.eVar13': '389367', 's.prop19': '1',
#                                                                          's.events': 'event320', 's.prop18': 'D=v6',
#                                                                          's.prop5': '389367', 's.prop15': '1',
#                                                                          's.prop3': '22 Anthony St, San Francisco, CA 94105, USA',
#                                                                          's.prop14': 'D=v7',
#                                                                          's.prop36': '|SI:anonymous|VS:returnVisitor|HCR:notApplicable|FC:notApplicable|NS:unknown|TI:notApplicable|SM:notApplicable|IR:anonymous|',
#                                                                          's.eVar93': 'aws.us-west-2.unknown',
#                                                                          's.prop2': 'Distance from address'}}}}}
#
#     length = len(res['data']['body']['searchResults']['results'])
#     print('no. of items '+str(length))
#     hotel_name=[]
#     address=[]
#     thumbnailUrl=[]
#     starRating=[]
#     guestReviews_total=[]
#     badgeText=[]
#     rate=[]
#     old_rate=[]
#     for i in range(length):
#         hotel_name.append(res['data']['body']['searchResults']['results'][i]['name'])
#         thumbnailUrl.append(res['data']['body']['searchResults']['results'][i]['thumbnailUrl'])
#         address.append(res['data']['body']['searchResults']['results'][i]['address']['streetAddress']+" "+res['data']['body']['searchResults']['results'][i]['address']['locality'])
#         starRating.append(res['data']['body']['searchResults']['results'][i]['starRating'])
#         guestReviews_total.append(res['data']['body']['searchResults']['results'][i]['guestReviews']['total'])
#         badgeText.append(res['data']['body']['searchResults']['results'][i]['guestReviews']['badgeText'])
#         rate.append(round(res['data']['body']['searchResults']['results'][i]['ratePlan']['price']['exactCurrent']*73))
#
#
#         print(old_rate)
#
#     print(hotel_name)
#     print(address)
#     print(range(length))
#     multi_list = zip(hotel_name,address,thumbnailUrl,starRating,guestReviews_total,badgeText,rate)
#     context = {'n':range(length),'multi_list':multi_list}
#     return render(request, 'hotel_list.html',context)





# def home_view(request):
#
#
#
#
#     usr = {
#         "email": request.user
#     }
#     return render(request, "home.html", usr)


def form(request):
    return render(request, "travel_box.html")




def flightdetails_listOfPlaces(request):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"
    querystring = {"query":"Chennai"}
    headers = {
          'x-rapidapi-key': sec.A,
          'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    res=dict(response.json())
    context={'Places':res['Places']}

    return render(request,'flight_details.html',context=context)

def flightdetails_place_to_place(request):
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/MAA-sky/DEL-sky/2020-11-30"

    querystring = {"inboundpartialdate":"2020-11-30"}

    headers = {
        'x-rapidapi-key': sec.A,
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    res=dict(response.json())
    context={'Quotes':res['Quotes']}
    return render(request,'flight_details_routes.html',context=context)


def hoteldetails(request):
    url = "https://hotels4.p.rapidapi.com/locations/search"

    querystring = {"query": "new york", "locale": "en_US"}

    headers = {
        'x-rapidapi-key': sec.A,
        'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = dict(response.json())
    context = {'res': res}
    return render(request, 'hotel_details.html', context=context)

