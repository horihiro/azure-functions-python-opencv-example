import logging
import os
import urllib.request as rq
import re
import azure.functions as func
import mimetypes

# Using `import cv2`, error, which SO files cannot be loaded, is occurred
# import cv2

# Instead of above, dynamic import cannot be used.
import ctypes
import importlib

exlibpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/tmp/'
ctypes.CDLL(exlibpath + 'libglib-2.0.so.0')
ctypes.CDLL(exlibpath + 'libgthread-2.0.so.0')

cv2 = importlib.import_module('cv2')

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    image_url = req.params.get('image_url')
    if not image_url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            image_url = req_body.get('image_url')

    if image_url:
        local = re.sub(r'^.*/([^/]+)$', r'\1', image_url)
        rq.urlretrieve(image_url, '/tmp/' + local)
        im = cv2.imread('/tmp/' + local)
        gry = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('/tmp/gray_' + local, gry)
        with open('/tmp/gray_' + local, 'rb') as f:
            mimetype = mimetypes.guess_type('/tmp/gray_' + local)
            return func.HttpResponse(f.read(), mimetype=mimetype[0])
        # return func.HttpResponse(f"Hello {image_url}!")
    else:
        return func.HttpResponse(
             "Please pass a image_url on the query string or in the request body",
             status_code=400
        )
