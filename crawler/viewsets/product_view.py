from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from crawler.utility.scraper import getProductDetails

class ProductViewSet(viewsets.ModelViewSet):

    @action(methods=['POST'], detail=False, url_path = 'fetch_details')
    def fetchProductInformation(self, request):
        body = request.data
        url = body.get('url')
        if not url:
            return Response({ "error": "Url Not Found" }, status=HTTP_400_BAD_REQUEST)
        
        product_infomation = getProductDetails(url)
        return Response({ "success": True, "product_details": product_infomation }, status= HTTP_200_OK)
    

    @action(methods=['GET'], detail=False)
    def getProductList(self, request):
        pass