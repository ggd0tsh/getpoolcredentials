import boto3

def get_pool_credentials(region, identity_pool):
	client = boto3.client('cognito-identity', region_name=region)
	
	_id=client.get_id(IdentityPoolId=identity_pool)
	_id=_id['IdentityId']
	
	credentials=client.get_credentials_for_identity(IdentityId=_id)
	
	access_key = credentials['Credentials']['AccessKeyId']
	secret_key = credentials['Credentials']['SecretKey']
	session_token = credentials['Credentials']['SessionToken']
	identity_id = credentials['IdentityId']
	
	print ("access key: %s\nsecret key: %s\nsessiontoken: %s\nidentityid: %s\n" % (access_key, secret_key, session_token, identity_id))
	
def main():
	get_pool_credentials("region", "key")
	
main();
