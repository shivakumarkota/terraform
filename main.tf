
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "large_server" {
  ami           = "ami-051f8a213df8bc089"
  instance_type = "m5.large"
}

resource "aws_instance" "medium_server" {
  ami           = "ami-0faac27e2fc42cead"
  instance_type = "t2.medium"
}

resource "aws_instance" "small_server" {
  ami           = "ami-0f98ffa30af  27acc6"
  instance_type = "t2.micro"
}
