from crewai import Agent, Task, Crew, LLM

def generate_content(llm, topic):
    
    planner = Agent(
        role = "Content Planner",
        goal = "Plan engaging and factually accurate content on {topic}",
        backstory = """You're working on planning a blog article about the topic: {topic}. 
        You collect information that helps the audience learn something and make informed decisions. 
        Your work is the basis for the Content Writer to write an article on this topic.""",
        llm = llm,
        allow_delegation = False,
	    verbose = True
    )
    
    plan = Task(
        description = """1. Prioritize the latest trends, key players, and noteworthy news on {topic}. 
        2. Identify the target audience, considering their interests and pain points. 
        3. Develop a detailed content outline including an introduction, key points, and a call to action. 
        4. Include SEO keywords and relevant data or sources.""",
        expected_output = """A comprehensive content plan document with an outline, audience analysis, SEO keywords, and resources.""",
        agent = planner,
    )
    
    writer = Agent(
        role = "Content Writer",
        goal = """Write insightful and factually accurate opinion piece about the topic: {topic}""",
        backstory = """You're working on a writing a new opinion piece about the topic: {topic}. 
        You base your writing on the work of the Content Planner, who provides an outline and relevant context about the topic. 
        You follow the main objectives and direction of the outline, as provide by the Content Planner. 
        You also provide objective and impartial insights and back them up with information provide by the Content Planner. 
        You acknowledge in your opinion piece when your statements are opinions as opposed to objective statements.""",
        llm = llm,
        allow_delegation = False,
        verbose = True
    )
    
    editor = Agent(
        role = "Editor",
        goal = "Edit a given blog post to align with the writing style of the organization.",
        backstory = """You are an editor who receives a blog post from the Content Writer. 
        Your goal is to review the blog post to ensure that it follows journalistic best practices, 
        provides balanced viewpoints when providing opinions or assertions, and also avoids major controversial topics 
        or opinions when possible.""",
        llm = llm,
        allow_delegation = False,
        verbose = True
    )
    
    
    