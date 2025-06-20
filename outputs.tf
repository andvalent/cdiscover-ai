# outputs.tf

output "instance_public_ip" {
  description = "The public IP address of the scraper EC2 instance"
  value       = aws_spot_instance_request.scraper_node.public_ip
}

output "s3_bucket_name" {
  description = "The name of the S3 bucket for data storage"
  value       = aws_s3_bucket.hyperion_data.id
}