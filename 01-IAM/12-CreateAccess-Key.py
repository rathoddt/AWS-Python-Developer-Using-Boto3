import boto3


# def create_access(username):
#     iam = boto3.client('iam')

#     response = iam.create_access_key(
#         UserName=username
#     )

#     print(response)



# create_access('testuser-01')




def update_access():
    iam = boto3.client('iam')
    iam.update_access_key(
        AccessKeyId='AKIAZ42E5SWXYP27E3GE',
        Status='Inactive',
        UserName='testuser-01'

    )


update_access()




