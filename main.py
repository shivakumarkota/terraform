# subprocess module used to run new codes and applications by creating new processes
import subprocess

# function to create EC2 instances
def create_ec2_instance(instance_type):
    # Define a mapping of instance types to Terraform resource names
    resource_mapping = {
        "large": "large_server",
        "medium": "medium_server",
        "small": "small_server",
    }

    # Run Terraform apply for the selected resource
    resource_name = resource_mapping.get(instance_type)
    if resource_name:
        subprocess.run(["terraform", "apply", "-auto-approve", "-target", f"aws_instance.{resource_name}"])
    else:
        print("Invalid selection. Available options: 'large', 'medium', 'small'.")

if __name__ == "__main__":
    print("Select a server type:")
    print("1. Image (Large Server)")
    print("2. Text (Medium Server)")
    print("3. Structured (Small Server)")

    choice = input("Enter the number of the server type: ").strip()

    if choice == "1":
        create_ec2_instance("large")
    elif choice == "2":
        create_ec2_instance("medium")
    elif choice == "3":
        create_ec2_instance("small")
    else:
        print("Invalid selection. Please choose 1, 2, or 3.")
