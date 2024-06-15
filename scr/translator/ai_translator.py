import anthropic
import os 
import getpass



def rewrite_article_for_5th_graders(article):       
    client = anthropic.Anthropic()
    message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    system="You are an expert author skilled at explaining medical, biological, and scientific concepts in an engaging way for a 5th grade audience. Your task is to rewrite the following article to suit this target audience:\n\nPlease follow these steps to complete the task:\n\n1. Read through the article carefully to understand its content and structure.\n\n2. Identify any complex concepts, jargon, or vocabulary that may be difficult for a 5th grade audience to understand. Make a mental note of these items.\n\n3. Begin rewriting the article, focusing on simplifying the language and explaining complex concepts in a way that is easy for 5th graders to grasp. You can be creative with your edits and make minor changes to the content and structure to enhance clarity and engagement. However, be sure to maintain the overall meaning and intent of the original article.\n\n4. If you encounter any direct quotes in the article, KEEP AS MUCH OF THE QUOTE AS POSSIBLE THAT THE AUDIENCE COULD UNDERSTAND. Keep the original quote and reference. If a quote contains language or concepts that may be too advanced for a 5th grader, provide a brief, simple explanation of what the quote means immediately after it.\n\n5. Throughout the rewriting process, keep the target audience in mind. Use age-appropriate vocabulary, engaging examples, and tone to make the content appealing and accessible to 5th graders.\n\n6. Once you have completed the rewrite, review your work to ensure that it accurately conveys the information from the original article in a manner suitable for the target audience.\n\n7. Break up the text into sections with appropriate titles\n\n8. Append the top 3 main ideas of the article before the re-written text. These should be main points that the article is trying to bring up. Name this section 'Key takeaways' \n\nPlease provide only the rewritten article as your output, without any additional text or tags. PRESERVE ALL FORMATTING AND HTML. DO NOT WRITE 'Rewritten article for 5th grades', after the main ideas, just start writing the article itself.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": article
                }
            ]
        }
    ]
)

    return message.content[0].text



if __name__ == "__main__":
    article = "this is a sophisticated article about science"
    print(rewrite_article_for_5th_graders(article))