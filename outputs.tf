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


output "api_server_public_dns" {
  description = "The public DNS name of the RAG API server."
  value       = aws_instance.rag_api_server.public_dns
}

output "api_test_command" {
  description = "A sample curl command to test the API."
  value       = "curl -X POST http://${aws_instance.rag_api_server.public_dns}/search -H \"Content-Type: application/json\" -d '{\"query\": \"recommend a cd with a 900 symphony inspired by nature\"}'"
}

