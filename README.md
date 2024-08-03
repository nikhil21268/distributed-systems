# Consolidated README for Distributed Systems Projects

Welcome to my GitHub repository where I share projects that implement complex distributed systems and computational concepts applied to real-world scenarios. These projects include building a distributed K-means clustering model using MapReduce, enhancing a Raft consensus algorithm for better performance in geo-distributed databases, and setting up an online shopping platform using gRPC.

## Project 1: Online Shopping Platform Using gRPC

### Overview
This project involves creating an online shopping platform that uses gRPC for communication between buyers, sellers, and a central marketplace. The system is designed to handle complex client-server interactions across multiple virtual machine instances.

### Features
- Dynamic interactions among markets, sellers, and buyers.
- Management of product listings, updates, purchases, and customer reviews.
- Notification system for important updates and transactions.

## Project 2: Enhanced Raft Consensus for Geo-distributed Databases

### Overview
This project modifies the Raft consensus algorithm to include a leader lease mechanism, optimizing read operations across geo-distributed databases. It focuses on maintaining high availability and integrity within a simulated database cluster.

### Features
- Leader election and lease management to reduce read latencies.
- Consistent log replication and commitment across the cluster.
- Enhanced fault tolerance to maintain operations despite node failures.

## Project 3: K-Means Clustering with MapReduce

### Overview
This project involves developing a distributed K-means clustering algorithm over a custom-built MapReduce framework, ideal for handling large datasets with efficient parallel processing.

### Features
- Distributed data processing using the MapReduce model.
- Iterative recalibration of cluster centroids for improved accuracy.
- Robust fault tolerance mechanisms to ensure consistent clustering performance.

## Technical Specifications

- **Programming Languages**: Python is primarily used, with some components in C++.
- **Technologies**: gRPC, MapReduce, Virtual Machines, IP Networking.
- **Tools and Libraries**: Protocol Buffers, gRPC tools, and various Python libraries.

## Setup and Execution

To run these projects:

1. Ensure all prerequisites are installed as per the setup instructions specific to each project.
2. Clone the repository and set up the environment according to the directory structure provided.
3. Execute the projects by navigating to their respective directories and ensuring all services are running.

## Evaluation and Testing

Each project is thoroughly tested to meet functionality and performance specifications, demonstrating the system's reliability against potential failures and edge cases.

## Conclusion

These projects aim to deepen understanding and demonstrate practical skills in distributed systems and computational algorithms. They reflect my ability to design and manage complex software solutions effectively.

---

For more details and in-depth understanding, please refer to the specific documentation and comments within each project's codebase.

# Copyright and License

## Copyright (c) 2024, Nikhil Suri

## All rights reserved

This code and the accompanying materials are made available on an "as is" basis, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

## No Licensing
This project is protected by copyright and other intellectual property laws. It does not come with any license that would permit reproduction, distribution, or creation of derivative works. You may not use, copy, modify, or distribute this software and its documentation without express written permission from the copyright holder.

## Contact Information
For further inquiries, you can reach me at nikhil21268@iiitd.ac.in
