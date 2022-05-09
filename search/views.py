
from django.shortcuts import render
from .forms import MostWatchedForm, BidsSearchForm, TypoSearchForm

from dateutil import parser

#models
from search.models import Listing

#ebay apis
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as finding
from ebaysdk.merchandising import Connection as merchandising
# from ebaysdk.trading import Connection as trading
# from ebaysdk.shopping import Connection as shopping

appID = 'MinToe-Capstone-PRD-1292f25b7-26b5f852'

############### ebay API calls #####################################
# c_id = category IDs

def getMostWatchedItems(c_id, num):
    api = merchandising(appid='MinToe-Capstone-PRD-1292f25b7-26b5f852', config_file=None)
    if int(c_id) == 0:
        response = api.execute('getMostWatchedItems', {'maxResults': num})
    else:
        response = api.execute('getMostWatchedItems', {'categoryId' : c_id, 'maxResults': num})
    return response

def getMostBids(c_id, keywords):
    api = finding(appid='MinToe-Capstone-PRD-1292f25b7-26b5f852', config_file=None)

    if int(c_id) == 0:
        request = {
            'keywords': keywords,
            'itemFilter': [
                {'name': 'ListingType', 'value': 'Auction'}
            ],
            'sortOrder': 'BidCountMost',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }
    else:
        request = {
            'categoryId' : c_id,
            'keywords': keywords,
            'itemFilter': [
                {'name': 'ListingType', 'value': 'Auction'}
            ],
            'sortOrder': 'BidCountMost',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }

    response = api.execute('findItemsAdvanced', request)
    return response

def getLeastBids(c_id, keywords):
    api = finding(appid='MinToe-Capstone-PRD-1292f25b7-26b5f852', config_file=None)

    if int(c_id) == 0:
        request = {
            'keywords': keywords,
            'itemFilter': [
                {'name': 'ListingType', 'value': 'Auction'}
            ],
            'sortOrder': 'BidCountFewest',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }
    else:
        request = {
            'categoryId' : c_id,
            'keywords': keywords,
            'itemFilter': [
                {'name': 'ListingType', 'value': 'Auction'}
            ],
            'sortOrder': 'BidCountFewest',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }

    response = api.execute('findItemsAdvanced', request)
    return response
    
def getEndingSoon(c_id, num):
    api = finding(appid='MinToe-Capstone-PRD-1292f25b7-26b5f852', config_file=None)
    if c_id == 0:
        response = api.execute('getMostWatchedItems', {'maxResults': num})
    else:
        response = api.execute('getMostWatchedItems', {'categoryId' : c_id, 'maxResults': num})
    return response

def getTypoSearch(c_id, keywords):
    api = finding(appid='MinToe-Capstone-PRD-1292f25b7-26b5f852', config_file=None)

    if int(c_id) == 0:
        request = {
            'keywords': keywords,
            'sortOrder': 'BestMatch',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }
    else:
        request = {
            'categoryId' : c_id,
            'keywords': keywords,
            'sortOrder': 'BestMatch',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }

    response = api.execute('findItemsAdvanced', request)
    return response

    
############### END OF ebay API calls #####################################


###################### START OF PYTHON FUNCTIONS #####################################

def butterfinger(text):
    res = "("

    for i in range(1, len(text)):
        new_str = text[:i - 1] +  text[i:]
        res += new_str
        res += ", "

    res += ")"
    return res

######################################################################################

###################### END OF PYTHON FUNCTIONS #####################################




###################### START OF VIEWS #####################################

def home(request):
    try:
        response = getMostWatchedItems(0, 4)
        objects = []
        objects2 = []

        for item in response.reply.itemRecommendations.item:
            object = Listing(title = item.title, watchCount = item.watchCount, viewItemURL = item.viewItemURL, imageURL = item.imageURL, 
            primaryCategoryName = item.primaryCategoryName, currentPrice = item.buyItNowPrice.value)
            objects.append(object)
            #object.save()

        qs = objects

        response = getMostWatchedItems(293, 4)

        for item in response.reply.itemRecommendations.item:
            object = Listing(title = item.title, watchCount = item.watchCount, viewItemURL = item.viewItemURL, imageURL = item.imageURL, 
            primaryCategoryName = item.primaryCategoryName, currentPrice = item.buyItNowPrice.value)
            objects2.append(object)
            #object.save()

        qa = objects2

        context = {
            'qs': qs,
            'qa': qa,
        }

        return render(request, 'search/home.html', context)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())
        return render(request, 'search/error.html')

