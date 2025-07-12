# variables.tf
variable "my_ip_address" {
  description = "My personal IP address for SSH access. Must be in CIDR notation (e.g., 1.2.3.4/32)."
  type        = string
}


variable "s3_bucket_name" {
  description = "The globally unique name for the S3 bucket to store scraped data."
  type        = string
}

variable "aws_region"{
  description = "The aws region"
  type        = string
}

variable "bedrock_model_id"{
  description = "Bedrock model for vectorization"
  type = string
}

variable "vector_store_prefix" {
  description = "s3 bucket to save parquet file"
  type = string
}