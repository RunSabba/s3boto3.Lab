import boto3

#set up the Variables for s3 bucket creation
s3 = boto3.resource('s3')
bucket_name = ()

#Check if bucket exists
#Create bucket if it does NOT exist
all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_my_buckets:
    print (f'{bucket_name} bucket does not exist. Creating now ... ')
    s3.create_bucket(Bucket=bucket_name)
    print (f'{bucket_name} bucket has been created')
else:
    print( " bucket already exists. NO need to make a new one")

#14-15 are the files im creating to add to my bucket    
file_1 = 'file1.txt'
file_2 = 'file2.txt'

#uploading file1 to bucket. The Run button gives me a FileNotFoundError: [Errno 2] No such file or directory: 'file1.txt' Error. Running script from Bash works fine. 
s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)

# Read and print file from the bucket
def s3readfile():
    obj = s3.Object(bucket_name, file_1)
    body = obj.get()['Body'].read()
    print (body)
s3readfile()
#Update file1 in the bucket with info from file2
s3.Object(bucket_name, file_1).put(Body=open(file_2, 'rb'))
s3readfile()

#delete the file from the bucket
s3.Object(bucket_name, file_1).delete()
