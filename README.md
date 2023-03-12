# EduAI
## Inspiration
EduAI was inspired by the growing demand for personalized education and the potential of AI to revolutionize the learning experience. As education becomes more global and digital, it is becoming increasingly important to tailor learning experiences to individual learners' unique needs and interests. AI technology can analyze vast amounts of data about learners, their preferences, and their performance to provide personalized learning experiences that optimize their learning outcomes. EduAI aims to leverage the power of AI to democratize education and make high-quality personalized learning accessible to all learners, regardless of their background or location.
## What it does
EduAI is an innovative platform that utilizes advanced AI technologies such as Amazon Transcribe and Amazon Textract to provide learners with efficient and effective note summarization and video summarization capabilities. With EduAI, learners can easily and quickly generate summaries of lengthy notes and videos, making it easier to review important information and retain key concepts.
Amazon Transcribe is a powerful speech recognition service that converts speech to text. EduAI utilizes this service to automatically transcribe the audio content of videos and convert it into text. Amazon Textract is a machine-learning service that extracts text and data from scanned documents, forms, and tables. EduAI uses Textract to extract important text and data from notes and documents automatically.
Learners can simply upload their notes or videos to the platform and let EduAI do the rest. The platform automatically analyzes the text and data, identifies the most important information, and generates a concise summary.
This technology is particularly useful for learners who struggle to keep up with the pace of lectures or who find it difficult to sift through lengthy notes or videos. With EduAI, they can quickly and easily generate a summary that captures the most important information, making it easier for them to review and retain key concepts.
## How we built it
EduAI is a cutting-edge platform that utilizes advanced AI technologies to provide learners with efficient and effective note summarization and video summarization capabilities. For note summarization, EduAI used a T5 model trained on the xsum dataset from hugging face. The platform used Amazon Textract to extract text from notes, and the T5 models were used to generate summaries.

To improve the accuracy of the note summarization, EduAI employed ensemble methods. This approach involved using multiple models to generate summaries and combining their results to achieve higher accuracy. EduAI also used OpenAI API to generate question-and-answer pairs, which helped learners better understand the material.

For video summarization, EduAI had to use OpenAI API for summarization because the text from videos was too long to be processed effectively by the T5 models. EduAI employed Streamlit for the front end of the platform and used Amazon Lambda functions to call the summarization functions. The platform was deployed using Amazon EC2 to help host the website, and the models were trained and run on Amazon SageMaker.

Overall, EduAI offers learners an efficient and effective way to summarize notes and videos. The use of advanced AI technologies and ensemble methods helps ensure high accuracy, while the deployment on Amazon Web Services provides scalability and reliability.

## Challenges we ran into
During the development and deployment of EduAI, we encountered several challenges that impacted the performance and usability of our platform. One of the major difficulties we faced was in generating accurate summaries, particularly for long text. We found that summarizing lengthy notes and videos using our T5 models resulted in summaries that were not always accurate or comprehensive. As a result, we had to resort to using OpenAI API for video summarization to achieve better results.

Another challenge we faced was in deploying our platform using Amazon EC2. While Amazon EC2 is a powerful tool that provides scalable cloud computing resources, setting it up and configuring it for our platform required a significant amount of technical expertise and time. We had to ensure that the different components of our platform, including the backend and front end, were properly configured and communicating with each other. We also had to optimize the performance of our platform by balancing the computing resources allocated to each component.

Despite these challenges, we were able to overcome them by collaborating closely as a team, seeking help from experts in relevant fields, and leveraging advanced AI technologies. We believe that by continually refining and improving our platform, we can provide learners with powerful tools to enhance their study experience and boost their learning outcomes.


## Accomplishments that we're proud of

We are proud of several achievements we accomplished with EduAI. Firstly, we integrated our platform with multiple AWS services such as Amazon Textract, Amazon Transcribe, and Amazon Lambda, which enabled us to improve the efficiency and scalability of our summarization process. Additionally, we created a user-friendly interface that is easy to use for learners to upload their notes and videos and receive accurate summaries in real-time. Our interface is optimized for desktop and mobile devices, providing learners with accessibility at all times. Finally, we successfully deployed our platform on AWS EC2 and Sagemaker, leveraging the powerful cloud computing resources offered by AWS. This ensured that our platform is reliable, scalable, and high-performing, ultimately enhancing the user experience for learners worldwide.
Overall, we are proud of the accomplishments we have achieved with EduAI, and we are committed to continuing to refine and improve our platform to help learners worldwide achieve their educational goals.

## What we learned
During the development of EduAI, we learned several important lessons that have helped us improve our skills and expertise in the field of AI and software development. Specifically, we learned about the importance of:

Collaboration: We learned that effective collaboration is key to developing a successful project. By working together, we were able to share our skills and expertise, leverage our strengths, and overcome challenges more efficiently.

Continuous learning: We realized that technology is constantly evolving and that we must keep learning and adapting to stay relevant. We learned how to integrate new tools and technologies into our project, such as T5 models and AWS services, and continuously improve our platform's performance and functionality.

Attention to detail: We learned that small details can have a significant impact on the overall user experience. We paid close attention to the design of our interface, the accuracy of our models, and the reliability of our deployment to ensure that our platform meets the needs and expectations of our users.

Flexibility: We learned the importance of being flexible and adaptable, especially when working with complex systems such as AWS. We had to troubleshoot technical issues, adjust our code to accommodate new requirements, and continuously improve our platform to meet the changing needs of our users.

Overall, these lessons have helped us develop a better understanding of the challenges and opportunities associated with AI development and software engineering, and we look forward to applying these lessons to future projects.
## What's next for EduAI
We have several exciting plans for EduAI in the future. Here are some of the things we have in store:
Adding new features: We plan to add new features to our platform, such as the ability to generate flashcards from summaries and the option to customize the level of summarization based on the user's preferences.

Expanding to new languages: Currently, EduAI supports English language notes and videos. We plan to expand our platform to support other languages, including Spanish, French, and Mandarin.

Partnerships: We plan to partner with educational institutions and online learning platforms to integrate our platform and provide learners with access to our summarization services directly within their learning management systems.

Mobile application: We also plan to develop a mobile application for EduAI, making it even easier for learners to access and utilize our platform on the go.
We are excited about the potential of EduAI to revolutionize the way learners access and consume educational content, and we look forward to continuing to develop and improve our platform in the future.
