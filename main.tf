# main.tf

# 1. The VPC - Your private network
resource "aws_vpc" "hyperion_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "Hyperion-VPC"
  }
}

# 2. The Public Subnet - Where the EC2 instance will live
resource "aws_subnet" "hyperion_public_subnet" {
  vpc_id     = aws_vpc.hyperion_vpc.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true # gives the EC2 a public IP
  tags = {
    Name = "Hyperion-Public-Subnet"
  }
}

# 3. The Internet Gateway - The door to the internet
resource "aws_internet_gateway" "hyperion_gw" {
  vpc_id = aws_vpc.hyperion_vpc.id
  tags = {
    Name = "Hyperion-IGW"
  }
}

# 4. The Route Table - The map telling the subnet how to use the door
resource "aws_route_table" "hyperion_rt" {
  vpc_id = aws_vpc.hyperion_vpc.id

  route {
    cidr_block = "0.0.0.0/0" # All outbound traffic
    gateway_id = aws_internet_gateway.hyperion_gw.id
  }

  tags = {
    Name = "Hyperion-Public-Route-Table"
  }
}

# Associate the route table with our public subnet
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.hyperion_public_subnet.id
  route_table_id = aws_route_table.hyperion_rt.id
}

# 5. The S3 Bucket - Your private data store
resource "aws_s3_bucket" "hyperion_data" {
  # Change this line
  bucket = var.s3_bucket_name # <--- Use a variable instead of a hard-coded string

  tags = {
    Name = "HyperionData"
  }
}

# 6. The EC2 Instance Request
resource "aws_instance" "scraper_node" {
  ami           = "ami-092ff8e60e2d51e19" 
  instance_type = "t3.micro"
  
  # Attach the IAM role for S3 access
  iam_instance_profile = aws_iam_instance_profile.s3_access_profile.name

  # Place it in our public subnet and attach the firewall
  subnet_id              = aws_subnet.hyperion_public_subnet.id
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  
  # Associate our public SSH key
  key_name = aws_key_pair.deployer_key.key_name

  # Run our startup script
  user_data = templatefile("user_data.sh.tpl", {
  bucket_name = aws_s3_bucket.hyperion_data.id
  })


  tags = {
    Name = "Hyperion-Scraper-Node"
  }
}