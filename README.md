NOTE: this readme is still a work in progress. More details will be added soon
# MedExplain: A Tool To Make Frontier Medical Research More Accessible 
Medical research progresses at a blinding pace, however the reading at which most texts are written is inaccessible to a vast majority of readers. MedExplain is a tool that aims to bridge this gap by using Large Language Models to translate the text to a more accessible reading level. Now, more individuals that are interested in medical research can stay up to date with medical advancements, written in a language that they can easily understand.

# Motivation
This tool is building upon the idea introduced by [Ayre Et Al.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10973278/) in which GPT-3.5 turbo was used to simplify health information documents. LLM wise, the main improvements of MedExplain are
- Switching the LLM model from GPT-3.5 to Claude Opus. Claude has shown to produce writing that sounds more organic and readable than any of OpenAI's offerings
- Used a much more sophisitcated system prompt

The system prompt used can be found below:

>
> You are an expert author skilled at explaining medical, biological, and scientific concepts in an engaging way for a 5th grade audience. Your task is to rewrite the following article to suit this target audience:
> 1. **Read through the article**: Carefully read the article to understand its content and structure.
> 2. **Identify complex concepts**: Identify any complex concepts, jargon, or vocabulary that may be difficult for a 5th grade audience to understand. Make a mental note of these items.
> 3. **Rewrite the article**: Begin rewriting the article, focusing on simplifying the language and explaining complex concepts in a way that is easy for 5th graders to grasp. You can be creative with your edits and make minor changes to the content and structure to enhance clarity and engagement. However, be sure to maintain the overall > meaning and intent of the original article.
> 4. **Handle direct quotes**: If you encounter any direct quotes in the article, keep as much of the quote as possible that the audience could understand. Keep the original quote and reference. If a quote contains language or concepts that may be too advanced for a 5th grader, provide a brief, simple explanation of what the quote means
> immediately after it.
> 5. **Maintain target audience focus**: Throughout the rewriting process, keep the target audience in mind. Use age-appropriate vocabulary, engaging examples, and tone to make the content appealing and accessible to 5th graders.
> 6. **Review your work**: Once you have completed the rewrite, review your work to ensure that it accurately conveys the information from the original article in a manner suitable for the target audience.
> 7. **Break up the text into sections**: Use appropriate titles for sections to organize the text.
> 8. **Key takeaways**: Append the top 3 main ideas of the article before the rewritten text. These should be the main points that the article is trying to bring up. Name this section "Key takeaways".

> Please provide only the rewritten article as your output, without any additional text or tags. Preserve all formatting and HTML. Do not write "Rewritten article for 5th graders"; after the main ideas, just start writing the article itself.
# Results
On average, the LLM edited text showed:
- A 3.7 point drop on the [SMOG](https://en.wikipedia.org/wiki/SMOG)
- 4.3 grade level drop on the [Flesch-Kincaid Grade Level](https://arc.net/l/quote/bywjvrug)
- 3.9 point drop on [Gunning-fog index](https://en.wikipedia.org/wiki/Gunning_fog_index)
- 23 point increase on [Flech-Kincaid Readability](https://arc.net/l/quote/hayttdag)

<p float="left">
  <img src="https://github.com/alexanderSolod/MedExplain/assets/47961133/484d8050-c329-4f66-8219-6d5c24c9c935" width = 500/>
  <img src="https://github.com/alexanderSolod/MedExplain/assets/47961133/3ad88b74-5450-4749-882c-2d3d9daa136b" width = 500/>
</p>

On average, the system was able to drop the average readability score from **university level** to **early high school**.

The analysis notebook can be found [here](https://github.com/alexanderSolod/MedExplain/blob/main/claude_analysis.ipynb)

# Translation pipeline
The other innovation is the introduction of an automatic translation pipeline, but as of right now that is still a work in progress. The pipeline should be run once a day, and will work like this 
1. Fetch new articles posted to https://news.yale.edu/topics/health-medicine (or any link)
2. Scrape articles contents and translate using LLM
3. Publish translated articles using a new template

As of right now we can scrape new articles and reliably contents for only some of the links
