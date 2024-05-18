'''
Required imports.
- boto3 for AWS
- json for all JSON processing
- datetime to get the current time
- pytz to get ensure accurate time zone
'''
import boto3
import json
import datetime
import pytz


'''
Define the s3 and ec2 boto3 client which we can use as needed
'''
ec2 = boto3.client("ec2")


'''
- Implement the `process_instance()` function
    - implement this function which takes an `instance` and `current_hour` as input and realizes the psedocode below:
        - if instance is running and current_time is 8pm stop it
        - if instance is stopped and current_time is 8am start it
        - in all other cases, leave the instance as is
    - the function should return a message indicating the acion that was taken
'''
def process_instance(instance, current_hour):
    
    instance_state = instance["State"]["Name"]
    instance_id = instance["InstanceId"]
    message = "No action"
    if instance_state == "running":
        if current_hour == 21:
            ec2.stop_instances(InstanceIds=[instance_id])
            message = "Instance was stopped"
    elif instance_state == "stopped":
        if current_hour == 8:
            ec2.start_instances(InstanceIds=[instance_id])
            message = "Instance was started"

    return message

        


'''
Implement Lambda Handler
'''
def lambda_handler(event, context):

    # - get a list of instances
    # - if there are no instances, print a message and exit
    # - get the current hour
    # - iterate over the list of instances
    # -   at this time, only print the instance id, we will return to this step
    # - print a message that processing is complete
    try:
        now = datetime.datetime.now(pytz.timezone("America/New_York"))
        current_hour = int(now.strftime("%H"))

        response = ec2.describe_instances()
        instances = response["Reservations"][0]["Instances"]

        num_instances = len(instances)
        if num_instances == 0:
            print("There are no instances")
        else:
            for instance in instances:
                result = process_instance(instance, current_hour)
                print(result)
    except:
        print("Unexpected error")
        
    return


'''
Invoke lambda_hanlder
'''
if __name__ == "__main__":
    lambda_handler(None, None)