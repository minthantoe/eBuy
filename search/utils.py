#ebay apis
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as finding
from ebaysdk.merchandising import Connection as merchandising

from search.models import Listing

def getLatestPostings(c_id, keywords):
    api = finding(appid='MinToe-Capstone-PRD-1292f25b7-26b5f852', config_file=None)

    if int(c_id) == 0:
        request = {
            'keywords': keywords,
            'sortOrder': 'StartTimeNewest',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }
    else:
        request = {
            'categoryId' : c_id,
            'keywords': keywords,
            'sortOrder': 'StartTimeNewest',
            'OutputSelectorType':  ['PictureURLLarge', 'PictureURLSuperSize']
        }

    response = api.execute('findItemsAdvanced', request)
    return response


def saveListing():
    """
    We get the lastest image and save it to our Photo Model in the Database
    """
    response = getLatestPostings(0, 'book')
    item = response.reply.searchResult.item
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

    if not Listing.objects.filter(itemId=object.itemId).exists():
        object.save()
