# variables.tf
variable "my_ip_address" {
  description = "My personal IP address for SSH access. Must be in CIDR notation (e.g., 1.2.3.4/32)."
  type        = string
}


variable "s3_bucket_name" {
  description = "The globally unique name for the S3 bucket to store scraped data."
  type        = string
}
