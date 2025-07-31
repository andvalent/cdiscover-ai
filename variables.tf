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

variable "create_scraper_node" {
  description = "If set to true, the Hyperion Scraper EC2 instance will be created. Set to false if it has already run its course."
  type        = bool
  default     = false # Set the default to false to prevent accidental creation
}

variable "create_vectorizer_node" {
  description = "If set to true, the Hyperion Vectorizer EC2 instance will be created. Set to false if it has already run its course."
  type        = bool
  default     = true # Set the default to false to prevent accidental creation
}

variable "create_rag_api" {
  description = "If set to true, the Hyperion Vectorizer EC2 instance will be created. Set to false if it has already run its course."
  type        = bool
  default     = false # Set the default to false to prevent accidental creation
}

variable "ssh_key_name" {
  description = "The name of the EC2 key pair for SSH access."
  type        = string
  default     = "hyperion_deploy_key" 
}

variable "github_username" {
  description = "GitHub username"
  type        = string
}

variable "github_pat" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}