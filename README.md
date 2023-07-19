## USING USER CONTROLLED SEARCH TERMS TO CREATE

# Abstract
With all the data that is being created via posts and discussion in social media, companies have for a
long time used this data to see how the public perceive them and to gauge their impact. Many compa-
nies use services like Hootsuite, Meltwater and Retriever which are all services that help companies
get a clear reports on views, amount of comments and likes on posts spanning several social media
platform. This project takes that process one step further and by using sentiment analysis it can label
the posts that is being made, as positive or negative. With this application any company can get a
quick overview of the public’s opinion. To do this the application is based on an SVM model that has
been trained on a dataset, that has been cleaned and transformed, to then accurately label pieces
of text as positive or negative. The application can base itself around pre-trained model based on a
specific language or it can translate the text to English and use an English trained model to label the
text. As per now the application only uses Twitter’s API, but how the application is setup it can take in
information from any site as long as it is in text form.
Based on real feedback form potential users of an application like this it seems like there is gap in
social media reports that this application could fill. I have talked to companies that deal with providing
internet services, power companies, larger grocery stores and tourism offices. Some of them felt like
a tool like this could be very useful, especially when the company is pushing a service or product that
is getting a lot of attention.

# Introduction
Social media has been a platform to voice peoples opinion on every subject known to man for several
years now. This produces a lot of data and this data has been used for a lot different kinds of data
mining and used to test different kinds of sentiment analysis models. Several projects have been done
using Twitter to test sentiment analysis since it is mostly raw text and most of the posts are open to
the public and is easy to search through based on hashtags and content. There has been projects
that has used Facebook or LinkedIn, which are also very text based social media sites, to tests
models but it requires more effort with the gathering of data. One project used a Facebook group for
their sentiment analysis model, but they had to ask all the members of the group to participate in their
project (Meire et al., 2016). This is a process that is difficult to do with a project that will use thousands
of posts. One could also use sites like Instagram, but then you have to look into image recognition
and classification, which is something I would like to do in the future with this project.
Twitter offers a much better access to its data through its API that is open for use (Roesslein, 2020).
For this project I will use Twitter as a main source of data to base the opinion mining, but hopefully in
the future it would not necessarily be limited by only using Twitter.
With this project I want to look into using sentiment analysis techniques to create a tool that can gather
the public’s opinion on any topic the user want to search for. By using a model that can label a text as
positive or negative and with the data from the social media platform Twitter, it would be able to give
the user an idea of how the public perceives a given product or service.
