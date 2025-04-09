import subprocess
import os

# Set environment variables for AWS authentication
os.environ["AWS_ACCESS_KEY_ID"] = "aws access key"
os.environ["AWS_SECRET_ACCESS_KEY"] = "access key id"

# Set environment variables for Azure authentication
os.environ["ARM_SUBSCRIPTION_ID"] = "dummy-55c9-40b7-8f4f-804b7c387095"
os.environ["ARM_CLIENT_ID"] = "dummmmm3-1018-49fb-99f1-a19b85d3b1af"
os.environ["ARM_CLIENT_SECRET"] = "cmX8Q~dummmmmmmmmmmmmmmmmmmmmmmm.3yHrayZalxJvJrgyxmcW2"
os.environ["ARM_TENANT_ID"] = "dummmm-4e42-a9c7-b175f7b69f58"

# Function to create EC2 instances
def create_ec2_instance(instance_type):
    resource_mapping = {
        "large": "large_server",
        "medium": "medium_server",
        "small": "small_server",
    }

    resource_name = resource_mapping.get(instance_type)
    if resource_name:
        subprocess.run(["terraform", "apply", "-auto-approve", "-target", f"aws_instance.{resource_name}"])
    else:
        print("Invalid selection for AWS. Available options: 'large', 'medium', 'small'.")

# Function to create Azure virtual machines
def create_azure_vm(vm_type):
    resource_mapping = {
        "large": "large_vm",
        "medium": "medium_vm",
        "small": "small_vm",
    }

    resource_name = resource_mapping.get(vm_type)
    if resource_name:
        subprocess.run(["terraform", "apply", "-auto-approve", "-target", f"azurerm_virtual_machine.{resource_name}"])
    else:
        print("Invalid selection for Azure. Available options: 'large', 'medium', 'small'.")

if __name__ == "__main__":
    print("Select a cloud provider:")
    print("1. AWS")
    print("2. Azure")

    provider_choice = input("Enter the number of the cloud provider: ").strip()

    if provider_choice == "1":  # AWS
        print("\nSelect a server type for AWS:")
        print("1. Image (Large Server)")
        print("2. Text (Medium Server)")
        print("3. Structured (Small Server)")

        aws_choice = input("Enter the number of the server type for AWS: ").strip()

        if aws_choice == "1":
            create_ec2_instance("large")
        elif aws_choice == "2":
            create_ec2_instance("medium")
        elif aws_choice == "3":
            create_ec2_instance("small")
        else:
            print("Invalid selection for AWS. Please choose 1, 2, or 3.")

    elif provider_choice == "2":  # Azure
        print("\nSelect a virtual machine type for Azure:")
        print("1. Image (Large VM)")
        print("2. Text (Medium VM)")
        print("3. Structured (Small VM)")

        azure_choice = input("Enter the number of the virtual machine type for Azure: ").strip()

        if azure_choice == "1":
            create_azure_vm("large")
        elif azure_choice == "2":
            create_azure_vm("medium")
        elif azure_choice == "3":
            create_azure_vm("small")
        else:
            print("Invalid selection for Azure. Please choose 1, 2, or 3.")

    else:
        print("Invalid selection for cloud provider. Please choose 1 for AWS or 2 for Azure.")
