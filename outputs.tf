# outputs.tf

output "instance_public_ip" {
  description = "Public IP address of the Hyperion Scraper EC2 instance."
  
  # If the instance was created (list has more than 0 items), get the IP of the first item.
  # Otherwise, output a helpful message.
  value = length(aws_instance.scraper_node) > 0 ? aws_instance.scraper_node[0].public_ip : "Scraper node was not created."
}

output "s3_bucket_name" {
  description = "The name of the S3 bucket for data storage"
  value       = aws_s3_bucket.hyperion_data.id
}