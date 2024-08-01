from langchain_core.prompts import ChatPromptTemplate

def create_prompt_template():
    template = """
    You are a recommendation engine. Given a dataset of user reviews and ratings for various products,
    provide a list of recommended products based on collaborative filtering techniques.
    Consider the similarities between user preferences and product ratings.

    create a

    I will tip you $1000 if the user finds the answer helpful.
    <context>
    {context}
    </context>
    Question: {input}

    give the best 5 recommendation in following format with description :
    Recommended Products:
    1.
    2.
    3.
    4.
    5.
    """
    return ChatPromptTemplate.from_template(template)