# Most Watch Search
def mostWatchSearch(request):
    if (request.method == "POST"):
        watchForm = MostWatchedForm(request.POST)

        if (watchForm.is_valid()):
            objects = []
            categoryId = watchForm.cleaned_data["categoryId"]

            response = getMostWatchedItems(categoryId, 20)

            for item in response.reply.itemRecommendations.item:
                # object = Listing(title = item.title, watchCount = item.watchCount, viewItemURL = item.viewItemURL, imageURL = item.imageURL)
                object = Listing()

                try:
                    object.bidCount = item.bidCount
                except:
                    pass

                try:
                    object.buyItNowPrice = item.buyItNowPrice.value
                except:
                    pass
                
                try:
                    object.currentPrice = item.currentPrice.value
                except:
                    pass
                
                try:
                    object.imageURL = item.imageURL
                except:
                    pass
                
                try:
                    object.itemId = item.itemId
                except:
                    pass
                
                try:
                    object.primaryCategoryName = item.primaryCategoryName
                except:
                    pass
                
                try:
                    object.primaryCategoryId = item.primaryCategoryId
                except:
                    pass
                
                try:
                    object.shippingCost = item.shippingCost
                except:
                    pass
                
                try:
                    endTime = parser.parse(item.timeLeft)
                    object.endTime = endTime
                except:
                    pass
                
                try:
                    object.title = item.title
                except:
                    pass
                
                try:
                    object.viewItemURL = item.viewItemURL 
                except:
                    pass
                
                try:
                    object.watchCount = item.watchCount
                except:
                    pass
                objects.append(object)

            qs = objects

            context = {
                'qs': qs,
                "join_form": MostWatchedForm(),
            }

            return render(request, 'search/mostWatchSearch.html', context)
        else:
            context = {
                'error': watchForm.errors,
                "join_form": MostWatchedForm(),
            }

            return render(request, 'search/mostWatchSearch.html', context)
    else:
        return render(request, 'search/mostWatchSearch.html', { "join_form": MostWatchedForm() })


# Most Bids Search
def mostBidsSearch(request):
    if (request.method == "POST"):
        watchForm = BidsSearchForm(request.POST)

        if (watchForm.is_valid()):
            objects = []
            keywords = watchForm.cleaned_data["keywords"]
            categoryId = watchForm.cleaned_data["categoryId"]

            response = getMostBids(categoryId, keywords)

            for item in response.reply.searchResult.item:
                object = Listing()

                try:
                    object.bidCount = item.sellingStatus.bidCount
                except:
                    pass

                try:
                    object.buyItNowPrice = item.listingInfo.buyItNowPrice
                except:
                    pass
                
                try:
                    object.currentPrice = item.sellingStatus.currentPrice.value
                except:
                    pass
                
                try:
                    object.imageURL = item.galleryURL
                except:
                    pass
                
                try:
                    object.itemId = item.itemId
                except:
                    pass
                
                try:
                    object.primaryCategoryName = item.primaryCategory.categoryName
                except:
                    pass
                
                try:
                    object.primaryCategoryId = item.primaryCategory.categoryId
                except:
                    pass
                
                try:
                    object.shippingCost = item.shippingInfo.shippingServiceCost
                except:
                    pass
                
                try:
                    object.endTime = item.listingInfo.endTime
                except:
                    pass
                
                try:
                    object.title = item.title
                except:
                    pass
                
                try:
                    object.viewItemURL = item.viewItemURL 
                except:
                    pass
                
                try:
                    object.watchCount = item.listingInfo.watchCount
                except:
                    pass
                objects.append(object)

            qs = objects

            context = {
                'qs': qs,
                "join_form": BidsSearchForm(),
                'keywords': keywords,
            }

            return render(request, 'search/mostBidsSearch.html', context)
        else:
            context = {
                'error': watchForm.errors,
                "join_form": BidsSearchForm(),
            }

            return render(request, 'search/mostBidsSearch.html', context)
    else:
        return render(request, 'search/mostBidsSearch.html', { "join_form": BidsSearchForm() })

