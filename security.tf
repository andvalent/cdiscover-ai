# security.tf

# The EC2 Instance's Firewall
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh_from_my_ip"
  description = "Allow SSH inbound traffic from my IP"
  vpc_id      = aws_vpc.hyperion_vpc.id

  ingress {
    description = "SSH from my IP"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip_address]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1" # Allow all outbound traffic
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Allow-SSH"
  }
}

# Resource for your SSH public key
resource "aws_key_pair" "deployer_key" {
  key_name   = "hyperion-key"
  # This tells Terraform to read your public key from a file.
  public_key = file("~/.ssh/id_rsa.pub")
}


resource "aws_key_pair" "vectorizer_key" {
  key_name   = "hyperion-vectorizer-key"

  # Use the new, correct path. Use forward slashes.
  public_key = file("C:/Users/valen/MyKeys/hyperion-vectorizer-key.pub")
}