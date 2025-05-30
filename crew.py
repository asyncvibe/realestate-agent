from crewai import Crew
from agents import property_researcher, property_analyst
from tasks import research_task, analysis_task

crew = Crew(
    agents=[property_researcher],#, property_analyst], 
    tasks=[research_task],#, analysis_task], 
    verbose=True
    )
input = "Melbourne"
task_output = crew.kickoff(inputs={"input": input})
print(task_output)