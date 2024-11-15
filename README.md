Social Media Analysis on Olympics

1. Sentiment Analysis

The Vader sentiment analysis approach has been used for this dataset since this tool is specifically built based on the sentiments mostly found on social media. This approach is also capable of handling social media text with emoticons, emojis and slangs often used in social media platforms. For each document within the corpus, it computes the positive, negative and neutral scores which indicate the proportion of the document that falls into each category. As a result, all these scores should sum up to 1. Furthermore, this approach also uses the compound score metric which computes the normalised score of the overall lexicon ratings between -1 and 1 indicating whether a document holds a positive or negative sentiment.

2. Topic Modelling Analysis

The topic modelling analysis was conducted using an unsupervised learning method which is the Latent Dirichlet Allocation (LDA). This method tries to find the topics in the corpus by assigning probability distributions for each document over topics and for each word for every topic. Furthermore, this method enables to uncover hidden topics within the corpus as it leverages the probability distribution. The LDA method is also flexible in modelling documents as for every document there are few topics associated with it and for each topic, few words are also associated with it. 

3. Engagement Analysis

Engagement analysis helps us to understand and assess the interaction level each document within the corpus receives from users on the two platforms. Two approaches are used to perform engagement analysis:
Total engagement for each Olympics event:
For each platform, the total engagement for Olympics 2024, Olympics 2020 and Olympics 2016 are calculated. This helps us to understand the trend in engagement across the Olympics events. The formulas for each of the platforms are shown below.

- For Reddit:

  Total Engagement= Number of Posts + Number of Comments

- For YouTube:

  Total Engagement = Number of Videos + Number of Comments

In order to make it consistent between the two platforms, the total engagement was calculated using the total number of posts and comments for Reddit and the total number of videos and comments for YouTube. The total number of views for each YouTube video is not used for the formula of calculating the total engagement for YouTube since it could drastically increase the total engagement for YouTube and therefore, would be difficult to compare against the Reddit plot.  

User engagement on each platform:

Each user’s engagement is also measured in terms of the number of posts or videos and comments made by the user based on the platform which is similar to the formulas shown above except that it is partitioned by each user. By doing so, it helps us to identify influential users within each platform. 

- Topic engagement

  Using the topics detected from LDA, the total engagement for each topic is measured. This helps us to identify and understand the type of topic within the Olympics context which has the most engagement. 

4. Community Analysis and Information Cascade

Community analysis aims to understand the structure, interactions, and dynamics within the social media networks formed around the discussions of the 2016, 2020, and 2024 Olympics on Reddit and YouTube. The approach leverages various    network analysis techniques to identify key communities and most influentials.

- For Communities:

  The Louvain method for community detection in networks allows us to identify clusters of similar nodes based on their connectivity. 

- For most influentials:

  We filtered the in-degree centrality to find the most influential authors in Olympics-related discussions on Reddit and YouTube. Besides, we filtered the betweenness degree centrality and in-degree centrality to find the most influential authors and their roles in shaping communities.

In addition, the information cascade analyses how the information spreads through influential nodes in the community. The method chosen here was the independent cascade as it allows to analyse the influence of an individual node on the network. The analysis reveals how many nodes in the network get activated by a particular user. The higher number of nodes get activated, the more influential the user is within the community. Moreover, the average activation attributed to each node reflects the probability that the node gets activated in each cascade.