# Least Bids Search
def leastBidsSearch(request):
    if (request.method == "POST"):
        watchForm = BidsSearchForm(request.POST)

        if (watchForm.is_valid()):
            objects = []
            keywords = watchForm.cleaned_data["keywords"]
            categoryId = watchForm.cleaned_data["categoryId"]

            response = getLeastBids(categoryId, keywords)

            for item in response.reply.searchResult.item:
                
                object = Listing()

                try:
                    object.bidCount = item.sellingStatus.bidCount
                except:
                    pass

                try:
                    object.buyItNowPrice = item.listingInfo.buyItNowPrice
                except:
                    pass
                
                try:
                    object.currentPrice = item.sellingStatus.currentPrice.value
                except:
                    pass
                
                try:
                    object.imageURL = item.galleryURL
                except:
                    pass
                
                try:
                    object.itemId = item.itemId
                except:
                    pass
                
                try:
                    object.primaryCategoryName = item.primaryCategory.categoryName
                except:
                    pass
                
                try:
                    object.primaryCategoryId = item.primaryCategory.categoryId
                except:
                    pass
                
                try:
                    object.shippingCost = item.shippingInfo.shippingServiceCost
                except:
                    pass
                
                try:
                    object.endTime = item.listingInfo.endTime
                except:
                    pass
                
                try:
                    object.title = item.title
                except:
                    pass
                
                try:
                    object.viewItemURL = item.viewItemURL 
                except:
                    pass
                
                try:
                    object.watchCount = item.listingInfo.watchCount
                except:
                    pass

                objects.append(object)

            qs = objects

            context = {
                'qs': qs,
                "join_form": BidsSearchForm(),
                'keywords': keywords,
            }

            return render(request, 'search/leastBidsSearch.html', context)
        else:
            context = {
                'error': watchForm.errors,
                "join_form": BidsSearchForm(),
            }

            return render(request, 'search/leastBidsSearch.html', context)
    else:
        return render(request, 'search/leastBidsSearch.html', { "join_form": BidsSearchForm() })


# Typo Search
def typoSearch(request):
    if (request.method == "POST"):
        watchForm = TypoSearchForm(request.POST)

        if (watchForm.is_valid()):
            objects = []
            typoText = watchForm.cleaned_data["keywords"]

            keywords = butterfinger(typoText)

            categoryId = watchForm.cleaned_data["categoryId"]

            response = getTypoSearch(categoryId, keywords)

            for item in response.reply.searchResult.item:
                    
                object = Listing()

                try:
                    object.bidCount = item.sellingStatus.bidCount
                except:
                    pass

                try:
                    object.buyItNowPrice = item.listingInfo.buyItNowPrice
                except:
                    pass
                
                try:
                    object.currentPrice = item.sellingStatus.currentPrice.value
                except:
                    pass
                
                try:
                    object.imageURL = item.galleryURL
                except:
                    pass
                
                try:
                    object.itemId = item.itemId
                except:
                    pass
                
                try:
                    object.primaryCategoryName = item.primaryCategory.categoryName
                except:
                    pass
                
                try:
                    object.primaryCategoryId = item.primaryCategory.categoryId
                except:
                    pass
                
                try:
                    object.shippingCost = item.shippingInfo.shippingServiceCost
                except:
                    pass
                
                try:
                    object.endTime = item.listingInfo.endTime
                except:
                    pass
                
                try:
                    object.title = item.title
                except:
                    pass
                
                try:
                    object.viewItemURL = item.viewItemURL 
                except:
                    pass
                
                try:
                    object.watchCount = item.listingInfo.watchCount
                except:
                    pass
                objects.append(object)

            qs = objects

            context = {
                'qs': qs,
                "join_form": TypoSearchForm(),
                'keywords': keywords,
            }

            return render(request, 'search/typoSearch.html', context)
        else:
            context = {
                'error': watchForm.errors,
                "join_form": TypoSearchForm(),
            }

            return render(request, 'search/typoSearch.html', context)
    else:
        return render(request, 'search/typoSearch.html', { "join_form": TypoSearchForm() })

# # Schedule Listing
def findListing(request):
    qs = Listing.objects.all()

    context = {
                'qs': qs,
            }

    return render(request, 'search/listing.html', context)