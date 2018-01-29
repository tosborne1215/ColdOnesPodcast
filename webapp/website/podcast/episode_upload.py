import boto3

from django.conf import settings
from django.core.files.storage import Storage
from django.core.cache import cache
from django.utils.deconstruct import deconstructible
# Initialize a session using Spaces
# session = boto3.session.Session()
# client = session.client('s3',
#                         region_name='nyc3',
#                         endpoint_url='https://nyc3.digitaloceanspaces.com',
#                         aws_secret_access_key='crvP5sqsCT4feRnKu9KR16h5Z6BTH75zdA6PCZxeFps',
#                         aws_access_key_id='6YAHACWH2IGRHFJCXIOU')
#
#https://nyc3.digitaloceanspaces.com/
#
# client.upload_file(file, bucket, key, ExtraArgs={'ACL': 'public-read'})

#             self.region_name='nyc3'
#             self.endpoint_url='https://nyc3.digitaloceanspaces.com'
#             self.aws_secret_access_key='crvP5sqsCT4feRnKu9KR16h5Z6BTH75zdA6PCZxeFps'
#             self.aws_access_key_id='6YAHACWH2IGRHFJCXIOU'
@deconstructible
class S3StorageWrapper(Storage):
    #boto3 client with service s3
    client = None
    bucket = None
    namespace = None
    cache = None

    def __init__(self, option=None):
        session = boto3.session.Session()
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS

        self.bucket = option['bucket']
        self.namespace = option['namespace']

        session = boto3.session.Session()
        self.client = session.client('s3',
                        region_name=option['region_name'],
                        endpoint_url=option['endpoint_url'],
                        aws_secret_access_key=option['aws_secret_access_key'],
                        aws_access_key_id=option['aws_access_key_id'])
        self.cache = cache


    def _open(self, name, mode='rb'):
        key = self.namespace + '/' + name

        with open(name, 'wb') as data:
            self.client.download_fileobj(self.bucket, key, data)
        return data


    #content is of File type
    def _save(self, name, content):
        key = self.namespace + '/' + name
        self.client.upload_fileobj(content, self.bucket, key, ExtraArgs={'ACL': 'public-read'})
        return name

    def url(self, name):
        print ("url")
        return "http://google.com/" + name

    #TODO: well that isnt hacky at all
    def exists(self, name):
        return False

    def path(self, name):
        print ("path")
        return "http://google.com/"+name

    def generate_filename(self, filename):
        print ("generate_filename")
        return filename
#
    def url(self, name):
        print ("url")
        print(name)
        return name

    def get_valid_name(self, name):
        return name

    #Fetches from either the cache or the server
    def retrieve_bucket_contents_dict(self):
        bucketResponse = self.client.list_objects(Bucket=self.bucket)
        httpCode = bucketResponse['ResponseMetadata']['HTTPStatusCode'];
        bucketContents = None

        if httpCode is 200:
            bucketContents = bucketResponse['Contents']
        else:
            #this is problematic
            pass

        return bucketContents

